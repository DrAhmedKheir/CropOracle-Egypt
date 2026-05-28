from __future__ import annotations
from flask import Flask, request, jsonify
from app.config import settings
from app.services.scenario_planner import extract_scenario
from app.services.apsim_runner import run_scenario_set
from app.services.advisory_generator import generate_advisory
from app.services.whatsapp_client import send_whatsapp_text
from app.agents.coordinator import CropOracleMultiAgentCoordinator

app = Flask(__name__)
coordinator = CropOracleMultiAgentCoordinator()

@app.route('/', methods=['GET'])
def health():
    return jsonify({'service': 'CropOracle Egypt Multi-Agent', 'status': 'running'})

@app.route('/webhook/whatsapp', methods=['GET'])
def verify_whatsapp_webhook():
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    if mode == 'subscribe' and token == settings.WHATSAPP_VERIFY_TOKEN:
        return challenge or '', 200
    return 'Verification failed', 403

@app.route('/webhook/whatsapp', methods=['POST'])
def receive_whatsapp_message():
    payload = request.get_json(force=True, silent=True) or {}
    try:
        entry = payload.get('entry', [])[0]
        change = entry.get('changes', [])[0]
        value = change.get('value', {})
        message_obj = value.get('messages', [])[0]
        from_phone = message_obj.get('from')
        text = message_obj.get('text', {}).get('body', '')

        state = coordinator.run(text, farmer_phone=from_phone)
        send_whatsapp_text(from_phone, state.advisory_text or 'Simulation completed, but no advisory was generated.')
        return jsonify({'status': 'ok', 'trace': [t.model_dump() for t in state.trace]}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e), 'payload': payload}), 500

@app.route('/simulate', methods=['POST'])
def simulate_direct():
    """Legacy single-pipeline endpoint."""
    data = request.get_json(force=True)
    text = data.get('message', '')
    phone = data.get('phone', 'demo')
    scenario = extract_scenario(text, farmer_phone=phone)
    results = run_scenario_set(scenario)
    reply = generate_advisory(scenario, results)
    return jsonify({
        'scenario': scenario.model_dump(),
        'results': results.to_dict(orient='records'),
        'reply': reply
    })

@app.route('/simulate-agent', methods=['POST'])
def simulate_agent_direct():
    """Recommended endpoint: full multi-agent CropOracle Egypt workflow."""
    data = request.get_json(force=True)
    text = data.get('message', '')
    phone = data.get('phone', 'demo')
    state = coordinator.run(text, farmer_phone=phone)
    return jsonify(state.model_dump())

if __name__ == '__main__':
    app.run(host=settings.FLASK_HOST, port=settings.FLASK_PORT, debug=settings.FLASK_DEBUG)

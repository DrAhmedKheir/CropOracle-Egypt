from app.agents.coordinator import CropOracleMultiAgentCoordinator

message = (
    "I am a wheat farmer in Kafr El-Sheikh. My farm is 5 feddan. "
    "Rainfall may decrease by 20% and temperature increase 2 C. "
    "Which sowing date is best: November or December?"
)

state = CropOracleMultiAgentCoordinator().run(message, farmer_phone="demo")
print("\n=== Advisory ===")
print(state.advisory_text)
print("\n=== Agent Trace ===")
for item in state.trace:
    print(f"- {item.agent}: {item.action} [{item.status}] {item.note or ''}")

from app.services.scenario_planner import extract_scenario

def test_extract_basic():
    s = extract_scenario('I am in Kafr El-Sheikh with 2 feddan. Rainfall decreases by 20%.')
    assert s.crop == 'wheat'
    assert s.farm_area_ha > 0
    assert s.rainfall_change_pct <= 0

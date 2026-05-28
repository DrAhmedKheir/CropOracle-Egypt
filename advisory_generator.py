from __future__ import annotations
import pandas as pd
from app.services.scenario_planner import FarmerScenario


def generate_advisory(scenario: FarmerScenario, results: pd.DataFrame) -> str:
    best = results.iloc[0]
    worst = results.iloc[-1]
    extra_kg_ha = best['yield_kg_ha'] - worst['yield_kg_ha']
    extra_total_kg = extra_kg_ha * scenario.farm_area_ha

    if scenario.language == 'ar':
        return (
            f"🌾 توصية CropOracle Egypt للقمح\n\n"
            f"الموقع: {scenario.governorate}\n"
            f"أفضل ميعاد زراعة: {best['sowing_date']}\n"
            f"المحصول المتوقع: {best['yield_t_ha']} طن/هكتار\n"
            f"أضعف اختيار في المقارنة: {worst['sowing_date']} = {worst['yield_t_ha']} طن/هكتار\n\n"
            f"الفرق المتوقع: حوالي {extra_kg_ha:.0f} كجم/هكتار. "
            f"لمساحة {scenario.farm_area_ha:.2f} هكتار، هذا يعادل {extra_total_kg:.0f} كجم إضافية.\n\n"
            f"هذه نتيجة محاكاة أولية ويجب تأكيدها بالمعايرة المحلية والظروف الحقلية."
        )

    return (
        f"🌾 CropOracle Egypt wheat recommendation\n\n"
        f"Location: {scenario.governorate}\n"
        f"Best sowing date: {best['sowing_date']}\n"
        f"Simulated yield: {best['yield_t_ha']} t/ha\n"
        f"Lowest option tested: {worst['sowing_date']} = {worst['yield_t_ha']} t/ha\n\n"
        f"Expected advantage: about {extra_kg_ha:.0f} kg/ha. "
        f"For {scenario.farm_area_ha:.2f} ha, this is about {extra_total_kg:.0f} kg extra grain.\n\n"
        f"Note: this is a prototype simulation result. Final deployment needs local APSIM calibration and validation."
    )

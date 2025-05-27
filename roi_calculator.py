def calculate_roi(rooftop_data):
    area = rooftop_data["estimated_area_sqm"]
    panel_efficiency = 0.18
    sun_hours_per_day = 5
    system_size_kw = (area * panel_efficiency) / 1.6
    annual_output_kwh = system_size_kw * sun_hours_per_day * 365
    cost_per_kw = 60000
    total_cost = system_size_kw * cost_per_kw
    savings_per_kwh = 6
    annual_savings = annual_output_kwh * savings_per_kwh
    payback_years = total_cost / annual_savings

    return {
        "system_size_kw": round(system_size_kw, 2),
        "annual_output_kwh": int(annual_output_kwh),
        "estimated_cost_inr": int(total_cost),
        "annual_savings_inr": int(annual_savings),
        "payback_period_years": round(payback_years, 1)
    }

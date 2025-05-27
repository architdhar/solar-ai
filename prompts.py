def generate_llm_output(data):
    return f"For a {data['estimated_area_sqm']} sqm, {data['orientation']} roof with {data['shadow_percentage']}% shadow, we recommend monocrystalline panels with a 25-year warranty. Expected ROI within {round((data['estimated_area_sqm']*0.18/1.6*60000)/(data['estimated_area_sqm']*0.18/1.6*5*365*6), 1)} years."

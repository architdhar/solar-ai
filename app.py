import streamlit as st
from rooftop_analyzer import analyze_rooftop
from roi_calculator import calculate_roi
from prompts import generate_llm_output
from PIL import Image

st.set_page_config(page_title="Solar Rooftop AI Tool", layout="centered")
st.title("🔆 AI-Powered Solar Rooftop Assessment")

uploaded_file = st.file_uploader("Upload a satellite image of your rooftop", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Rooftop", use_column_width=True)

    with st.spinner("Analyzing rooftop image..."):
        rooftop_data = analyze_rooftop(image)

    st.success("Rooftop analysis complete!")
    st.json(rooftop_data)

    with st.spinner("Generating solar installation and ROI report..."):
        llm_output = generate_llm_output(rooftop_data)
        roi = calculate_roi(rooftop_data)

    st.subheader("🔍 LLM Recommendations")
    st.write(llm_output)

    st.subheader("📊 ROI Analysis")
    st.write(roi)

    st.download_button("Download Report", data=str(llm_output)+"\n"+str(roi), file_name="solar_report.txt")

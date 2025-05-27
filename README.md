# AI-Powered Solar Rooftop Tool

## Overview
This tool helps assess the solar potential of rooftops using AI. Upload a satellite image, and receive panel recommendations and ROI analysis.

## Setup Instructions
1. Clone the repo
2. Run `pip install -r requirements.txt`
3. Run `streamlit run app.py`

## Example Use
Upload a rooftop image. Output includes:
- Usable area
- System size
- Annual generation
- ROI & recommendations

## Future Improvements
- Use YOLO/SAM for real image segmentation
- Integrate sun angle API by location
- Add downloadable PDF reports

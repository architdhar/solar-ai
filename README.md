# ☀️ Solar Industry AI Assistant

An AI-powered web app for analyzing rooftop images and estimating solar panel potential. Developed for the Solar Industry AI Assistant Internship Assessment 2024, this tool helps users estimate installation feasibility, ROI, and system recommendations based on uploaded satellite imagery.

---

## 🚀 Features

- 📤 Upload rooftop satellite images
- 🧠 AI-simulated (mocked) rooftop feature estimation
- 📈 ROI calculator for system cost, energy savings, and payback period
- 🤖 Template-based LLM-style installation recommendations
- 📄 Downloadable report in JSON format

---

## 🗂 Project Structure

| File | Purpose |
|------|---------|
| `app.py` | Main Streamlit interface |
| `rooftop_analyzer.py` | Simulates rooftop area, tilt, and orientation (mocked) |
| `roi_calculator.py` | Performs ROI calculation and outputs solar metrics |
| `prompts.py` | Generates suggestion text using a formatted template |
| `requirements.txt` | Python dependencies for running the app |
| `sample_rooftop.jpg` | Example rooftop image used in testing |
| `README.md` | Project documentation (this file) |

---

## 🛠 Setup Instructions

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/yourusername/solar-ai-assistant.git
cd solar-ai-assistant

 2. Create and activate a virtual environment
python -m venv env
source env/bin/activate          

# 3. Install required packages
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run app.py

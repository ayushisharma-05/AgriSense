<<<<<<< HEAD
import streamlit as st
from src.predict import predict_crop

st.set_page_config(page_title="AgriSense", page_icon="🌱", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp { background: #fffef5; }
.block-container { padding: 2rem 3rem; max-width: 1100px; }
div.stButton > button {
    background: #14532d; color: white; border: none;
    border-radius: 8px; font-weight: 600;
}
div.stButton > button:hover { background: #166534; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align:center'>🌱 AgriSense</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#6b7280;margin-top:-10px'>Smart Crop Planning Advisor</p>", unsafe_allow_html=True)
st.divider()

def get_reason(n, p, k, temp, humidity, ph, rain):
    if rain > 180 and humidity > 75:
        return "Thrives in high moisture and rainfall conditions."
    if temp > 28 and humidity > 80:
        return "Loves warm, humid tropical climate."
    if n > 80 and rain > 150:
        return "High nitrogen and good rainfall support strong growth."
    if ph < 6.0 and temp > 20:
        return "Prefers slightly acidic soil with warm temperatures."
    if rain < 70:
        return "Well suited for dry conditions with low water need."
    if k > 60:
        return "Rich potassium levels boost yield and disease resistance."
    return "Soil nutrients and climate are well balanced for this crop."

left, right = st.columns([1.1, 0.9], gap="large")

with left:
    c1, c2 = st.columns(2)
    with c1:
        N = st.number_input("Nitrogen (N)", value=90.0)
        K = st.number_input("Potassium (K)", value=43.0)
        humidity = st.number_input("Humidity (%)", value=82.0)
        ph = st.number_input("Soil pH", value=6.5)
    with c2:
        P = st.number_input("Phosphorus (P)", value=42.0)
        temperature = st.number_input("Temperature (°C)", value=20.8)
        rainfall = st.number_input("Rainfall (mm)", value=202.9)
    predict = st.button("Predict Best Crop", use_container_width=True)

with right:
    EMOJI = {"rice":"🌾","maize":"🌽","banana":"🍌","mango":"🥭","grapes":"🍇",
             "watermelon":"🍉","apple":"🍎","orange":"🍊","coconut":"🥥","coffee":"☕",
             "cotton":"🌿","chickpea":"🫘","kidneybeans":"🫘","lentil":"🥣",
             "pigeonpeas":"🌱","mungbean":"🫘","blackgram":"🫘","papaya":"🍈"}

    if predict:
        crop = predict_crop([N, P, K, temperature, humidity, ph, rainfall])
        emoji = EMOJI.get(crop.lower(), "🌿")
        reason = get_reason(N, P, K, temperature, humidity, ph, rainfall)
        st.markdown(f"""
        <div style="background:white;border-radius:14px;padding:2.5rem 2rem;text-align:center;
                    border:1px solid #e5e7eb;min-height:340px;">
            <div style="font-size:3.5rem">{emoji}</div>
            <div style="font-size:0.7rem;color:#9ca3af;letter-spacing:.1em;margin:10px 0 4px">RECOMMENDED CROP</div>
            <div style="font-size:2.2rem;font-weight:700;color:#14532d;margin-bottom:1rem">{crop.title()}</div>
            <div style="background:#f0fdf4;border-radius:10px;padding:0.8rem 1rem;
                        font-size:0.85rem;color:#374151;text-align:left;margin-bottom:1rem">
                <span style="font-weight:600;color:#15803d">Why this crop?</span><br>{reason}
            </div>
            <div style="font-size:0.78rem;color:#9ca3af">
                pH {ph} · Rain {rainfall:.0f}mm · N–P–K {int(N)}–{int(P)}–{int(K)}
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="border-radius:14px;padding:2.5rem 2rem;text-align:center;
                    border:1px dashed #d1d5db;color:#9ca3af;min-height:340px;
                    display:flex;flex-direction:column;align-items:center;justify-content:center;">
            <div style="font-size:2.5rem">🌾</div>
            <div style="margin-top:0.5rem;font-size:0.85rem">Fill values and click predict</div>
        </div>
        """, unsafe_allow_html=True)
# import streamlit as st
# from src.predict import predict_crop

# st.set_page_config(page_title="AgriSense", page_icon="🌱", layout="wide")

# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

# html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

# .stApp {
#     background: radial-gradient(ellipse at top left, #d1fae5 0%, #f9fdf9 40%),
#                 radial-gradient(ellipse at bottom right, #fef9c3 0%, #f9fdf9 50%);
#     min-height: 100vh;
# }

# .block-container { padding: 2.5rem 4rem 2rem; max-width: 1280px; }

# .ag-header { text-align: center; margin-bottom: 2.2rem; }
# .ag-logo-row {
#     display: flex; align-items: center;
#     justify-content: center; gap: 12px; margin-bottom: 4px;
# }
# .ag-logo-row h1 { font-size: 2.8rem; font-weight: 800; color: #1a6b2f; margin: 0; }
# .ag-tagline { font-size: 0.95rem; font-weight: 600; color: #3a8a4a; margin-bottom: 5px; }
# .ag-sub { font-size: 0.85rem; color: #6b7280; }

# .ag-card {
#     background: rgba(255,255,255,0.88);
#     backdrop-filter: blur(12px);
#     border: 1px solid rgba(255,255,255,0.95);
#     border-radius: 22px; padding: 2rem;
#     box-shadow: 0 4px 20px rgba(0,0,0,0.05);
# }

# .ag-card-title { font-size: 1.05rem; font-weight: 700; color: #111827; }
# .ag-title-row {
#     display: flex; align-items: center;
#     justify-content: space-between; margin-bottom: 1.4rem;
# }
# .ag-field-label {
#     font-size: 0.82rem; font-weight: 600;
#     color: #374151; margin-bottom: 3px;
# }
# .ag-field-label span { font-weight: 400; color: #9ca3af; }

# div[data-testid="stNumberInput"] > div > div > input {
#     border-radius: 100px !important;
#     border: 1.5px solid #e5e7eb !important;
#     padding: 10px 18px !important;
#     font-size: 0.9rem !important;
#     background: rgba(255,255,255,0.95) !important;
#     box-shadow: none !important;
# }
# div[data-testid="stNumberInput"] > div > div > input:focus {
#     border-color: #22c55e !important;
#     box-shadow: 0 0 0 3px rgba(34,197,94,.1) !important;
# }

# div.stButton > button {
#     background: linear-gradient(135deg, #16a34a, #22c55e);
#     color: white; border: none; border-radius: 100px;
#     padding: 0.78rem 1rem; font-size: 0.98rem; font-weight: 700;
#     width: 100%; margin-top: 1.1rem;
#     box-shadow: 0 4px 14px rgba(22,163,74,.3); transition: .25s ease;
# }
# div.stButton > button:hover {
#     transform: translateY(-2px);
#     box-shadow: 0 8px 22px rgba(22,163,74,.35);
# }

# .ag-idle {
#     display: flex; flex-direction: column;
#     align-items: center; justify-content: center;
#     min-height: 440px; text-align: center; gap: .9rem;
# }
# .ag-idle-circle {
#     width: 110px; height: 110px; border-radius: 50%;
#     background: #f0fdf4;
#     display: flex; align-items: center; justify-content: center;
#     font-size: 3rem;
# }
# .ag-idle h3 { font-size: 1.1rem; font-weight: 700; color: #16a34a; margin: 0; }
# .ag-idle p  { font-size: 0.83rem; color: #9ca3af; margin: 0; max-width: 210px; line-height: 1.5; }

# .ag-result {
#     display: flex; flex-direction: column;
#     align-items: center; justify-content: center;
#     min-height: 440px; text-align: center; padding: 1rem 0;
# }
# .ag-result-circle {
#     width: 120px; height: 120px; border-radius: 50%;
#     background: linear-gradient(135deg, #dcfce7, #bbf7d0);
#     display: flex; align-items: center; justify-content: center;
#     font-size: 3.5rem; margin-bottom: 1.1rem;
#     box-shadow: 0 8px 24px rgba(34,197,94,.18);
# }
# .ag-result-tag {
#     font-size: 0.68rem; letter-spacing: .12em;
#     text-transform: uppercase; color: #6b7280;
#     font-weight: 600; margin-bottom: 3px;
# }
# .ag-result-crop {
#     font-size: 2.3rem; font-weight: 800;
#     color: #14532d; margin-bottom: 1.1rem; line-height: 1;
# }
# .ag-insight {
#     background: #f0fdf4; border-left: 3px solid #22c55e;
#     border-radius: 0 12px 12px 0;
#     padding: .8rem 1rem; text-align: left;
#     width: 100%; margin-bottom: 1.1rem;
# }
# .ag-insight p { font-size: 0.84rem; color: #374151; line-height: 1.6; margin: 0; }
# .ag-metrics { display: flex; flex-wrap: wrap; gap: 6px; justify-content: center; }
# .ag-metric {
#     font-size: 0.77rem; font-weight: 500;
#     background: #f0fdf4; color: #166534;
#     border: 1px solid #bbf7d0;
#     padding: 4px 12px; border-radius: 100px;
# }

# .ag-footer { text-align:center; margin-top:1.8rem; font-size:.76rem; color:#9ca3af; }
# </style>
# """, unsafe_allow_html=True)

# CROP_EMOJI = {
#     "rice":"🌾","maize":"🌽","chickpea":"🫘","kidneybeans":"🫘",
#     "pigeonpeas":"🌱","mungbean":"🫘","blackgram":"🫘","lentil":"🥣",
#     "banana":"🍌","mango":"🥭","grapes":"🍇","watermelon":"🍉",
#     "apple":"🍎","orange":"🍊","papaya":"🍈","coconut":"🥥",
#     "cotton":"🌿","coffee":"☕",
# }

# def get_insight(n, p, k, rain):
#     tips = []
#     if n > 70:     tips.append("High nitrogen will accelerate vegetative growth.")
#     if p > 50:     tips.append("Strong phosphorus boosts root development.")
#     if k > 50:     tips.append("Rich potassium improves disease resistance.")
#     if rain > 150: tips.append("Ample rainfall suits this water-intensive variety.")
#     elif rain < 70:tips.append("Low water need makes it ideal for dry conditions.")
#     if not tips:   tips.append("Your balanced soil profile is optimal for this crop.")
#     return " ".join(tips[:2])

# # ── Header ────────────────────────────────────────────────────────────────────
# st.markdown("""
# <div class="ag-header">
#   <div class="ag-logo-row">
#     <span style="font-size:2.6rem">🌱</span>
#     <h1>AgriSense</h1>
#   </div>
#   <div class="ag-tagline">Smart Crop Planning Advisor</div>
#   <div class="ag-sub">Enter soil and climate parameters to get AI-powered crop recommendations.</div>
# </div>
# """, unsafe_allow_html=True)

# # ── Layout ────────────────────────────────────────────────────────────────────
# left, right = st.columns([1, 1], gap="large")

# with left:
#     st.markdown('<div class="ag-card">', unsafe_allow_html=True)
#     st.markdown("""
#     <div class="ag-title-row">
#       <span class="ag-card-title">Soil &amp; Climate Inputs</span>
#       <span style="font-size:0.8rem;font-weight:500;color:#16a34a;">Use sample</span>
#     </div>
#     """, unsafe_allow_html=True)

#     c1, c2 = st.columns(2)
#     with c1:
#         st.markdown('<div class="ag-field-label">Nitrogen (N) <span>mg/kg</span></div>', unsafe_allow_html=True)
#         N = st.number_input("N", min_value=0.0, max_value=140.0, value=None, placeholder="e.g. 90", label_visibility="collapsed")

#         st.markdown('<div class="ag-field-label">Potassium (K) <span>mg/kg</span></div>', unsafe_allow_html=True)
#         K = st.number_input("K", min_value=0.0, max_value=205.0, value=None, placeholder="e.g. 43", label_visibility="collapsed")

#         st.markdown('<div class="ag-field-label">Humidity <span>%</span></div>', unsafe_allow_html=True)
#         humidity = st.number_input("Humidity", min_value=0.0, max_value=100.0, value=None, placeholder="e.g. 80", label_visibility="collapsed")

#     with c2:
#         st.markdown('<div class="ag-field-label">Phosphorus (P) <span>mg/kg</span></div>', unsafe_allow_html=True)
#         P = st.number_input("P", min_value=0.0, max_value=145.0, value=None, placeholder="e.g. 42", label_visibility="collapsed")

#         st.markdown('<div class="ag-field-label">Temperature <span>°C</span></div>', unsafe_allow_html=True)
#         temperature = st.number_input("Temp", min_value=0.0, max_value=50.0, value=None, placeholder="e.g. 24.5", label_visibility="collapsed")

#         st.markdown('<div class="ag-field-label">pH</div>', unsafe_allow_html=True)
#         ph = st.number_input("pH", min_value=0.0, max_value=14.0, value=None, placeholder="e.g. 6.5", label_visibility="collapsed")

#     st.markdown('<div class="ag-field-label" style="margin-top:2px;">Rainfall <span>mm</span></div>', unsafe_allow_html=True)
#     rainfall = st.number_input("Rainfall", min_value=0.0, max_value=300.0, value=None, placeholder="e.g. 200", label_visibility="collapsed")

#     predict = st.button("🔍  Predict Best Crop")
#     st.markdown('</div>', unsafe_allow_html=True)

# with right:
#     st.markdown('<div class="ag-card">', unsafe_allow_html=True)

#     all_filled = all(v is not None for v in [N, P, K, temperature, humidity, ph, rainfall])

#     if predict and not all_filled:
#         st.warning("Please fill in all 7 fields before predicting.", icon="⚠️")

#     if predict and all_filled:
#         crop   = predict_crop([N, P, K, temperature, humidity, ph, rainfall])
#         emoji  = CROP_EMOJI.get(crop.lower(), "🌿")
#         reason = get_insight(N, P, K, rainfall)
#         st.markdown(f"""
#         <div class="ag-result">
#           <div class="ag-result-circle">{emoji}</div>
#           <div class="ag-result-tag">recommended crop</div>
#           <div class="ag-result-crop">{crop.title()}</div>
#           <div class="ag-insight"><p>💡 {reason}</p></div>
#           <div class="ag-metrics">
#             <span class="ag-metric">pH {ph:.1f}</span>
#             <span class="ag-metric">Rain {rainfall:.0f} mm</span>
#             <span class="ag-metric">N–P–K &nbsp;{int(N)}–{int(P)}–{int(K)}</span>
#             <span class="ag-metric">{temperature:.1f}°C · {humidity:.0f}% RH</span>
#           </div>
#         </div>
#         """, unsafe_allow_html=True)
#         st.balloons()
#     else:
#         st.markdown("""
#         <div class="ag-idle">
#           <div class="ag-idle-circle">🌿</div>
#           <h3>Awaiting your inputs</h3>
#           <p>Your crop recommendation will appear here.</p>
#         </div>
#         """, unsafe_allow_html=True)

#     st.markdown('</div>', unsafe_allow_html=True)

# st.markdown(
#     '<div class="ag-footer">AgriSense · Python · Scikit-learn · Streamlit</div>',
#     unsafe_allow_html=True
# )

# import streamlit as st
# from src.predict import predict_crop

# # ---------------- Page Config ----------------
# st.set_page_config(
#     page_title="AgriSense",
#     page_icon="🌱",
#     layout="wide"
# )

# # ---------------- Custom CSS ----------------
# st.markdown("""
# <style>
# .stApp {
#     background: linear-gradient(135deg, #e8f5e9 0%, #ffffff 100%);
# }

# .block-container {
#     padding-top: 2rem;
#     padding-bottom: 2rem;
#     max-width: 1200px;
# }

# .main-title {
#     font-size: 3.5rem;
#     font-weight: 800;
#     color: #1b5e20;
#     text-align: center;
#     margin-bottom: 0;
# }

# .sub-title {
#     font-size: 1.2rem;
#     color: #4b5563;
#     text-align: center;
#     margin-bottom: 2rem;
# }

# .glass-card {
#     background: rgba(255, 255, 255, 0.85);
#     border-radius: 24px;
#     padding: 2rem;
#     box-shadow: 0 12px 30px rgba(0, 0, 0, 0.08);
#     backdrop-filter: blur(10px);
# }

# .result-card {
#     background: linear-gradient(135deg, #2e7d32, #66bb6a);
#     color: white;
#     border-radius: 24px;
#     padding: 3rem 2rem;
#     text-align: center;
#     box-shadow: 0 15px 35px rgba(46, 125, 50, 0.25);
#     min-height: 420px;
#     display: flex;
#     flex-direction: column;
#     justify-content: center;
# }

# .placeholder-card {
#     background: rgba(255, 255, 255, 0.85);
#     border-radius: 24px;
#     padding: 3rem 2rem;
#     text-align: center;
#     box-shadow: 0 12px 30px rgba(0, 0, 0, 0.08);
#     min-height: 420px;
#     display: flex;
#     flex-direction: column;
#     justify-content: center;
# }

# .footer {
#     text-align: center;
#     margin-top: 2rem;
#     color: #6b7280;
#     font-size: 0.9rem;
# }

# div.stButton > button {
#     background: linear-gradient(135deg, #2e7d32, #43a047);
#     color: white;
#     font-weight: 600;
#     border: none;
#     border-radius: 12px;
#     padding: 0.8rem 1.2rem;
#     width: 100%;
#     transition: 0.3s;
# }

# div.stButton > button:hover {
#     transform: translateY(-2px);
#     box-shadow: 0 8px 20px rgba(46, 125, 50, 0.25);
# }
# </style>
# """, unsafe_allow_html=True)

# # ---------------- Crop Emojis ----------------
# crop_emojis = {
#     "rice": "🌾",
#     "maize": "🌽",
#     "chickpea": "🫘",
#     "kidneybeans": "🫘",
#     "pigeonpeas": "🌱",
#     "mungbean": "🫘",
#     "blackgram": "🫘",
#     "lentil": "🥣",
#     "banana": "🍌",
#     "mango": "🥭",
#     "grapes": "🍇",
#     "watermelon": "🍉",
#     "apple": "🍎",
#     "orange": "🍊",
#     "papaya": "🍈",
#     "coconut": "🥥",
#     "cotton": "☁️",
#     "coffee": "☕"
# }

# # ---------------- Header ----------------
# st.markdown(
#     '<h1 class="main-title">🌱 AgriSense</h1>',
#     unsafe_allow_html=True
# )

# st.markdown(
#     '<p class="sub-title">AI-Powered Smart Crop Planning Advisor</p>',
#     unsafe_allow_html=True
# )

# # ---------------- Layout ----------------
# left_col, right_col = st.columns([1.1, 0.9], gap="large")

# # ---------------- Input Form ----------------
# with left_col:
#     st.markdown('<div class="glass-card">', unsafe_allow_html=True)

#     st.subheader("🧪 Soil & Climate Inputs")

#     col1, col2 = st.columns(2)

#     with col1:
#         N = st.number_input("Nitrogen (N)", value=90.0)
#         P = st.number_input("Phosphorus (P)", value=42.0)
#         K = st.number_input("Potassium (K)", value=43.0)
#         temperature = st.number_input("Temperature (°C)", value=20.8)

#     with col2:
#         humidity = st.number_input("Humidity (%)", value=82.0)
#         ph = st.number_input("pH", value=6.5)
#         rainfall = st.number_input("Rainfall (mm)", value=202.9)

#     predict_button = st.button("🔍 Predict Best Crop")

#     st.markdown('</div>', unsafe_allow_html=True)

# # ---------------- Result Panel ----------------
# with right_col:
#     if predict_button:
#         features = [N, P, K, temperature, humidity, ph, rainfall]
#         prediction = predict_crop(features)

#         emoji = crop_emojis.get(prediction.lower(), "🌿")

#         st.markdown(
#             f"""
#             <div class="result-card">
#                 <div style="font-size: 5rem;">{emoji}</div>
#                 <p style="font-size: 1rem; opacity: 0.9;">
#                     Recommended Crop
#                 </p>
#                 <h1 style="margin: 0; font-size: 2.8rem;">
#                     {prediction.upper()}
#                 </h1>
#                 <p style="margin-top: 1rem; font-size: 1rem; opacity: 0.95;">
#                     This crop is best suited for the given
#                     soil and weather conditions.
#                 </p>
#             </div>
#             """,
#             unsafe_allow_html=True
#         )
#     else:
#         st.markdown(
#             """
#             <div class="placeholder-card">
#                 <div style="font-size: 5rem;">🌾</div>
#                 <h3>Your crop recommendation will appear here</h3>
#                 <p>
#                     Enter the input values and click
#                     <b>Predict Best Crop</b>.
#                 </p>
#             </div>
#             """,
#             unsafe_allow_html=True
#         )

# # ---------------- Footer ----------------
# st.markdown(
#     '<div class="footer">Built with Python, Scikit-learn and Streamlit</div>',
#     unsafe_allow_html=True
# )

# import streamlit as st
# from src.predict import predict_crop

# # Page config
# st.set_page_config(
#     page_title="AgriSense",
#     page_icon="🌱",
#     layout="wide"
# )

# # Custom CSS
# st.markdown("""
# <style>
# .main {
#     background: linear-gradient(135deg, #e8f5e9, #ffffff);
# }

# .title {
#     font-size: 3rem;
#     font-weight: 700;
#     color: #2e7d32;
#     text-align: center;
# }

# .subtitle {
#     font-size: 1.2rem;
#     color: #555;
#     text-align: center;
#     margin-bottom: 2rem;
# }

# .result-box {
#     background: linear-gradient(135deg, #43a047, #66bb6a);
#     padding: 2rem;
#     border-radius: 20px;
#     color: white;
#     text-align: center;
#     box-shadow: 0 8px 24px rgba(0,0,0,0.15);
#     margin-top: 2rem;
# }

# .metric-card {
#     background: #ffffff;
#     padding: 1rem;
#     border-radius: 15px;
#     box-shadow: 0 4px 12px rgba(0,0,0,0.08);
# }
# </style>
# """, unsafe_allow_html=True)

# # Crop emojis
# crop_emojis = {
#     "rice": "🌾",
#     "maize": "🌽",
#     "chickpea": "🫘",
#     "kidneybeans": "🫘",
#     "pigeonpeas": "🌱",
#     "mothbeans": "🫘",
#     "mungbean": "🫘",
#     "blackgram": "🫘",
#     "lentil": "🥣",
#     "pomegranate": "🍎",
#     "banana": "🍌",
#     "mango": "🥭",
#     "grapes": "🍇",
#     "watermelon": "🍉",
#     "muskmelon": "🍈",
#     "apple": "🍎",
#     "orange": "🍊",
#     "papaya": "🍈",
#     "coconut": "🥥",
#     "cotton": "☁️",
#     "jute": "🧵",
#     "coffee": "☕"
# }

# # Header
# st.markdown('<div class="title">🌱 AgriSense</div>', unsafe_allow_html=True)
# st.markdown(
#     '<div class="subtitle">AI-Powered Smart Crop Planning Advisor</div>',
#     unsafe_allow_html=True
# )

# # Sidebar inputs
# st.sidebar.header("🧪 Soil & Weather Inputs")

# N = st.sidebar.number_input("Nitrogen (N)", min_value=0.0, value=90.0)
# P = st.sidebar.number_input("Phosphorus (P)", min_value=0.0, value=42.0)
# K = st.sidebar.number_input("Potassium (K)", min_value=0.0, value=43.0)

# temperature = st.sidebar.number_input(
#     "Temperature (°C)", value=20.8
# )
# humidity = st.sidebar.number_input(
#     "Humidity (%)", min_value=0.0, max_value=100.0, value=82.0
# )
# ph = st.sidebar.number_input(
#     "pH", min_value=0.0, max_value=14.0, value=6.5
# )
# rainfall = st.sidebar.number_input(
#     "Rainfall (mm)", min_value=0.0, value=202.9
# )

# # Main content
# col1, col2, col3 = st.columns(3)

# with col1:
#     st.metric("Nitrogen", N)

# with col2:
#     st.metric("Temperature", f"{temperature} °C")

# with col3:
#     st.metric("pH", ph)

# st.write("")

# # Predict button
# if st.button("🔍 Predict Best Crop", use_container_width=True):
#     features = [N, P, K, temperature, humidity, ph, rainfall]
#     prediction = predict_crop(features)

#     emoji = crop_emojis.get(prediction.lower(), "🌿")

#     st.markdown(
#         f"""
#         <div class="result-box">
#             <h1>{emoji}</h1>
#             <h2>Recommended Crop</h2>
#             <h1>{prediction.upper()}</h1>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

# # Footer
# st.markdown("---")
# st.caption(
#     "Built with Streamlit and Scikit-learn | "
#     "AgriSense Smart Crop Planning Advisor"
# )

# ---------------------------------------------------------------------------------------------------------
# import streamlit as st
# from src.predict import predict_crop

# st.set_page_config(
#     page_title="AgriSense",
#     page_icon="🌱",
#     layout="centered"
# )

# st.title("🌱 AgriSense")
# st.subheader("Smart Crop Planning Advisor")

# st.write("Enter soil and climate values to get the best crop recommendation.")

# # Input fields
# N = st.number_input("Nitrogen (N)", value=90)
# P = st.number_input("Phosphorus (P)", value=42)
# K = st.number_input("Potassium (K)", value=43)

# temperature = st.number_input("Temperature (°C)", value=20.8)
# humidity = st.number_input("Humidity (%)", value=82.0)
# ph = st.number_input("pH", value=6.5)
# rainfall = st.number_input("Rainfall (mm)", value=202.9)

# # Predict button
# if st.button("Predict Crop"):
#     features = [N, P, K, temperature, humidity, ph, rainfall]
#     prediction = predict_crop(features)

=======
import streamlit as st
from src.predict import predict_crop

st.set_page_config(page_title="AgriSense", page_icon="🌱", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp { background: #fffef5; }
.block-container { padding: 2rem 3rem; max-width: 1100px; }
div.stButton > button {
    background: #14532d; color: white; border: none;
    border-radius: 8px; font-weight: 600;
}
div.stButton > button:hover { background: #166534; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align:center'>🌱 AgriSense</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#6b7280;margin-top:-10px'>Smart Crop Planning Advisor</p>", unsafe_allow_html=True)
st.divider()

def get_reason(n, p, k, temp, humidity, ph, rain):
    if rain > 180 and humidity > 75:
        return "Thrives in high moisture and rainfall conditions."
    if temp > 28 and humidity > 80:
        return "Loves warm, humid tropical climate."
    if n > 80 and rain > 150:
        return "High nitrogen and good rainfall support strong growth."
    if ph < 6.0 and temp > 20:
        return "Prefers slightly acidic soil with warm temperatures."
    if rain < 70:
        return "Well suited for dry conditions with low water need."
    if k > 60:
        return "Rich potassium levels boost yield and disease resistance."
    return "Soil nutrients and climate are well balanced for this crop."

left, right = st.columns([1.1, 0.9], gap="large")

with left:
    c1, c2 = st.columns(2)
    with c1:
        N = st.number_input("Nitrogen (N)", value=90.0)
        K = st.number_input("Potassium (K)", value=43.0)
        humidity = st.number_input("Humidity (%)", value=82.0)
        ph = st.number_input("Soil pH", value=6.5)
    with c2:
        P = st.number_input("Phosphorus (P)", value=42.0)
        temperature = st.number_input("Temperature (°C)", value=20.8)
        rainfall = st.number_input("Rainfall (mm)", value=202.9)
    predict = st.button("Predict Best Crop", use_container_width=True)

with right:
    EMOJI = {"rice":"🌾","maize":"🌽","banana":"🍌","mango":"🥭","grapes":"🍇",
             "watermelon":"🍉","apple":"🍎","orange":"🍊","coconut":"🥥","coffee":"☕",
             "cotton":"🌿","chickpea":"🫘","kidneybeans":"🫘","lentil":"🥣",
             "pigeonpeas":"🌱","mungbean":"🫘","blackgram":"🫘","papaya":"🍈"}

    if predict:
        crop = predict_crop([N, P, K, temperature, humidity, ph, rainfall])
        emoji = EMOJI.get(crop.lower(), "🌿")
        reason = get_reason(N, P, K, temperature, humidity, ph, rainfall)
        st.markdown(f"""
        <div style="background:white;border-radius:14px;padding:2.5rem 2rem;text-align:center;
                    border:1px solid #e5e7eb;min-height:340px;">
            <div style="font-size:3.5rem">{emoji}</div>
            <div style="font-size:0.7rem;color:#9ca3af;letter-spacing:.1em;margin:10px 0 4px">RECOMMENDED CROP</div>
            <div style="font-size:2.2rem;font-weight:700;color:#14532d;margin-bottom:1rem">{crop.title()}</div>
            <div style="background:#f0fdf4;border-radius:10px;padding:0.8rem 1rem;
                        font-size:0.85rem;color:#374151;text-align:left;margin-bottom:1rem">
                <span style="font-weight:600;color:#15803d">Why this crop?</span><br>{reason}
            </div>
            <div style="font-size:0.78rem;color:#9ca3af">
                pH {ph} · Rain {rainfall:.0f}mm · N–P–K {int(N)}–{int(P)}–{int(K)}
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="border-radius:14px;padding:2.5rem 2rem;text-align:center;
                    border:1px dashed #d1d5db;color:#9ca3af;min-height:340px;
                    display:flex;flex-direction:column;align-items:center;justify-content:center;">
            <div style="font-size:2.5rem">🌾</div>
            <div style="margin-top:0.5rem;font-size:0.85rem">Fill values and click predict</div>
        </div>
        """, unsafe_allow_html=True)
# import streamlit as st
# from src.predict import predict_crop

# st.set_page_config(page_title="AgriSense", page_icon="🌱", layout="wide")

# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

# html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

# .stApp {
#     background: radial-gradient(ellipse at top left, #d1fae5 0%, #f9fdf9 40%),
#                 radial-gradient(ellipse at bottom right, #fef9c3 0%, #f9fdf9 50%);
#     min-height: 100vh;
# }

# .block-container { padding: 2.5rem 4rem 2rem; max-width: 1280px; }

# .ag-header { text-align: center; margin-bottom: 2.2rem; }
# .ag-logo-row {
#     display: flex; align-items: center;
#     justify-content: center; gap: 12px; margin-bottom: 4px;
# }
# .ag-logo-row h1 { font-size: 2.8rem; font-weight: 800; color: #1a6b2f; margin: 0; }
# .ag-tagline { font-size: 0.95rem; font-weight: 600; color: #3a8a4a; margin-bottom: 5px; }
# .ag-sub { font-size: 0.85rem; color: #6b7280; }

# .ag-card {
#     background: rgba(255,255,255,0.88);
#     backdrop-filter: blur(12px);
#     border: 1px solid rgba(255,255,255,0.95);
#     border-radius: 22px; padding: 2rem;
#     box-shadow: 0 4px 20px rgba(0,0,0,0.05);
# }

# .ag-card-title { font-size: 1.05rem; font-weight: 700; color: #111827; }
# .ag-title-row {
#     display: flex; align-items: center;
#     justify-content: space-between; margin-bottom: 1.4rem;
# }
# .ag-field-label {
#     font-size: 0.82rem; font-weight: 600;
#     color: #374151; margin-bottom: 3px;
# }
# .ag-field-label span { font-weight: 400; color: #9ca3af; }

# div[data-testid="stNumberInput"] > div > div > input {
#     border-radius: 100px !important;
#     border: 1.5px solid #e5e7eb !important;
#     padding: 10px 18px !important;
#     font-size: 0.9rem !important;
#     background: rgba(255,255,255,0.95) !important;
#     box-shadow: none !important;
# }
# div[data-testid="stNumberInput"] > div > div > input:focus {
#     border-color: #22c55e !important;
#     box-shadow: 0 0 0 3px rgba(34,197,94,.1) !important;
# }

# div.stButton > button {
#     background: linear-gradient(135deg, #16a34a, #22c55e);
#     color: white; border: none; border-radius: 100px;
#     padding: 0.78rem 1rem; font-size: 0.98rem; font-weight: 700;
#     width: 100%; margin-top: 1.1rem;
#     box-shadow: 0 4px 14px rgba(22,163,74,.3); transition: .25s ease;
# }
# div.stButton > button:hover {
#     transform: translateY(-2px);
#     box-shadow: 0 8px 22px rgba(22,163,74,.35);
# }

# .ag-idle {
#     display: flex; flex-direction: column;
#     align-items: center; justify-content: center;
#     min-height: 440px; text-align: center; gap: .9rem;
# }
# .ag-idle-circle {
#     width: 110px; height: 110px; border-radius: 50%;
#     background: #f0fdf4;
#     display: flex; align-items: center; justify-content: center;
#     font-size: 3rem;
# }
# .ag-idle h3 { font-size: 1.1rem; font-weight: 700; color: #16a34a; margin: 0; }
# .ag-idle p  { font-size: 0.83rem; color: #9ca3af; margin: 0; max-width: 210px; line-height: 1.5; }

# .ag-result {
#     display: flex; flex-direction: column;
#     align-items: center; justify-content: center;
#     min-height: 440px; text-align: center; padding: 1rem 0;
# }
# .ag-result-circle {
#     width: 120px; height: 120px; border-radius: 50%;
#     background: linear-gradient(135deg, #dcfce7, #bbf7d0);
#     display: flex; align-items: center; justify-content: center;
#     font-size: 3.5rem; margin-bottom: 1.1rem;
#     box-shadow: 0 8px 24px rgba(34,197,94,.18);
# }
# .ag-result-tag {
#     font-size: 0.68rem; letter-spacing: .12em;
#     text-transform: uppercase; color: #6b7280;
#     font-weight: 600; margin-bottom: 3px;
# }
# .ag-result-crop {
#     font-size: 2.3rem; font-weight: 800;
#     color: #14532d; margin-bottom: 1.1rem; line-height: 1;
# }
# .ag-insight {
#     background: #f0fdf4; border-left: 3px solid #22c55e;
#     border-radius: 0 12px 12px 0;
#     padding: .8rem 1rem; text-align: left;
#     width: 100%; margin-bottom: 1.1rem;
# }
# .ag-insight p { font-size: 0.84rem; color: #374151; line-height: 1.6; margin: 0; }
# .ag-metrics { display: flex; flex-wrap: wrap; gap: 6px; justify-content: center; }
# .ag-metric {
#     font-size: 0.77rem; font-weight: 500;
#     background: #f0fdf4; color: #166534;
#     border: 1px solid #bbf7d0;
#     padding: 4px 12px; border-radius: 100px;
# }

# .ag-footer { text-align:center; margin-top:1.8rem; font-size:.76rem; color:#9ca3af; }
# </style>
# """, unsafe_allow_html=True)

# CROP_EMOJI = {
#     "rice":"🌾","maize":"🌽","chickpea":"🫘","kidneybeans":"🫘",
#     "pigeonpeas":"🌱","mungbean":"🫘","blackgram":"🫘","lentil":"🥣",
#     "banana":"🍌","mango":"🥭","grapes":"🍇","watermelon":"🍉",
#     "apple":"🍎","orange":"🍊","papaya":"🍈","coconut":"🥥",
#     "cotton":"🌿","coffee":"☕",
# }

# def get_insight(n, p, k, rain):
#     tips = []
#     if n > 70:     tips.append("High nitrogen will accelerate vegetative growth.")
#     if p > 50:     tips.append("Strong phosphorus boosts root development.")
#     if k > 50:     tips.append("Rich potassium improves disease resistance.")
#     if rain > 150: tips.append("Ample rainfall suits this water-intensive variety.")
#     elif rain < 70:tips.append("Low water need makes it ideal for dry conditions.")
#     if not tips:   tips.append("Your balanced soil profile is optimal for this crop.")
#     return " ".join(tips[:2])

# # ── Header ────────────────────────────────────────────────────────────────────
# st.markdown("""
# <div class="ag-header">
#   <div class="ag-logo-row">
#     <span style="font-size:2.6rem">🌱</span>
#     <h1>AgriSense</h1>
#   </div>
#   <div class="ag-tagline">Smart Crop Planning Advisor</div>
#   <div class="ag-sub">Enter soil and climate parameters to get AI-powered crop recommendations.</div>
# </div>
# """, unsafe_allow_html=True)

# # ── Layout ────────────────────────────────────────────────────────────────────
# left, right = st.columns([1, 1], gap="large")

# with left:
#     st.markdown('<div class="ag-card">', unsafe_allow_html=True)
#     st.markdown("""
#     <div class="ag-title-row">
#       <span class="ag-card-title">Soil &amp; Climate Inputs</span>
#       <span style="font-size:0.8rem;font-weight:500;color:#16a34a;">Use sample</span>
#     </div>
#     """, unsafe_allow_html=True)

#     c1, c2 = st.columns(2)
#     with c1:
#         st.markdown('<div class="ag-field-label">Nitrogen (N) <span>mg/kg</span></div>', unsafe_allow_html=True)
#         N = st.number_input("N", min_value=0.0, max_value=140.0, value=None, placeholder="e.g. 90", label_visibility="collapsed")

#         st.markdown('<div class="ag-field-label">Potassium (K) <span>mg/kg</span></div>', unsafe_allow_html=True)
#         K = st.number_input("K", min_value=0.0, max_value=205.0, value=None, placeholder="e.g. 43", label_visibility="collapsed")

#         st.markdown('<div class="ag-field-label">Humidity <span>%</span></div>', unsafe_allow_html=True)
#         humidity = st.number_input("Humidity", min_value=0.0, max_value=100.0, value=None, placeholder="e.g. 80", label_visibility="collapsed")

#     with c2:
#         st.markdown('<div class="ag-field-label">Phosphorus (P) <span>mg/kg</span></div>', unsafe_allow_html=True)
#         P = st.number_input("P", min_value=0.0, max_value=145.0, value=None, placeholder="e.g. 42", label_visibility="collapsed")

#         st.markdown('<div class="ag-field-label">Temperature <span>°C</span></div>', unsafe_allow_html=True)
#         temperature = st.number_input("Temp", min_value=0.0, max_value=50.0, value=None, placeholder="e.g. 24.5", label_visibility="collapsed")

#         st.markdown('<div class="ag-field-label">pH</div>', unsafe_allow_html=True)
#         ph = st.number_input("pH", min_value=0.0, max_value=14.0, value=None, placeholder="e.g. 6.5", label_visibility="collapsed")

#     st.markdown('<div class="ag-field-label" style="margin-top:2px;">Rainfall <span>mm</span></div>', unsafe_allow_html=True)
#     rainfall = st.number_input("Rainfall", min_value=0.0, max_value=300.0, value=None, placeholder="e.g. 200", label_visibility="collapsed")

#     predict = st.button("🔍  Predict Best Crop")
#     st.markdown('</div>', unsafe_allow_html=True)

# with right:
#     st.markdown('<div class="ag-card">', unsafe_allow_html=True)

#     all_filled = all(v is not None for v in [N, P, K, temperature, humidity, ph, rainfall])

#     if predict and not all_filled:
#         st.warning("Please fill in all 7 fields before predicting.", icon="⚠️")

#     if predict and all_filled:
#         crop   = predict_crop([N, P, K, temperature, humidity, ph, rainfall])
#         emoji  = CROP_EMOJI.get(crop.lower(), "🌿")
#         reason = get_insight(N, P, K, rainfall)
#         st.markdown(f"""
#         <div class="ag-result">
#           <div class="ag-result-circle">{emoji}</div>
#           <div class="ag-result-tag">recommended crop</div>
#           <div class="ag-result-crop">{crop.title()}</div>
#           <div class="ag-insight"><p>💡 {reason}</p></div>
#           <div class="ag-metrics">
#             <span class="ag-metric">pH {ph:.1f}</span>
#             <span class="ag-metric">Rain {rainfall:.0f} mm</span>
#             <span class="ag-metric">N–P–K &nbsp;{int(N)}–{int(P)}–{int(K)}</span>
#             <span class="ag-metric">{temperature:.1f}°C · {humidity:.0f}% RH</span>
#           </div>
#         </div>
#         """, unsafe_allow_html=True)
#         st.balloons()
#     else:
#         st.markdown("""
#         <div class="ag-idle">
#           <div class="ag-idle-circle">🌿</div>
#           <h3>Awaiting your inputs</h3>
#           <p>Your crop recommendation will appear here.</p>
#         </div>
#         """, unsafe_allow_html=True)

#     st.markdown('</div>', unsafe_allow_html=True)

# st.markdown(
#     '<div class="ag-footer">AgriSense · Python · Scikit-learn · Streamlit</div>',
#     unsafe_allow_html=True
# )

# import streamlit as st
# from src.predict import predict_crop

# # ---------------- Page Config ----------------
# st.set_page_config(
#     page_title="AgriSense",
#     page_icon="🌱",
#     layout="wide"
# )

# # ---------------- Custom CSS ----------------
# st.markdown("""
# <style>
# .stApp {
#     background: linear-gradient(135deg, #e8f5e9 0%, #ffffff 100%);
# }

# .block-container {
#     padding-top: 2rem;
#     padding-bottom: 2rem;
#     max-width: 1200px;
# }

# .main-title {
#     font-size: 3.5rem;
#     font-weight: 800;
#     color: #1b5e20;
#     text-align: center;
#     margin-bottom: 0;
# }

# .sub-title {
#     font-size: 1.2rem;
#     color: #4b5563;
#     text-align: center;
#     margin-bottom: 2rem;
# }

# .glass-card {
#     background: rgba(255, 255, 255, 0.85);
#     border-radius: 24px;
#     padding: 2rem;
#     box-shadow: 0 12px 30px rgba(0, 0, 0, 0.08);
#     backdrop-filter: blur(10px);
# }

# .result-card {
#     background: linear-gradient(135deg, #2e7d32, #66bb6a);
#     color: white;
#     border-radius: 24px;
#     padding: 3rem 2rem;
#     text-align: center;
#     box-shadow: 0 15px 35px rgba(46, 125, 50, 0.25);
#     min-height: 420px;
#     display: flex;
#     flex-direction: column;
#     justify-content: center;
# }

# .placeholder-card {
#     background: rgba(255, 255, 255, 0.85);
#     border-radius: 24px;
#     padding: 3rem 2rem;
#     text-align: center;
#     box-shadow: 0 12px 30px rgba(0, 0, 0, 0.08);
#     min-height: 420px;
#     display: flex;
#     flex-direction: column;
#     justify-content: center;
# }

# .footer {
#     text-align: center;
#     margin-top: 2rem;
#     color: #6b7280;
#     font-size: 0.9rem;
# }

# div.stButton > button {
#     background: linear-gradient(135deg, #2e7d32, #43a047);
#     color: white;
#     font-weight: 600;
#     border: none;
#     border-radius: 12px;
#     padding: 0.8rem 1.2rem;
#     width: 100%;
#     transition: 0.3s;
# }

# div.stButton > button:hover {
#     transform: translateY(-2px);
#     box-shadow: 0 8px 20px rgba(46, 125, 50, 0.25);
# }
# </style>
# """, unsafe_allow_html=True)

# # ---------------- Crop Emojis ----------------
# crop_emojis = {
#     "rice": "🌾",
#     "maize": "🌽",
#     "chickpea": "🫘",
#     "kidneybeans": "🫘",
#     "pigeonpeas": "🌱",
#     "mungbean": "🫘",
#     "blackgram": "🫘",
#     "lentil": "🥣",
#     "banana": "🍌",
#     "mango": "🥭",
#     "grapes": "🍇",
#     "watermelon": "🍉",
#     "apple": "🍎",
#     "orange": "🍊",
#     "papaya": "🍈",
#     "coconut": "🥥",
#     "cotton": "☁️",
#     "coffee": "☕"
# }

# # ---------------- Header ----------------
# st.markdown(
#     '<h1 class="main-title">🌱 AgriSense</h1>',
#     unsafe_allow_html=True
# )

# st.markdown(
#     '<p class="sub-title">AI-Powered Smart Crop Planning Advisor</p>',
#     unsafe_allow_html=True
# )

# # ---------------- Layout ----------------
# left_col, right_col = st.columns([1.1, 0.9], gap="large")

# # ---------------- Input Form ----------------
# with left_col:
#     st.markdown('<div class="glass-card">', unsafe_allow_html=True)

#     st.subheader("🧪 Soil & Climate Inputs")

#     col1, col2 = st.columns(2)

#     with col1:
#         N = st.number_input("Nitrogen (N)", value=90.0)
#         P = st.number_input("Phosphorus (P)", value=42.0)
#         K = st.number_input("Potassium (K)", value=43.0)
#         temperature = st.number_input("Temperature (°C)", value=20.8)

#     with col2:
#         humidity = st.number_input("Humidity (%)", value=82.0)
#         ph = st.number_input("pH", value=6.5)
#         rainfall = st.number_input("Rainfall (mm)", value=202.9)

#     predict_button = st.button("🔍 Predict Best Crop")

#     st.markdown('</div>', unsafe_allow_html=True)

# # ---------------- Result Panel ----------------
# with right_col:
#     if predict_button:
#         features = [N, P, K, temperature, humidity, ph, rainfall]
#         prediction = predict_crop(features)

#         emoji = crop_emojis.get(prediction.lower(), "🌿")

#         st.markdown(
#             f"""
#             <div class="result-card">
#                 <div style="font-size: 5rem;">{emoji}</div>
#                 <p style="font-size: 1rem; opacity: 0.9;">
#                     Recommended Crop
#                 </p>
#                 <h1 style="margin: 0; font-size: 2.8rem;">
#                     {prediction.upper()}
#                 </h1>
#                 <p style="margin-top: 1rem; font-size: 1rem; opacity: 0.95;">
#                     This crop is best suited for the given
#                     soil and weather conditions.
#                 </p>
#             </div>
#             """,
#             unsafe_allow_html=True
#         )
#     else:
#         st.markdown(
#             """
#             <div class="placeholder-card">
#                 <div style="font-size: 5rem;">🌾</div>
#                 <h3>Your crop recommendation will appear here</h3>
#                 <p>
#                     Enter the input values and click
#                     <b>Predict Best Crop</b>.
#                 </p>
#             </div>
#             """,
#             unsafe_allow_html=True
#         )

# # ---------------- Footer ----------------
# st.markdown(
#     '<div class="footer">Built with Python, Scikit-learn and Streamlit</div>',
#     unsafe_allow_html=True
# )

# import streamlit as st
# from src.predict import predict_crop

# # Page config
# st.set_page_config(
#     page_title="AgriSense",
#     page_icon="🌱",
#     layout="wide"
# )

# # Custom CSS
# st.markdown("""
# <style>
# .main {
#     background: linear-gradient(135deg, #e8f5e9, #ffffff);
# }

# .title {
#     font-size: 3rem;
#     font-weight: 700;
#     color: #2e7d32;
#     text-align: center;
# }

# .subtitle {
#     font-size: 1.2rem;
#     color: #555;
#     text-align: center;
#     margin-bottom: 2rem;
# }

# .result-box {
#     background: linear-gradient(135deg, #43a047, #66bb6a);
#     padding: 2rem;
#     border-radius: 20px;
#     color: white;
#     text-align: center;
#     box-shadow: 0 8px 24px rgba(0,0,0,0.15);
#     margin-top: 2rem;
# }

# .metric-card {
#     background: #ffffff;
#     padding: 1rem;
#     border-radius: 15px;
#     box-shadow: 0 4px 12px rgba(0,0,0,0.08);
# }
# </style>
# """, unsafe_allow_html=True)

# # Crop emojis
# crop_emojis = {
#     "rice": "🌾",
#     "maize": "🌽",
#     "chickpea": "🫘",
#     "kidneybeans": "🫘",
#     "pigeonpeas": "🌱",
#     "mothbeans": "🫘",
#     "mungbean": "🫘",
#     "blackgram": "🫘",
#     "lentil": "🥣",
#     "pomegranate": "🍎",
#     "banana": "🍌",
#     "mango": "🥭",
#     "grapes": "🍇",
#     "watermelon": "🍉",
#     "muskmelon": "🍈",
#     "apple": "🍎",
#     "orange": "🍊",
#     "papaya": "🍈",
#     "coconut": "🥥",
#     "cotton": "☁️",
#     "jute": "🧵",
#     "coffee": "☕"
# }

# # Header
# st.markdown('<div class="title">🌱 AgriSense</div>', unsafe_allow_html=True)
# st.markdown(
#     '<div class="subtitle">AI-Powered Smart Crop Planning Advisor</div>',
#     unsafe_allow_html=True
# )

# # Sidebar inputs
# st.sidebar.header("🧪 Soil & Weather Inputs")

# N = st.sidebar.number_input("Nitrogen (N)", min_value=0.0, value=90.0)
# P = st.sidebar.number_input("Phosphorus (P)", min_value=0.0, value=42.0)
# K = st.sidebar.number_input("Potassium (K)", min_value=0.0, value=43.0)

# temperature = st.sidebar.number_input(
#     "Temperature (°C)", value=20.8
# )
# humidity = st.sidebar.number_input(
#     "Humidity (%)", min_value=0.0, max_value=100.0, value=82.0
# )
# ph = st.sidebar.number_input(
#     "pH", min_value=0.0, max_value=14.0, value=6.5
# )
# rainfall = st.sidebar.number_input(
#     "Rainfall (mm)", min_value=0.0, value=202.9
# )

# # Main content
# col1, col2, col3 = st.columns(3)

# with col1:
#     st.metric("Nitrogen", N)

# with col2:
#     st.metric("Temperature", f"{temperature} °C")

# with col3:
#     st.metric("pH", ph)

# st.write("")

# # Predict button
# if st.button("🔍 Predict Best Crop", use_container_width=True):
#     features = [N, P, K, temperature, humidity, ph, rainfall]
#     prediction = predict_crop(features)

#     emoji = crop_emojis.get(prediction.lower(), "🌿")

#     st.markdown(
#         f"""
#         <div class="result-box">
#             <h1>{emoji}</h1>
#             <h2>Recommended Crop</h2>
#             <h1>{prediction.upper()}</h1>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

# # Footer
# st.markdown("---")
# st.caption(
#     "Built with Streamlit and Scikit-learn | "
#     "AgriSense Smart Crop Planning Advisor"
# )

# ---------------------------------------------------------------------------------------------------------
# import streamlit as st
# from src.predict import predict_crop

# st.set_page_config(
#     page_title="AgriSense",
#     page_icon="🌱",
#     layout="centered"
# )

# st.title("🌱 AgriSense")
# st.subheader("Smart Crop Planning Advisor")

# st.write("Enter soil and climate values to get the best crop recommendation.")

# # Input fields
# N = st.number_input("Nitrogen (N)", value=90)
# P = st.number_input("Phosphorus (P)", value=42)
# K = st.number_input("Potassium (K)", value=43)

# temperature = st.number_input("Temperature (°C)", value=20.8)
# humidity = st.number_input("Humidity (%)", value=82.0)
# ph = st.number_input("pH", value=6.5)
# rainfall = st.number_input("Rainfall (mm)", value=202.9)

# # Predict button
# if st.button("Predict Crop"):
#     features = [N, P, K, temperature, humidity, ph, rainfall]
#     prediction = predict_crop(features)

>>>>>>> 19137ea1d5975c14c34245cd8df0c89bb93be8b7
#     st.success(f"Recommended Crop: {prediction.upper()}")
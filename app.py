import streamlit as st
import math
import requests

# --- PAGE CONFIG ---
st.set_page_config(page_title="Astrophysics Research Portal", layout="wide", page_icon="🔭")

# --- NASA APOD INTEGRATION ---
def get_nasa_picture():
    url = "https://nasa.gov"
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except:
        return None

# --- PROFESSIONAL SCIENTIFIC STYLING ---
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; color: #E0E0E0; }
    .stApp { background-color: #050505; }
    h1, h2, h3 { font-family: 'Roboto Mono', monospace; color: #FFFFFF; }
    .stMetric { background: #111; padding: 10px; border-radius: 10px; border: 1px solid #333; }
    a { color: #4A90E2 !important; text-decoration: none; font-weight: 600; }
    a:hover { text-decoration: underline; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("Astro-Portal v2.9")
    st.markdown("---")
    menu = st.selectbox("Navigation", 
                        ["Dashboard", "Scientific Calculator", "Fundamental Forces", "Laws of Motion", "People", "My Projects"])
    
    st.markdown("---")
    st.markdown("### 🧮 Fast-Calc Tool")
    val = st.number_input("Input Value", value=1.0)
    op = st.selectbox("Operation", ["Square Root", "Natural Log", "log10", "Square"])
    if st.button("Compute"):
        if op == "Square Root": res = math.sqrt(val)
        elif op == "Natural Log": res = math.log(val)
        elif op == "log10": res = math.log10(val)
        else: res = val**2
        st.code(f"Result: {res}")

    st.markdown("---")
    st.markdown("🌐 [Official NASA Website](https://nasa.gov)")

# --- DASHBOARD (NASA FEED) ---
if menu == "Dashboard":
    st.header("Live Cosmic Observation")
    nasa_data = get_nasa_picture()
    if nasa_data and "url" in nasa_data:
        st.image(nasa_data["url"], caption=f"Observation: {nasa_data.get('title', 'Unknown')}", use_container_width=True)
    else:
        st.image("https://unsplash.com", use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 🔍 Global Research Search")
    query = st.text_input("", placeholder="Search astrophysics archives...")
    
    st.markdown("""
    **🔭 Quick Access Research Databases:**
    *   [NASA ADS (Astrophysics Data System)](https://harvard.edu)
    *   [ArXiv (Astrophysics Pre-prints)](https://arxiv.org)
    *   [SIMBAD Astronomical Database](http://u-strasbg.fr)
    *   [ESA Sky (Star Map)](https://esa.int)
    """)

# --- CALCULATORS & FORCES ---
elif menu == "Scientific Calculator":
    st.header("Physics Computation Lab")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Gravity Calculator")
        m1 = st.number_input("Mass 1 (kg)", value=5.97e24, format="%.2e")
        m2 = st.number_input("Mass 2 (kg)", value=7.34e22, format="%.2e")
        r = st.number_input("Distance (m)", value=3.84e8, format="%.2e")
        G = 6.67430e-11
        force = G * (m1 * m2) / (r**2)
        st.metric("Gravitational Force", f"{force:.2e} N")
    with col2:
        st.subheader("Energy-Mass Equivalence")
        mass = st.number_input("Object Mass (kg)", value=1.0)
        c = 3e8
        energy = mass * (c**2)
        st.metric("Energy (Joules)", f"{energy:.2e} J")

elif menu == "Fundamental Forces":
    st.header("The Four Fundamental Forces")
    forces = {"Gravity": "Governs planetary and galactic motion.", "Electromagnetism": "Controls light and atomic structure.", "Weak Nuclear": "Responsible for radioactive decay.", "Strong Nuclear": "Holds atomic nuclei together."}
    for f, desc in forces.items():
        with st.expander(f): st.write(desc)

elif menu == "Laws of Motion":
    st.header("Newtonian Dynamics")
    st.markdown("1. **Inertia**")
    st.latex(r"F = ma")
    st.markdown("2. **Acceleration**")
    st.markdown("3. **Reaction**")

# --- PEOPLE (NEW ROBUST IMAGE LINKS) ---
elif menu == "People":
    st.header("Scientific Pioneers")
    st.write("Explorers of the fundamental laws of nature.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://pixabay.com", caption="Sir Isaac Newton (Historical Profile)")
        st.write("**Classical Mechanics**: Developed the laws of motion and gravitation.")
    with col2:
        st.image("https://pixabay.com", caption="Albert Einstein (Theoretical Physics)")
        st.write("**Relativity**: Theory that revolutionized space and time.")
    with col3:
        st.image("https://pixabay.com", caption="Stephen Hawking (Cosmology Focus)")
        st.write("**Cosmology**: Transformed our understanding of black holes.")

elif menu == "My Projects":
    st.header("Project Repository")
    st.info("Status: Analyzing Gravitational Lensing Data from JWST.")

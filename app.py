import streamlit as st
import math
import requests

# --- PAGE CONFIG ---
st.set_page_config(page_title="Astrophysics Research Portal", layout="wide", page_icon="🔭")

# --- NASA APOD INTEGRATION ---
def get_nasa_picture():
    # Public NASA API for live space images
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
    /* Link styling for professional feel */
    a { color: #4A90E2 !important; text-decoration: none; font-weight: 600; }
    a:hover { text-decoration: underline; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION (TASKBAR) ---
with st.sidebar:
    st.title("Astro-Portal v2.5")
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
    st.markdown("🌐 [Official NASA Website](https://www.nasa.gov/)")

# --- DASHBOARD (LIVE NASA FEED) ---
if menu == "Dashboard":
    st.header("Live Cosmic Observation")
    nasa_data = get_nasa_picture()
    
    if nasa_data and "url" in nasa_data:
        st.image(nasa_data["url"], caption=f"Observation: {nasa_data.get('title', 'Unknown')}", use_container_width=True)
        with st.expander("Read Scientific Briefing"):
            st.write(nasa_data.get("explanation", "Data stream active, briefing loading..."))
    else:
        st.warning("Deep space connection unstable. Using JWST backup archives.")
        st.image("https://nasa.gov", use_container_width=True)

    st.markdown("---")
    st.markdown("### 🔍 Global Research Search")
    query = st.text_input("", placeholder="Search archives for G.U.T., Newton, or Spacetime...")
    if query: st.info(f"Initiating archival search for: '{query}'...")
    
    # NEW: Quick Access Links at the bottom of searchbar
    st.markdown("""
    **Quick Access Research Databases:**
    *   [NASA ADS (Astrophysics Data System)](https://harvard.edu)
    *   [ArXiv Astrophysics Pre-prints](https://arxiv.org)
    *   [SIMBAD Astronomical Database](http://u-strasbg.fr)
    """)

# --- SCIENTIFIC CALCULATOR ---
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

# --- FUNDAMENTAL FORCES ---
elif menu == "Fundamental Forces":
    st.header("The Four Fundamental Forces")
    forces = {
        "Gravity": "Weakest force, infinite range. Governs planetary and galactic motion.",
        "Electromagnetism": "Between charged particles. Controls light, magnetism, and atomic bonds.",
        "Weak Nuclear": "Short range. Responsible for radioactive beta decay in stars.",
        "Strong Nuclear": "Strongest force. Holds quarks together to form protons and neutrons."
    }
    for f, desc in forces.items():
        with st.expander(f): st.write(desc)

# --- LAWS OF MOTION ---
elif menu == "Laws of Motion":
    st.header("Newtonian Dynamics")
    st.markdown("1. **Inertia**: Velocity remains constant unless a net force acts.")
    st.latex(r"F = ma")
    st.markdown("2. **Acceleration**: Directly proportional to force, inversely to mass.")
    st.markdown("3. **Reaction**: Every action has an equal and opposite reaction.")

# --- PEOPLE (SCIENTIST PORTRAITS) ---
elif menu == "People":
    st.header("Scientific Pioneers")
    st.write("Explorers of the fundamental laws of nature.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://wikimedia.org", caption="Sir Isaac Newton")
        st.write("**Classical Mechanics**: Developed the laws of motion and gravitation.")
    with col2:
        st.image("https://wikimedia.org", caption="Albert Einstein")
        st.write("**Relativity**: Revolutionized space, time, and gravity.")
    with col3:
        st.image("https://wikimedia.org", caption="Stephen Hawking")
        st.write("**Cosmology**: Transformed our understanding of black holes.")

# --- MY PROJECTS ---
elif menu == "My Projects":
    st.header("Project Repository")
    st.info("Current Analysis: Gravitational Lensing Data from JWST Observations.")
    st.info("Archive: Theoretical groundwork for Grand Unified Field Theory.")

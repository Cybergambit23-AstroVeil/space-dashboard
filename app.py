import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Cosmic Explorer", layout="wide", page_icon="🚀")

# --- FUN FONTS & THEMES ---
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    .stApp { font-family: 'Orbitron', sans-serif; }
    h1 {
        font-family: 'Bangers', cursive;
        color: #FFD700;
        text-shadow: 2px 2px #ff4b4b;
        font-size: 3.5rem !important;
        text-align: center;
    }
    /* Search Bar Styling */
    .stTextInput > div > div > input { border-radius: 20px; border: 2px solid #702963; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (THE 3 LINES DROPDOWN MENU) ---
with st.sidebar:
    st.markdown("# 🌌 Navigation")
    mode = st.radio("Display Mode:", ["✨ Starry Night (Dark)", "☀️ Supernova (Light)"])
    st.divider()
    
    # Taskbar content including the requested Gravity Calculator
    menu = st.selectbox("Explore the Universe", 
                        ["Home", "Current Projects", "Equations & Laws", "Wormholes & Black Holes", "Gravity Calculator 🪐", "Space News 🛰️"])
    
    st.divider()
    if st.button("👽 Contact Aliens"):
        st.balloons()
        st.success("Signal sent to Andromeda!")

# --- MAIN CONTENT LOGIC ---
if menu == "Home":
    st.markdown("<h1>🚀 COSMIC DASHBOARD 🚀</h1>")
    st.image("https://nasa.gov", 
             caption="NASA James Webb Deep Field Image", use_container_width=True)
    
    # Search Bar Section
    st.write("### 🔍 Search Research Databases")
    search_query = st.text_input("Find theories or laws...", placeholder="e.g. Newton's Laws or G.U.T.")
    if search_query:
        st.info(f"Scanning deep-space archives for: **{search_query}**... 🛸")

elif menu == "Current Projects":
    st.header("🛸 Active Missions")
    st.write("Current goal: Finding the **Grand Unified Field Theory** to bridge quantum and gravity!")
    st.write("- **Mars AI Mapping**: Finding lava tubes for future colonies.")

elif menu == "Equations & Laws":
    st.header("📜 The Laws of Motion")
    st.latex(r"F = ma")
    st.write("**Newton's Second Law**: Acceleration is produced when a force acts on a mass.")

elif menu == "Wormholes & Black Holes":
    st.header("🕳️ Spacetime Anomalies")
    st.image("https://wikimedia.org", width=500)
    st.warning("Approaching the Event Horizon! Information paradox detected.")

elif menu == "Gravity Calculator 🪐":
    st.header("⚖️ Interplanetary Gravity Lab")
    st.write("Ever wondered how much you would weigh on another world?")
    
    user_weight = st.number_input("Enter your weight on Earth (kg or lbs):", min_value=1.0, value=70.0)
    planet = st.selectbox("Select a Planet:", ["Moon", "Mars", "Jupiter", "Saturn", "Neptune"])
    
    # Gravity factors relative to Earth
    gravity_map = {"Moon": 0.165, "Mars": 0.377, "Jupiter": 2.528, "Saturn": 1.065, "Neptune": 1.137}
    
    new_weight = user_weight * gravity_map[planet]
    st.metric(label=f"Your weight on {planet}", value=f"{round(new_weight, 2)} units")
    st.write(f"The gravity on {planet} is {int(gravity_map[planet]*100)}% of Earth's gravity.")

elif menu == "Space News 🛰️":
    st.header("📰 Latest Galactic News (May 2026)")
    news = [
        "🛸 **UFO Files Declassified**: Pentagon releases new footage [via New York Times](https://nytimes.com).",
        "🌕 **Artemis II Mission**: Crewed lunar fly-around confirmed for next month [via Space.com](https://space.com).",
        "🔭 **James Webb Update**: New detailed images of the [Carina Nebula](https://esawebb.org/images/) revealed."
    ]
    for item in news: st.markdown(item)

# --- LIGHT/DARK MODE TOGGLE ---
if mode == "☀️ Supernova (Light)":
    st.markdown("<style>.stApp { background-color: white; color: black; }</style>", unsafe_allow_html=True)
else:
    st.markdown("<style>.stApp { background-color: #0E1117; color: white; }</style>", unsafe_allow_html=True)

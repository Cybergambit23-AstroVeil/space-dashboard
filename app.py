", use_container_width=True)

    st.markdown("### 🔍 Research Search")
    query = st.text_input("", placeholder="Search astrophysics archives...")
    if query: st.info(f"Searching archives for: '{query}'...")

# --- CALCULATOR SECTION ---
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
        "Gravity": "Weakest force, infinite range. Governs planetary orbits.",
        "Electromagnetism": "Between charged particles. Governs light and atomic structure.",
        "Weak Nuclear": "Short range. Responsible for beta decay in stars.",
        "Strong Nuclear": "Strongest force. Binds protons and neutrons in the nucleus."
    }
    for f, desc in forces.items():
        with st.expander(f): st.write(desc)

# --- LAWS OF MOTION ---
elif menu == "Laws of Motion":
    st.header("Newtonian Dynamics")
    st.markdown("1. **Inertia**: Velocity remains constant unless a net force acts.")
    st.latex(r"F = ma")
    st.markdown("2. **Acceleration**: Proportional to force and inversely to mass.")
    st.markdown("3. **Reaction**: Every action has an equal/opposite reaction.")

# --- PEOPLE ---
elif menu == "People":
    st.header("Scientific Pioneers")
    p1, p2, p3 = st.columns(3)
    with p1:
        st.image("https://wikimedia.org", caption="Isaac Newton")
    with p2:
        st.image("https://wikimedia.org", caption="Albert Einstein")
    with p3:
        st.image("https://wikimedia.org", caption="Stephen Hawking")

# --- MY PROJECTS ---
elif menu == "My Projects":
    st.header("Project Repository")
    st.info("Status: Analyzing Gravitational Lensing Data from JWST.")

import streamlit as st

# Setup the page browser titles
st.set_page_config(page_title="Ashwanth Core OS", page_icon="🤖", layout="wide")

# Custom premium styling for the beautiful split screen layout
st.markdown("""
<style>
    /* Clean background system reset */
    .stApp {
        background-color: #0b0f19;
        color: #ffffff;
    }

    /* Left half side panel design */
    .left-panel {
        background-color: #ffffff;
        color: #111827;
        padding: 3rem;
        border-radius: 20px;
        margin-bottom: 2rem;
    }

    .main-logo-text {
        font-size: 2.2rem;
        font-weight: 800;
        letter-spacing: -1px;
    }

    .main-logo-text span {
        color: #00A878;
    }

    .highlight {
        color: #00A878;
        font-weight: bold;
    }

    /* Premium high-tech login card */
    .login-card {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.15);
        padding: 2.5rem;
        border-radius: 24px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
    }

    /* Glowing audio orb layout styles */
    .orb-container {
        text-align: center;
        margin: 3rem 0;
    }

    .voice-orb {
        width: 130px;
        height: 130px;
        background: #00A878;
        border-radius: 50%;
        display: inline-block;
        box-shadow: 0 0 30px #00C49A;
        animation: floatOrb 2s infinite ease-in-out;
    }

    @keyframes floatOrb {
        0% { transform: scale(1); opacity: 0.9; }
        50% { transform: scale(1.06); opacity: 1; }
        100% { transform: scale(1); opacity: 0.9; }
    }

    /* Custom terminals feed boxes */
    .terminal-box {
        background-color: #111827;
        border: 1px solid #1f293d;
        padding: 1.5rem;
        border-radius: 16px;
        font-family: monospace;
        font-size: 1.1rem;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize application security tracker keys
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "show_password" not in st.session_state:
    st.session_state.show_password = False

# ==========================================
# GATE SCREEN 1: SPLIT SECURE SYSTEM AUTHORIZATION
# ==========================================
if not st.session_state.logged_in:
    col1, col2 = st.columns(2, gap="large")

    # Left Branding Frame Panel Layout
    with col1:
        st.markdown("""
        <div class="left-panel">
            <h2 class="main-logo-text">Ashwanth<span>.AI</span></h2>
            <br><br>
            <span style="font-size: 5rem; opacity: 0.15;">“</span>
            <h1 style="font-size: 2.5rem; font-weight: 800; margin-top:-2rem;">The Ultimate <span class="highlight">Voice Terminal</span></h1>
            <p style="font-size: 1.2rem; font-style: italic; color: #4B5563; margin-top: 1rem;">
                "The best way to predict the future is to invent it."
            </p>
            <p style="font-weight: 600; color: #9CA3AF; letter-spacing: 1px;">— ALAN KAY</p>
        </div>
        """, unsafe_allow_html=True)

    # Right Input Form Panel Layout
    with col2:
        st.markdown('<div class="login-card">', unsafe_allow_html=True)
        st.subheader("System Authorization")
        st.caption("Please sign in to access your secure voice portal dashboard.")

        user_input = st.text_input("Username", placeholder="Enter 'admin'...")

        # Interactive toggling text vs secret dot view box engine
        pass_type = "text" if st.session_state.show_password else "password"
        pass_input = st.text_input("Password", type=pass_type, placeholder="Enter your key...")

        # The Checkbox tool that mimics your custom eye tracker button click
        if st.checkbox("Show Secret Passkey Characters 👁️"):
            st.session_state.show_password = True
        else:
            st.session_state.show_password = False

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("LOGIN TO SYSTEMS &rarr;", use_container_width=True):
            # Change 'nexus123' here if you want to switch up your password!
            if user_input.strip() == "admin" and pass_input.strip() == "nexus123":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Invalid secure developer credentials matching parameters!")
        st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# HUB SCREEN 2: MAIN VOICE CORES CONTROL PANEL
# ==========================================
else:
    # Top Status Navigation bar panels
    head_col1, head_col2 = st.columns([4, 1])
    with head_col1:
        st.markdown('<h2 class="main-logo-text" style="color: white;">Ashwanth<span>.AI</span></h2>',
                    unsafe_allow_html=True)
    with head_col2:
        if st.button("LOGOUT 🚪", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()

    st.markdown("<hr style='border-color: #1f293d;'>", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center;'>Ashwanth Voice System v1.0</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center; color: #9CA3AF;'>SYSTEM STATUS: <span style='color: #00C49A; font-weight: bold;'>ONLINE</span></p>",
        unsafe_allow_html=True)

    # Glowing Pulsing Graphic Representation Orb
    st.markdown("""
    <div class="orb-container">
        <div class="voice-orb"></div>
    </div>
    """, unsafe_allow_html=True)

    # Simple input bar to replace broken browser mic links safely!
    st.markdown(
        "<p style='text-align: center; color: #9CA3AF; font-weight: bold;'>🗣️ Type or Say Your Command Below:</p>",
        unsafe_allow_html=True)
    voice_command = st.text_input("", placeholder="Type math question here, like 'What is 52 minus 32'...",
                                  label_visibility="collapsed")

    if voice_command:
        cmd_text = voice_command.lower().strip()
        reply_msg = f"I heard you say: '{voice_command}'. Ask me any math or say hello!"

        # ADVANCED MATHEMATICAL CALCULATORS CORE (Reads spoken digits seamlessly!)
        import re

        numbers = re.findall(r'\d+', cmd_text)

        if any(x in cmd_text for x in ['plus', '+', 'add']) and len(numbers) >= 2:
            res = int(numbers[0]) + int(numbers[1])
            reply_msg = f"{numbers[0]} plus {numbers[1]} equals {res}, boss!"

        elif any(x in cmd_text for x in ['minus', '-', '–', '—', 'subtract']) and len(numbers) >= 2:
            res = int(numbers[0]) - int(numbers[1])
            reply_msg = f"{numbers[0]} minus {numbers[1]} equals {res}, boss!"

        elif any(x in cmd_text for x in ['times', 'multiply', 'x']) and len(numbers) >= 2:
            res = int(numbers[0]) * int(numbers[1])
            reply_msg = f"{numbers[0]} times {numbers[1]} equals {res}, boss!"

        # TALK COMBINATIONS LOGIC CHANNELS
        elif 'hello' in cmd_text or 'hi' in cmd_text:
            reply_msg = "Hello! Welcome back to your custom command terminal. I am online and ready, boss!"
        elif 'name' in cmd_text:
            reply_msg = "My structural design name is set to Ashwanth AI, custom engineered by a prodigy coder."
        elif 'old' in cmd_text or 'age' in cmd_text:
            reply_msg = "My software core module matrix compiled today, but my creator Ashwanth is an awesome 10-year-old!"
        elif 'joke' in cmd_text:
            reply_msg = "Why did the computer go to the doctor? Because it had a virus! Haha!"

        # Show logs values interactively on grid columns structures
        t_col1, t_col2 = st.columns(2)
        with t_col1:
            st.markdown(f"<h3>🗣️ What You Said:</h3><div class='terminal-box'>{voice_command}</div>",
                        unsafe_allow_html=True)
        with t_col2:
            st.markdown(
                f"<h3>🤖 System Response:</h3><div class='terminal-box' style='color: #00C49A;'>{reply_msg}</div>",
                unsafe_allow_html=True)

import streamlit as st
import random

# Force the page to take up the full screen width and set a cool browser tab title
st.set_page_config(page_title="Nexus Premium Portal", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS to inject high-end design styling
st.markdown("""
    <style>
    /* Remove all default Streamlit padding */
    .block-container {
        padding: 0rem !important;
        max-width: 100% !important;
    }

    /* Ensure the app hides default headers */
    header, footer {
        visibility: hidden !important;
    }

    /* Make columns fill the entire monitor height */
    [data-testid="stColumns"] {
        min-height: 100vh;
        gap: 0rem;
    }

    /* Left Panel Styling */
    .left-panel {
        background-color: #FFFFFF;
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        padding: 5rem;
    }
    .nexus-logo {
        font-size: 2.2rem;
        font-weight: 800;
        color: #111827;
        letter-spacing: -1px;
    }
    .nexus-logo span {
        color: #00C49A;
    }
    .quote-mark {
        font-size: 6rem;
        color: rgba(0, 196, 154, 0.2);
        font-family: serif;
        line-height: 0;
        margin-bottom: 1.5rem;
    }
    .main-heading {
        font-size: 3rem;
        font-weight: 800;
        color: #111827;
        line-height: 1.2;
        margin-bottom: 1.5rem;
    }
    .main-heading span {
        color: #00C49A;
    }
    .quote-body {
        font-size: 1.3rem;
        color: #4B5563;
        line-height: 1.6;
        font-style: italic;
        margin-bottom: 1rem;
    }
    .quote-author {
        font-size: 1rem;
        font-weight: 600;
        color: #9CA3AF;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Right Panel Styling with Smooth Gradient */
    .right-panel {
        background: linear-gradient(135deg, #00A878 0%, #00C49A 100%);
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 4rem;
        position: relative;
    }

    /* Upgraded Floating Login Card */
    .login-card {
        background: rgba(255, 255, 255, 0.12);
        padding: 3.5rem 3rem;
        border-radius: 24px;
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        width: 100%;
        max-width: 420px;
        border: 1px solid rgba(255, 255, 255, 0.25);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }

    /* Make input labels bright white */
    .stTextInput label {
        color: white !important;
        font-weight: 600 !important;
    }

    /* Premium bottom copyright note */
    .copyright-tag {
        position: absolute;
        bottom: 2rem;
        color: rgba(255, 255, 255, 0.6);
        font-size: 0.85rem;
        letter-spacing: 0.5px;
    }
    </style>
""", unsafe_allow_html=True)

# Quote Database for the interactive refresh button
quotes_pool = [
    {"text": "The secret of getting ahead is getting started. The complex is made simple one step at a time.",
     "author": "Mark Twain"},
    {"text": "Believe you can and you're halfway there. Great achievements begin with a decision to try.",
     "author": "Theodore Roosevelt"},
    {"text": "The only way to do great work is to love what you do. Keep looking, don't settle.",
     "author": "Steve Jobs"},
    {"text": "Do what you can, with what you have, where you are.", "author": "Theodore Roosevelt"}
]

# Initialize state variables
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "quote_index" not in st.session_state:
    st.session_state.quote_index = 0

# --- VIEW 1: THE PREMIUM LOGIN SCREEN ---
if not st.session_state.logged_in:

    # Split the screen into two clean halves
    left_col, right_col = st.columns(2)

    with left_col:
        # Top Brand Section
        st.markdown('<div class="left-panel">', unsafe_allow_html=True)
        st.markdown('<div class="nexus-logo">ne<span>x</span>us</div>', unsafe_allow_html=True)

        # Center Quote Section
        st.markdown('<div>', unsafe_allow_html=True)
        st.markdown('<div class="quote-mark">“</div>', unsafe_allow_html=True)
        st.markdown('<div class="main-heading">Unlock Your <span>Potential</span></div>', unsafe_allow_html=True)

        current_quote = quotes_pool[st.session_state.quote_index]
        st.markdown(f'<div class="quote-body">"{current_quote["text"]}"</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="quote-author">— {current_quote["author"]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Interactive Feature: Change Quote Button
        if st.button("🔄 Shuffle Quote", key="shuffle"):
            st.session_state.quote_index = (st.session_state.quote_index + 1) % len(quotes_pool)
            st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

    with right_col:
        st.markdown('<div class="right-panel">', unsafe_allow_html=True)

        # Container wrapper for the sleek forms
        st.markdown('<div class="login-card">', unsafe_allow_html=True)

        username = st.text_input("Username / Email", placeholder="Enter your username...")
        password = st.text_input("Password", type="password", placeholder="••••••••")

        st.markdown("<br>", unsafe_allow_html=True)

        # Highly Styled Login Action Button
        if st.button("LOGIN →", use_container_width=True, type="secondary"):
            # Set a fun secret password to show off to your dad
            if username == "admin" and password == "nexus123":
                st.session_state.logged_in = True
                st.rerun()
            elif not username or not password:
                st.warning("Please type your username and password first!")
            else:
                st.error("Access Denied! Incorrect credentials.")

        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="copyright-tag">Copyright © 1998, 2026. All rights reserved.</div>',
                    unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- VIEW 2: THE SECRET PREMIUM DASHBOARD ---
else:
    st.balloons()
    st.snow()

    st.title("🚀 Nexus Command Center Pro")
    st.subheader(f"Welcome back, Administrator. Systems are nominal.")

    st.write("---")

    # Showcase advanced dashboard widgets your dad's app didn't have
    col1, col2, col3 = st.columns(3)
    col1.metric("Server Speed", "142 Mbps", "+12%")
    col2.metric("Database Health", "99.9%", "Stable")
    col3.metric("Project Budget Saved", "1,000 INR", "100%")

    st.write("### 🎛️ Portal Management Terminal")
    st.info("This premium system bypasses hosting limits and runs fully customized open-source parameters.")

    st.text_area("System Log Feed",
                 value="[INFO] Database connection secure.\n[INFO] AI UI interface pipeline activated.\n[SUCCESS] Successfully beat dad's web layout template.")

    if st.button("🚪 Securely Log Out", type="primary"):
        st.session_state.logged_in = False
        st.rerun()

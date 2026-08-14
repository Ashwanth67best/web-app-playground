import streamlit as st

# Force the page to take up the full screen width and set a custom browser tab title
st.set_page_config(page_title="Nexus Premium Portal", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS to structure the text layers cleanly over the backgrounds
st.markdown("""
    <style>
    /* Global screen overrides */
    .block-container {
        padding: 0rem !important;
        max-width: 100% !important;
    }
    header, footer {
        visibility: hidden !important;
    }

    /* Layout structural boxes */
    .split-container {
        display: flex;
        width: 100%;
        min-height: 100vh;
    }

    .left-box-wrapper {
        width: 50%;
        background-color: #FFFFFF;
        padding: 5rem;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .right-box-wrapper {
        width: 50%;
        background: linear-gradient(135deg, #00A878 0%, #00C49A 100%);
        padding: 5rem;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        position: relative;
    }

    /* Typography style guidelines */
    .brand-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #111827;
        letter-spacing: -1px;
    }
    .brand-title span {
        color: #00C49A;
    }
    .quote-graphic {
        font-size: 6rem;
        color: rgba(0, 196, 154, 0.2);
        font-family: serif;
        line-height: 0;
        margin-bottom: 1.5rem;
    }
    .heading-bold {
        font-size: 3rem;
        font-weight: 800;
        color: #111827;
        line-height: 1.2;
        margin-bottom: 1.5rem;
    }
    .heading-bold span {
        color: #00C49A;
    }
    .quote-content {
        font-size: 1.3rem;
        color: #4B5563;
        line-height: 1.6;
        font-style: italic;
        margin-bottom: 1rem;
    }
    .author-tag {
        font-size: 1rem;
        font-weight: 600;
        color: #9CA3AF;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Floating Login Form Card overlay overrides */
    .form-overlay-card {
        background: rgba(255, 255, 255, 0.15);
        padding: 3.5rem 3rem;
        border-radius: 24px;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        width: 100%;
        max-width: 420px;
        border: 1px solid rgba(255, 255, 255, 0.25);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
    }

    /* Force Streamlit widget texts inside panels to show white labels */
    .right-box-wrapper label {
        color: white !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
    }

    .footer-stamp {
        position: absolute;
        bottom: 2rem;
        color: rgba(255, 255, 255, 0.6);
        font-size: 0.85rem;
        letter-spacing: 0.5px;
    }
    </style>
""", unsafe_allow_html=True)

# Quote pool tracker parameters
quotes_pool = [
    {"text": "The secret of getting ahead is getting started. The complex is made simple one step at a time.",
     "author": "Mark Twain"},
    {"text": "Believe you can and you're halfway there. Great achievements begin with a decision to try.",
     "author": "Theodore Roosevelt"},
    {"text": "The only way to do great work is to love what you do. Keep looking, don't settle.",
     "author": "Steve Jobs"}
]

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "quote_index" not in st.session_state:
    st.session_state.quote_index = 0

# --- SCENE 1: THE RE-BUILT SPLIT SCREEN LOGIN ---
if not st.session_state.logged_in:

    # We use Streamlit native layout blocks to anchor the components correctly on top
    left_side, right_side = st.columns(2)

    with left_side:
        st.markdown('<div class="left-box-wrapper">', unsafe_allow_html=True)
        st.markdown('<div class="brand-title">ne<span>x</span>us</div>', unsafe_allow_html=True)

        st.markdown('<div>', unsafe_allow_html=True)
        st.markdown('<div class="quote-graphic">“</div>', unsafe_allow_html=True)
        st.markdown('<div class="heading-bold">Unlock Your <span>Potential</span></div>', unsafe_allow_html=True)

        active_q = quotes_pool[st.session_state.quote_index]
        st.markdown(f'<div class="quote-content">"{active_q["text"]}"</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="author-tag">— {active_q["author"]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Interactive item placement
        if st.button("🔄 Shuffle Quote Link"):
            st.session_state.quote_index = (st.session_state.quote_index + 1) % len(quotes_pool)
            st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

    with right_side:
        # We nest the widgets inside standard columns to prevent them dropping beneath elements
        st.markdown('<div class="right-box-wrapper">', unsafe_allow_html=True)
        st.markdown('<div class="form-overlay-card">', unsafe_allow_html=True)

        user_input = st.text_input("Username / Email Address", placeholder="Enter account username...", key="user")
        pass_input = st.text_input("Account Password Key", type="password", placeholder="••••••••", key="pass")

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("LOGIN →", use_container_width=True):
            if user_input == "admin" and pass_input == "nexus123":
                st.session_state.logged_in = True
                st.rerun()
            elif not user_input or not pass_input:
                st.warning("Please enter your account details.")
            else:
                st.error("Invalid passcode combination.")

        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="footer-stamp">Copyright © 1998, 2026. All rights reserved.</div>',
                    unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- SCENE 2: PREMIUM MEMBER CORE HOME ---
else:
    st.balloons()
    st.title("🚀 Premium Web Workspace App")
    st.write("---")

    metric_a, metric_b = st.columns(2)
    metric_a.metric("Server Connection Status", "100% Online", "Optimal")
    metric_b.metric("Development Budget Saved", "1,000 INR", "100%")

    st.success("Authorized account profile verified securely.")

    if st.button("🚪 Disconnect Secure Session", type="primary"):
        st.session_state.logged_in = False
        st.rerun()

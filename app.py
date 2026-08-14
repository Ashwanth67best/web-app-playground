import streamlit as st

# Force full screen mode and add a browser page title
st.set_page_config(page_title="Nexus Premium Portal", layout="wide", initial_sidebar_state="collapsed")

# Simple CSS to style the fonts and hide the default Streamlit header bar
st.markdown("""
    <style>
    header, footer {
        visibility: hidden !important;
    }
    .brand {
        font-size: 2.5rem;
        font-weight: bold;
        color: #111827;
    }
    .brand span {
        color: #00A878;
    }
    .main-heading {
        font-size: 3rem;
        font-weight: 800;
        color: #111827;
        margin-top: 2rem;
    }
    .main-heading span {
        color: #00A878;
    }
    .quote-text {
        font-size: 1.4rem;
        color: #4B5563;
        font-style: italic;
        margin-top: 1rem;
    }
    .quote-author {
        font-size: 1.1rem;
        color: #9CA3AF;
        font-weight: 600;
        margin-top: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Quote pool data
quotes_pool = [
    {"text": "The secret of getting ahead is getting started. The complex is made simple one step at a time.",
     "author": "Mark Twain"},
    {"text": "Believe you can and you're halfway there. Great achievements begin with a decision to try.",
     "author": "Theodore Roosevelt"},
    {"text": "The only way to do great work is to love what you do. Keep looking, don't settle.",
     "author": "Steve Jobs"}
]

# State management initialization
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "quote_index" not in st.session_state:
    st.session_state.quote_index = 0

# --- VIEW 1: LOGIN PAGE ---
if not st.session_state.logged_in:

    # Make two clean, balanced screen halves using Streamlit's official columns
    left_col, right_col = st.columns(2, gap="large")

    # Left Half: Clean Text Layout
    with left_col:
        st.markdown('<div class="brand">ne<span>x</span>us</div>', unsafe_allow_html=True)
        st.markdown('<div class="main-heading">Unlock Your <span>Potential</span></div>', unsafe_allow_html=True)

        current_q = quotes_pool[st.session_state.quote_index]
        st.markdown(f'<div class="quote-text">"{current_q["text"]}"</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="quote-author">— {current_q["author"]}</div>', unsafe_allow_html=True)

        st.write("")  # Add some spacing

        if st.button("🔄 Shuffle Quote Link", use_container_width=False):
            st.session_state.quote_index = (st.session_state.quote_index + 1) % len(quotes_pool)
            st.rerun()

    # Right Half: Styled Container Box for the Login inputs
    with right_col:
        # st.container puts a clean visual card box around the input fields
        with st.container(border=True):
            st.subheader("Account Authorization Secure Portal")
            st.write("Please sign in with your credential files.")

            user_input = st.text_input("Username / Email Address", placeholder="Enter account username...",
                                       key="user_field")
            pass_input = st.text_input("Account Password Key", type="password", placeholder="••••••••",
                                       key="pass_field")

            st.write("")

            if st.button("LOGIN →", use_container_width=True, type="primary"):
                if user_input == "admin" and pass_input == "nexus123":
                    st.session_state.logged_in = True
                    st.rerun()
                elif not user_input or not pass_input:
                    st.warning("Please fill out both entry slots.")
                else:
                    st.error("Invalid passcode combination entered.")

# --- VIEW 2: LOGGED IN PREMIUM DASHBOARD ---
else:
    st.balloons()
    st.title("🚀 Premium Web Workspace App")
    st.write("---")

    col1, col2 = st.columns(2)
    col1.metric("Server Connection Status", "100% Online", "Optimal")
    col2.metric("Development Budget Saved", "1,000 INR", "100%")

    st.success("Authorized account profile verified securely.")

    if st.button("🚪 Disconnect Secure Session", type="primary"):
        st.session_state.logged_in = False
        st.rerun()

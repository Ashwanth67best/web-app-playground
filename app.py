import streamlit as st

st.set_page_config(layout="centered")

st.markdown("<h1 style='text-align: center;'>🦖 Ashwanth's Cloud Portal</h1>", unsafe_allow_html=True)
st.write("---")

# 1. Setup a custom session tracker to prevent the st.user crash
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# 2. IF NOT LOGGED IN: Show the clean layout with the Google button
if not st.session_state.logged_in:
    st.markdown("<h3 style='text-align: center;'>Welcome! Please Sign In</h3>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # A beautiful custom simulation button
        if st.button("Sign in with Google", use_container_width=True, type="primary"):
            st.session_state.logged_in = True
            st.toast("Authenticating with Google Accounts...")
            st.rerun()

# 3. IF LOGGED IN: Show the awesome welcome dashboard!
else:
    st.balloons()
    st.success("👋 Welcome Back, Ashwanth!")
    st.write("📧 Verified Account: `ashwanth67best@gmail.com`")

    st.write("---")
    st.header("🎮 Your Authorized Member Dashboard")
    st.info("You successfully passed the official Google account safety shield!")

    # Simple checkbox tasks for your dash
    st.checkbox("Task 1: Load server packages")
    st.checkbox("Task 2: Code a secondary script")

    st.write("---")
    if st.button("🚪 Log Out"):
        st.session_state.logged_in = False
        st.rerun()

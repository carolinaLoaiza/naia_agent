import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader



with open('auth_config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)
try:
    authenticator.login()
except stauth.AuthenticationError as e:
    st.error(e)


# Authenticating user
if st.session_state['authentication_status']:    
    authenticator.logout("Log Out", "sidebar")
    page = st.navigation(["pages/home.py", "pages/chat.py", "pages/checklist.py", "pages/symptom_tracker.py", "pages/faq.py"])
    page.run()
    
elif st.session_state['authentication_status'] is False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] is None:
    st.warning('Please enter your username and password')

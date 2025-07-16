import streamlit as st 

st.set_page_config(
    page_title="GPT Lab - FAQ",
    #page_icon="https://api.dicebear.com/5.x/bottts-neutral/svg?seed=gptLAb"#,
    #menu_items={"About": "GPT Lab is a user-friendly app that allows anyone to interact with and create their own AI Assistants powered by OpenAI's GPT language model. Our goal is to make AI accessible and easy to use for everyone, so you can focus on designing your Assistant without worrying about the underlying infrastructure.", "Get help": None, "Report a Bug": None}
)


st.markdown(
    "<style>#MainMenu{visibility:hidden;}</style>",
    unsafe_allow_html=True
)

#au.render_cta()

st.title("FAQ")

#st.markdown("---")
#au.robo_avatar_component()

st.markdown("#### General")
with st.expander("What is NAIA?", expanded=False):
    st.markdown("NAIA is a user-friendly app ....")


with st.expander("Why use NAIA?"):
    st.markdown("NAIA aims to ....")

with st.expander("QUESTION 3?"):
    st.markdown("ANSWER 3....")

with st.expander("QUESTION 4?"):
    st.markdown("ANSWER 4....")

with st.expander("QUESTION 5?"):
    st.markdown("ANSWER 5....")

with st.expander("QUESTION 6?"):
    st.markdown("ANSWER 6....")

st.markdown("#### How to use NAIA")

with st.expander("QUESTION 1?"):
    st.markdown("ANSWER 1....")

with st.expander("QUESTION 2?"):
    st.markdown("ANSWER 2....")

with st.expander("QUESTION 3?"):
    st.markdown("ANSWER 3....")

with st.expander("QUESTION 4?"):
    st.markdown("ANSWER 4....")

with st.expander("QUESTION 5?"):
    st.markdown("ANSWER 5....")

with st.expander("QUESTION 6?"):
    st.markdown("ANSWER 6....")

st.markdown("#### Privacy, Platform Guidelines, and Intellectual Property")

with st.expander("Is my information kept confidential on GPT Lab?"):
    st.markdown("Yes, we take your privacy and confidentiality very seriously. We do not store any personally identifiable information, and instead use a secure hashing algorithm to store a hashed version of your OpenAI API Key. Additionally, session transcripts are encrypted.")

with st.expander("How does NAIA ensure the security of my information?"):
    st.markdown("""We use the SHA-256 PBKDF2 algorithm, a highly secure one-way hashing algorithm, to hash your OpenAI API Key and store it securely. This ensures that your key is protected and cannot be used for any unauthorized purposes. 
    
Additionally, we use a symmetric AES-128 encryption algorithm, with a unique key for each user, to encrypt your chat transcripts with the AI Assistants.""")

with st.expander("Are there any restrictions on the type of NAIA as an AI Assistants?"):
    st.markdown("""
    Our Terms of Use have outlined some common sense restrictions you should follow. Please review our Terms of Use, available on the Terms page, for more information. 
    Additionally, since our NAIA Assistant use the Groq AI language models, you should also comply with the [Groq Cloud Usage policies](https://groq.com/terms-of-use).  \n
    We recommend ...  \n
    Please note that NAIA does not assume ....
    """)
with st.expander("Who owns the prompts created in NAIA?"):
    st.markdown("You do! The prompts created by the users in NAIA belong to the users themselves. NAIA is a platform that enables users to interact with AI Assistants powered by Groq language models, and the prompts created by the users in the app are the property of the users themselves. NAIA does not claim any ownership or rights to the prompts created by the users.")
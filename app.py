import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="My Personal AI", layout="centered")
st.title("🤖 My Private AI Assistant")

# Sidebar for API Key & Settings
with st.sidebar:
    st.header("Admin Control")
    api_key = st.text_input("Enter Gemini API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Image Generator Module
    st.subheader("🎨 Unlimited Image Generator")
    img_prompt = st.text_input("Enter image prompt:")
    if st.button("Generate Image"):
        if img_prompt:
            encoded_prompt = img_prompt.replace(" ", "%20")
            img_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1080&height=1080&nologo=true"
            st.image(img_url, caption=img_prompt)
    
    st.divider()
    
    # Chat Module
    st.subheader("💬 AI Chat & Code Agent")
    user_input = st.text_area("Aapka Aadesh (Instructions):")
    if st.button("Send Instruction"):
        response = model.generate_content(user_input)
        st.write(response.text)
else:
    st.warning("Kripya sidebar me apni Gemini API Key darj karein.")

import streamlit as st
import urllib.parse
import google.generativeai as genai

st.set_page_config(page_title="My AI Generator", layout="wide")
st.title("🤖 My Private AI Generator")

# Sidebar for Gemini API Key (Chat ke liye)
with st.sidebar:
    st.header("🔑 API Settings")
    gemini_key = st.text_input("Gemini API Key (Chat ke liye):", type="password")

st.header("🎨 AI Image Generator")
image_prompt = st.text_input("Enter image prompt:")

if st.button("Generate Image"):
    if not image_prompt:
        st.warning("Kripya koi prompt type karein.")
    else:
        try:
            with st.spinner("Image ban rahi hai..."):
                # Clean and encode prompt text
                clean_prompt = urllib.parse.quote(image_prompt)
                # Unlimited & Free High-Quality Image URL
                image_url = f"https://image.pollinations.ai/prompt/{clean_prompt}?width=1024&height=1024&nologo=true"
                st.image(image_url, caption=image_prompt, use_container_width=True)
        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("---")

st.header("💬 AI Chat Agent")
user_instruction = st.text_area("Aapka Aadesh (Instructions):")

if st.button("Send Instruction"):
    if not gemini_key:
        st.error("Kripya sidebar me Gemini API Key darj karein.")
    elif not user_instruction:
        st.warning("Kripya koi instruction likhein.")
    else:
        try:
            genai.configure(api_key=gemini_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(user_instruction)
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")

import streamlit as st
import replicate
import google.generativeai as genai

st.set_page_config(page_title="My Private AI Assistant", layout="wide")
st.title("🤖 My Private AI Assistant")

# Sidebar for API Keys
with st.sidebar:
    st.header("🔑 API Settings")
    gemini_key = st.text_input("Gemini API Key (Chat ke liye):", type="password")
    replicate_key = st.text_input("Replicate API Key (Images ke liye):", type="password")

st.header("🎨 Open Image Generator (Flux)")
image_prompt = st.text_input("Enter image prompt:")

if st.button("Generate Image"):
    if not replicate_key:
        st.error("Kripya sidebar me Replicate API Key darj karein.")
    elif not image_prompt:
        st.warning("Kripya koi prompt type karein.")
    else:
        try:
            with st.spinner("Image ban rahi hai..."):
                client = replicate.Client(api_token=replicate_key)
                output = client.run(
                    "black-forest-labs/flux-schnell",
                    input={"prompt": image_prompt}
                )
                st.image(output[0], caption=image_prompt)
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

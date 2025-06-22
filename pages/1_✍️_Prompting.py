import requests
import streamlit as st
import time
import base64
from io import BytesIO
from requests_futures.sessions import FuturesSession

# ✨ Page Configuration
st.set_page_config(page_title="AI Image Generator", layout="centered")
st.title("🎨 AI-Powered Text-to-Image Generator")

# ✅ Theme Toggle
dark_mode = st.toggle("🌗 Toggle Dark Mode")

# Apply Custom CSS for Dark Mode
if dark_mode:
    st.markdown(
        """
        <style>
        body { background-color: #121212; color: white; }
        .stTextArea, .stButton { background-color: #333333; color: white; }
        </style>
        """,
        unsafe_allow_html=True,
    )

# 🔑 Load API credentials
try:
    account_id = st.secrets["CLOUDFLARE_ACCOUNT_ID"]
    api_token = st.secrets["CLOUDFLARE_API_TOKEN"]
except KeyError:
    st.error("⚠️ API credentials missing! Please check your Streamlit secrets.")
    st.stop()

# 🔥 Function to Call Cloudflare AI API
def generate_image(model, prompt, quality):
    """Generates an AI image using Cloudflare Workers AI API."""
    url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/{model}"
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.post(url, headers=headers, json={"prompt": prompt, "quality": quality})
    return response

# 🔥 Function to Generate Prompt Suggestions
def generate_prompt_suggestions(prompt):
    """Generates alternative creative prompts for better image results."""
    prompt_model = "@hf/thebloke/mistral-7b-instruct-v0.1-awq"
    prompt_url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/{prompt_model}"
    headers = {"Authorization": f"Bearer {api_token}"}
    
    system_message = """
    You are a Stable Diffusion prompt engineer.
    The user provides a prompt, and you generate three detailed variations in different artistic styles.
    """

    response = requests.post(
        prompt_url,
        headers=headers,
        json={"messages": [{"role": "system", "content": system_message}, {"role": "user", "content": prompt}]}
    )
    return response

# ✅ Initialize session state for image history
if "image_history" not in st.session_state:
    st.session_state.image_history = []

# 🎨 Interactive UI Elements
with st.form("text_to_image"):
    st.subheader("🎨 Generate an AI Image from Text")
    
    # Model Selection
    model = st.selectbox(
        "Choose your Text-To-Image model",
        options=(
            "@cf/lykon/dreamshaper-8-lcm",
            "@cf/bytedance/stable-diffusion-xl-lightning",
            "@cf/stabilityai/stable-diffusion-xl-base-1.0",
        ),
    )
    
    # User Input Prompt with Live Counter
    prompt = st.text_area("Enter your creative prompt", placeholder="Example: A futuristic city at sunset...")
    char_count = len(prompt)
    st.caption(f"Characters used: {char_count}/500")
    
    # Quality Slider
    quality = st.slider("Select Image Quality", min_value=1, max_value=10, value=5)
    
    # Submit Button
    submitted = st.form_submit_button("🎨 Generate Image")

# ✨ Process Request on Submission
if submitted and prompt:
    st.info("🚀 Processing request... Please wait.")
    progress_bar = st.progress(0)
    
    session = FuturesSession()
    
    # Simulate progress
    for percent in range(0, 101, 10):
        time.sleep(0.2)
        progress_bar.progress(percent)
    
    # Send requests
    future_image = session.post(
        f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/{model}",
        headers={"Authorization": f"Bearer {api_token}"},
        json={"prompt": prompt, "quality": quality},
    )

    future_prompt = session.post(
        f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/@hf/thebloke/mistral-7b-instruct-v0.1-awq",
        headers={"Authorization": f"Bearer {api_token}"},
        json={
            "messages": [
                {"role": "system", "content": "You are a Stable Diffusion prompt engineer. Provide three creative variations."},
                {"role": "user", "content": prompt},
            ]
        },
    )
    
    # 🎨 Display Generated Image
    with st.spinner("🎨 Generating AI Image..."):
        image_response = future_image.result()
        if image_response.status_code == 200:
            img_data = image_response.content
            st.image(img_data, caption=prompt, use_container_width=True)
            st.success("✅ Image successfully generated!")
            
            # Convert image to downloadable format
            buffer = BytesIO(img_data)
            b64_img = base64.b64encode(buffer.getvalue()).decode()
            href = f'<a href="data:image/png;base64,{b64_img}" download="generated_image.png">💾 Download Image</a>'
            st.markdown(href, unsafe_allow_html=True)

            # ✅ Save image to session state
            st.session_state.image_history.append(img_data)
        else:
            st.error("❌ Image generation failed. Please try again.")
    
    # 💡 Display Alternative Prompts
    with st.spinner("✨ Generating alternative prompt suggestions..."):
        prompt_response = future_prompt.result()
        if prompt_response.status_code == 200:
            try:
                result = prompt_response.json().get("result", {})
                if "response" in result:
                    st.subheader("🔍 Alternative Prompt Suggestions")
                    st.write(result["response"])
                else:
                    st.warning("⚠️ No suggestions found. Try another prompt.")
            except Exception as e:
                st.error(f"⚠️ Error processing suggestions: {e}")
        else:
            st.error("❌ Failed to generate alternative prompts.")

# ✅ Show Image History
if st.session_state.image_history:
    st.subheader("📜 Previously Generated Images")
    for img in st.session_state.image_history:
        st.image(img, use_container_width=True)

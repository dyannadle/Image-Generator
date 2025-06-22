import streamlit as st
import random

# Configure the page layout
st.set_page_config(
    page_title="Cloudflare Workers AI Image Demos",
    page_icon="🎨",
    layout="wide"  # Expands the page width
)

# Custom styling for a modern look
st.markdown("""
    <style>
        body {
            background-color: #1e1e1e;
            color: #f5f5f5;
        }
        .title {
            font-size: 40px;
            text-align: center;
            font-weight: bold;
            color: #FFD700;
        }
        .subheader {
            font-size: 24px;
            font-weight: bold;
            color: #FFA500;
        }
        .stMarkdown {
            font-size: 18px;
            line-height: 1.6;
            color: #f5f5f5;
        }
        .stInfo {
            background-color: #333;
            color: #FFD700;
            padding: 15px;
            border-radius: 10px;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🌟 Welcome to AI Art Generation with GANs!</div>', unsafe_allow_html=True)

# 🎭 How GANs Work? (Expanded Section)
st.markdown('<div class="subheader">🎭 How GANs Work?</div>', unsafe_allow_html=True)
st.markdown("""
Generative Adversarial Networks (GANs) are a special type of deep learning model made up of **two neural networks**:  

✅ **Generator (Creator)**  
   - Starts with random noise and **tries to create realistic images**.  
   - Improves its outputs by learning from the Discriminator’s feedback.  

✅ **Discriminator (Critic)**  
   - Takes both real and generated images and **tries to distinguish between them**.  
   - Provides feedback to the Generator to improve its results.  

This process is similar to an **art forger (Generator)** trying to **fool an art expert (Discriminator)**. Over time, the forger improves so much that even experts struggle to tell real from fake!  

### 📌 **How GANs Train & Improve**
1️⃣ **Generator creates random images** (initially unrealistic).  
2️⃣ **Discriminator evaluates** images, labeling them as "Real" or "Fake."  
3️⃣ **Generator gets feedback** from the Discriminator & improves.  
4️⃣ **This cycle repeats thousands of times**, making images increasingly realistic.  

### 📊 **Mathematical Concept Behind GANs**
GANs use a **min-max game**:  
- The Generator **minimizes** the Discriminator’s ability to detect fakes.  
- The Discriminator **maximizes** its accuracy in distinguishing real vs. fake.  

The loss function of a GAN is:  
**L(G, D) = E[log(D(real))] + E[log(1 - D(fake))]**  

Where:  
- **D(real)** = Probability that the Discriminator classifies a real image correctly.  
- **D(fake)** = Probability that the Discriminator classifies a generated image correctly.  

### 🛠️ **Real-World Applications of GANs**
🔹 **AI Art & Style Transfer** – Used in apps like DeepArt & Prisma.  
🔹 **Image Super-Resolution** – Enhances low-quality images (used by NASA & medical imaging).  
🔹 **3D Object Generation** – Helps in gaming, AR, and architecture.  
🔹 **AI-Powered Animation** – GANs create new anime characters & avatars.  

### 🔬 **Variants of GANs**
- **DCGAN** (Deep Convolutional GAN) – Used for **image synthesis**.  
- **CycleGAN** – Transforms images **from one style to another** (e.g., **turning summer photos into winter scenes**).  
- **StyleGAN** – Creates **ultra-realistic human faces**.  
- **Pix2Pix** – Converts sketches into **photorealistic images**.  

### 🏆 **Future of GANs**
- **AI-generated movies & storytelling**.  
- **Instant realistic avatars for VR/Metaverse**.  
- **AI-assisted architecture & product design**.  
""")

# 🌍 Impact on Society
st.markdown('<div class="subheader">🌍 Impact on Society</div>', unsafe_allow_html=True)
st.markdown("""
GANs have transformed **creativity and technology** in multiple fields:

✅ **Art & Creativity** 🎨  
   - AI-generated paintings **sold for over $400,000** at auctions.  
   - Allows **artists to co-create with AI**, boosting creativity.  

✅ **Healthcare & Science** 🏥  
   - Generates **synthetic medical images** for safer research.  
   - Assists in **drug discovery** by predicting molecular structures.  

✅ **Gaming & Virtual Reality** 🎮  
   - AI-generated characters & environments in **realistic games**.  
   - Helps create **ultra-realistic textures & designs**.  

✅ **Fashion & Design** 👗  
   - AI can **design new clothing lines** based on trends.  
   - Brands use GANs to **create virtual models**.  
""")

# 🚨 Risks & Ethical Concerns 
st.markdown('<div class="subheader">🚨 Risks & Ethical Concerns</div>', unsafe_allow_html=True)
st.markdown("""
🔴 **Deepfakes & Fake Media** – GANs can generate highly realistic **fake videos** (deepfakes) that might be used for **misinformation, fraud, or defamation**.  

🔴 **Copyright Issues** – AI-generated art raises **legal debates** about ownership and **who gets credit** for digital creations, potentially violating existing intellectual property laws.  

🔴 **Bias in AI** – If trained on **biased data**, GANs may **unintentionally reinforce societal biases** in their generated outputs, leading to unfair or discriminatory results.  

🔴 **Privacy Violations** – AI can create **synthetic identities** or **reconstruct faces** from minimal data, raising concerns about surveillance and misuse of personal imagery.  

🔴 **Misinformation & Propaganda** – AI-generated images and videos can be used for **political manipulation, spreading false narratives, and influencing public opinion**.  

🔴 **Environmental Impact** – Training large AI models, including GANs, requires **high computational power**, leading to **significant carbon emissions** and energy consumption.  

🔴 **Job Displacement** – AI-generated media may replace **human artists, photographers, and content creators**, leading to **job losses** in creative industries.  

🔴 **Security Threats** – AI-generated fake identities can be used for **cybercrime, identity theft, and bypassing authentication systems**.  
""")


# 💡 Fun facts (Changes every refresh)
fun_facts = [
    "GANs were invented by Ian Goodfellow in 2014.",
    "AI-generated art has been sold for over $400,000 at auctions!",
    "Some GANs can generate hyper-realistic human faces that don’t exist.",
    "Deepfake videos use GANs to swap faces in real time.",
    "AI-powered GANs have been used to restore old and damaged photos.",
    "Some GAN models can generate music compositions from scratch!",
    "Tesla uses AI similar to GANs for self-driving car simulations.",
    "AI-generated fake fingerprints can fool biometric security!",
    "AI GANs help NASA enhance deep-space images."
    "AI can recreate famous art styles like Van Gogh’s. 🎨"
    "AI once confused a Chihuahua with a muffin! 🐶🧁"
    "People trust AI-generated faces more than real ones. 😲"
    "AI can restore and animate old photos. 📸"
    "Google’s DeepDream creates psychedelic images. 🌙"
]
st.markdown(f'<div class="stInfo">💡 Fun Fact: {random.choice(fun_facts)}</div>', unsafe_allow_html=True)


# 🎨 Example AI Image Prompt (New Section Added)
("""
If you'd like to generate an AI artwork similar to the image below, try using this prompt in a GAN-based AI generator like **MidJourney, Stable Diffusion, or DALL·E**:

**Prompt:**
"

Use this prompt and adjust parameters like **lighting, style, or aspect ratio** to fine-tune the results!
""")

# List of 10 AI-generated images (Replace with actual file names or URLs)
image_list = [
    "ai_art.jpg", "ai_art2.jpg", "ai_art3.jpg", "ai_art4.jpg", "ai_art5.jpg",
    "ai_art6.jpg", "ai_art7.jpg", "ai_art8.jpg", "ai_art9.jpg", "ai_art10.jpg"
]

# Initialize session state for tracking the image index
if "image_index" not in st.session_state:
    st.session_state.image_index = 0

# Ensure images are displayed in sequential order
current_index = st.session_state.image_index

# Corresponding captions for each image
captions = [
"Little Giorgia Meloni, dressed in an elegant Italian school uniform, clutches a book on politics, her eyes filled with ambition as she stands in a charming European town.",
"A young Narendra Modi, draped in traditional Indian attire, stands by a bustling tea stall, his sharp gaze hinting at the leader he is destined to become.",
"Shivajirao Gaekwad transforms into a fearless gangster, exuding power and charisma in his intense, menacing look.",
"Albert Einstein, lost in the rhythm of a musical instrument, blending genius with melody in a rare artistic moment.",  
"Virat Kohli, sporting a fierce expression, radiates passion and determination, ready to take on the world.",  
"Narendra Modi reimagined as a Bollywood-style gangster, donning a rugged look with a powerful aura of dominance.",  
"An elderly Indian general in a majestic vintage military uniform, his wise eyes and decorated attire reflecting a lifetime of honor and leadership Ft. Mahatma Gandhi (Bappu)).",  
"Little Donald Trump, dressed in a sharp suit and red tie, confidently gestures at a toy skyscraper, already dreaming big in a lavish golden room.",
"A young Amit Shah, standing boldly at a political rally, his determined stance foreshadowing his future as a master strategist.",
"Kim Jong Un as a serious-faced child, dressed in a crisp military uniform, standing with unwavering authority before the North Korean flags.", 
]

# Display the current image with its unique caption
st.image(image_list[st.session_state.image_index], 
         caption=captions[st.session_state.image_index], 
         width=600)  # Adjust width as needed

# Navigation buttons for Previous & Next
col1, col2, col3 = st.columns([1, 2, 1])

# Function to change the image index
def change_image(new_index):
    st.session_state.image_index = new_index
    st.rerun()  # Forces Streamlit to update immediately
    
with col1:
    if st.button("⬅️ Previous", key="prev"):
        if current_index > 0:
            st.session_state.image_index -= 1  # Move to the previous image
        else:
            st.session_state.image_index = len(image_list) - 1  # Loop to last image

with col3:
    if st.button("Next ➡️", key="next"):
        if current_index < len(image_list) - 1:
            st.session_state.image_index += 1  # Move to the next image
        else:
            st.session_state.image_index = 0  # Loop back to the first image

# Numbered selection buttons for direct image access
st.markdown("### Select an Image:")
cols = st.columns(len(image_list))

for i, col in enumerate(cols):
    with col:
        if st.button(f"{i+1}", key=f"img_{i}"):
            st.session_state.image_index = i  # Direct selection of an image


# 🎨 Example GAN-Generated Art (Optional Placeholder)
# 📌 About the Project Section (Displayed at the Bottom of the Web Page)
st.markdown("---")  # Adds a separator line
st.markdown("<h2 style='text-align: center;'>📝 About the Project</h2>", unsafe_allow_html=True)

st.markdown("""
## **🌟 Overview**  
This project is an **AI-powered Text-to-Image Generation Web App** built using **Streamlit** and **Cloudflare Workers AI**. It allows users to **convert text descriptions (prompts) into images** using advanced deep learning models. The app is designed to be **user-friendly, interactive, and efficient**, making AI-generated artwork accessible to everyone.

---

## **🚀 Key Features**
✅ **AI-Powered Image Generation** – Users can enter a **text description** (prompt) and generate high-quality images using **Cloudflare’s AI models**.  

✅ **Multiple AI Models** – The app provides access to **three state-of-the-art AI models** for text-to-image generation:  
   - **DreamShaper 8 LCM** – Creates stunning, detailed artistic images.  
   - **Stable Diffusion XL Lightning** – Generates images quickly with high realism.  
   - **Stable Diffusion XL Base** – Offers high-quality and versatile image outputs.  

✅ **Enhanced Prompt Suggestions** – The app suggests **three improved prompt variations** using the **Mistral-7B AI model**, helping users generate **better, more artistic results**.  

✅ **User-Friendly Interface** – Built with **Streamlit**, ensuring an **interactive, responsive, and easy-to-use UI**.  

✅ **Cloud-Based Processing** – Utilizes **Cloudflare Workers AI**, meaning **no need for local GPU power**—everything runs on the cloud!  

✅ **Real-Time Image Generation** – Generates images within seconds, making the experience seamless.  

✅ **Free to Use** – Uses **Cloudflare’s free AI API**, making AI-generated art **accessible to everyone**.  

---

## **🔄 How It Works?**  
1️⃣ **Select an AI Model** – Choose one of the **three AI models** for generating images.  
2️⃣ **Enter a Prompt** – Type a **detailed description** of the image you want to create.  
3️⃣ **Click "Generate"** – The selected AI model processes your prompt and **generates an image**.  
4️⃣ **Explore Improved Prompts** – The app suggests **three alternative prompts** that may yield better results.  
5️⃣ **View & Download Image** – The generated image is displayed, and users can **save it** for later use.  

---

## **🛠️ Technologies Used**
🔹 **Streamlit** – For building the web application and UI.  
🔹 **Cloudflare Workers AI** – For running AI models in the cloud.  
🔹 **Stable Diffusion & DreamShaper** – Advanced AI models for image generation.  
🔹 **Mistral-7B AI Model** – Generates **better prompt suggestions** for improved AI outputs.  
🔹 **Python & Requests** – Handles API calls to Cloudflare's AI services.  

---

## **🌐 Why Use This Project?**
🔹 **AI Art for Everyone** – No coding or design skills required.  
🔹 **Fast & Efficient** – Get results in **seconds**.  
🔹 **No Expensive Hardware Needed** – Runs **entirely on the cloud**.  
🔹 **Creative Freedom** – Generate **unique images** for projects, marketing, or personal use.  
🔹 **Free & Open-Source** – No cost to use and easy to modify for new features.  


""", unsafe_allow_html=True)

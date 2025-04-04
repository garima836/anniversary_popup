import streamlit as st
from PIL import Image
import base64

# Function to embed audio
def get_audio_player(file_path):
    with open(file_path, "rb") as audio_file:
        audio_bytes = audio_file.read()
    encoded_audio = base64.b64encode(audio_bytes).decode()
    return f"""
        <audio controls autoplay loop>
            <source src="data:audio/mp3;base64,{encoded_audio}" type="audio/mp3">
        </audio>
    """

# Streamlit app setup
st.set_page_config(page_title="Anniversary Celebration", layout="centered")
st.title("🎉 Happy Anniversary Utkarsh & Garima! 🎉")

# Load the collage image
image_path = "anniversary_collage.png"
image = Image.open(image_path)

# Show image in popup
if st.button("Click to View Your Special Surprise! 💖"):
    st.image(image, caption="Celebrating 6 Years of Happiness", use_column_width=True)

# Add audio player
#song_path = "tum_se_hi.mp3"  # Ensure this file is in the same directory
#st.markdown(get_audio_player(song_path), unsafe_allow_html=True)

st.write("LOVE YOU SOO MUCH BABBYY ❤️💋")

# Load second image for "Love You Forever" button
second_image_path = "image2.jpg"  # Ensure this file is in the same directory
second_image = Image.open(second_image_path)

if st.button("Love You Forever 💖"):
    st.image(second_image, caption="Love You Forever", use_column_width=True)


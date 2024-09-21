import streamlit as st
from PIL import Image
import random

def display_image(image_path):
    image = Image.open(image_path)
    st.image(image, caption="Peppa Pig", use_column_width=True)

responses = {
    "Hello": "Hello! I'm Peppa Pig!",
    "How are you?": "I'm great! Thanks for asking!",
    "What do you like to do?": "I love jumping in muddy puddles!",
    "What's your favorite color?": "I love pink!",
    "Goodbye": "Goodbye! See you next time!",
}

st.title("Talk with Peppa Pig!")
st.write("Type something to talk to Peppa Pig:")

user_input = st.text_input("Your message:")

if user_input:
    response = responses.get(user_input, "I don't understand that.")
    st.write(f"Peppa Pig: {response}")

    image_choice = random.choice([f"images/peppa{i}.png" for i in range(1, 4)])
    display_image(image_choice)

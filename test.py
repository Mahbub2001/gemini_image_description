import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash") 

image_path = "c.jpg"

try:
    image = Image.open(image_path)
    response = model.generate_content(
        [image, "Give me the description of this image. Dont use '**' this type of symbol. only give description in a paragraph."],  
    )
    print(response.text)
except FileNotFoundError:
    print(f"Error: Image file not found at {image_path}")
except Exception as e:
    print(f"An error occurred: {e}")

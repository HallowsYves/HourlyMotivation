import openai
import os
import time
import shutil
import pathlib
import urllib
from datetime import datetime
# from PIL import Image

#SETUP
API_KEY = open("API_KEY", "r").read()
openai.api_key = API_KEY

# QUOTE
response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages= [
        {"role": "user", "content": "generate a motivational Quote"}
    ]
)
quote = response['choices'][0]['message']['content']
str1 = "Beautiful Nature background with text saying :" 
real_prompt = str1 + quote
print(real_prompt)

# IMG GEN
img_response = openai.Image.create(
    prompt= real_prompt,
    n=5,
    size="256x256",
)

img_url = img_response['data'][0]['url']
file_name = str(datetime.now()) + ".png"

folder_path = "/home/yves/HourlyMotivation/Media/Images"
file_path = os.path.join(folder_path, file_name)

urllib.request.urlretrieve(img_url, file_path)

print(img_url)
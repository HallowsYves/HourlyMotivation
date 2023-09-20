import openai
import os
import urllib
import time
from datetime import datetime
from textwrap import fill
from PIL import Image, ImageDraw, ImageFont, ImageFilter


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
formatted_quote = fill(quote,20)
# IMG GEN
img_response = openai.Image.create(
    prompt= "Beautiful Nature background",
    n=1,
    size="512x512",
)
img_url = img_response['data'][0]['url']
file_name = str(datetime.now()) + ".png"

# SAVE IMG
folder_path = "/Users/hallowsyves/Documents/HourlyMotivation/Media/Images"
file_path = os.path.join(folder_path, file_name)
urllib.request.urlretrieve(img_url, file_path)


# LOAD IMG a
image_ = Image.open(file_path)
image_.putalpha(127)
image_.filter(ImageFilter.GaussianBlur(5))
image_load = ImageDraw.Draw(image_)
# LOAD FONT

times_new = ImageFont.truetype('/Users/hallowsyves/Documents/HourlyMotivation/Fonts/AUGUSTUS.TTF', 25)
image_load.text((60, 50), formatted_quote, fill=(255,255,255), font=times_new)
image_.show()
image_.save('output.png')

print(img_url)

import openai
import os
import time
import urllib
import pygame
import textwrap
from datetime import datetime
from textwrap import fill

pygame.font.init()

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
true_quote = fill(quote,20)

# IMG GEN
img_response = openai.Image.create(
    prompt= "Beautiful Nature background",
    n=1,
    size="512x512",
)
img_url = img_response['data'][0]['url']
file_name = str(datetime.now()) + ".png"

# SAVE IMG
folder_path = "/home/yves/HourlyMotivation/Media/Images"
file_path = os.path.join(folder_path, file_name)
urllib.request.urlretrieve(img_url, file_path)

# LOAD IMG
def center_text(surface, text):
    text_rect = text.get_rect()
    surface_rect = surface.get_rect()

    text_x = (surface_rect.width - text_rect.width) // 2
    text_y = (surface_rect.height - text_rect.height) // 2

    surface.blit(text, (text_x, text_y))



surface = pygame.image.load(file_path)
font = pygame.font.SysFont("Arial", 20)
text = font.render(quote, True, (0,0,0))
center_text(surface, text)



pygame.image.save(surface, "output.png")

print(img_url)
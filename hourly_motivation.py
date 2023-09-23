import openai
import os
import urllib
import sqlite3
from handling import QuoteAlreadyInDatabaseException
from datetime import datetime
from textwrap import fill
from PIL import Image, ImageDraw, ImageFont, ImageFilter

#SETUP
API_KEY = open("API_KEY", "r").read()
openai.api_key = API_KEY

def generate_quote(prompt):
    # Generate Quote
    response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages= [
        {"role": "user", "content": prompt}
        ]
    )

    gen_response = response['choices'][0]['message']['content']
    # Check if it's already in the database
    if not check_for_duplicates(gen_response):
        raise QuoteAlreadyInDatabaseException(gen_response)  
    
    add_to_database(gen_response)
    formatted_response = fill(gen_response,20)
    return formatted_response

def generate_image(usr_prompt):
    """Generate & Return the Image to the user"""
    img_response = openai.Image.create(
        prompt=usr_prompt,
        n=1,
        size="512x512",
    )
    # Retrieve Image URL & save it
    img_url = img_response['data'][0]['url']
    image_location = save_image(img_url)
    print(image_location)
    return image_location


    
def save_image(url):
    file_name = str(datetime.now()) + ".png"
    folder_path = "/Users/hallowsyves/Documents/HourlyMotivation/Media/Images"
    file_path = os.path.join(folder_path, file_name)
    urllib.request.urlretrieve(url, file_path)
    return file_path



def load_image(image, quote):
    # Load Background Image
    image_ = Image.open(image)
    image_.putalpha(127)

    # center text
    center_x = image_.width / 2
    center_y = image_.height / 2

    image_.filter(ImageFilter.GaussianBlur(5))
    image_load = ImageDraw.Draw(image_)

    # Draw Image
    font = load_font()
    image_load.text((center_x,center_y), quote, anchor='mm', font=font, fill=(255,255,255))

    # Show new Image with quote
    image_.show()
    image_.save(image)



def load_font():
    times_new = ImageFont.truetype('/Users/hallowsyves/Documents/HourlyMotivation/Fonts/AUGUSTUS.TTF', 25)
    return times_new

def check_for_duplicates(quote):
    conn = sqlite3.connect('quotes.db')
    cursor = conn.cursor()
    query = 'SELECT * FROM {}'.format('quotes')
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        if quote in row:
            return False
    
    return True

def add_to_database(quote):
    connection = sqlite3.connect('quotes.db')
    cursor = connection.cursor()

    query = 'INSERT INTO quotes (quote) VALUES (?)'
    cursor.execute(query, (quote,))

    connection.commit()
    cursor.close()
    connection.close()

def print_database():
    connection = sqlite3.connect('quotes.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM quotes')
    quotes = cursor.fetchall()

    for quote in quotes:
        print(quote)
    connection.close()
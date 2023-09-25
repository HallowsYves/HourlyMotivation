import requests

# SETUP
page_id = 133011489894765
F_KEY = open("F_KEY", "r").read()

def make_post(quote, image):
    msg = quote
    image_url = 'https://graph.facebook.com/{}/photos'.format(page_id)
    image_location = image

    img_payload = {
        'url': image_location,
        'access_token': F_KEY
    }

    response = requests.post(image_url, data=img_payload)
    



    if response.status_code != 200:
        raise Exception("Failed to post to Facebook: {}".format(response.content))
    print("Posted.")

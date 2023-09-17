import openai

API_KEY = open("API_KEY", "r").read()
openai.api_key = API_KEY

response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages= [
        {"role": "user", "content": "generate a motivational Quote"}
    ]
)


img_response = openai.Image.create(
    prompt= response['choices'][0]['message']['content'],
    n=1,
    size="1024x1024",
)
img_url = img_response['data'][0]['url']
print(img_url)
print(response)
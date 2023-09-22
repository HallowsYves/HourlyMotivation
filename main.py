from hourly_motivation import generate_image, generate_quote, load_image
# Generate Quote
quote = generate_quote("Generate a motivational quote, WITHOUT using any quotes from anyone else in history, without *** at the beginning and without *** at the end")

# Generate Image
background_img = generate_image("Beautiful Nature Background")

# Load Image
load_image(background_img, quote)

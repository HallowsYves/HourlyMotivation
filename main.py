import hourly_motivation
from hourly_motivation import generate_image, generate_quote, load_image
# Generate Quote
quote = generate_quote("Generate a motivational quote")

# Generate Image
background_img = generate_image("Beautiful Nature Background")

# Load Image
load_image(background_img, quote)

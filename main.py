import hourly_motivation
from hourly_motivation import generate_image, generate_quote, load_image, print_database
# Generate Quote
quote = generate_quote("Generate a motivational quote, without quoting anyone from history.")

# Generate Image
background_img = generate_image("Beautiful Nature Background")

# Load Image
load_image(background_img, quote)


# quick test
print_database()
from hourly_motivation import generate_image, generate_quote, load_image, print_database, generate_test_img
from posts import make_post
# Generate Quote

quote = generate_quote("Generate a motivational quote, without quoting anyone from history.")
# Generate Image
background_img = generate_image("Beautiful Nature Background")


# This posted the background image, not the actual image, need to fix
make_post(quote, background_img)

# Load Image
load_image(background_img, quote)


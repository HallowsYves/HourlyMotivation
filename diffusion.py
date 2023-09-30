import torch
from diffusers import StableDiffusionPipeline

# STABLE DIFFUSION
model_id = "dreamlike-art/dreamlike-photoreal-2.0"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompts = ["Cute Rabbit, Ultra HD, realistic, futuristic, sharp, octane render, photoshopped, photorealistic, soft, pastel, Aesthetic, Magical background",
           "Anime style aesthetic landscape, 90's vintage style, digital art, ultra HD, 8k, photoshopped, sharp focus, surrealism, akira style, detailed line art",
           "Beautiful, abstract art of a human mind, 3D, highly detailed, 8K, aesthetic"]


images = []

for i, prompt in enumerate(prompts):
    image = pipe(prompt).images[0]
    image.save(f'result_{i}.jpg')
    images.append(image) 
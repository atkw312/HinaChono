import torch
from diffusers import (
    StableDiffusionXLPipeline, 
    EulerAncestralDiscreteScheduler,
    AutoencoderKL,
    DPMSolverMultistepScheduler
)
from PIL import Image
from safetensors.torch import load_file
from compel import Compel, ReturnedEmbeddingsType
from expressions import exp


vae = AutoencoderKL.from_pretrained(
    "madebyollin/sdxl-vae-fp16-fix", 
    torch_dtype=torch.float16
)

lora_filename = "./models/Chono_Hina-63.safetensors"
modelID = "./models/waiNSFWIllustrious_v80.safetensors"

expressions = exp

pipe = StableDiffusionXLPipeline.from_single_file(
    modelID, 
    vae=vae,
    torch_dtype=torch.float16, 
    use_safetensors=True,
    clip_skip=2,
)

pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)
pipe.to('cuda')
pipe.load_lora_weights(lora_filename)
pipe.fuse_lora(lora_scale=0.8)
pipe.load_textual_inversion("./models/easynegative.safetensors", token="EasyNegative") #TODO check this later

async def generate_image(p: str) -> Image:

    opener = 'masterpiece,best quality,amazing quality, chono hina, pink hair, pink eyes, hair bun, 1girl, solo, '
    outfit = 'school uniform, blue blazer, red ribbon, jacket, white shirt, shirt, ribbon, neck ribbon, '
    location = 'classroom, '
    prompt = opener + outfit + location + exp[p]
    print(prompt)
    negative_prompt = "bad quality,worst quality,worst detail,sketch,censor, simple background,transparent background, EasyNegative"
    guidance_scale = 5
    inference_steps = 20


    compel = Compel(
        tokenizer=[pipe.tokenizer, pipe.tokenizer_2] ,
        text_encoder=[pipe.text_encoder, pipe.text_encoder_2],
        returned_embeddings_type=ReturnedEmbeddingsType.PENULTIMATE_HIDDEN_STATES_NON_NORMALIZED,
        requires_pooled=[False, True]
    )

    conditioning, pooled = compel(prompt)

    image = pipe(
        prompt_embeds=conditioning, 
        pooled_prompt_embeds=pooled, 
        negative_prompt=negative_prompt, 
        width=1024,
        height=576,
        guidance_scale=guidance_scale,
        num_inference_steps=inference_steps
    ).images[0]

    return image


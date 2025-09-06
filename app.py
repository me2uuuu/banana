# app.py
import os
from io import BytesIO
from PIL import Image
import gradio as gr
from google import genai

API_KEY = os.getenv("GEMINI_API_KEY") or "여기_API_키"
MODEL = "gemini-2.5-flash-image-preview"
client = genai.Client(api_key=API_KEY)

BASE_PROMPT = (
    "Convert this photo into a Roblox-style low-poly 3D avatar, "
    "blocky cubic geometry, flat shading, simple bright colors, front view, 1:1 aspect ratio."
)

def build_prompt(add_sword: bool, add_torch: bool):
    extras = []
    if add_sword:
        extras.append("add a sword")
    if add_torch:
        extras.append("add a torch")
    if extras:
        return BASE_PROMPT + " " + ", ".join(extras) + "."
    return BASE_PROMPT

def pil_to_png_bytes(img: Image.Image) -> bytes:
    buf = BytesIO()
    img.convert("RGB").save(buf, format="PNG")
    return buf.getvalue()

def robloxify(photo: Image.Image, add_sword: bool, add_torch: bool):
    if photo is None:
        return None

    prompt = build_prompt(add_sword, add_torch)

    try:
        resp = client.models.generate_content(
            model=MODEL,
            contents=[prompt, photo]
        )
    except Exception:
        png_bytes = pil_to_png_bytes(photo)
        resp = client.models.generate_content(
            model=MODEL,
            contents=[
                prompt,
                {"inline_data": {"mime_type": "image/png", "data": png_bytes}},
            ],
        )

    for part in resp.candidates[0].content.parts:
        if getattr(part, "inline_data", None):
            out = Image.open(BytesIO(part.inline_data.data)).convert("RGB")
            return out
    return None

with gr.Blocks(title="Roblox-Style Photo Avatarizer") as demo:
    gr.Markdown("# 🧱 Roblox-Style Photo → Avatar")
    with gr.Row():
        inp = gr.Image(type="pil", label="Upload a photo")
        with gr.Column():
            sword = gr.Checkbox(label="Add sword", value=True)
            torch = gr.Checkbox(label="Add torch", value=False)
            btn = gr.Button("Convert")
    out = gr.Image(type="pil", label="Roblox-style result")

    btn.click(robloxify, [inp, sword, torch], out)

if __name__ == "__main__":
    demo.launch()

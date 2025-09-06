# 🧱 Roblox Kitsch Goods

We built a **Roblox-style photo-to-avatar converter** using the
Gemini 2.5 Flash Image Preview model (Nano Banana).  
By uploading any photo, the app transforms it into a **blocky,
low-poly Roblox-style avatar**. Options allow adding a sword, a torch,
or even a helmet. The results carry a playful **병맛감성** vibe:
funny, endearing, and almost like collectible goods.

## ✨ Features
- Upload a photo → get a Roblox-style avatar
- Add fun extras like sword, torch, or helmet
- Built with Gradio for a simple demo UI

## 🚀 How to Run
```bash
pip install -r requirements.txt
export GEMINI_API_KEY="your_key"
python app.py

⚠️ Notes

This project calls the Gemini API.

Running inside Kaggle Notebook may show errors like:

SyntaxError: Unexpected token 'F', "Forbidden" is not valid JSON


This happens because external API calls can be restricted in Kaggle.

✅ To test properly, run locally on your machine with a valid API key.

📹 Submission Notes (≈190 words)

We created a Roblox-style photo-to-avatar converter using the Gemini 2.5 Flash Image Preview model (Nano Banana). The idea was to make something fun and lighthearted for the hackathon: instead of generating avatars only from text, we let users upload any photo and see it reimagined as a blocky, low-poly Roblox-style character.

Our prototype uses a simple Gradio web interface. The user uploads a picture, selects optional accessories (such as a sword, a torch, or a helmet), and presses a button. The app sends both the prompt and the uploaded photo to the model. The model returns an inline image, which is decoded and displayed instantly in the browser. The outputs are deliberately imperfect — but this is where the charm lies. They are funny, endearing, and carry a retro 병맛감성: a “work-in-progress” look that feels playful and almost like collectible goods.

This small project demonstrates how Nano Banana can be applied creatively to reimagine ordinary content. It shows that with minimal code, developers can wrap Gemini into playful tools that remix images and generate stylized avatars. It’s not polished — and that’s exactly why it feels cute, funny, and memorable.





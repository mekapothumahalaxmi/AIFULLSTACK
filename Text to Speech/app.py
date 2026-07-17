!pip install -q gradio google-genai

import gradio as gr
from google import genai

client = genai.Client(api_key="AQ.Ab8RN6I_OAtGs72pa0IQvqZdVA9y_rly4pdqYd8Sf8TYhGN3fg")

def transcribe(audio_path):
    if audio_path is None:
        return "Please record some audio."

    audio_file = client.files.upload(file=audio_path)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            "Transcribe this audio exactly as spoken. Do not summarize. Include punctuation.",
            audio_file
        ]
    )

    return response.text

with gr.Blocks(title="Gemini Audio Transcription") as demo:

    gr.Markdown("# 🎤 Gemini Speech to Text")

    audio = gr.Audio(
        sources=["microphone"],
        type="filepath",
        label="Record your voice"
    )

    output = gr.Textbox(
        label="Transcription",
        lines=10
    )

    btn = gr.Button("Transcribe")

    btn.click(
        fn=transcribe,
        inputs=audio,
        outputs=output
    )

demo.launch()

import gradio as gr
import soundfile as sf
import numpy as np
import os
from kittentts import KittenTTS

# Initialize the model
model = KittenTTS("KittenML/kitten-tts-nano-0.1")

# Available voices
VOICES = [
    'expr-voice-2-m', 
    'expr-voice-2-f', 
    'expr-voice-3-m', 
    'expr-voice-3-f',  
    'expr-voice-4-m', 
    'expr-voice-4-f', 
    'expr-voice-5-m', 
    'expr-voice-5-f'
]

def generate_speech(text, voice):
    # Generate audio
    audio = model.generate(text, voice=voice)
    
    # Save to temporary file
    output_path = "temp_output.wav"
    sf.write(output_path, audio, 24000)
    
    # Return the path to the audio file
    return output_path

# Create Gradio interface
with gr.Blocks(title="KittenTTS Demo") as demo:
    gr.Markdown("# 🐱 KittenTTS Demo")
    gr.Markdown("Enter text and select a voice to generate speech!")
    
    with gr.Row():
        with gr.Column():
            text_input = gr.Textbox(
                label="Input Text",
                placeholder="Enter text to convert to speech...",
                lines=5
            )
            voice_selector = gr.Dropdown(
                choices=VOICES,
                value=VOICES[0],
                label="Select Voice"
            )
            generate_btn = gr.Button("Generate Speech", variant="primary")
        with gr.Column():
            audio_output = gr.Audio(label="Generated Speech", type="filepath")
    
    # Examples
    gr.Examples(
        examples=[
            ["Hello, welcome to the KittenTTS demo! This is an ultra-lightweight text-to-speech model.", "expr-voice-2-m"],
            ["The quick brown fox jumps over the lazy dog.", "expr-voice-3-f"],
            ["Artificial intelligence is transforming the world in remarkable ways.", "expr-voice-4-m"],
        ],
        inputs=[text_input, voice_selector],
        outputs=audio_output,
        fn=generate_speech,
        cache_examples=True
    )
    
    # Connect the button to the function
    generate_btn.click(
        fn=generate_speech,
        inputs=[text_input, voice_selector],
        outputs=audio_output
    )

if __name__ == "__main__":
    demo.launch()
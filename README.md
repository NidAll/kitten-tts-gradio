# KittenTTS Gradio Interface

This is a simple Gradio interface for the KittenTTS text-to-speech model.

## Features

- Convert text to speech using the ultra-lightweight KittenTTS model
- Choose from 8 different voices
- Real-time audio generation and playback

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/NidAll/kitten-tts-gradio/
   cd https://github.com/NidAll/kitten-tts-gradio/
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   python app.py
   ```

5. Open your browser and go to `http://localhost:7860`

## Usage

1. Enter text in the input box
2. Select a voice from the dropdown
3. Click "Generate Speech"
4. Listen to the generated audio

## Voices

Available voices:
- expr-voice-2-m (Male)
- expr-voice-2-f (Female)
- expr-voice-3-m (Male)
- expr-voice-3-f (Female)
- expr-voice-4-m (Male)
- expr-voice-4-f (Female)
- expr-voice-5-m (Male)
- expr-voice-5-f (Female)

## Model

This interface uses the [KittenTTS](https://github.com/KittenML/KittenTTS) model, an ultra-lightweight text-to-speech model with just 15 million parameters.
=======
# kitten-tts-gradio

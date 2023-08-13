import os
import yaml
import openai
import gradio as gr
import os
from pathlib import Path

# sample .wav files
# https://www2.cs.uic.edu/~i101/SoundFiles/preamble.wav

## API INSTANTIATION
## ---------------------------------------------------------------------------------------------------------------------
# Loading the API key and organization ID from file (NOT pushed to GitHub)
# store API keys in yaml file like "sample.yml"
all_keys = yaml.safe_load(open(Path(os.getenv("API_KEYS_FILE"))))
api_key = all_keys["API_KEYS"]["OPENAI"]

# Applying our API key and organization ID to OpenAI
openai.organization = api_key['ORG_ID']
openai.api_key = api_key['API_KEY']



## GRADIO HELPER FUNCTIONS
## ---------------------------------------------------------------------------------------------------------------------
def transcribe(audio_intake_file):
    '''
    Transcribes the input audio using OpenAI's Whisper API

    Inputs:
        - audio_intake_file (.wav audio file): Audio intake received from the Gradio UI

    Returns:
        - transcript (Gradio textbox): The transcription provided by OpenAI's Whisper API
    '''

    # Appending the .wav file extension to the existing audio file
    # os.rename(audio_intake_file, audio_intake_file + '.wav')
    print(audio_intake_file)

    # Loading the audio file in a read-only bytes format
    rb_audio = open(audio_intake_file, 'rb')

    # Getting the transcription from OpenAI's Whisper API
    transcript = openai.Audio.transcribe(
        model = api_key["MODELS"]["AUDIO2TEXT"], 
        file = rb_audio)

    return transcript





## GRADIO UI LAYOUT & FUNCTIONALITY
## ---------------------------------------------------------------------------------------------------------------------
# Defining the building blocks that represent the form and function of the Gradio UI
with gr.Blocks() as demo:
    
    # Instantiating the UI interface
    header = gr.Markdown('# Whisper-Gradio UI!')
    audio_intake = gr.Audio(source = 'upload', type = 'filepath')
    transcript = gr.Textbox(label = 'Transcription', interactive = False)
    transcribe_button = gr.Button('Transcribe My Audio')

    # Defining the behavior for when the transcribe button is clicked
    transcribe_button.click(fn = transcribe,
                            inputs = audio_intake,
                            outputs = transcript)




## SCRIPT INVOCATION
## ---------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":

    # Launching the Gradio UI
    demo.launch()
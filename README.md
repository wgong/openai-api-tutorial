## Using OpenAI, LangChain, and Gradio to Build Custom GenAI Applications

- https://youtu.be/1MsmqMg3yUc 

- https://github.com/dkhundley/openai-api-tutorial/tree/main/src


## Setup

```
$ git clone git@github.com:wgong/openai-api-tutorial.git
$ conda create -n gradio
$ conda activate gradio
$ pip install -r requirements.txt
```
create an env var called `API_KEYS_FILE` which points to a file located at `~/Documents/keys/API-keys.yaml` that stores OpenAI API key info
## Run
```
$ cd openai-api-tutorial/src
$ gradio chat-ui.py
$ gradio combined-dalle-ui.py
$ gradio whisper.py

```
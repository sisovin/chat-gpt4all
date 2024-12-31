import json
import os
from gpt4all import GPT4All

# Load configuration from config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

model_name = config["model_name"]
dir_path = "models"

# Debug print statements
# print(f"Model name: {model_name}")
# print(f"Directory path: {dir_path}")

# Create a directory to store the model
if not os.path.exists(dir_path):
    os.makedirs(dir_path, exist_ok=True)

# Update model_path to include the directory path
full_model_path = os.path.join(dir_path, model_name)

# Check if the model file exists locally
if not os.path.exists(full_model_path):
    print(
        f"Model file {full_model_path} does not exist locally. Attempting to download..."
    )

# Initialize the model
try:
    model = GPT4All(
        model_name, model_path=dir_path, device="cpu", allow_download=True
    )  # Use CPU backend if CUDA is not available
    with model.chat_session():
        print(
            model.generate(
                "How can I run LLMs efficiently on my laptop?", max_tokens=1024
            )
        )
except ValueError as e:
    print(f"Error initializing model: {e}")
except RuntimeError as e:
    print(f"Runtime error: {e}")

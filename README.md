# GPT4All Chatbot

This project demonstrates how to use the GPT4All library to run a large language model (LLM) on your local machine. The script loads a model configuration from a JSON file, checks if the model file exists locally, and downloads it if necessary. It then initializes the model and generates a response to a sample query.

## Requirements

- Python 3.7+
- CUDA (optional, for GPU acceleration)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/sisovin/chat-gpt4all.git
    cd chat-gpt4all
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv gpt4all-dev
    gpt4all-dev\Scripts\activate  # On Windows
    source gpt4all-dev/bin/activate  # On macOS/Linux
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. (Optional) If you want to use GPU acceleration, install the CUDA dependencies:

    ```sh
    pip install "gpt4all[cuda]"
    ```

## Configuration

Create a config.json  file in the project directory with the following content:

```json
{
    "model_name": "Llama-3.2-3B-Instruct-Q4_0.gguf"
}
```

## Usage

Run the main.py script:

```sh
python main.py
```

The script will:

1. Load the model configuration from config.json.
2. Check if the model file exists locally in the models directory.
3. Download the model file if it does not exist locally.
4. Initialize the model and generate a response to a sample query.

## Troubleshooting

If you encounter any issues related to missing CUDA libraries, ensure that you have installed the necessary CUDA dependencies and that they are accessible. Refer to the [CUDA Installation Guide for Windows](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html) for detailed instructions.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
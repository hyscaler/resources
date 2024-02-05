# How to Set Up and Use LocalAI

## Introduction
LocalAI is a versatile, open-source alternative to OpenAI that serves as a drop-in replacement for the REST API, fully compatible with OpenAI API specifications. With LocalAI, you gain the power to perform local inferencing, enabling you to run Large Language Models (LLMs), generate images, audio, and more, all on consumer-grade hardware or within your on-premises infrastructure. Notably, LocalAI is designed to function without the need for a GPU, making it accessible to a wider range of users.

**Key Features:**
- **Local, OpenAI Drop-In Alternative REST API:** You retain complete ownership of your data and processing.
- **No GPU Required:** LocalAI can operate efficiently on standard hardware, eliminating the need for expensive GPU setups.
- **No Internet Access Required:** Your AI operations stay entirely within your local environment, ensuring data security and privacy.
- **Optional GPU Acceleration:** For users with GPU resources, LocalAI offers the option to leverage GPU acceleration.
- **Supports Multiple Models:** LocalAI is compatible with various model families and architectures, giving you flexibility in your AI tasks.
- **Efficient Model Loading:** Once loaded for the first time, models are kept in memory for faster and more responsive inferencing.
- **Optimized Inference:** LocalAI doesn't shell out to external processes but utilizes efficient bindings, resulting in improved inference speed and performance.

LocalAI is actively maintained by the dedicated team led by mudler, offering an open and community-driven approach to AI deployment and inference. Whether you're a developer, researcher, or business professional, LocalAI empowers you to harness the potential of AI without compromising on control and privacy.

Visit [LocalAI](https://localai.io/) to learn more and start using this powerful open-source AI platform today!


## Requirements

To run the LocalAI with Gradio interface, you'll need the following prerequisites:

- **Docker:** To run LocalAI's Docker container for model inference.
- **Python (>=3.10.6):** The programming language used to create the Gradio interface.
- **Pip:** The Python package manager for installing Python libraries.
- **Gradio:** A Python library for creating web-based UIs for interacting with AI models.

## Step-by-Step Guide

**Step 1: Install Docker**

Docker allows you to run containerized applications, which are necessary to use LocalAI. Follow these steps to install Docker on your system:

1. Visit the official Docker website at https://docs.docker.com/get-docker/ and download Docker Desktop for your operating system (Windows, macOS, or Linux).
2. Install Docker by following the installation instructions for your specific operating system.
3. Once Docker is installed, ensure it's running on your system.

**Step 2: Pull LocalAI Docker Image and Run**

LocalAI provides Docker container images that contain all the necessary dependencies and models. Follow these steps to pull the LocalAI Docker image:

1. Open your terminal or command prompt.
2. Run the following command to pull the LocalAI Docker image and run that:

   ```
   docker run -ti -p 8080:8080 --gpus all localai/localai:v2.7.0-cublas-cuda12-core phi-2
   ```

3. Docker will download the image, which may take some time depending on your internet connection.

**Step 3: Setup Python and Pip**

Python is the backbone of this project, and Pip is the package manager used to install necessary libraries. First, ensure you have Python installed. Then, install or upgrade Pip using:

```bash
python3 -m pip install --user --upgrade pip
```
This command ensures you have the latest version of Pip installed.

**Step 4: Creating a Virtual Environment**

A virtual environment in Python is a self-contained directory that contains a Python installation for a particular project. This approach avoids conflicts between project dependencies. Create and activate a virtual environment with:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Step 5: Installing Required Packages**

Install Gradio using Pip. [Gradio](https://www.gradio.app/) is an open-source library for creating user-friendly web interfaces for machine learning models.

```bash
pip install gradio
```

**Step 5: Initial Code Setup**

Write the following code in a file named `main.py`. This script sets up a basic Gradio interface to interact with the LocalAI API Endpoint.

```python
import gradio as gr
import requests

def get_response_from_api(message):
    url = "http://localhost:8082/v1/chat/completions"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": "phi-2",
        "messages": [{"role": "user", "content": message, "temperature": 0.1}]
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers).json()
        choices = response.get('choices', [])
        if choices:
            bot_message = choices[0].get('message', {}).get('content', "Sorry I don't understand")
        else:
            bot_message = "Sorry I don't understand"
    except Exception as e:
        print(f"An exception occurred: {e}")
        bot_message = "Sorry, I'm unable to reach the server right now."
    
    return bot_message

def chat_with_bot(message, chat_history):
    bot_message = get_response_from_api(message)
    chat_history.append((message, bot_message))
    return "", chat_history

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    msg.submit(chat_with_bot, [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
    demo.launch()
```

To run this script, use:

```bash
python3 main.py
```

This will provide you with a URL. When you open this URL, it will take you to the Gradio interface where you can input your prompts.

## Conclusion
In conclusion, LocalAI offers an exciting opportunity to harness the potential of AI with control and privacy. With this open-source alternative to OpenAI, you can perform local inferencing, run AI models, and create powerful applications—all without the need for GPUs.

For a detailed visual walkthrough of the setup process, we invite you to watch our comprehensive video presentation on YouTube: [LocalAI Setup Guide Video](https://www.youtube.com/watch?v=ojpU7W35-Ww). This video provides step-by-step instructions and additional insights to ensure your success with LocalAI.

Get started today with LocalAI, and join the community of developers, researchers, and businesses that are unlocking the full potential of AI while keeping data ownership in their hands. Visit the [LocalAI website](https://localai.io/) to begin your AI journey.

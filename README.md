# Day 21: Product Photo Background Swapper

An AI-powered tool that automatically removes the background from product photos and replaces them with professional studio-quality backgrounds. It also utilizes a vision model via the Groq API to analyze the product and recommend the best background style.

## Features

- **AI Analysis**: Uses Groq's Large Vision Models (LLM) to detect the product, analyze its style, and recommend a fitting background.
- **Background Removal**: Seamlessly strips the background using `rembg` (U-2-Net model).
- **Background Application**: Applies a variety of pre-defined professional studio gradients, or you can specify a custom hex color.
- **Batch Generation**: Option to generate the product image across all available background styles at once.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/gnarendra9014-blind/day_21-of-ML-Projects.git
   cd day_21-of-ML-Projects
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your Groq API Key:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

## How to Run

Run the script from your terminal:
```bash
python app.py
```

Follow the prompts to:
1. Provide the absolute path to your product image (e.g., `C:\path\to\image.png`).
2. Wait for the AI to analyze the image and recommend a background.
3. Choose the background number from the list or enter a custom hex color.

## Requirements

- Python 3.8+
- Groq API Key

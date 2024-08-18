import PyPDF2
import os
import json
import openai
import anthropic
import requests
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

def load_config() -> dict:
    with open('config.json', 'r') as f:
        return json.load(f)

def load_llm_config() -> dict:
    with open('llm_config.json', 'r') as file:
        return json.load(file)

def load_prompt() -> str:
    with open('prompt.md', 'r') as f:
        return f.read()

def extract_text_from_pdf(pdf_path: str) -> str:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

def preprocess_text(text: str) -> str:
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    
    processed_sentences = []
    for sentence in sentences:
        words = word_tokenize(sentence.lower())
        words = [lemmatizer.lemmatize(word) for word in words if word.isalnum() and word not in stop_words]
        processed_sentences.append(' '.join(words))
    
    return ' '.join(processed_sentences)

def count_tokens(text: str, model_name: str) -> int:
    try:
        def custom_tokenize(text):
            return text.split()  # Simple whitespace tokenization
        return len(custom_tokenize(text))
    except Exception as e:
        print(f"Error loading tokenizer for model {model_name}: {str(e)}")
        return 0  # Return 0 tokens if there's an error

def get_cost_per_token(model_name: str) -> float:
    costs = {
        "gpt-4o": 0.03 / 1000,
        "claude-3-sonnet": {"input": 0.003 / 1000, "output": 0.015 / 1000},
    }
    return costs.get(model_name, 0.0)

def analyze_with_gpt4(text: str, title: str, prompt: str) -> str:
    openai.api_key = os.getenv('OPENAI_API_KEY')
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": f"Title: {title}\n\nContent: {text}"}
            ]
        )
        print(f"Response from OpenAI: {response}")  # Debugging line
        return response['choices'][0]['message']['content']
    except Exception as e:
        raise Exception(f"Error in GPT-4o analysis: {str(e)}")

def analyze_paper_with_llm(text: str, title: str, prompt: str, llm_config: dict) -> tuple:
    llm = llm_config['llms']['text_generation']['default']
    try:
        if llm == "gpt-4o":
            analysis = analyze_with_gpt4(text, title, prompt)
        else:
            raise ValueError(f"Unsupported LLM: {llm}")
    except Exception as e:
        print(f"Error occurred while analyzing with {llm}: {str(e)}")
        return "Analysis failed due to an error.", ""

    formatted_output = f"# {title}\n\n{analysis.strip()}"
    return formatted_output, text

def process_pdfs_in_directory(input_dir: str, output_dir: str, llm_config: dict, prompt: str):
    os.makedirs(output_dir, exist_ok=True)

    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.pdf'):
                pdf_path = os.path.join(root, file)
                title = os.path.splitext(file)[0]
                
                relative_path = os.path.relpath(root, input_dir)
                output_subdir = os.path.join(output_dir, relative_path)
                os.makedirs(output_subdir, exist_ok=True)
                output_file = os.path.join(output_subdir, f"{title}_analysis.md")
                
                if os.path.exists(output_file):
                    print(f"Skipping {file} as analysis already exists.")
                    continue

                try:
                    text = extract_text_from_pdf(pdf_path)
                except Exception as e:
                    print(f"Error extracting text from {file}: {str(e)}")
                    continue

                analysis, preprocessed_text = analyze_paper_with_llm(text, title, prompt, llm_config)

                with open(output_file, 'w') as f:
                    f.write(analysis)
                
                print(f"Completed analysis of {file} using {llm_config['llms']['text_generation']['default']}.")

def main():
    config = load_config()
    llm_config = load_llm_config()
    prompt = load_prompt()

    input_dir = config['input_dir']
    output_dir = config['output_dir']

    if not os.path.exists(input_dir):
        print(f"Input directory {input_dir} does not exist. Exiting.")
        return

    process_pdfs_in_directory(input_dir, output_dir, llm_config, prompt)

    print("All PDF files processed.")

if __name__ == "__main__":
    main()
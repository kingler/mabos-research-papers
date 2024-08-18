import PyPDF2
import os
import json
import openai



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
        return response.choices[0].message['content']
    except Exception as e:
        raise Exception(f"Error in GPT-4 analysis: {str(e)}")

def test_model_access(pdf_path: str):
    config = load_config()
    llm_config = load_llm_config()
    prompt = load_prompt()

    title = os.path.splitext(os.path.basename(pdf_path))[0]
    text = extract_text_from_pdf(pdf_path)

    try:
        analysis = analyze_with_gpt4(text, title, prompt)
        print(f"Analysis for {title}:\n{analysis}")
    except Exception as e:
        print(f"Error occurred while analyzing with gpt-4o: {str(e)}")

# Example usage
test_model_access('/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-research-papers/Model Driven Development/Business and Model-Driven Development of BDI Multi-Agent Systems.pdf')
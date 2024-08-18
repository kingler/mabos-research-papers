import os
import json
import anthropic
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load configuration files
with open('llm_config.json', 'r') as f:
    llm_config = json.load(f)

with open('reformat_text_prompt.md', 'r') as f:
    prompt_template = f.read()

# Set up API details
api_url = llm_config['llms']['text_generation']['available'][0]['claude-3-5-sonnet-20240620']['url']
api_key = os.getenv('ANTHROPIC_API_KEY')

def reformat_text(text):
    """
    Process a single text file using the Claude 3.5 sonnet LLM.
    """
    prompt = prompt_template.replace('{{TEXT_TO_FORMAT}}', text)
    
    client = anthropic.Anthropic(api_key=api_key)
    
    try:
        message = client.messages.create(
            model="claude-3-sonnet-20240620",
            max_tokens=8192,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return message.content
    except anthropic.APIError as e:
        print(f"Error calling Claude API: {e}")
        return None

def process_file(file_path):
    """
    Process a single file, reformat its content, and save the result.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        reformatted_content = reformat_text(content)
        
        if reformatted_content:
            new_file_path = file_path.replace('.txt', '_reformatted.txt')
            with open(new_file_path, 'w', encoding='utf-8') as f:
                f.write(reformatted_content)
            print(f"Reformatted: {file_path} -> {new_file_path}")
        else:
            print(f"Failed to reformat: {file_path}")
    except IOError as e:
        print(f"Error processing file {file_path}: {e}")

def traverse_directories(directory):
    """
    Recursively traverse directories and process text files.
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt') and not file.endswith('_reformatted.txt'):
                process_file(os.path.join(root, file))

def main():
    output_directory = "Output_Directory"
    if not os.path.exists(output_directory):
        print(f"Error: Directory '{output_directory}' does not exist.")
        return
    
    traverse_directories(output_directory)

if __name__ == "__main__":
    main()
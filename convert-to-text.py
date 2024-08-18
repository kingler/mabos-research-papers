import os
import json
from PyPDF2 import PdfReader

def load_config(config_path):
    with open(config_path, 'r') as file:
        return json.load(file)

def convert_pdf_to_txt(pdf_path, txt_path):
    with open(pdf_path, 'rb') as pdf_file:
        reader = PdfReader(pdf_file)
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            for page in reader.pages:
                txt_file.write(page.extract_text() + '\n')

def main():
    config_path = 'config.json'
    config = load_config(config_path)

    input_dir = config['input_dir']
    output_dir = config['output_dir']

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through the directory structure defined in config.json
    for root, dirs, files in os.walk(input_dir):
        for filename in files:
            if filename.endswith('.pdf'):
                pdf_path = os.path.join(root, filename)
                
                # Create the corresponding output path
                relative_path = os.path.relpath(root, input_dir)
                output_subdir = os.path.join(output_dir, relative_path)
                
                # Ensure the output subdirectory exists
                if not os.path.exists(output_subdir):
                    os.makedirs(output_subdir)

                txt_filename = filename.replace('.pdf', '.txt')
                txt_path = os.path.join(output_subdir, txt_filename)

                # Convert PDF to TXT
                convert_pdf_to_txt(pdf_path, txt_path)
                print(f'Converted: {pdf_path} to {txt_path}')

if __name__ == "__main__":
    main()
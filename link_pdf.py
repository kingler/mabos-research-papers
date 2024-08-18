import os
import json

# Function to read and parse the config.json file
def load_config(config_path):
    with open(config_path, 'r') as file:
        return json.load(file)

# Function to format PDF links correctly
def format_pdf_link(filename):
    return f'![[{filename}]]'

# Function to correct PDF links in markdown files
def correct_pdf_links(output_dir, folder_structure):
    for folder, subfolders in folder_structure.items():
        folder_path = os.path.join(output_dir, folder)
        if os.path.exists(folder_path):
            for filename in os.listdir(folder_path):
                if filename.endswith('.md'):
                    markdown_file_path = os.path.join(folder_path, filename)

                    # Read the content of the markdown file
                    with open(markdown_file_path, 'r') as md_file:
                        content = md_file.readlines()

                    # Initialize variables to track the title and modified content
                    modified_content = []
                    title_found = False
                    pdf_link = format_pdf_link(filename.replace('.md', '.pdf'))

                    for line in content:
                        # Check for the title line
                        if line.startswith('# Title:'):
                            title_found = True
                            modified_content.append(line)  # Keep the title line
                            modified_content.append(pdf_link + '\n')  # Insert the correct link
                            continue  # Move to the next line

                        # Skip incorrect links and double links
                        if '![[' in line and ']]' not in line:
                            continue  # Skip incorrect link lines
                        if '![[' in line and ']]' in line:
                            continue  # Skip existing correct links

                        modified_content.append(line)

                    # Write the modified content back to the markdown file
                    with open(markdown_file_path, 'w') as md_file:
                        md_file.writelines(modified_content)

# Main function to execute the script
def main():
    config_path = 'config.json'
    output_dir = 'Output_Directory'

    # Check if the Output_Directory exists
    if not os.path.exists(output_dir):
        print(f"Error: The directory '{output_dir}' does not exist.")
        return

    # Load the configuration
    try:
        config = load_config(config_path)
    except json.JSONDecodeError:
        print("Error: The config.json file is not valid JSON.")
        return

    # Correct PDF links in the specified directory
    correct_pdf_links(output_dir, config['directories'])

# Run the script
if __name__ == "__main__":
    main()
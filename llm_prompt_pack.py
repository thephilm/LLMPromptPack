import os
from datetime import datetime
from tkinter import filedialog, Tk

def select_directory():
    root = Tk()
    root.withdraw()  # Hide the main window
    directory = filedialog.askdirectory(title="Select Project Directory")
    return directory

def generate_directory_structure(directory, output_file):
    with open(output_file, 'a', encoding='utf-8') as output:
        output.write("Directory Structure:\n")
        output.write(generate_structure(directory, ''))

def generate_structure(directory, indent, last=True):
    directory_content = ""
    files_and_dirs = sorted(os.listdir(directory))
    for i, item in enumerate(files_and_dirs):
        item_path = os.path.join(directory, item)
        connector = '└── ' if i == len(files_and_dirs) - 1 else '├── '
        if os.path.isdir(item_path):
            directory_content += f"{indent}{connector}{item}/\n"
            directory_content += generate_structure(item_path, indent + ('    ' if last else '│   '), i == len(files_and_dirs) - 1)
        else:
            directory_content += f"{indent}{connector}{item}\n"
    return directory_content

def collect_text_from_files(directory, output_file):
    target_extensions = ['.js', '.py', '.txt', '.xml', '.html', '.css']
    with open(output_file, 'a', encoding='utf-8') as output:
        output.write("\n\nFile Contents:\n")
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_extension = os.path.splitext(file)[1].lower()
                if file_extension in target_extensions:
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            output.write(f"--- File: {file_path} ---\n")
                            output.write(content)
                            output.write("\n--- End of File ---\n\n")
                    except Exception as e:
                        print(f"Failed to read {file_path}: {e}")

if __name__ == "__main__":
    directory = select_directory()
    if directory:
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        output_file = f"project_contents_{timestamp}.txt"
        
        with open(output_file, 'w', encoding='utf-8') as output:
            output.write("")
        
        generate_directory_structure(directory, output_file)
        collect_text_from_files(directory, output_file)
        print(f"Project contents have been written into: {output_file}")
    else:
        print("No directory selected.")
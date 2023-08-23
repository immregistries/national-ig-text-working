import os
import re

def find_special_characters(directory):
    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith(".html"):
                print(f' - Looking at file: {file_name}')
                file_path = os.path.join(root, file_name)
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    if re.search(r'[^\x00-\x7F]', content):
                        print(f" + File with special characters found: {file_path}")


current_directory = os.getcwd()
print('Will find files that need have special characters this directory: ' + current_directory)

find_special_characters(current_directory)
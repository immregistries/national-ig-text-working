from bs4 import BeautifulSoup
import os
import logging

# Configure logging
logging.basicConfig(filename='error_log.log', level=logging.ERROR)

def prettify_html(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.html'):
                try:
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as f:
                        soup = BeautifulSoup(f, 'html.parser')

                    pretty_html = soup.prettify(formatter="html")

                    with open(file_path, 'w') as f:
                        f.write(pretty_html)
                    print(f"Reformatted file {file_path}")
                    
                except Exception as e:
                    logging.error(f"Error reformatting file {file_path}: {e}")

current_directory = os.getcwd()
print('Will prettify data from this directory: ' + current_directory)

# Commenting out, this function is converting html entities such as &mdash; to their unicode equivalents
prettify_html(current_directory)
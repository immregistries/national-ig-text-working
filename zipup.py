import zipfile
import os

def zip_html_files(zipf_path):
    with zipfile.ZipFile(zipf_path, 'w') as zipf:
        for root, dirs, files in os.walk('.'):
            # Add directories even if empty
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                zipf.write(dir_path, os.path.relpath(dir_path))
            # Add HTML files
            for file in files:
                if file.endswith('.html'):
                    path_in_zip = os.path.join('/', os.path.relpath(root), file)
                    zipf.write(os.path.join(root, file), arcname=path_in_zip)

zip_file_name = 'The Interim, Computable HL7 v2.5.1 Implementation Guide for Immunization Messaging.zip'
zip_html_files(zip_file_name)
print(f"{zip_file_name} created successfully.")
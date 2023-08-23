import zipfile
import os

def zip_html_files(zipf_path):
    with zipfile.ZipFile(zipf_path, 'w') as zipf:
        for root, _, files in os.walk('.'):
            for file in files:
                if file.endswith('.html'):
                    path_in_zip = os.path.join('The Interim, Computable HL7 v2.5.1 Implementation Guide for Immunization Messaging/_/', os.path.relpath(root), file)
                    zipf.write(os.path.join(root, file), arcname=path_in_zip)

zip_file_name = 'The Interim, Computable HL7 v2.5.1 Implementation Guide for Immunization Messaging.zip'
zip_html_files(zip_file_name)
print(f"{zip_file_name} created successfully.")
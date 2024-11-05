import shutil 
import os.path

# Creating the ZIP file 
archived = shutil.make_archive('./zip_1', 'zip', './')

if os.path.exists('./zip_1.zip'):
   print(archived) 
else: 
   print("ZIP file not created")
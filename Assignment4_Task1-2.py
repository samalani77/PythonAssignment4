import os
file_name = "sample.txt"

if os.path.exists(file_name):
    print(f"File exists")
else:
    print(f"Error : The file {file_name} was not found.")


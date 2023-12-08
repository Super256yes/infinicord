import requests
import ast
import os

def hexDecoder(hex_data, exported_file_name):
    try:
        binary_data = bytes.fromhex(hex_data)

        with open(exported_file_name, "wb") as decoded_file:
            decoded_file.write(binary_data)
        print(f"File '{exported_file_name}' successfully created with the hex data.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Input file name to download
requested_file_name = input("File to download: ")
requested_file_path = os.path.join("uploadedFiles", f"{requested_file_name}.txt")

print("Attempting to download file[s] within: " + requested_file_path)

# Read the content of the file
with open(requested_file_path, "r") as f:
    file_contents = f.read()
    print("Contents from file: " + file_contents)

# Convert the string representation of a list to an actual list
try:
    list_from_requested_file = ast.literal_eval(file_contents)
    print("List:", list_from_requested_file)
except (SyntaxError, ValueError) as e:
    print(f"Error converting string to list: {e}")
    list_from_requested_file = []

# Handle the case where the list contains a Boolean and a URL
if len(list_from_requested_file) == 2 and isinstance(list_from_requested_file[0], str) and isinstance(list_from_requested_file[1], str):
    url = list_from_requested_file[1]
    file_name = list_from_requested_file[0]

    try:
        response = requests.get(url)
        if response.status_code == 200:
            hexDecoder(response.text, file_name)
            print(f"File '{file_name}' created successfully.")
        else:
            print(f"Error: Unable to fetch content. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print("Unexpected list structure. Please check the format.")

import requests
import ast

requestedFileDir = "uploadedFiles/" + input("File to download: ") + ".txt"
print("attempting to download file[s] within: " + requestedFileDir)
with open(requestedFileDir, "r") as f:
    fileContents = f.read()
    print("Contents from file:" + fileContents)
try:
    listFromRequestedFile = ast.literal_eval(fileContents)
    print("List:", listFromRequestedFile)
except (SyntaxError, ValueError) as e:
    print(f"Error converting string to list: {e}")
#use for loop to get all the hexidecimal Strings


url = listFromRequestedFile[1]
fileName = "message.txt"

def hexDecoder(hex, exportedFileName):
    try:
        binaryData = bytes.fromhex(hex)

        with open(exportedFileName, "wb") as decodedFile:
            decodedFile.write(binaryData)
        print(f"File '{exportedFileName}' successfully created with the hex data.")

    except Exception as e:
        print(f"An error occurred: {e}")

try:
    response = requests.get(url)
    if response.status_code == 200:
        hexDecoder(response.text, fileName)
        print("Response Code 200 - Success")
        print("Hex String which was returned: " + response.text)
    else:
        print(f"Error: Unable to fetch content. Status code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {e}")

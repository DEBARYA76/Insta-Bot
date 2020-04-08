import json
from getpass import getpass

def cred_input(json_file):
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    clarifai_api = input("Enter your ClarifAI api key: ")

    # Data to be written
    cred_dictionary = {
        "username" : username,
        "password" : password,
        "clarifai_api" : clarifai_api
    }
    # Serializing json
    json_object = json.dumps(cred_dictionary, indent = 4)
    # Writing to json file
    with open(json_file, "w") as outfile:
        outfile.write(json_object)
    return 0

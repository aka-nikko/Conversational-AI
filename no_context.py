import requests
from time import sleep
from huggingface_api import api

API_URL = "https://api-inference.huggingface.co/models/aka-nikko/ainz-ooal-gown"
headers = {"Authorization": "Bearer " + api}

def warm_up_model():
    warm_up_input = "This is a warm-up input."
    payload = {"inputs": warm_up_input}
    response = requests.post(API_URL, headers=headers, json=payload)
    response_json = response.json()
    return response_json

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

print("Warming Up The Model...")
warm_up_model()
sleep(30)

print("Type A Text And Ainz Ooal Gown Will Respond.\nPress CTRL+C To Exit.\n")

while True:
    try:
        user_input = input("You : ")

        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Ainz: Goodbye!")
            break
        
        print("Ainz: " + query({"inputs": user_input})['generated_text'])
    except KeyboardInterrupt:
        print("\nExiting...")
        exit()
    except Exception as e:
        print(f"An ERROR Occurred: {e}")
        print("Restarting Model... This Will Take A Minute")
        warm_up_model()
        sleep(30)
        continue

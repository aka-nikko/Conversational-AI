import requests
from time import sleep
from huggingface_api import api

API_URL = "https://api-inference.huggingface.co/models/aka-nikko/ainz-ooal-gown"
API_TOKEN = "YOUR_HUGGINGFACE_API_TOKEN"

headers = {"Authorization": f"Bearer {api}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

conversation = {
    "inputs": {
        "past_user_inputs": [],
        "generated_responses": [],
        "text": ""
    }
}

print("Type A Text And Ainz Ooal Gown Will Respond.\nPress CTRL+C To Exit.\n")

while True:
	try:
		user_input = input("You : ")

		if user_input.lower() in ['quit', 'exit', 'bye']:
			print("Ainz: Goodbye!")
			break
		
		conversation["inputs"]["past_user_inputs"].append(user_input)
		conversation["inputs"]["text"] = user_input
		response = query(conversation)
		ai_response = response['generated_text']
		conversation["inputs"]["generated_responses"].append(ai_response)

		print("Ainz:", ai_response)
	except KeyboardInterrupt:
		print("\nExiting...")
		exit()
	except KeyError:
		print("Starting Model. Wait a Minute.")
		sleep(60)
		continue
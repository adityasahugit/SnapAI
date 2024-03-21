import json
import requests
import gradio


url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json',
}

data = {
        "model": "SnapAI",
        "stream": False,
        "prompt": "who are you",
    }
response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        # conversation_history.append(actual_response)
        print(actual_response)      
else:
        print(response.status_code, response)
        print("Error:", response.status_code, response.text)

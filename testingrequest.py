import requests

def send_post_request(url, data):
    try:
        response = requests.post(url, json=data)
        response_data = response.json()
        return response_data
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

if __name__ == "__main__":
    url = "https://chatbotmentalh-production.up.railway.app/api/chatbot/"
    data = {
        "email": "a.aussarbekov@gmail.com",
        "user_input": "here is text"
    }

    response_data = send_post_request(url, data)

    if "response" in response_data:
        print("Response:", response_data["response"])
    else:
        print("Error:", response_data["error"])

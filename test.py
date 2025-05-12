import google.generativeai as genai

genai.configure(api_key="AIzaSyCuTDEI_l6RHpIDS6Vk20Zv0N3wJxIroYo")

models = genai.list_models()
for model in models:
    print(model.name, model.supported_generation_methods)





# import requests

# API_KEY = "AIzaSyCuTDEI_l6RHpIDS6Vk20Zv0N3wJxIroYo"
# url = f"https://generativelanguage.googleapis.com/v1/models?key={API_KEY}"

# response = requests.get(url)

# if response.status_code == 200:
#     print("API key is valid!")
# else:
#     print("Invalid API key:", response.json())

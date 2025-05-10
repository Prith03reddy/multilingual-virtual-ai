import google.generativeai as genai

genai.configure(api_key="AIzaSyCuTDEI_l6RHpIDS6Vk20Zv0N3wJxIroYo")

models = genai.list_models()
for model in models:
    print(model.name, model.supported_generation_methods)

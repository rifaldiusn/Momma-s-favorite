import google.generativeai as genai

genai.configure(api_key="AIzaSyDYfBBHZJHW23obwa9quusj12fJA7-jzxI")

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("Help me find a key", stream=True)

for chunk in response:
  print(chunk.text)
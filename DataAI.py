import google.generativeai as genai

class ai_results:
  def __init__ (self,ai_text_result):
    self.ai_text_result = None

genai.configure(api_key="AIzaSyDYfBBHZJHW23obwa9quusj12fJA7-jzxI")

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("Give me solution for saving our money in 2024 and give me the cheapest thing to buy with the price in Rupiah", stream=True)

for chunk in response:
  ai_results.ai_text_result = chunk.text
  print(ai_results)
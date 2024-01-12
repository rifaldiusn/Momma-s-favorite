from DataAI import ai_results

data = open("Data.txt", "w")
data.write(ai_results.ai_text_result)
data.close()
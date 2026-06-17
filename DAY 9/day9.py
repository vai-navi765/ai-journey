ai_models = ["GPT-4", "Claude", "Gemini", "Mistral", "Llama"]
print(ai_models)

ai_model = {
    "model name": "Claude",
    "company": "Anthropic",
    "year": 2023, 
    "parameter": "1000 billion"
}
print(ai_model)
print(ai_model["model name"])
print(ai_model["company"])
print(ai_model["year"])
print(ai_model["parameter"])

with open("sample.txt", "r") as file:
    file_content = file.read()
print(file_content)

file_content = file_content.lower()
print(file_content)
words = file_content.split()
print(len(words))
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1
for word in word_count:
    print(word + " : " + str(word_count[word]))

import numpy as np
random_numbers = np.random.randint(1, 100, size=10)
print(random_numbers)
print("Mean:", np.mean(random_numbers))
print("Max:", np.max(random_numbers))
print("Min:", np.min(random_numbers))

import pandas as pd
data = {
    "model": ["GPT-4", "Claude", "Gemini", "Llama"],
    "company": ["OpenAI", "Anthropic", "Google", "Meta"],
    "parameters_billions": [1000, 500, 1000, 70],
    "open_source": [False, False, False, True]
}
df = pd.DataFrame(data)
print(df)

large_models = df[df["parameters_billions"] >= 500]
print(large_models)
df["is_large"] = df["parameters_billions"] >= 500
print(df)

import matplotlib.pyplot as plt
plt.bar(df["model"], df["parameters_billions"])
plt.title("AI Model Parameters Comparison")
plt.xlabel("Model")
plt.ylabel("Parameters (Billions)")
plt.show()



        






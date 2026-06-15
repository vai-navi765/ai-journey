import pandas as pd
data = {
    "name": ("GPT-4", "Claude", "Gemini", "LIama", "Mistral"),
    "company": ("openAI", "Anthropic", "Google", "Meta", "Mistral"),
    "year": ( 2023, 2023, 2023, 2023, 2023),
    "parameters_billion": (1000, 500, 1000, 70, 7),
    "open_source": (False, False, False, True, True)
}

df = pd.DataFrame(data)
print("Full DataFrame:")
print(df)

print("Open source models:")
open_source_models = df[df["open_source"] == True]
print(open_source_models)

print("Models above 100 billion parameters:")
large_models = df[df["parameters_billion"] >= 100]
print(large_models)

df["is_large"] = df["parameters_billion"] >= 100
print("With is_large column:")
print(df)
print("Mean parameters:", df['parameters_billion'].mean())



import ollama

def give_suggestion(prompt):
    response = ollama.generate(
        model="mistral",
        prompt=f"You are an expert software engineer and accordingly answer the prompt:{prompt}"
    )
    return response['response']

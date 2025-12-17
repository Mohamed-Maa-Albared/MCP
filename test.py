from langchain.llms import Ollama

# Specify the model you want to use.  Make sure it's pulled from Ollama.
ollama_model_name = "mistral"  # Or any other model you have in Ollama

# Initialize the Ollama LLM.
ollama_llm = Ollama(model=ollama_model_name)

# Get the prompt from the user.
prompt = input("Enter your prompt: ")

# Generate the response using the LLM.
response = ollama_llm.invoke(prompt)

# Print the response.
print(response)
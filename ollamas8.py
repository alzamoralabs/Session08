import ollama

model_name = 'llama3.2'
prompt_file = 'system_prompt.txt'

with open(prompt_file, 'r', encoding='utf-8') as f:
    system_prompt = f.read()
print("Bienvenido a 🐶 VeterinarIA 🤖\n ¿Cómo podemos ayudarle? (Presione X para Salir)")
while(1):
    user_input = input("👨 PetLover: ")
    if user_input.lower() == "x":
        break
    else:
        response = ollama.chat(
            model=model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ]
        )
        if response['message']['content'].contains("JSON_PAYLOAD"):
            with open('output.json', 'w', encoding='utf-8') as json_file:
                json_file.write(response['message']['content'])
        print("🐶🤖 VeterinarIA:", response['message']['content'])
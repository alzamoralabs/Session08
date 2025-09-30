import ollama

model_name = 'llama3.2'
prompt_file = 'system_prompt2.txt'
customer_data_file = 'Customer.json'

def update_customer_data(new_data):
    with open(customer_data_file, 'a', encoding='utf-8') as f:
        f.write(new_data)

with open(prompt_file, 'r', encoding='utf-8') as f:
    system_prompt = f.read()
with open(customer_data_file, 'r', encoding='utf-8') as f:
    customer_data = f.read()
# Reemplaza el marcador de posición [JSON_FILE] con el contenido del archivo JSON
system_prompt = system_prompt.replace("[JSON_FILE]", customer_data)
print(system_prompt)


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
        response_content = response['message']['content']
        if "UPDATE_RECORD" in response_content:
            # Extraer el JSON de la respuesta
            start_index = response_content.index("UPDATE_RECORD") + len("UPDATE_RECORD")
            json_data = response_content[start_index:].strip()
            update_customer_data(json_data)
            print("Registro de cliente actualizado.")
        print("🐶🤖 VeterinarIA:", response['message']['content'])
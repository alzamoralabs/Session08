import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Leer el system prompt desde el archivo
with open('system_prompt.txt', 'r', encoding='utf-8') as f:
    system_prompt = f.read()

# Configura tu clave de API de OpenAI
load_dotenv()
openaikey = os.getenv("OPENAIKEY")  # Reemplaza con tu clave real

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=openaikey
)

def chat_with_openai():
    print("Bienvenido a 🐶 VeterinarIA 🤖\n ¿Cómo podemos ayudarle? (Presione X para Salir)")
    messages = [{"role": "system", "content": system_prompt}]
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == 'X':
            break
        messages.append({"role": "user", "content": user_input})

        messages = [
            (
                "system",
                system_prompt,
            ),
            (   "human", user_input),
        ]
        llm.invoke(messages)

        response = llm.invoke(messages=messages)
        reply = response.choices[0].message.content.strip()
        print("Asistente:")
        for chunk in llm.stream(messages):
            print(chunk.text(), end="")
        print()  # Nueva línea después de la respuesta

if __name__ == "__main__":
    chat_with_openai()
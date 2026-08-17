import os
from pathlib import Path 
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Api key not found")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
prompt="Expain how internet works"
message={
    "role":"user",
    "content":prompt
}
messages=[message]
stream=client.chat.completions.create(model=model,messages=messages,stream=True)

for chunk in stream:
    content=chunk.choices[0].delta.content
    if content:
        print(content,end="",flush=True) #display data in smaller chunks one by one 





import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Api Error")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
role="user"

# structure it

from pydantic import BaseModel
class Ticket(BaseModel):
    name:str
    email:str
    issue:str

schema = Ticket.model_json_schema()

response_format={
    "type":"json_object"
}
system_prompt=f""" 
Extract the personal information from the ticket strictly based on this schema and give a json output.
{schema}"""

message_system={
    "role":"system",
    "content":system_prompt
}


text="hello my name is Ayushi Vispute i have an iphone which is not working at all my address is Maharastra my email is ayushi22@gmail.com my contact no is 84455"

prompt=f"""This is customer ticket please extract personal information from this {text}"""


message={
    "role":role,
    "content":prompt  
}

messages=[message_system,message]

response=client.chat.completions.create(model=model,messages=messages,response_format=response_format)


answer=response.choices[0].message.content
print(answer)

#structured json

#isko padhte kaise hai aage!
import json 
raw_json=answer
data_file=json.loads(raw_json)
ticket=Ticket(**data_file)

#inko pass kr sakte hai aage!
print(ticket.name)
print(ticket.email)
print(ticket.issue)







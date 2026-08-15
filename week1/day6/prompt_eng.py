import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
        raise ValueError("API key not found")

client=Groq(api_key=my_api_key)
model="llama-3.3-70b-versatile"

def llm_ans(prompt):
  message={
      "role":"user",
      "content":prompt
  } 
  messages=[message] 
  response=client.chat.completions.create(model=model,messages=messages)
  ans=response.choices[0].message.content
  return ans

prompts="""
#Role:
You are support assistant at a mobile/labtop company
#Task
you have to classify the issue in a category
#Constraints
You have to classify the issue in one of three categories namely billing,tecnical,return
#Output Format
your answer should be in one word only.the one word should be one of the categories given in constraints
#Example 
for instance if a user compalin says he wants a refund then the category is Return 
#FallBack
if the issue is unrelated to any of the categories mentioned in constraints, then the answer should be OTHER


This is a user complaint:
my laptop is not working"""

print(llm_ans(prompts))


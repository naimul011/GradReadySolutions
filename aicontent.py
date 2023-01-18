import os
import openai
import config
openai.api_key=config.OPENAI_API_KEY

def productDescription(query):
    response = openai.Completion.create(
    engine="davinci-instruct-beta-v3",
    prompt=query,
    temperature=.7,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0)
    
    print(response["choices"][0]["text"])
     

    
    

query = "Write an email to professor Hasan for a phd position at cse department"
productDescription(query)

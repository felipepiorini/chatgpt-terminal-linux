from openai import OpenAI
import os
import argparse

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

model_engine = "gpt-3.5-turbo"

def generate_response(prompt):
  response = client.chat.completions.create(model=model_engine,
  messages=[{"role": "user", "content": prompt}])
  return response.choices[0].message.content

parser = argparse.ArgumentParser(description='Gerar resposta do ChatGPT')
parser.add_argument('prompt', type=str, help='O prompt do usuario')

args = parser.parse_args()
prompt = args.prompt

response = generate_response(prompt)

print(response)
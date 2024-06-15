from django.conf import settings
import os
from openai import OpenAI
from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "health360/Healix-1.1B-V1-Chat-dDPO"


if settings.OPENAI_KEY != 'no_key' or settings.OPENAI_KEY != None:
    api = OpenAI(api_key=settings.OPENAI_KEY)

    def interpret_query(query):
        response = api.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI assistant specialized in health. Answer the query strictly as it is without providing spelling or grammar suggestions."
                },
                {
                    "role": "user",
                    "content": query
                }
            ]
        )
        answer = response.choices[0].message
        return answer.content


    def generate_health_plan(user_data):
        age = user_data['age']
        weight = user_data['weight']
        medical_history = user_data.get('medical_history', 'no')

        response = api.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": f"Suggest a personalized health plan for a {age} year old, weighing {weight} kg with {'no' if not medical_history else medical_history} medical history."
                }
            ]
        )
        answer = response.choices[0].message
        return answer.content
else:
    model = GPT2LMHeadModel.from_pretrained(model_name, force_download=True)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name, force_download=True)
    def interpret_query(query):
        prompt = (
            "You are an AI assistant specialized in health. "
            "Answer the query strictly as it is without providing spelling or grammar suggestions.\n\n"
            f"User: {query}\nAssistant:"
        )

        inputs = tokenizer(prompt, return_tensors='pt')
        outputs = model.generate(inputs['input_ids'], max_length=200, num_return_sequences=1)
        answer = tokenizer.decode(outputs[0], skip_special_tokens=True)


        answer = answer.split("Assistant:")[1].strip() if "Assistant:" in answer else answer
        return answer



    def generate_health_plan(user_data):
        age = user_data['age']
        weight = user_data['weight']
        medical_history = user_data.get('medical_history', 'no')

        prompt = (
            f"Suggest a personalized health plan for a {age} year old, "
            f"weighing {weight} kg with "
            f"{'no' if not medical_history else medical_history} medical history."
        )

        inputs = tokenizer.encode(prompt, return_tensors='pt')
        outputs = model.generate(inputs, max_length=200, num_return_sequences=1)
        answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return answer
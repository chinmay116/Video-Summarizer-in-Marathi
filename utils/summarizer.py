# from openai import OpenAI
# import os
#
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
#
#
# def generate_summary(text):
#     """Generate summary using GPT-3.5"""
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are a professional content summarizer. Create a concise summary of the following text, highlighting the key points and main ideas."
#             },
#             {
#                 "role": "user",
#                 "content": text
#             }
#         ],
#         max_tokens=500,
#         temperature=0.7
#     )
#
#     return response.choices[0].message.content

# class MockOpenAI:
#     @staticmethod
#     def Chatcompletion_create(model, messages):
#         return {
#             "choices": [{
#                 "messages": {
#                     "content": "This is a mocked response"
#                 }
#             }]
#         }
# openai = MockOpenAI
#
# def generate_summary(text):
#     """Generate summary using GPT-3.5"""
#     response = openai.Chatcompletion_create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are a professional content summarizer. Create a concise summary of the following text, highlighting the key points and main ideas."
#             },
#             {
#                 "role": "user",
#                 "content": text
#             }
#         ]
#         # max_tokens=500,
#         # temperature=0.7
#     )
#
#     return response.choices[0].message.content


import google.generativeai as genai
import os


def setup_gemini():
    """Initialize Gemini API"""
    genai.configure(api_key=("Your API Key"))
    return genai.GenerativeModel('gemini-pro')


def generate_summary(text):
    """Generate summary using Gemini"""
    model = setup_gemini()

    prompt = f"""Please create a concise summary of the following text, 
    highlighting the key points and main ideas:

    {text}
    """

    response = model.generate_content(prompt)
    return response.text
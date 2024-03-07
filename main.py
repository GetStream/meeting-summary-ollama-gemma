import json
import ollama
import requests

def load_conversation_data():
  with open("meeting_transcript.json") as f:
      json_file = json.load(f)
      extraction = lambda x: f"{x['speaker']}: {x['text']}"
      conversation = list(map(extraction, json_file))
      conversation_string = "\n".join(conversation)
      return conversation_string
  
def meeting_summary():
     conversation_string = load_conversation_data()
     response = ollama.chat(model='gemma:2b', messages=[
          {
          'role': 'system',
          'content': 'Your goal is to summarize the text that is given to you in roughly 300 words. It is from a meeting between one or more people. Only output the summary without any additional text. Focus on providing a summary in freeform text with a summary of what people said and the action items coming out of it.'
          },
     {
          'role': 'user',
          'content': conversation_string,
     },
     ])
     return response['message']['content']
  
def meeting_summary_rest():
     conversation_string = load_conversation_data()

     prompt = """Your goal is to summarize the text that is given to you 
     in roughly 300 words. It is from a meeting between one or more people. 
     Only output the summary without any additional text. 
     Focus on providing a summary in freeform text with a summary of what 
     people said and the action items coming out of it."""

     OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"

     OLLAMA_PROMPT = f"{prompt}: {conversation_string}"
     OLLAMA_DATA = {
          "model": "gemma:2b",
          "prompt": OLLAMA_PROMPT,
          "stream": False,
          "keep_alive": "1m",
     }

     response = requests.post(OLLAMA_ENDPOINT, json=OLLAMA_DATA)
     return response.json()["response"]

print("Summary using the library:")
print(meeting_summary())
print("---------------------------")
print("Summary using the REST API:")
print(meeting_summary_rest())
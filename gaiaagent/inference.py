# complete the inference from the env and return the key here 
import os 

from groq import Groq 
from config import MODEL_ID
from dotenv import load_dotenv


load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


# testing 
# chat_completion = client.chat.completions.create(
#     model=MODEL_ID,
#     messages=[
#         {
#             "role":"user",
#             "content":"Explain the importance of an agent"
#         }
#     ]
# )

# print(chat_completion.choices[0].message.content)
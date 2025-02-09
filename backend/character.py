from openai import OpenAI
from prompt import p

try:
    from mykey import OPENAI_KEY
    print("🔑 Using OPENAI_KEY from mykey.py")
except ImportError:
    from keys import OPENAI_KEY
    print("🔑 Using OPENAI_KEY from keys.py (fallback)")

chat_history = []

client = OpenAI(
  organization='org-8mp3GqL065se45HMQDqJwI5q',
  project='proj_1a4a7U3ioBOQSsmXTu7WWIIR',
  api_key=OPENAI_KEY
)

prompt = p

async def generate_chat(prompt: str):
  stream = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[{"role": "user", "content": prompt}],
      stream=True,
  )

  full_response = ""
  for chunk in stream:
      if chunk.choices[0].delta.content is not None:
        full_response += chunk.choices[0].delta.content
        # print(chunk.choices[0].delta.content, end="")
  chat_history.append(full_response)

  return full_response


rp = generate_chat(prompt)
print(rp)
print(chat_history)
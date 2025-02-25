from openai import OpenAI

def initialize_fastapi(proj, org, key):
    global client
    client = OpenAI(
        organization=org,
        project=proj,
        api_key=key
    )
  

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

  return full_response


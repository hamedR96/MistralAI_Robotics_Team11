from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_core.pydantic_v1 import BaseModel, Field
import os

key = "The OpenAI API Key"

class Notes(BaseModel):
    notes: str = Field(description="The notes from the melody of the requested music.")

model= "gpt-4o"

model = ChatOpenAI(model=model, openai_api_key=key, temperature=0)
structured_llm = model.with_structured_output(Notes)


def return_music_notes(name_of_music):

    prompt=f"Return the 10 second of piano notes for the melody of '{name_of_music}' covering 10 seconds, formatted for MIDI readability. Respond with notes only — no explanations or extra text."

    message = HumanMessage(content=[{"type": "text", "text": prompt},],)

    response=structured_llm.invoke([message])
    notes=response.notes.split()
    return notes
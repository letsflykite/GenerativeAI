import openai
import gradio as gr
import pandas as pd
import numpy as np
from openai.embeddings_utils import distances_from_embeddings
import pinecone


df = pd.read_csv('qa_demo.csv', usecols=['text','embedding'])
openai.api_key = "Your API key" 


pinecone.init(
    api_key='Your key', 
    environment='env'
)


index_name = 'chatgpt-demo-cpcs'
if not index_name in pinecone.list_indexes():
    raise KeyError(f"Index '{index_name}' does not exist.")

index = pinecone.Index(index_name)


def create_context(question, topk=3):
    """
    Create a context for a question by finding the most similar context from the dataframe
    """

    # Get the embeddings for the question
    q_embeddings = openai.Embedding.create(input=question, engine='text-embedding-ada-002')['data'][0]['embedding']
    res = index.query(q_embeddings, top_k = topk)
    contexts = []
    for row in res['matches']:
        contexts.append(df.iloc[int(row['id'])]['text'])
    return "\n\n###\n\n".join(contexts)


def respond(question):
    context = create_context(question)
    response = openai.ChatCompletion.create(
            messages=[{
                "role": "system",
                "content": f"Answer the question based on the context below, and if the question can't be answered based on the context, say \"I don't know\"\n\nContext: {context}\n\n---\n\nQuestion: {question}\nAnswer:",
            }],
            temperature=0,
            model = "gpt-3.5-turbo" 
        )
    reply = response.choices[0].message["content"].strip()
    return reply

inputs = gr.Textbox(label="QA System based on Pinecone Chat")
outputs = gr.TextArea(label="Reply")
gr.Interface(fn=respond, inputs=inputs, outputs=outputs, title="Ask me!",
             description="Ask about FIFA 2022 World Cup").launch()


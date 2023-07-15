import openai
import gradio as gr
import pandas as pd
import numpy as np
from openai.embeddings_utils import distances_from_embeddings

openai.api_key = "Your API key" 


# embedding df
df = pd.read_csv('qa_demo.csv', usecols=['text','embedding'])
df['embedding'] = df['embedding'].apply(eval).apply(np.array)
df.head()

def create_context(question, topk=3):
    """
    Create a context for a question by finding the most similar context from the dataframe
    """

    # Get the embeddings for the question
    q_embeddings = openai.Embedding.create(input=question, engine='text-embedding-ada-002')['data'][0]['embedding']

    # Get the distances from the embeddings
    df['distances'] = distances_from_embeddings(q_embeddings, df['embedding'].values, distance_metric='cosine')


    returns = []
    cur_len = 0

    # Sort by distance and add the text to the context until the context is too long
    for i, row in df.sort_values('distances', ascending=True).iterrows():
        if len(returns) >= topk:
            break
        
        # Else add it to the text that is being returned
        returns.append(row["text"])

    # Return the context
    return "\n\n###\n\n".join(returns)

def respond(question):
    context = create_context(question)
    response = openai.Completion.create(
            prompt=f"Answer the question based on the context below, and if the question can't be answered based on the context, say \"I don't know\"\n\nContext: {context}\n\n---\n\nQuestion: {question}\nAnswer:",
            temperature=0,
            model = "text-davinci-003"
        )
    reply = response.choices[0]["text"].strip()
    return reply

inputs = gr.Textbox(label="QA System")
outputs = gr.TextArea(label="Reply")
gr.Interface(fn=respond, inputs=inputs, outputs=outputs, title="Ask me!",
             description="Ask about FIFA 2022 World Cup").launch()


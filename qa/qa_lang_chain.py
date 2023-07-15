import gradio as gr
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
import pinecone


llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key="Your API Key")

embeddings = OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key="Your API Key")
pinecone.init(
    api_key="Your key",
    environment="env"
)

index = Pinecone.from_existing_index(index_name="lang-chain-cpcs", embedding=embeddings)

chain = load_qa_chain(llm, chain_type="stuff")

def respond(question):
  similar_docs = index.similarity_search(question, k=20)
  return chain.run(input_documents=similar_docs, question=question)

inputs = gr.Textbox(label="QA System based on lang chain")
outputs = gr.TextArea(label="Reply")
gr.Interface(fn=respond, inputs=inputs, outputs=outputs, title="Ask me!",
             description="Ask about FIFA 2022 World Cup").launch()

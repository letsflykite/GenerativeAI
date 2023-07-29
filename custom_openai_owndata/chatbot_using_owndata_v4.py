from llama_index import SimpleDirectoryReader, LLMPredictor, GPTVectorStoreIndex, PromptHelper, ServiceContext, load_index_from_storage, StorageContext
from langchain.chat_models import ChatOpenAI

#https://pypi.org/project/llama-index/

import gradio as gr
import sys
import os
import openai
import argparse


openai_api_key = os.environ['OPENAI_API_KEY']

model_name = "gpt-3.5-turbo"
# define prompt helper
max_input_size = 4096
num_output = 1000 # number of output tokens
max_chunk_overlap = 20
chunk_size_limit = 1024

prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap, chunk_size_limit=chunk_size_limit)
llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0.7, model_name=model_name, max_tokens=num_output))

service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)

parser = argparse.ArgumentParser(description="Launch chatbot")
parser.add_argument('-t', "-train", action="store_true", help="Train the model")
parser.add_argument('-i', "-input", default="output", help="Set input directory path")
parser.add_argument('-o', "-output", default="./gpt_store", help="Set output directory path")
args = parser.parse_args()

def construct_index():
    print("Constructing index…")
    # load in the documents
    print("*"*5, "Documents parsing initiated", "*"*5)
    file_metadata = lambda x : {"filename": x}
    reader = SimpleDirectoryReader(args.i, file_metadata=file_metadata)
    docs = reader.load_data()

    index = GPTVectorStoreIndex.from_documents(docs, service_context=service_context)

    # save index to disk
    index.set_index_id("vector_index")
    index.storage_context.persist(persist_dir=args.o)

    return index



def chatbot(input_text):
    # If not already done, initialize ‘index’ and ‘query_engine’
    if not hasattr(chatbot, "index"):
        # rebuild storage context and load index
        storage_context = StorageContext.from_defaults(persist_dir=args.o)
        chatbot.index = load_index_from_storage(service_context=service_context, storage_context=storage_context, index_id="vector_index")
                           
    # Initialize query engine
    chatbot.query_engine = chatbot.index.as_query_engine()
    print("Context initialized")

    # Submit query
    response = chatbot.query_engine.query(input_text)
    return response.response


inputs = gr.inputs.Textbox(lines=7, label="User input")
outputs = gr.outputs.Textbox(label="Response")


css = """
<style>
body {
    font-family: 'Arial', sans-serif;
    color: #f2f2f2; /* White-ish color for general text */
    background-color: #0d253f; /* Dark blue for the background */
}
h1 {
    color: #ff6347; /* Tomato color for the title */
    font-family: 'Courier New', Courier, monospace; /* Font family for the title */
    text-shadow: 2px 2px #000000; /* Shadow effect for the title */
}
.label, .output-text, input[type=text] {
    font-family: 'Courier New', Courier, monospace; /* Same font family for labels, output text and input text */
    font-size: 18px;
    color: #ffd700; /* Gold color for labels and output text */
}
input[type=text] {
    font-size: 16px;
    width: 300px;
    height: 50px;
    border: 2px solid #ffd700; /* Border color same as text */
    border-radius: 4px;
    background-color: #0d253f; /* Input box same color as body background */
    color: #f2f2f2; /* Input text color */
}
</style>
"""

iface = gr.Interface(
    fn=chatbot,
    inputs=inputs,
    outputs=outputs,
    title="Custom AI Chatbot",
    css=css,
)

if args.t:
    construct_index()

iface.launch(share=True)










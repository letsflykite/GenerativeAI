import os
import openai
import gradio as gr

openai_api_key = os.environ['OPENAI_API_KEY']
json_schema_version1 = {
  "$id": "https://example.com/person.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Person",
  "type": "object",
  "properties": {
    "firstName": {
      "type": "string",
      "description": "The person's first name."
    },
    "lastName": {
      "type": "string",
      "description": "The person's last name."
    },
    "age": {
      "description": "Age in years which must be equal to or greater than zero.",
      "type": "integer",
      "minimum": 0
    }
  }
}

print(json_schema_version1)

json_schema_version2 = {
  "$id": "https://example.com/person.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Person",
  "type": "object",
  "properties": {
    "firstName": {
      "type": "string",
      "description": "The person's first name."
    },
    "lastName": {
      "type": "string",
      "description": "The person's last name."
    },
    "data": {
      "description": "include age, ssn",
      "type": "object",
      "properties": {
        "ssn": {
          "type": "string",
          "description": "The social security number."
        },
       "age": {
       "description": "Age in years which must be equal to or greater than zero.",
        "type": "integer",
        "minimum": 0
       }
      }
    }
  }
}

json_1 = {
  "firstName": "John",
  "lastName": "Doe",
  "age": 21
}

json_2 = {
  "firstName": "Jason",
  "lastName": "Ha",
  "data": {
      "ssn": "873-91-8309",
      "age": 88
   }
}

system_message = f"You are a smart json generator. There are two versions of json schemas. Schema Version 1: {json_schema_version1} A json of schema version 1 for first name of John and last name of Doe and age as 21 is: {json_1} Schema version 2: {json_schema_version2} A json of schema version 2 for Jason Ha of 88 years old and social security number of 873-91-8309 is {json_2}"
print(system_message)

messages = [
            {'role':'system', 
            'content':system_message},
            ]

def chat(user_input):
    if user_input:
        messages.append({'role':'user','content':user_input})
    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=messages
    )
    reply = response.choices[0].message.content
    messages.append({'role':'assistant','content':reply})
    return reply


inputs = gr.inputs.Textbox(label="User input")
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

gr.Interface(
    fn=chat,
    inputs=inputs,
    outputs=outputs,
    title="a simple json generator",
    css=css,
).launch(share=True)
The following utilities rely on openai API
### Json Generaton Service

Service to generate json from text

### Environment

##### Venv + Pip

`conda deactivate`
`conda remove --name openaiutils_env_dev --all`
`conda update -n base -c defaults conda`
Create a virtual env with conda

`sudo conda env create -f openaiutils_env_dev.yml python=3.9`

`conda activate openaiutils_env_dev`

Make sure OPENAI_API_KEY is set in your environment variables
`source ~/.bashrc`
===========================




### Run standalone 
        `bash`
        `python simple_json_gen.py`

### Sample output

Demo: (demo link is good for 72 hours)
https://56deba46396c573069.gradio.live

Sample turn 1 input:
Can you generate a json of schema version 1 for Johnny Smith of age 2

Sample turn 1 output:
```
{
    "firstName": "Johnny",
    "lastName": "Smith",
    "age": 2
}
```


Sample turn 2 input:
Please generate a json of schema version 2 for Johnny Smith of age 2

Sample turn 2 output:

```
{
    "firstName": "Johnny",
    "lastName": "Smith",
    "data": {
        "ssn": "123-45-6789",
        "age": 2
    }
}
```

Sample turn 3 input:
Please generate a json of schema version 2 for Jane Smith of age 2 and her social security number is 987-65-4321

Sample turn 3 output:

```
{
    "firstName": "Jane",
    "lastName": "Smith",
    "data": {
        "ssn": "987-65-4321",
        "age": 2
    }
}
```

Sample turn 4 input:
Please generate a json of schema version 1 for Jane Smith of age 2 and her social security number is
987-65-4321

Sample turn 4 output:

```
{
    "firstName": "Jane",
    "lastName": "Smith",
    "age": 2
}
```


![ScreenShot](/screenshots/sample_turn4.png)

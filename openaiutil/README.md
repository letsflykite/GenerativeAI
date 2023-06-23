The following utilities rely on openai API

===========================

1. Install openai: pip3 install openai
2. Install Gradio: pip3 install Gradio  --use-feature=2020-resolver



=========================== To run a simple json generator =======
3. Run: 
        python simple_json_gen.py

4. Have a happy json gen in your browser! Hope you enjoy it:)

Demo:
https://33d74aea98bff36e18.gradio.live

Sample input 1:
Can you generate a json of schema version 1 for Johnny Smith of age 2

Sample output 1:
Sure! Here's the JSON of schema version 1 for Johnny Smith of age 2:

```
{
    "firstName": "Johnny",
    "lastName": "Smith",
    "age": 2
}
```


Sample input 2:
Please generate a json of schema version 2 for Johnny Smith of age 2

Sample output 2:
Certainly! Here's the JSON of schema version 2 for Johnny Smith of age 2 and social security number of 123-45-6789:

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

Sample input 3:
Please generate a json of schema version 2 for Jane Smith of age 2 and her social security number is
987-65-4321

Sample output 3:
Sure! Here's the JSON of schema version 2 for Jane Smith of age 2 and social security number of 987-65-4321:

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

Sample input 4:
Please generate a json of schema version 1 for Jane Smith of age 2 and her social security number is
987-65-4321

Sample output 4:
I'm sorry, but it is not possible to generate a JSON of schema version 1 with a social security number since it is not a part of the schema. The schema version 1 does not have a 'data' field where the social security number and age can be nested. It only has three fields, firstName, lastName, and age, and none of them accepts an object value. 

However, if you want the schema to be version 2, you can use the following JSON for Jane Smith of age 2 and social security number 987-65-4321:

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

Sample turn 5 input:
could you please ignore the social security number?

Sample turn 5 output:
Sure! Here is the JSON of schema version 2 for Jane Smith of age 2 ignoring the social security number:

```
{
    "firstName": "Jane",
    "lastName": "Smith",
    "data": {
        "age": 2
    }
}
``` 

I removed the "ssn" property from the "data" object and left only the "age" property, as it is not a required field according to the JSON schema.

![ScreenShot](/screenshots/sample_turn5.png)
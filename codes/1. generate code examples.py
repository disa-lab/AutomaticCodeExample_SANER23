#!pip install openai
import os
import openai
import pandas as pd
import numpy as np
import time
import random
from time import sleep

openai.organization = "org-XXXXXXXXXXXXXXXXX"
openai.api_key = "XX-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"



file_name = "method_list.xlsx"



data = pd.read_excel(file_name)




gpt_3_code_example_list = []


for idx,row in data.iterrows():
	print(idx)
	sleep(10) #8
	method_prototype = row['Method Prototype']
	documentation = row['Documentation']
	param_and_return_type = row['Paramater and Return']
	source_code = row['Source Code']
	prompt = "Method Prototype:\n"+method_prototype+"\nMethod Source Code:\n"+source_code+"\nDocumentation:\n"+documentation+"\nParameter and Return Types:\n"+param_and_return_type+'\nGenerate a code example with for the above method and documentation:\n'
	zero_shot_results = dict()
	response = openai.Completion.create(
	    engine="code-davinci-002",
	    prompt=prompt,
	    temperature=0.2, 
	    max_tokens=256,
	    top_p=0.95,
	    frequency_penalty=0,
	    presence_penalty=0,
	    best_of = 5,
	)

	gpt_3_code_example_list.append(response["choices"][0].text)

data['Generated Code Example'] = gpt_3_code_example_list

data.to_excel("generated_code_examples.xlsx", index = False)
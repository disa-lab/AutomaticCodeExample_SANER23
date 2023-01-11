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



file_name = "generated_code_examples.xlsx"



data = pd.read_excel(file_name)


gpt_3_code_example_list = []


for idx,row in data.iterrows():
	print(idx)
	passable = row['Passability']

	if passable==0:
	
		sleep(10)
		method_prototype = row['Method Prototype']
		documentation = row['Documentation']
		param_and_return_type = row['Paramater and Return']
		source_code = row['Source Code']
		generated_code_example = row['Generated Code Example']
		error_msg = row['Error Message']
		
		prompt = "Code with Error:\n"+generated_code_example+"\nError Message:\n"+error_msg+'\nCorrect the code based on the error message:'
		zero_shot_results = dict()
		response = openai.Completion.create(
		    engine="code-davinci-002", 
		    prompt=prompt,
		    temperature=0.2, #0
		    max_tokens=256,
		    top_p=0.95,
		    frequency_penalty=0,
		    presence_penalty=0,
		    best_of = 5,
		)
	
		gpt_3_code_example_list.append(response["choices"][0].text)
	else:
		gpt_3_code_example_list.append("N/A")

data['Corrected Code Example'] = gpt_3_code_example_list

data.to_excel("generated_and_corrected_code_examples.xlsx", index = False)
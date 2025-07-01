

import openai
import os
import json


with open("config.json") as f:
    config = json.load(f)


openai_api_key = config['OPENAI_API_KEY']


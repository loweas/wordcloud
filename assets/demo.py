import json 
import pandas as pd 
from pandas.io.json import json_normalize

with open('oregonstateuniversity.json', encoding='utf-8-sig') as f:
	data = json.load(f) 

df = json_normalize(data)

df.to_csv('oregonstateuniversity.csv', encoding='utf-8', index=False)





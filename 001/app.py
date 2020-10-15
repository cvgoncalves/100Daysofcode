# import pandas and json modules

import pandas as pd
import json

# read json url

url = "http://projects.bobbelderbos.com/pcc/cars.json"
df = pd.read_json(url)

print(df)

print(df.automaker.value_counts())

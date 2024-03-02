import json
import os

class InputAsJsonFile:

    # Parse the JSON file
    with open('news.json') as f:
        data = json.load(f)

    # Iterate over the items
    for key, value in data.items():
        print(value['publication_type'], '------------')
        print(value['news'])
        print(value['date'])
        print("\n")







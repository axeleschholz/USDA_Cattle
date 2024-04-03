import json

# read json fil encodings.json
with open('encodings.json', 'r') as f:
    encodings = json.load(f)
    encodings = dict(encodings)

for key in encodings.keys():
    print(f'CASE [{key}]')
    for i, value in enumerate(encodings[key]):
        print(f'when "{i}" THEN "{value}"')
    print('ELSE "Unknown"')
    print('END')

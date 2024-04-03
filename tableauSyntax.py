import json

# read json fil encodings.json
with open('encodings.json', 'r') as f:
    encodings = json.load(f)
    encodings = dict(encodings)

with open('tableauCode.txt', 'w') as f:
    for key in encodings.keys():
        f.write(f'CASE [{key}]\n')
        for i, value in enumerate(encodings[key]):
            f.write(f'when "{i}" THEN "{value}"\n')
        f.write('ELSE "Unknown"\n')
        f.write('END\n\n')

import json

# Load the JSON encodings
with open('encodings.json', 'r') as f:
    encodings = json.load(f)

# Initialize an empty string to store the Markdown content
md_content = ''

# Define the number of columns
num_columns = 3

# Iterate over the encodings
for key, values in encodings.items():
    # Add the key as a header
    md_content += f'## {key}\n'
    max_lengths = [max(len(f'[{i+j}] {value}') for i in range(0, len(values), num_columns)
                       for j, value in enumerate(values[i:i+num_columns])) for _ in range(num_columns)]

    md_content += '| ' + ' | '.join('---' for _ in range(num_columns)) + ' |\n'
    md_content += '| ' + ' | '.join('---' for _ in range(num_columns)) + ' |\n'
    for i in range(0, len(values), num_columns):
        row_values = values[i:i+num_columns]
        md_content += '| ' + ' | '.join(f'[{i+j}] {value}'.ljust(
            max_lengths[j]) for j, value in enumerate(row_values)) + ' |\n'
        md_content += '\n'

# Write the Markdown content to a file
with open('encodings.md', 'w') as f:
    f.write(md_content)

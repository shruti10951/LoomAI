import json

# Path to the input and output files
input_file = '1000_stories.jsonl'
output_file = 'formatted_1000_stories.txt'

# Define special tokens
start_token = "<s>"
end_token = "</s>"
inst_start_token = "[INST]"
inst_end_token = "[/INST]"

def format_data(story):
    prompt = story['prompt']
    target = story['story']
   
    # Combine the prompt and story with special tokens
    combined_text = f"{start_token} {inst_start_token} {prompt} {inst_end_token} {target} {end_token}"
   
    return combined_text

with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    for line in infile:
        entry = json.loads(line)
        formatted_entry = format_data(entry)
        outfile.write(formatted_entry + '\n')

print("Preprocessing complete.")


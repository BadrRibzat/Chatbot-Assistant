import os
import json

def convert_dailydialog_to_json(input_file, output_file):
    conversations = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            # Split the line into utterances
            utterances = line.strip().split('__eou__')
            # Remove empty utterances (e.g., trailing separator)
            utterances = [u.strip() for u in utterances if u.strip()]
            # Pair consecutive utterances as input-response
            for i in range(len(utterances) - 1):
                conversations.append({
                    "input": utterances[i],
                    "response": utterances[i + 1]
                })

    # Write to JSON file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(conversations, f, ensure_ascii=False, indent=2)
    print(f"Converted {len(conversations)} conversation pairs to {output_file}")

if __name__ == "__main__":
    input_file = "data/ijcnlp_dailydialog/dialogues_text.txt"  # Updated to match your file
    output_file = "data/conversations.json"
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found. Ensure the DailyDialog dataset is in the data/ directory.")
    else:
        convert_dailydialog_to_json(input_file, output_file)

import json

def extract_subset(input_file, output_file, num_entries):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    subset = data[:num_entries]
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(subset, f, ensure_ascii=False, indent=2)
    print(f"Extracted {num_entries} entries to {output_file}")

if __name__ == "__main__":
    extract_subset('data/conversations.json', 'data/small_conversations.json', 10)

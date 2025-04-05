import json
import os
import django
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments
from datasets import load_dataset

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()
from django.conf import settings

def train_model():
    dataset = load_dataset('json', data_files='data/small_conversations.json')
    train_data = dataset['train']

    tokenizer = GPT2Tokenizer.from_pretrained('distilgpt2')
    model = GPT2LMHeadModel.from_pretrained('distilgpt2')

    tokenizer.pad_token = tokenizer.eos_token

    def tokenize_function(examples):
        inputs = [f"{inp} [SEP] {resp}" for inp, resp in zip(examples['input'], examples['response'])]
        encodings = tokenizer(inputs, padding="max_length", truncation=True, max_length=16)
        encodings['labels'] = encodings['input_ids'].copy()
        return encodings

    tokenized_dataset = train_data.map(tokenize_function, batched=True, remove_columns=train_data.column_names)

    training_args = TrainingArguments(
        output_dir='./chatbot_model',
        num_train_epochs=3,
        per_device_train_batch_size=1,
        gradient_accumulation_steps=4,
        save_steps=50,
        save_total_limit=2,
        logging_dir='./logs',
        fp16=False,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
    )

    trainer.train()
    model.save_pretrained('chatbot/model')
    tokenizer.save_pretrained('chatbot/model')
    print("Model trained and saved to chatbot/model/")

if __name__ == "__main__":
    train_model()

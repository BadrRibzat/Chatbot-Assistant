import json
import os
import django
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments
from datasets import load_dataset

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()
from django.conf import settings

def train_model():
    # Load dataset
    dataset = load_dataset('json', data_files='data/conversations.json')
    train_data = dataset['train']

    # Initialize tokenizer and model
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    model = GPT2LMHeadModel.from_pretrained('gpt2')

    # Tokenize data
    def tokenize_function(examples):
        inputs = [f"{ex['input']} [SEP] {ex['response']}" for ex in examples]
        return tokenizer(inputs, padding="max_length", truncation=True, max_length=128)

    tokenized_dataset = train_data.map(tokenize_function, batched=True)

    # Training arguments
    training_args = TrainingArguments(
        output_dir='./chatbot_model',
        num_train_epochs=3,
        per_device_train_batch_size=4,
        save_steps=10_000,
        save_total_limit=2,
        logging_dir='./logs',
    )

    # Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
    )

    # Train the model
    trainer.train()
    model.save_pretrained('chatbot/model')
    tokenizer.save_pretrained('chatbot/model')
    print("Model trained and saved to chatbot/model/")

if __name__ == "__main__":
    train_model()

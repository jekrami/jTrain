from datasets import load_from_disk

tokenized_dataset = load_from_disk("tokenized_password_hash_dataset")
print("✅ Loaded tokenized dataset from disk")

from transformers import AutoTokenizer, EncoderDecoderModel

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

model = EncoderDecoderModel.from_encoder_decoder_pretrained("bert-base-uncased", "gpt2")

# Important config settings
model.config.decoder_start_token_id = tokenizer.cls_token_id
model.config.pad_token_id = tokenizer.pad_token_id
model.config.vocab_size = model.config.encoder.vocab_size

from transformers import TrainingArguments

training_args = TrainingArguments(
    output_dir="./password_guesser_model",
    evaluation_strategy="epoch",
    per_device_train_batch_size=16,
    num_train_epochs=3,
    logging_dir="./logs",
    logging_steps=50,
    save_total_limit=2,
    save_strategy="epoch",
    fp16=True  # Set to True only if using GPU
)

from transformers import Trainer

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    eval_dataset=tokenized_dataset.select(range(100)),  # quick eval
    tokenizer=tokenizer
)

trainer.train()

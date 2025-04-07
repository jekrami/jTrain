from transformers import AutoTokenizer
from datasets import Dataset
import pandas as pd

# Load CSV
df = pd.read_csv("password_hash_pairs.csv")

# Drop missing or empty values
df.dropna(subset=["password", "hash"], inplace=True)
df = df[(df["password"].str.strip() != "") & (df["hash"].str.strip() != "")]

# Enforce password length <= 16
df = df[df["password"].str.len() <= 16]

# Enforce hash length == 64 (for SHA256)
df = df[df["hash"].str.len() == 64]

# Optional: drop duplicates
df.drop_duplicates(inplace=True)

# Final count
print(f"✅ Cleaned dataset size: {len(df)} rows")

# Convert to HF dataset
dataset = Dataset.from_pandas(df)


# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Define tokenization function (batched)
def tokenize(examples):
    model_inputs = tokenizer(
        text=examples["hash"],
        padding="max_length",
        truncation=True,
        max_length=64
    )
    labels = tokenizer(
        text_target=examples["password"],
        padding="max_length",
        truncation=True,
        max_length=16
    )
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

  
# Windows multiprocessing fix
if __name__ == "__main__":
    tokenized_dataset = dataset.map(
        tokenize,
        batched=True,
        remove_columns=["password", "hash"],
        num_proc=4  # or lower depending on your CPU
    )

    tokenized_dataset.save_to_disk("tokenized_password_hash_dataset")
    print("✅ Tokenization complete and saved.")

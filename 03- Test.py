# Load trained model
model = EncoderDecoderModel.from_pretrained("./password_guesser_model")
tokenizer = AutoTokenizer.from_pretrained("./password_guesser_model")

def guess_password(hash_str):
    inputs = tokenizer(hash_str, return_tensors="pt", padding=True, truncation=True)
    output_ids = model.generate(**inputs, max_length=16)
    guess = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return guess

# Test with a known hash
sample_pwd = "password"
sample_hash = hashlib.sha256(sample_pwd.encode()).hexdigest()
predicted = guess_password(sample_hash)

print(f"Original: {sample_pwd}")
print(f"Predicted: {predicted}")

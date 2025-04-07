import hashlib
import pandas as pd

# Path to your rockyou.txt (change if needed)
rockyou_path = "rockyou.txt"

# Read rockyou.txt — it's usually one password per line
with open(rockyou_path, "r", encoding="latin-1") as f:  # latin-1 handles special characters
    passwords = [line.strip() for line in f if line.strip()]

# Optional: Limit to first N lines (e.g. 100k for now)
passwords = passwords[:10_000]

# Hash each password with SHA256
data = []
for pwd in passwords:
    hash_ = hashlib.sha256(pwd.encode()).hexdigest()
    data.append((pwd, hash_))

# Save to CSV
df = pd.DataFrame(data, columns=["password", "hash"])
df.to_csv("password_hash_pairs.csv", index=False)

print(f"✅ Created password_hash_pairs.csv with {len(df)} rows")
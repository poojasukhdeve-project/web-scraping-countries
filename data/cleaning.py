import pandas as pd
import re

# ✅ Load dataset (update path if needed)
df = pd.read_csv("data/raw_data.csv")

# ✅ Common word corrections (improves quality)
corrections = {
    "bihday": "birthday",
    "impoant": "important",
    "sho": "short",
    "hu": "hurt",
    "u": "you",
    "ur": "your",
    "dont": "do not",
    "cant": "cannot",
    "im": "i am",
    "ive": "i have"
}

# ✅ Function: clean raw text
def clean_text(text):
    text = str(text)

    # Remove @mentions
    text = re.sub(r'@\w+', '', text)

    # Remove hashtags
    text = re.sub(r'#\w+', '', text)

    # Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)

    # Remove HTML entities (e.g., &amp;)
    text = re.sub(r'&\w+;', '', text)

    # Remove emojis / non-ASCII
    text = re.sub(r'[^\x00-\x7F]+', '', text)

    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)

    # Convert to lowercase
    text = text.lower()

    # Remove numbers
    text = re.sub(r'\d+', '', text)

    # Fix common words
    words = text.split()
    words = [corrections.get(word, word) for word in words]
    text = " ".join(words)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text

# ✅ Apply cleaning
df['clean_tweet'] = df['tweet'].apply(clean_text)

# ✅ Filter bad sentences
def is_valid(text):
    words = text.split()
    return (
        len(words) >= 6 and       # at least 6 words
        len(text) > 30 and        # meaningful sentence length
        text != ''                # not empty
    )

df = df[df['clean_tweet'].apply(is_valid)]

# ✅ Remove duplicates
df = df.drop_duplicates(subset=['clean_tweet'])

# ✅ Reset index (clean structure)
df = df.reset_index(drop=True)

# ✅ Save full cleaned dataset
df.to_csv("data/cleaned_data.csv", index=False)

# ✅ Save ONLY clean text (best for ML / NanoGPT later)
df[['clean_tweet']].to_csv("data/clean_text_only.csv", index=False)

# ✅ Print summary
print("✅ Cleaning complete!")
print(f"Original size: {len(pd.read_csv('data/raw_data.csv'))}")
print(f"Final cleaned size: {len(df)}")
print("Files saved:")
print("→ data/cleaned_data.csv")
print("→ data/clean_text_only.csv")
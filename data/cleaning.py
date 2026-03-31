import pandas as pd
import re

# Load dataset
df = pd.read_csv("raw_data.csv")

# Function to clean text
def clean_text(text):
    text = str(text)
    
    # Remove @user
    text = re.sub(r'@\w+', '', text)
    
    # Remove hashtags
    text = re.sub(r'#\w+', '', text)
    
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    
    # Remove special characters & emojis
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

# Apply cleaning
df['clean_tweet'] = df['tweet'].apply(clean_text)

# Save cleaned file
df.to_csv("cleaned_data.csv", index=False)

print("Cleaning done! File saved as cleaned_data.csv")
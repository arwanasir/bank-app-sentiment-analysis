import pandas as pd
import numpy as np

def preprocess_reviews(df):
    """
    Clean and preprocess the scraped reviews
    """
    print("Starting data preprocessing...")
    print(f"Initial data shape: {df.shape}")
    
    # Remove duplicates
    initial_count = len(df)
    df = df.drop_duplicates(subset=['review_id'])
    print(f"Removed {initial_count - len(df)} duplicate reviews")
    
    # Handle missing data
    missing_before = df.isnull().sum()
    df = df.dropna(subset=['review_text'])
    df['date'] = df['date'].fillna(pd.Timestamp.now().strftime('%Y-%m-%d'))
    
    print(f"Missing data handled. Removed {missing_before['review_text']} rows with missing reviews")
    
    # Data validation
    print(f"Final data shape: {df.shape}")
    print(f"Reviews per bank:\n{df['bank'].value_counts()}")
    
    return df

if __name__ == "__main__":
    df = pd.read_csv('../data/raw/raw_reviews.csv')
    cleaned_df = preprocess_reviews(df)
    cleaned_df.to_csv('../data/processed/cleaned_reviews.csv', index=False)
    print("✅ Saved cleaned data")
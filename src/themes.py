import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import re

def extract_themes(df):
    """
    Extract themes from reviews using keyword-based approach
    """
    print("Extracting themes from reviews...")
    
    # Define theme categories and keywords
    theme_keywords = {
        'Transaction Issues': ['slow', 'transfer', 'transaction', 'loading', 'time', 'wait'],
        'Login Problems': ['login', 'password', 'fingerprint', 'face', 'authentication', 'access'],
        'App Performance': ['crash', 'bug', 'freeze', 'performance', 'error', 'not working'],
        'User Interface': ['interface', 'design', 'layout', 'navigation', 'button', 'screen'],
        'Customer Support': ['support', 'help', 'service', 'response', 'contact', 'complaint'],
        'Feature Requests': ['feature', 'should', 'could', 'please add', 'want', 'need']
    }
    
    def assign_theme(text):
        text_lower = str(text).lower()
        for theme, keywords in theme_keywords.items():
            if any(keyword in text_lower for keyword in keywords):
                return theme
        return 'Other'
    
    df['theme'] = df['review_text'].apply(assign_theme)
    
    print("Theme distribution:")
    print(df['theme'].value_counts())
    
    return df

if __name__ == "__main__":
    df = pd.read_csv('../data/processed/reviews_with_sentiment.csv')
    df = extract_themes(df)
    df.to_csv('../data/processed/final_analyzed_reviews.csv', index=False)
    print("✅ Saved reviews with theme analysis")
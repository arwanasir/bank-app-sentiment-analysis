import pandas as pd
from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyze sentiment using TextBlob
    """
    if pd.isna(text) or text == '':
        return 'neutral', 0.0
    
    analysis = TextBlob(str(text))
    polarity = analysis.sentiment.polarity
    
    if polarity > 0.1:
        return 'positive', polarity
    elif polarity < -0.1:
        return 'negative', polarity
    else:
        return 'neutral', polarity

def perform_sentiment_analysis(df):
    """
    Perform sentiment analysis on review text
    """
    print("Performing sentiment analysis...")
    
    sentiments = []
    scores = []
    
    for review in df['review_text']:
        sentiment, score = analyze_sentiment(review)
        sentiments.append(sentiment)
        scores.append(score)
    
    df['sentiment_label'] = sentiments
    df['sentiment_score'] = scores
    
    print("Sentiment distribution:")
    print(df['sentiment_label'].value_counts())
    
    return df

if __name__ == "__main__":
    df = pd.read_csv('../data/processed/cleaned_reviews.csv')
    df = perform_sentiment_analysis(df)
    df.to_csv('../data/processed/reviews_with_sentiment.csv', index=False)
    print("✅ Saved reviews with sentiment analysis")
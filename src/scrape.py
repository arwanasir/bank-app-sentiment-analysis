import pandas as pd
from google_play_scraper import reviews_all, Sort
import time

def scrape_bank_reviews():
    """
    Scrape reviews for three Ethiopian banks from Google Play Store
    """
    bank_apps = {
        'Commercial Bank of Ethiopia': 'com.combanketh.mobilebanking',
        'Bank of Abyssinia': 'com.boa.boaMobileBanking', 
        'Dashen Bank': 'com.dashen.dashensuperapp'
    }
    
    all_reviews = []
    
    for bank_name, app_id in bank_apps.items():
        print(f"Scraping reviews for {bank_name}...")
        
        try:
            bank_reviews = reviews_all(
                app_id,
                lang='en',
                country='et',
                sort=Sort.NEWEST,
            )
            
            for review in bank_reviews:
                all_reviews.append({
                    'review_id': review['reviewId'],
                    'review_text': review['content'],
                    'rating': review['score'],
                    'date': review['at'].strftime('%Y-%m-%d'),
                    'bank': bank_name,
                    'source': 'Google Play'
                })
            
            print(f"✅ Collected {len(bank_reviews)} reviews for {bank_name}")
            
        except Exception as e:
            print(f"❌ Error scraping {bank_name}: {e}")
        
        time.sleep(2)
    
    return pd.DataFrame(all_reviews)

if __name__ == "__main__":
    df = scrape_bank_reviews()
    df.to_csv('../data/raw/raw_reviews.csv', index=False)
    print(f"✅ Saved {len(df)} total reviews")
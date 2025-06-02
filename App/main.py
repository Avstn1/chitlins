# main.py

import yaml
import json
from scrapers.facebook_scraper import scrape_facebook_listings

def load_config(path="config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)
    
def save_listings_to_json(listings, filename="output/listings.json"):
    import os
    os.makedirs("output", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(listings, f, indent=2, ensure_ascii=False)
    print(f"\n✅ Listings saved to: {filename}")

def main():
    config = load_config()
    
    if config.get("facebook", {}).get("enabled", False):
        listings = scrape_facebook_listings(config["facebook"])
        
        print("\n📦 Scraped Listings:")
        for item in listings:
            print(f"- {item['price']} ({item['url']})")

        save_listings_to_json(listings)

if __name__ == "__main__":
    main()
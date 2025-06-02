# main.py

import yaml
from scrapers.facebook_scraper import scrape_facebook_listings

def load_config(path="config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def main():
    config = load_config()
    
    if config.get("facebook", {}).get("enabled", False):
        listings = scrape_facebook_listings(config["facebook"])
        
        print("\n📦 Scraped Listings:")
        for item in listings:
            print(f"- {item['title']} ({item['url']})")

if __name__ == "__main__":
    main()
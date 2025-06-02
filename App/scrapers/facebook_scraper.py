# scrapers/facebook_scraper.py

from playwright.sync_api import sync_playwright
from typing import List, Dict
import os

SESSION_FILE = "facebook_state.json"

def scrape_facebook_listings(config: Dict) -> List[Dict]:
    """Scrape Facebook Marketplace listings using Playwright with saved session."""
    listings = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=config.get("headless", True))

        # Use saved session if available
        if os.path.exists(SESSION_FILE):
            context = browser.new_context(storage_state=SESSION_FILE)
        else:
            # Manual login required for first-time setup
            context = browser.new_context()
            page = context.new_page()
            page.goto("https://www.facebook.com/")
            print("🔐 Please log into Facebook manually in the browser window.")
            input("✅ After logging in, press Enter here to continue...")
            context.storage_state(path=SESSION_FILE)
            print(f"💾 Session saved to {SESSION_FILE}")

        page = context.new_page()

        # Build the search URL
        location = config.get("location", "toronto-on")
        base_url = f"https://www.facebook.com/marketplace/{location}/search"

        for keyword in config.get("search_terms", []):
            print(f"[INFO] Searching for: {keyword}")
            search_url = f"{base_url}?query={keyword.replace(' ', '%20')}"
            page.goto(search_url, timeout=60000)
            page.wait_for_timeout(5000)  # Wait for listings to load

            # Save a screenshot
            page.screenshot(path=f"./debugs/debug_{keyword}.png", full_page=True)

            # Save page HTML
            with open(f"./debugs/debug_{keyword}.html", "w", encoding="utf-8") as f:
                f.write(page.content())

            items = page.locator('a[href*="/marketplace/item/"]').all()
            for item in items:
                try:
                    price = item.locator("span").first.inner_text()
                    link = item.get_attribute("href")

                    # Validate content
                    if not price or not link:
                        continue

                    listings.append({
                        "price": price,
                        "url": f"https://facebook.com{link}",
                        "search_term": keyword
                    })

                except Exception as e:
                    print(f"[ERROR] Could not parse item: {e}")

        browser.close()

    return listings
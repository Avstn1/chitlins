# 🛒 Marketplace Scraper & Automation Tool

A modular Python tool designed to monitor Facebook Marketplace (and other e-commerce platforms) for new listings and automate interactions (e.g. opening browser, sending alerts, pre-filling forms).

---

## ✨ Goals

- 🔍 Scrape listings based on filters (location, keyword, price)
- 🚨 Notify user when relevant items are found
- 🧠 Open browser to listing and optionally prepare messages or autofill
- 🔄 Expandable to Best Buy, Kijiji, Craigslist, etc.

---

## 🛠️ Technologies

| Area             | Tool           |
|------------------|----------------|
| Scraping         | Playwright / Requests / BeautifulSoup |
| Automation       | Playwright     |
| Notifications    | Plyer / Pushbullet / Webhook |
| Config Handling  | YAML           |
| Logging          | Custom / Built-in |
| Future Scaling   | Plugin-ready modules for other sites |

---

## ⚙️ Config (`config.yaml`)

```yaml
facebook:
  enabled: true
  location: "Toronto, ON"
  radius_km: 10
  search_terms:
    - "Nintendo Switch"
    - "LEGO"
  price_range:
    min: 50
    max: 300
  check_interval_seconds: 60
  headless: false

notifications:
  enabled: true
  methods: ["desktop"]
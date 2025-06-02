# 🧩 Component Overview — Marketplace Scraper & Alert System

This document outlines the modular components of your background scraper tool. It is designed for headless operation, meaning it silently checks listings, applies filters, and alerts you to matches — without launching a browser window.

---

## 🗂️ Project Structure

```
marketplace_automation/
├── main.py
├── config.yaml
├── scrapers/
│   └── facebook.py
├── filters/
│   └── keyword_filter.py
├── notifications/
│   └── notifier.py
├── utils/
│   └── logger.py
```

---

## 🧠 Core Components

### `main.py`
- **Purpose**: Main entrypoint and orchestrator.
- **Responsibilities**:
  - Load configuration from `config.yaml`
  - Initialize logging
  - Schedule periodic scraping
  - Pass listings through filters
  - Trigger alerts for matches

---

## 🕷 scrapers/facebook.py
- **Purpose**: Collect raw item listings from Facebook Marketplace.
- **Responsibilities**:
  - Log in via saved session or cookies
  - Navigate to location-specific search pages
  - Extract listings: title, price, location, time, URL
  - Return a list of structured dictionaries:
    ```python
    [
      {"title": "MacBook Pro", "price": 800, "location": "Toronto", "url": "..."},
      ...
    ]
    ```

---

## 🧹 filters/keyword_filter.py
- **Purpose**: Apply filters based on config.
- **Responsibilities**:
  - Match keywords from `config.yaml`
  - Enforce min/max price constraints
  - Deduplicate using a seen-items store or hash
  - Return only new, valid listings

---

## 🔔 notifications/notifier.py
- **Purpose**: Notify the user when a matching listing is found.
- **Responsibilities**:
  - Send a desktop notification (via `plyer`)
  - Display item title, price, and a clickable link
  - (Future: Telegram/Discord webhook options)

---

## ⚙️ config.yaml

Example:

```yaml
facebook:
  enabled: true
  location: "Toronto"
  radius_km: 30
  search_terms:
    - "macbook"
    - "gaming laptop"
    - "3070"
  price_range:
    min: 300
    max: 1500
  check_interval_seconds: 120
  headless: true
  deduplicate: true

notifications:
  enabled: true
  method: "desktop"
```

---

## 🔁 System Flow

```
[main.py]
   ├──> [scrapers/facebook.py] → Get new listings
   ├──> [filters/keyword_filter.py] → Apply filters
   └──> [notifications/notifier.py] → Send alerts
```

---

## 🧪 Future Add-ons

| Component               | Purpose                                  |
|------------------------|------------------------------------------|
| `data/store.py`         | Save seen items to avoid duplicates      |
| `scheduler.py`          | Custom polling logic & async timing      |
| `telegram_notifier.py`  | Telegram-based alert system              |
| `kijiji.py`             | Support for additional marketplaces      |
| `anti_bot.py`           | Add rate-limiting / bot avoidance logic |

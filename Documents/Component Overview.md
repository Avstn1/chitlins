# 🧩 Component Overview

This document outlines each module of the Marketplace Scraper & Automation Tool. The system is designed for modularity, so you can easily add platforms like Kijiji or Best Buy later.

---

## 🗂️ Project Structure Summary

```
marketplace_automation/
├── main.py
├── config.yaml
├── scrapers/
├── automation/
├── notifications/
├── utils/
```

---

## 🧠 Core Components

### `main.py`
- **Purpose**: Orchestrates the overall execution of the app.
- **Responsibilities**:
  - Load `config.yaml`
  - Initialize logging
  - Start scraper loop (e.g., Facebook first)
  - Send new listings to notifier and browser automation

---

## 🕷 scrapers/

### `scrapers/facebook.py`
- **Purpose**: Extract item listings from Facebook Marketplace.
- **Responsibilities**:
  - Login via Playwright and saved session (or manually)
  - Navigate to target search URL
  - Scrape listings: title, price, location, time, URL
  - Apply filters from `config.yaml`
  - Deduplicate results to avoid spam

### `scrapers/kijiji.py` _(stub)_
- Placeholder for Kijiji scraping logic using similar interface.

### `scrapers/bestbuy.py` _(stub)_
- Placeholder for Best Buy product and inventory scraping.

---

## 🤖 automation/

### `automation/browser_controller.py`
- **Purpose**: Handles browser interactions.
- **Responsibilities**:
  - Open marketplace listing in user’s browser
  - Optionally scroll, click, or prepare UI for manual input
  - Wait for human to handle CAPTCHA or send message

### `automation/autofill.py`
- **Purpose**: Autofill saved contact details.
- **Responsibilities**:
  - Inject basic form data (e.g., message to seller)
  - Uses Playwright or browser APIs
  - Only acts when site allows safe form manipulation

---

## 🔔 notifications/

### `notifications/notifier.py`
- **Purpose**: Alert user when a relevant item is detected.
- **Responsibilities**:
  - Send desktop alert (via `plyer`)
  - Include item name, price, location, and a clickable link
  - Optional webhook/Telegram/Slack extensions

---

## 🧰 utils/

### `utils/logger.py`
- **Purpose**: Consistent logging system.
- **Responsibilities**:
  - Log events to console and file
  - Include timestamps, levels, and optionally color

---

## ⚙️ config.yaml

- Central location for runtime settings:
```yaml
facebook:
  enabled: true
  location: "Toronto"
  radius_km: 25
  search_terms:
    - "gaming pc"
    - "macbook"
  price_range:
    min: 100
    max: 1200
  check_interval_seconds: 90
  headless: false

notifications:
  enabled: true
  method: "desktop"
```

---

## 🔄 Interactions Summary

```text
[main.py]
   ├──> [scrapers/facebook.py]
   ├──> [automation/browser_controller.py]
   ├──> [notifications/notifier.py]
   └──> [utils/logger.py]
```

---

## 🧪 Future Add-ons

| Component           | Purpose                                 |
|--------------------|------------------------------------------|
| `data/store.py`     | Save seen items to avoid duplicates      |
| `scheduler.py`      | Polling and retry logic                  |
| `anti_bot.py`       | Handle delays, captchas, retrying safely |
| `telegram_notifier.py` | Send alerts via Telegram bot        |

---

## 📦 Extending to More Marketplaces

To add a new source like Kijiji:
1. Create a module in `scrapers/`
2. Implement standard interface:
   - `load_page()`
   - `extract_listings()`
3. Update `main.py` to include the new platform
4. Add configuration block in `config.yaml`

---

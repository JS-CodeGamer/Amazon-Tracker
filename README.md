# Amazon-Tracker

- Get Link to Website with Items
- Get Items Links
- Extract Info about Items
- Generate Report Based on Info

## Initial Setup Instructions

- Specify the correct config.
- Create folder reports.
- Change base url to match one for your country.
- Make sure to [download](https://chromedriver.chromium.org/downloads) correct chromedriver matching to the current version of your google chrome and operating system.

### Setup Python Virtual Environment

```buildoutcfg
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

## Running Script

```buildoutcfg
python simple_tracker.py
```

#### Note: This script works at the time of creation (proof below) but needs to be changed in acordance with amazon.com source code (by inspecting it).
```json
{
  "title": "PS4",
  "date": "08-07-2022 05:06:35",
  "best_item": null,
  "currency": "\u20b9",
  "filters": {
    "min": "0",
    "max": "200000"
  },
  "base_link": "http://www.amazon.in/",
  "products": [
    null,
    {
      "asin": "B073HJQ49W",
      "url": "http://www.amazon.in/dp/B073HJQ49W",
      "title": "Sony PS4 Dualshock Magma - V2 (Red)",
      "seller": "Visit the Sony Store",
      "price": 5050.0
    },
    null,
    null,
    null,
    {
      "asin": "B085LZSG6F",
      "url": "http://www.amazon.in/dp/B085LZSG6F",
      "title": "Ghost of Tsushima | PS4 Game (PlayStation 4)",
      "seller": "Visit the Sony Store",
      "price": 1992.0
    },
    null,
    null,
    {
      "asin": "B09MDJD84W",
      "url": "http://www.amazon.in/dp/B09MDJD84W",
      "title": "Grand Theft Auto: The Trilogy - The Definitive Edition (PS4)",
      "seller": "Brand: ROCKSTAR GAMES",
      "price": 2725.0
    },
    null,
    null,
    {
      "asin": "B08NF3HJRH",
      "url": "http://www.amazon.in/dp/B08NF3HJRH",
      "title": "WWE 2K20 - PS4",
      "seller": "Brand: 2K GAMES.",
      "price": 1577.0
    },
    null,
    {
      "asin": "B08NYC5KL4",
      "url": "http://www.amazon.in/dp/B08NYC5KL4",
      "title": "Sony Playstation 4 Dualshock Midnight Blue V2",
      "seller": "Visit the Sony Store",
      "price": 5050.0
    },
    {
      "asin": "B0842LZBN5",
      "url": "http://www.amazon.in/dp/B0842LZBN5",
      "title": "Batman Arkham Collection (PS4)",
      "seller": "Brand: WB Games",
      "price": 1799.0
    },
    {
      "asin": "B07X23YRCS",
      "url": "http://www.amazon.in/dp/B07X23YRCS",
      "title": "Marvel's Spider-Man G.O.T.Y (PS4)",
      "seller": "Visit the Sony Store",
      "price": 1680.0
    }
  ]
}
```

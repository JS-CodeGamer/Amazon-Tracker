# Amazon-Tracker

- Get Link to Website with Items
- Get Items Links
- Extract Info about Items
- Generate Report Based on Info

## Initial Setup Instructions

- Specify the correct config.
- Change base url to match one for your country.
- Change the currency to match one showed in your Base URL.
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
  "title": "IPhone",
  "date": "10-07-2022 12:14:06",
  "best_item": {
    "asin": "B09G99YPQM",
    "url": "http://www.amazon.in/dp/B09G99YPQM",
    "title": "Apple iPhone 13 Pro (128GB) - Sierra Blue",
    "seller": "Visit the Apple Store",
    "price": 116.0
  },
  "currency": "\u20b9",
  "filters": {
    "min": "50000",
    "max": "150000"
  },
  "base_link": "http://www.amazon.in/",
  "products": [
    {
      "asin": "B09G99YPQM",
      "url": "http://www.amazon.in/dp/B09G99YPQM",
      "title": "Apple iPhone 13 Pro (128GB) - Sierra Blue",
      "seller": "Visit the Apple Store",
      "price": 116.0
    },
    {
      "asin": "B09G99YPQM",
      "url": "http://www.amazon.in/dp/B09G99YPQM",
      "title": "Apple iPhone 13 Pro (128GB) - Sierra Blue",
      "seller": "Visit the Apple Store",
      "price": 116.0
    },
    {
      "asin": "B09V48BYGP",
      "url": "http://www.amazon.in/dp/B09V48BYGP",
      "title": "Apple iPhone 13 Pro (128 GB) - Alpine Green",
      "seller": "Visit the Apple Store",
      "price": 116.0
    },
    {
      "asin": "B09G9H3RZH",
      "url": "http://www.amazon.in/dp/B09G9H3RZH",
      "title": "Apple iPhone 13 Pro Max (128GB) - Sierra Blue",
      "seller": "Visit the Apple Store",
      "price": 126.0
    },
    {
      "asin": "B09G91FCBT",
      "url": "http://www.amazon.in/dp/B09G91FCBT",
      "title": "Apple iPhone 13 Pro Max (256GB) - Sierra Blue",
      "seller": "Visit the Apple Store",
      "price": 136.0
    },
    {
      "asin": "B09G91FCBT",
      "url": "http://www.amazon.in/dp/B09G91FCBT",
      "title": "Apple iPhone 13 Pro Max (256GB) - Sierra Blue",
      "seller": "Visit the Apple Store",
      "price": 136.0
    },
    {
      "asin": "B09G94T2NY",
      "url": "http://www.amazon.in/dp/B09G94T2NY",
      "title": "Apple iPhone 13 Pro Max (256GB) - Graphite",
      "seller": "Visit the Apple Store",
      "price": 136.0
    },
    {
      "asin": "B09G93NZVW",
      "url": "http://www.amazon.in/dp/B09G93NZVW",
      "title": "Apple iPhone 13 Pro Max (256GB) - Gold",
      "seller": "Visit the Apple Store",
      "price": 136.0
    },
    {
      "asin": "B09V4KVP3K",
      "url": "http://www.amazon.in/dp/B09V4KVP3K",
      "title": "Apple iPhone 13 Pro Max (256 GB) - Alpine Green",
      "seller": "Visit the Apple Store",
      "price": 137.0
    },
    {
      "asin": "B08L5TQT4X",
      "url": "http://www.amazon.in/dp/B08L5TQT4X",
      "title": "Apple iPhone 12 Mini (64GB) - (Product) RED",
      "seller": "Visit the Apple Store",
      "price": 54990.0
    },
    {
      "asin": "B08L5TQT4X",
      "url": "http://www.amazon.in/dp/B08L5TQT4X",
      "title": "Apple iPhone 12 Mini (64GB) - (Product) RED",
      "seller": "Visit the Apple Store",
      "price": 54990.0
    },
    {
      "asin": "B08L5TDRQC",
      "url": "http://www.amazon.in/dp/B08L5TDRQC",
      "title": "Apple iPhone 12 Mini (64GB) - Green",
      "seller": "Visit the Apple Store",
      "price": 54990.0
    },
    {
      "asin": "B08L5W16HX",
      "url": "http://www.amazon.in/dp/B08L5W16HX",
      "title": "Apple iPhone 12 (64GB) - Green",
      "seller": "Visit the Apple Store",
      "price": 54999.0
    },
    {
      "asin": "B08L5TGWD1",
      "url": "http://www.amazon.in/dp/B08L5TGWD1",
      "title": "Apple iPhone 12 (64GB) - (Product) RED",
      "seller": "Visit the Apple Store",
      "price": 54999.0
    },
    {
      "asin": "B08L5W16HX",
      "url": "http://www.amazon.in/dp/B08L5W16HX",
      "title": "Apple iPhone 12 (64GB) - Green",
      "seller": "Visit the Apple Store",
      "price": 54999.0
    },
    {
      "asin": "B08L5TGWD1",
      "url": "http://www.amazon.in/dp/B08L5TGWD1",
      "title": "Apple iPhone 12 (64GB) - (Product) RED",
      "seller": "Visit the Apple Store",
      "price": 54999.0
    },
    {
      "asin": "B08L5VJYV7",
      "url": "http://www.amazon.in/dp/B08L5VJYV7",
      "title": "Apple iPhone 12 (64GB) - White",
      "seller": "Visit the Apple Store",
      "price": 54999.0
    },
    {
      "asin": "B08L5WHFT9",
      "url": "http://www.amazon.in/dp/B08L5WHFT9",
      "title": "Apple iPhone 12 (64GB) - Blue",
      "seller": "Visit the Apple Store",
      "price": 54999.0
    },
    {
      "asin": "B0932MWFJB",
      "url": "http://www.amazon.in/dp/B0932MWFJB",
      "title": "Apple iPhone 12 Mini (128GB) - Purple",
      "seller": "Visit the Apple Store",
      "price": 59490.0
    },
    {
      "asin": "B08L5VN68Y",
      "url": "http://www.amazon.in/dp/B08L5VN68Y",
      "title": "Apple iPhone 12 Mini (128GB) - Blue",
      "seller": "Visit the Apple Store",
      "price": 59490.0
    },
    {
      "asin": "B0932MWFJB",
      "url": "http://www.amazon.in/dp/B0932MWFJB",
      "title": "Apple iPhone 12 Mini (128GB) - Purple",
      "seller": "Visit the Apple Store",
      "price": 59490.0
    },
    {
      "asin": "B08L5VN68Y",
      "url": "http://www.amazon.in/dp/B08L5VN68Y",
      "title": "Apple iPhone 12 Mini (128GB) - Blue",
      "seller": "Visit the Apple Store",
      "price": 59490.0
    },
    {
      "asin": "B08L5TNJHG",
      "url": "http://www.amazon.in/dp/B08L5TNJHG",
      "title": "Apple iPhone 12 (128GB) - Blue",
      "seller": "Visit the Apple Store",
      "price": 59999.0
    },
    {
      "asin": "B08L5TNJHG",
      "url": "http://www.amazon.in/dp/B08L5TNJHG",
      "title": "Apple iPhone 12 (128GB) - Blue",
      "seller": "Visit the Apple Store",
      "price": 59999.0
    },
    {
      "asin": "B08L5WD9D6",
      "url": "http://www.amazon.in/dp/B08L5WD9D6",
      "title": "Apple iPhone 12 (128GB) - Black",
      "seller": "Visit the Apple Store",
      "price": 59999.0
    },
    {
      "asin": "B08L5VG843",
      "url": "http://www.amazon.in/dp/B08L5VG843",
      "title": "Apple iPhone 12 Mini (128GB) - Black",
      "seller": "Visit the Apple Store",
      "price": 59999.0
    },
    {
      "asin": "B09G9L2B3L",
      "url": "http://www.amazon.in/dp/B09G9L2B3L",
      "title": "Apple iPhone 13 Mini (128GB) - Pink",
      "seller": "Visit the Apple Store",
      "price": 64999.0
    },
    {
      "asin": "B09G9L2B3L",
      "url": "http://www.amazon.in/dp/B09G9L2B3L",
      "title": "Apple iPhone 13 Mini (128GB) - Pink",
      "seller": "Visit the Apple Store",
      "price": 64999.0
    },
    {
      "asin": "B09G9FNN4X",
      "url": "http://www.amazon.in/dp/B09G9FNN4X",
      "title": "Apple iPhone 13 Mini (128GB) - Midnight",
      "seller": "Visit the Apple Store",
      "price": 64999.0
    },
    {
      "asin": "B08ZWRG1X2",
      "url": "http://www.amazon.in/dp/B08ZWRG1X2",
      "title": "New Apple iPhone 12 Mini (128GB) - Blue with AirPods with Charging Case",
      "seller": "Visit the Apple Store",
      "price": 70489.0
    },
    {
      "asin": "B09G9FPGTN",
      "url": "http://www.amazon.in/dp/B09G9FPGTN",
      "title": "Apple iPhone 13 (128GB) - Pink",
      "seller": "Visit the Apple Store",
      "price": 71990.0
    },
    {
      "asin": "B09G9D8KRQ",
      "url": "http://www.amazon.in/dp/B09G9D8KRQ",
      "title": "Apple iPhone 13 (128GB) - Starlight",
      "seller": "Visit the Apple Store",
      "price": 71990.0
    },
    {
      "asin": "B09G9HD6PD",
      "url": "http://www.amazon.in/dp/B09G9HD6PD",
      "title": "Apple iPhone 13 (128GB) - Midnight",
      "seller": "Visit the Apple Store",
      "price": 71990.0
    },
    {
      "asin": "B09G9FPGTN",
      "url": "http://www.amazon.in/dp/B09G9FPGTN",
      "title": "Apple iPhone 13 (128GB) - Pink",
      "seller": "Visit the Apple Store",
      "price": 71990.0
    },
    {
      "asin": "B09G9D8KRQ",
      "url": "http://www.amazon.in/dp/B09G9D8KRQ",
      "title": "Apple iPhone 13 (128GB) - Starlight",
      "seller": "Visit the Apple Store",
      "price": 71990.0
    },
    {
      "asin": "B09G9HD6PD",
      "url": "http://www.amazon.in/dp/B09G9HD6PD",
      "title": "Apple iPhone 13 (128GB) - Midnight",
      "seller": "Visit the Apple Store",
      "price": 71990.0
    },
    {
      "asin": "B09G9BL5CP",
      "url": "http://www.amazon.in/dp/B09G9BL5CP",
      "title": "Apple iPhone 13 (128GB) - Blue",
      "seller": "Visit the Apple Store",
      "price": 71990.0
    },
    {
      "asin": "B09G99CW2N",
      "url": "http://www.amazon.in/dp/B09G99CW2N",
      "title": "Apple iPhone 13 (128GB) - (Product) RED",
      "seller": "Visit the Apple Store",
      "price": 71990.0
    },
    {
      "asin": "B09V4B6K53",
      "url": "http://www.amazon.in/dp/B09V4B6K53",
      "title": "Apple iPhone 13 (128GB) - Green",
      "seller": "Visit the Apple Store",
      "price": 72990.0
    },
    {
      "asin": "B09V4MXBSN",
      "url": "http://www.amazon.in/dp/B09V4MXBSN",
      "title": "Apple iPhone 13 (256 GB) - Green",
      "seller": "Visit the Apple Store",
      "price": 80990.0
    },
    {
      "asin": "B09G93H3BR",
      "url": "http://www.amazon.in/dp/B09G93H3BR",
      "title": "Apple iPhone 13 (256GB) - Blue",
      "seller": "Visit the Apple Store",
      "price": 80990.0
    },
    {
      "asin": "B09G9HRYFZ",
      "url": "http://www.amazon.in/dp/B09G9HRYFZ",
      "title": "Apple iPhone 13 (256GB) - Pink",
      "seller": "Visit the Apple Store",
      "price": 80990.0
    },
    {
      "asin": "B09G9BQS98",
      "url": "http://www.amazon.in/dp/B09G9BQS98",
      "title": "Apple iPhone 13 (256GB) - Midnight",
      "seller": "Visit the Apple Store",
      "price": 80990.0
    },
    {
      "asin": "B09V4MXBSN",
      "url": "http://www.amazon.in/dp/B09V4MXBSN",
      "title": "Apple iPhone 13 (256 GB) - Green",
      "seller": "Visit the Apple Store",
      "price": 80990.0
    },
    {
      "asin": "B09G93H3BR",
      "url": "http://www.amazon.in/dp/B09G93H3BR",
      "title": "Apple iPhone 13 (256GB) - Blue",
      "seller": "Visit the Apple Store",
      "price": 80990.0
    },
    {
      "asin": "B09G9HRYFZ",
      "url": "http://www.amazon.in/dp/B09G9HRYFZ",
      "title": "Apple iPhone 13 (256GB) - Pink",
      "seller": "Visit the Apple Store",
      "price": 80990.0
    },
    {
      "asin": "B09G9BQS98",
      "url": "http://www.amazon.in/dp/B09G9BQS98",
      "title": "Apple iPhone 13 (256GB) - Midnight",
      "seller": "Visit the Apple Store",
      "price": 80990.0
    },
    {
      "asin": "B09G9BFKZN",
      "url": "http://www.amazon.in/dp/B09G9BFKZN",
      "title": "Apple iPhone 13 (256GB) - Starlight",
      "seller": "Visit the Apple Store",
      "price": 80990.0
    }
  ]
}
```


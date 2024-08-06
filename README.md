# Ekantipur News Scraper

This Python script scrapes the latest news headlines from the Ekantipur website. It uses the [`requests`](command:_github.copilot.openSymbolFromReferences?%5B%22requests%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fmnt%2FDATA%2FBibek%2FExtras%2Fgit-repo-test%2Fekantipur-scrape%2Fnews_scraper.py%22%2C%22external%22%3A%22file%3A%2F%2F%2Fmnt%2FDATA%2FBibek%2FExtras%2Fgit-repo-test%2Fekantipur-scrape%2Fnews_scraper.py%22%2C%22path%22%3A%22%2Fmnt%2FDATA%2FBibek%2FExtras%2Fgit-repo-test%2Fekantipur-scrape%2Fnews_scraper.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A7%7D%7D%5D%5D "Go to definition") library to fetch the webpage content and [`BeautifulSoup`](command:_github.copilot.openSymbolFromReferences?%5B%22BeautifulSoup%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fmnt%2FDATA%2FBibek%2FExtras%2Fgit-repo-test%2Fekantipur-scrape%2Fnews_scraper.py%22%2C%22external%22%3A%22file%3A%2F%2F%2Fmnt%2FDATA%2FBibek%2FExtras%2Fgit-repo-test%2Fekantipur-scrape%2Fnews_scraper.py%22%2C%22path%22%3A%22%2Fmnt%2FDATA%2FBibek%2FExtras%2Fgit-repo-test%2Fekantipur-scrape%2Fnews_scraper.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A16%7D%7D%5D%5D "Go to definition") from the [`bs4`](command:_github.copilot.openSymbolFromReferences?%5B%22bs4%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fmnt%2FDATA%2FBibek%2FExtras%2Fgit-repo-test%2Fekantipur-scrape%2Fnews_scraper.py%22%2C%22external%22%3A%22file%3A%2F%2F%2Fmnt%2FDATA%2FBibek%2FExtras%2Fgit-repo-test%2Fekantipur-scrape%2Fnews_scraper.py%22%2C%22path%22%3A%22%2Fmnt%2FDATA%2FBibek%2FExtras%2Fgit-repo-test%2Fekantipur-scrape%2Fnews_scraper.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A5%7D%7D%5D%5D "Go to definition") library to parse the HTML.

## Features

- **Major Headlines**: Extracts and prints the major headlines from the homepage.
- **Banner Section**: Extracts and prints articles from the banner section.
- **Samachar Section**: Extracts and prints articles from the Samachar section.

## Requirements

- Python 3.x
- [`requests`](command:_github.copilot.openSymbolFromReferences?%5B%22requests%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fmnt%2FDATA%2FBibek%2FExtras%2Fgit-repo-test%2Fekantipur-scrape%2Fnews_scraper.py%22%2C%22external%22%3A%22file%3A%2F%2F%2Fmnt%2FDATA%2FBibek%2FExtras%2Fgit-repo-test%2Fekantipur-scrape%2Fnews_scraper.py%22%2C%22path%22%3A%22%2Fmnt%2FDATA%2FBibek%2FExtras%2Fgit-repo-test%2Fekantipur-scrape%2Fnews_scraper.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A7%7D%7D%5D%5D "Go to definition") library
- `beautifulsoup4` library

## Installation

Install the required libraries using pip:

```bash
pip install requests beautifulsoup4
```

## Usage

Run the script to print the latest news headlines:

```bash
python news_scraper.py
```

## Example Output

```

Major Headlines:
गुल्मीमा पहिरोले घर बगाउँदा ४ जनाको मृत्यु
More: https://ekantipur.com/pradesh-5/2024/08/06/4-members-of-the-same-family-died-when-the-house-was-swept-away-by-a-landslide-in-gulmi-01-24.html

--------------------------------------------------------------

सरकारले श्वास फेर्ने हावामा कर लगाउने कानुन ल्याउन मात्रै बाँकी छ : सांसद शर्मा:
कांग्रेस सांसद डा. सुनिल शर्माले सरकारले जनताले सास फेर्ने हावामा कर लगाउने कानुन ल्याउन मात्रै बाँकी रहेको बताएका छन् ।
More: https://ekantipur.com/news/2024/08/06/all-that-is-left-for-the-government-is-to-bring-a-law-to-tax-breathing-air-mp-sharma-23-56.html
...
```

## License

This project is licensed under the MIT License.
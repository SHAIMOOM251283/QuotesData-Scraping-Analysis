# QuotesData - Scraping & Analysis

## Overview

QuotesData is a Python project that scrapes quotes from the website [Quotes to Scrape](https://quotes.toscrape.com), analyzes the sentiment of the quotes, and visualizes the results using bar and pie charts. This project consists of four main scripts that handle the scraping, data processing, and visualization of quotes.

## Scripts

### 1. `scrape_link_tags.py`

This script extracts all unique tags from the quotes website. It navigates through multiple pages, collects the tags, and provides options to construct URLs for either the homepage or specific tags.

### 2. `scrape_data.py`

This script utilizes the tag extraction from `scrape_link_tags.py` to scrape quotes based on the selected tag or homepage. It detects whether the selected URL has multiple pages and processes the data accordingly. Finally, it saves the scraped quotes to a CSV file.

### 3. `sentiment_analysis_bar_chart.py`

This script reads the scraped quotes from the CSV file and classifies each quote's sentiment using the NLTK Sentiment Intensity Analyzer. It visualizes the sentiment distribution of quotes by author in a stacked bar chart.

### 4. `sentiment_analysis_pie_chart.py`

Similar to `sentiment_analysis_bar_chart.py`, this script also classifies the sentiment of quotes but focuses on visualizing the sentiment distribution for a specific author in a pie chart format. It allows users to input the author’s name and generates a sentiment pie chart for that author.

## Visual Outputs

### Bar Chart
Below is the bar chart visualizing the sentiment distribution of quotes by author.

![Bar Chart](https://github.com/SHAIMOOM251283/QuotesData-Scraping-Analysis/blob/main/bar_chart.png)

### Pie Chart
Below is the pie chart representing the sentiment distribution for a selected author.

![Pie Chart](https://github.com/SHAIMOOM251283/QuotesData-Scraping-Analysis/blob/main/pie_chart.png)

## Installation

### Clone the repository using the terminal:

```bash
git clone https://github.com/SHAIMOOM251283/QuotesData.git
cd QuotesData
```

### Clone the repository using VS Code's Git integration:

1. Open VS Code.
2. Press `Ctrl + Shift + P` (or `Cmd + Shift + P` on macOS) to open the Command Palette.
3. Type `Git: Clone` and select the option.
4. Enter the repository URL: `https://github.com/SHAIMOOM251283/QuotesData.git`.
5. Choose a local folder to clone the repository into, and select Open to load it in VS Code.

### Clone the repository using VS Code's Integrated Terminal:

1. Open VS Code and open the integrated terminal by pressing `Ctrl + `` (backtick) or navigating to `Terminal > New Terminal`.
2. Run the following commands:

```bash
git clone https://github.com/SHAIMOOM251283/QuotesData.git
cd QuotesData
```

### Install the required packages:

Make sure you have Python installed, then run:

```bash
pip install requests beautifulsoup4 pandas plotly nltk
```

### Download NLTK resources:

You need to download the VADER lexicon for sentiment analysis. Open a Python shell and run:

```python
import nltk
nltk.download('vader_lexicon')
```

## Usage

1. Run `scrape_link_tags.py` to extract tags from the quotes website.
2. Run `scrape_data.py` to scrape quotes based on the selected tag or homepage.
3. Run `sentiment_analysis_bar_chart.py` to visualize the sentiment distribution of quotes by author in a bar chart.
4. Run `sentiment_analysis_pie_chart.py` to visualize the sentiment distribution for a specific author in a pie chart.

## Data Output

The scraped quotes will be saved in a CSV file located in the `data` directory (e.g., `data/all_quotes.csv`). This file will contain the author and quote information, which is used for sentiment analysis and visualization.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Quotes to Scrape](https://quotes.toscrape.com) for providing the data.
- [NLTK](https://www.nltk.org/) for the sentiment analysis tools.
- [Plotly](https://plotly.com/python/) for creating interactive visualizations.
```

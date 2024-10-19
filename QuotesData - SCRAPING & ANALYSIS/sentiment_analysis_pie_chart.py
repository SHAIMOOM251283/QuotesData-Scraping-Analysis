import pandas as pd
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer

# Load the CSV file
df = pd.read_csv('data/all_quotes.csv')

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Function to classify sentiment
def classify_sentiment(quote):
    score = sia.polarity_scores(quote)
    compound_score = score['compound']
    
    if compound_score >= 0.05:
        return 'Positive'
    elif compound_score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Apply sentiment classification
df['sentiment'] = df['quote'].apply(classify_sentiment)

# Count sentiments by author
sentiment_counts = df.groupby(['author', 'sentiment']).size().unstack(fill_value=0).stack().reset_index(name='count')

# Ask for user input to select the author
author_input = input("Enter the name of the author for whom you want to generate the sentiment pie chart: ")

# Filter the data for the selected author
author_data = sentiment_counts[sentiment_counts['author'] == author_input]

# Check if the author exists in the dataset
if not author_data.empty:
    # Create the pie chart for the selected author
    fig_pie = px.pie(author_data, 
                     values='count', 
                     names='sentiment', 
                     title=f'Sentiment Distribution for {author_input}',
                     hole=0.3)
    
    fig_pie.show()
else:
    print(f"Author '{author_input}' not found in the dataset.")

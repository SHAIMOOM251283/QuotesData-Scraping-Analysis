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

# Stacked bar chart using Plotly
fig_bar = px.bar(sentiment_counts, 
                  x='author', 
                  y='count', 
                  color='sentiment', 
                  title='Sentiment Distribution of Quotes by Author',
                  labels={'count': 'Number of Quotes', 'author': 'Author'},
                  text='count',
                  barmode='stack')

fig_bar.update_layout(xaxis_tickangle=-45)
fig_bar.show()

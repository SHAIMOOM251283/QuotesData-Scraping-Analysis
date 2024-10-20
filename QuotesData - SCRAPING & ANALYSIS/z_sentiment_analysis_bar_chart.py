import pandas as pd
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer

class SentimentAnalyzerVisualizer:

    def __init__(self):
        self.df = pd.read_csv('data/all_quotes.csv')
        self.sia = SentimentIntensityAnalyzer()
        
    # Function to classify sentiment
    def classify_sentiment(self, quote):
        score = self.sia.polarity_scores(quote)
        compound_score = score['compound']
    
        if compound_score >= 0.05:
            return 'Positive'
        elif compound_score <= -0.05:
            return 'Negative'
        else:
            return 'Neutral'

    def sentiment_classification(self):
        self.df['sentiment'] = self.df['quote'].apply(self.classify_sentiment)
        self.sentiment_counts = self.df.groupby(['author', 'sentiment']).size().unstack(fill_value=0).stack().reset_index(name='count')

    def visualize_data(self):
        fig_bar = px.bar(self.sentiment_counts, 
                        x='author', 
                        y='count', 
                        color='sentiment', 
                        title='Sentiment Distribution of Quotes by Author',
                        labels={'count': 'Number of Quotes', 'author': 'Author'},
                        text='count',
                        barmode='stack')

        fig_bar.update_layout(xaxis_tickangle=-45)
        fig_bar.show()
    
    def run(self):
        self.sentiment_classification()
        self.visualize_data()

if __name__ == '__main__':
    analyzer_visualizer = SentimentAnalyzerVisualizer()
    analyzer_visualizer.run()
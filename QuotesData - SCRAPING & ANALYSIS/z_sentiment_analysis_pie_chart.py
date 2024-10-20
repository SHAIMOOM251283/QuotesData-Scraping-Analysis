import pandas as pd
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer

class SentimentAnalyzerVisualizer:

    def __init__(self):
        self.df = pd.read_csv('data/all_quotes.csv')
        self.sia = SentimentIntensityAnalyzer()

    def extract_author_names(self):
        author_names = self.df['author'].unique()
        print("*** AUTHORS ***")
        for author in author_names:
            print(author)

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
        
        self.author_input = input("\nEnter the name of the author for whom you want to generate the sentiment pie chart: ")
        self.author_data = self.sentiment_counts[self.sentiment_counts['author'] == self.author_input]

    def visualize_data(self):
        if not self.author_data.empty:
            # Create the pie chart for the selected author
            fig_pie = px.pie(self.author_data, 
                            values='count', 
                            names='sentiment', 
                            title=f'Sentiment Distribution for {self.author_input}',
                            hole=0.3)
    
            fig_pie.show()
        else:
            print(f"Author '{self.author_input}' not found in the dataset.")

    def run(self):
        self.extract_author_names()
        self.sentiment_classification()
        self.visualize_data()

if __name__ == '__main__':
    analyzer_visualizer = SentimentAnalyzerVisualizer()
    analyzer_visualizer.run()
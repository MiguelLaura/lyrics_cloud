# =============================================================================
# Script to create word cloud from lyrics
# =============================================================================
#
# Helpers:
#   - https://www.datacamp.com/tutorial/wordcloud-python

import argparse

import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import warnings

from lyrics_cloud.utils import clean_lyrics, prepare_text


def generate_word_cloud(text):
    """
    Function to plot a text word cloud.

    Args:
        text (str): text to output in the word cloud.
    """
    text = set(text.split(" "))
    text = " ".join(text)
    wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    warnings.filterwarnings("ignore")

    stopwords = set(STOPWORDS)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--artist",
        required=True,
        help="artist singing the song to get recommendations from",
    )
    parser.add_argument(
        "--csv-file", required=True, help="csv file containing the lyrics"
    )
    parser.add_argument(
        "--title", required=True, help="song title to get recommendations from"
    )
    args = parser.parse_args()

    artist = args.artist.lower()
    csv_file = args.csv_file
    title = args.title.lower()

    df = pd.read_csv(csv_file)
    df["artist_prepared"] = df.artist.apply(func=clean_lyrics)
    df["title_prepared"] = df.title.apply(func=clean_lyrics)
    df.lyrics = df.lyrics.apply(func=prepare_text)

    lyrics = df.loc[(df["artist_prepared"] == artist) & (df["title_prepared"] == title)]
    generate_word_cloud(lyrics.iloc[0].lyrics)

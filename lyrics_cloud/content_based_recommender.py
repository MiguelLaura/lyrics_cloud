# =============================================================================
# Script to create content-based recommender systems
# =============================================================================
#
# Helpers:
#   - https://builtin.com/machine-learning/nlp-word2vec-python
#   - https://github.com/devalindey/Recommender-Systems-using-Word-Embeddings/blob/master/Recommender.ipynb

import argparse
import warnings

warnings.filterwarnings("ignore")

from gensim.models import Word2Vec
import nltk

nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_similarity


def clean_lyrics(lyrics):
    """
    Function to clean the lyrics (remove stop words, punctuation, etc.).

    Args:
        lyrics (str): lyrics of a song.
    """

    lyrics = lyrics.lower()

    # Remove stop words
    lyrics = lyrics.split()
    stops = set(stopwords.words("english"))
    lyrics = [w for w in lyrics if not w in stops]
    lyrics = " ".join(lyrics)

    # Function for removing punctuation
    tokenizer = RegexpTokenizer(r"\w+")
    lyrics = tokenizer.tokenize(lyrics)
    lyrics = " ".join(lyrics)

    return lyrics


def build_recommender_word2vec(corpus):
    """
    Function to load and train the Word2Vec model on the corpus.

    Args:
        corpus (list[list[str]]): corpus of songs.
    """
    # Training the corpus with the model
    model = Word2Vec(vector_size=300, window=5, min_count=2, workers=-1)
    model.build_vocab(corpus)

    model.train(corpus, total_examples=model.corpus_count, epochs=5)

    return model


def create_avg_word2vec_embeddings(df_lyrics, model):
    """
    Function to create the averaged word2vec embeddings.

    Args:
        df_lyrics (Series): lyrics.
        model: the trained word2vec model.
    """
    word_embeddings = []

    for line in df_lyrics:

        avgword2vec = None
        count = 0

        for word in line.split():
            if not word in model.wv.key_to_index:
                continue
            count += 1
            avgword2vec = (
                model.wv[word] if avgword2vec is None else avgword2vec + model.wv[word]
            )

        if avgword2vec is not None:
            avgword2vec = avgword2vec / count
            word_embeddings.append(avgword2vec)

    return word_embeddings


def visualize_embeddings(w2v):
    """
    Function to visualize the word2vec embeddings.

    Args:
        w2v: the trained word2vec model.
    """
    X = w2v.wv[w2v.wv.key_to_index]
    pca = PCA(n_components=2)
    result = pca.fit_transform(X)

    words = list(w2v.wv.key_to_index)

    pca_df = pd.DataFrame(result, columns=["x", "y"])
    pca_df["word"] = words
    pca_df.head()

    fig = go.Figure(
        data=go.Scattergl(
            x=pca_df["x"],
            y=pca_df["y"],
            mode="markers",
            marker=dict(
                color=np.random.randn(1000000), colorscale="Viridis", line_width=1
            ),
            text=pca_df["word"],
            textposition="bottom center",
        )
    )

    fig.show()

    return pca_df


def recommend_with_word2vec(df, artist, title, word_embeddings):
    """
    Function to recommend a song based on a title and artist.

    Args:
        df (dataframe): base dataframe with all the information.
        artist (str): artist singing the song to get recommendations from.
        title (str): song title to get recommendations from.
        word_embeddings: averaged word2vec embeddings.
    """
    lyrics = df.loc[(df["artist"] == artist) & (df["title"] == title), "lyrics"]

    # Finding cosine similarity for the vectors
    cosine_similarities = cosine_similarity(word_embeddings, word_embeddings)

    # Reverse mapping of the index
    indices = pd.Series(df.index, index=df["lyrics"]).drop_duplicates()

    idx = indices[lyrics]
    sim_scores = list(enumerate(cosine_similarities[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    song_indices = [i[0] for i in sim_scores]
    recommend = df.iloc[song_indices]

    for _, row in recommend.iterrows():
        print("Result: ", row["title"], row["artist"])


if __name__ == "__main__":

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

    artist = args.artist
    csv_file = args.csv_file
    title = args.title

    df = pd.read_csv(csv_file)
    df.lyrics = df.lyrics.apply(func=clean_lyrics)

    # Create corpus
    corpus = []
    for words in df.lyrics:
        corpus.append(words.split())

    model = build_recommender_word2vec(corpus)

    word_embeddings = create_avg_word2vec_embeddings(df.lyrics, model)

    visualize_embeddings(model)

    recommend_with_word2vec(df, artist, title, word_embeddings)

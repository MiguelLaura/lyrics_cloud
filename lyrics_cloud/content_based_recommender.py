# =============================================================================
# Script to create content-based recommender systems
# =============================================================================
#
# Helpers:
#   - https://builtin.com/machine-learning/nlp-word2vec-python
#   - https://github.com/devalindey/Recommender-Systems-using-Word-Embeddings/blob/master/Recommender.ipynb

import argparse
import warnings

from gensim.models import Word2Vec
import nltk
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_similarity

from lyrics_cloud.utils import clean_lyrics, prepare_text


def build_recommender_word2vec(corpus):
    """
    Function to load and train the word2vec model on the corpus.

    Args:
        corpus (list[list[str]]): corpus of songs.
    Returns:
        model: trained word2vec model.
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
        model: trained word2vec model.
    Returns:
        list[float]: lyrics averaged word2vec embeddings.
    """
    embeddings = []

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
            embeddings.append(avgword2vec)

    return embeddings


def visualize_embeddings(w2v):
    """
    Function to visualize the word2vec embeddings.

    Args:
        w2v: trained word2vec model.
    Returns:
        dataframe: PCA dataframe.
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


def recommend_with_word2vec(idx, embeddings, nb_reco=5):
    """
    Function to recommend a song based on a title and artist.

    Args:
        idx (int): index of the item to get recommendations from.
        embeddings (list[float]): averaged word2vec embeddings.
        nb_reco (int): number of recommendations to return.
    Returs:
        list(int): list of indexes of the items recommended.
    """
    cosine_similarities = cosine_similarity(embeddings, embeddings)

    sim_scores = list(enumerate(cosine_similarities[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1 : nb_reco + 1]
    result = [i[0] for i in sim_scores]

    return result


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    nltk.download("stopwords")

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

    lyrics_corpus = []
    for words in df.lyrics:
        lyrics_corpus.append(words.split())
    lyrics_model = build_recommender_word2vec(lyrics_corpus)
    lyrics_embeddings = create_avg_word2vec_embeddings(df.lyrics, lyrics_model)
    visualize_embeddings(lyrics_model)

    lyrics = df.loc[(df["artist_prepared"] == artist) & (df["title_prepared"] == title)]
    idx = lyrics.index.values[0]
    song_indices = recommend_with_word2vec(idx, lyrics_embeddings)
    recommend = df.iloc[song_indices]

    result = []
    for index, (_, row) in enumerate(recommend.iterrows()):
        print(index + 1, row["title"], "by", row["artist"])
        result.append((row["artist"], row["title"]))

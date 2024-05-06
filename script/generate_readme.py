# =============================================================================
# Script to generate README.md
# =============================================================================
#

from contextlib import redirect_stdout
import io

from docdocdoc.build import generate_readme

from lyrics_cloud.artists_lyrics import get_artists_from_file, get_lyrics
from lyrics_cloud.content_based_recommender import (
    build_recommender_word2vec,
    create_avg_word2vec_embeddings,
    recommend_with_word2vec,
    visualize_embeddings,
)
from lyrics_cloud.word_cloud import generate_word_cloud
from lyrics_cloud.utils import clean_lyrics, prepare_text


DOCS = [
    {
        "title": "Scraper",
        "fns": [
            get_artists_from_file,
            get_lyrics,
        ],
    },
    {
        "title": "Recommender",
        "fns": [
            build_recommender_word2vec,
            create_avg_word2vec_embeddings,
            recommend_with_word2vec,
            visualize_embeddings,
        ],
    },
    {
        "title": "Word cloud",
        "fns": [
            generate_word_cloud,
        ],
    },
    {
        "title": "Utils",
        "fns": [
            clean_lyrics,
            prepare_text,
        ],
    },
]


if __name__ == "__main__":
    f = io.StringIO()

    with redirect_stdout(f):
        generate_readme(DOCS)

    readme = f.getvalue()

    with open("README.md", "w") as file:
        file.write(readme)

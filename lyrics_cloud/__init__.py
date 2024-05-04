# =============================================================================
# Lyrics_cloud Library Endpoint
# =============================================================================
#

from lyrics_cloud.artists_lyrics import get_lyrics
from lyrics_cloud.content_based_recommender import (
    build_recommender_word2vec,
    create_avg_word2vec_embeddings,
    prepare_lyrics,
    recommend_with_word2vec,
    visualize_embeddings,
)
from lyrics_cloud.utils import clean_lyrics

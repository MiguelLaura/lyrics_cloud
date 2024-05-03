# =============================================================================
# Script to generate README.md
# =============================================================================
#

from docdocdoc.build import generate_readme
from lyrics_cloud.artists_lyrics import get_lyrics

DOCS = [{"title": "Functions", "fns": [get_lyrics]}]

generate_readme(DOCS)

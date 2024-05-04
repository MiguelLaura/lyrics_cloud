# =============================================================================
# Script to generate README.md
# =============================================================================
#

from contextlib import redirect_stdout
import io

from docdocdoc.build import generate_readme
from lyrics_cloud.artists_lyrics import get_lyrics
from lyrics_cloud.utils import clean_lyrics


DOCS = [{"title": "Functions", "fns": [get_lyrics, clean_lyrics]}]

if __name__ == "__main__":
    f = io.StringIO()

    with redirect_stdout(f):
        generate_readme(DOCS)

readme = f.getvalue()

with open("README.md", "w") as file:
    file.write(readme)

"""
tdd2_slugify — Solution
"""
import re


def slugify(text: str, sep: str = "-") -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", sep, text)
    return text.strip(sep)


# ---------------------------------------------------------------- tests


def test_basic_and_lowercase():
    assert slugify("Hello World") == "hello-world"


def test_special_characters_and_punctuation():
    assert slugify("FastAPI & PyTest!") == "fastapi-pytest"


def test_stripping_and_consecutive_separators():
    assert slugify("   many   spaces   ") == "many-spaces"
    assert slugify("---already-dashed---") == "already-dashed"

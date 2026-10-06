TARGET = "slugify"
import re


def _no_lowercase(text, sep="-"):
    return re.sub(r"[^a-zA-Z0-9]+", sep, text).strip(sep)


def _no_strip(text, sep="-"):
    return re.sub(r"[^a-z0-9]+", sep, text.lower())


def _keeps_punctuation(text, sep="-"):
    return text.lower().replace(" ", sep).strip(sep)


MUTANTS = {
    "does not lowercase text": _no_lowercase,
    "does not strip leading/trailing separators": _no_strip,
    "keeps special punctuation characters instead of replacing": _keeps_punctuation,
}

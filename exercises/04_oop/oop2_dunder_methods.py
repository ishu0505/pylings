"""
oop2_dunder_methods — Custom collection container     difficulty: medium

Build `Playlist`:
- `__init__(self, name: str)`: stores name and an empty songs list
- `add_song(self, song: str) -> None`: appends song to playlist
- `__len__(self) -> int`: number of songs
- `__getitem__(self, index: int) -> str`: allows indexing `p[0]`
- `__contains__(self, song: str) -> bool`: allows `'Bohemian Rhapsody' in p`
- `__repr__(self) -> str`: returns `Playlist('Rock', ['Song A', ...])`
- `__eq__(self, other) -> bool`: equal if name and songs are equal
"""

# I AM NOT DONE

# Concept Tip: Dunder methods turn standard objects into first-class Python syntax citizens.


class Playlist:
    # TODO: implement
    pass


# ---------------------------------------------------------------- tests


def test_playlist_dunders():
    p = Playlist("Chill")
    p.add_song("Song 1")
    p.add_song("Song 2")

    assert len(p) == 2
    assert p[0] == "Song 1"
    assert "Song 2" in p
    assert "Song 3" not in p
    assert repr(p) == "Playlist('Chill', ['Song 1', 'Song 2'])"

    p2 = Playlist("Chill")
    p2.add_song("Song 1")
    p2.add_song("Song 2")
    assert p == p2

    p3 = Playlist("Party")
    assert p != p3

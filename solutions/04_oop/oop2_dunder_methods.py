"""
oop2_dunder_methods — Solution
"""


class Playlist:
    def __init__(self, name: str) -> None:
        self.name = name
        self.songs: list[str] = []

    def add_song(self, song: str) -> None:
        self.songs.append(song)

    def __len__(self) -> int:
        return len(self.songs)

    def __getitem__(self, index: int) -> str:
        return self.songs[index]

    def __contains__(self, song: str) -> bool:
        return song in self.songs

    def __repr__(self) -> str:
        return f"Playlist({self.name!r}, {self.songs!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Playlist):
            return False
        return self.name == other.name and self.songs == other.songs


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

# Week 6 - Music Library Manager

songs = []
genre_count = {}

print("Welcome to Music Library Manager!\n")

# collect 5 songs
for i in range(1, 6):
    print(f"Enter Song {i}")
    name = input("Song name: ")
    genre = input("Genre: ")

    song = (name, genre)
    songs.append(song)

    # Count genres safely
    genre_count[genre] = genre_count.get(genre, 0) + 1
    print()

# display songs
print("=== YOUR MUSIC LIBRARY ===")
for index, (name, genre) in enumerate(songs, 1):
    print(f"{index}. {name} ({genre})")

# display statistics
print("\n=== GENRE STATISTICS ===")
for genre, count in genre_count.items():
    print(f"{genre}: {count} songs")

most_popular = max(genre_count, key=genre_count.get)
print(f"\nMost popular genre: {most_popular}")

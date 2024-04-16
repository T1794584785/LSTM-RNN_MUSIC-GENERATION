import os
import music21 as m21

KERN_DATASET_PATH = "C:\\Users\\86183\\PycharmProjects\\pythonProject2\\3-Data pre-processing\\deutschl\\test"

def load_songs_in_kern(dataset_path):
    songs = []
    for path, subdirs, files in os.walk(dataset_path):
        for file in files:
            if file.endswith('.krn'):
                song_path = os.path.join(path, file)
                print(f"loading: {song_path}")
                song = m21.converter.parse(song_path)
                songs.append(song)
    return songs

if __name__ == "__main__":
    songs = load_songs_in_kern(KERN_DATASET_PATH)
    print(f"Loaded {len(songs)} songs.")
    if songs:
        song = songs[0]
        song.show()
    else:
        print("Not find any songs.")

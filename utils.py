import librosa

def mp3_to_midi(path_to_file):
    y, sr = librosa.load(path_to_file)
    # 2. Pitch tracking using librosa's piptrack
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
    # 3. Extract strongest pitches over time
    notes = []
    for t in range(pitches.shape[1]):
        index = magnitudes[:, t].argmax()
        pitch = pitches[index, t]
        if pitch > 0:  # filter out silence
            midi_note = librosa.hz_to_midi(pitch)
            notes.append(int(round(midi_note)))
    # 4. Remove duplicate/similar notes (optional)
    clean_notes = []
    for i in range(len(notes)):
        if i == 0 or notes[i] != notes[i - 1]:
            clean_notes.append(notes[i])
    return clean_notes

def notes_to_midi(note_list):
    note_to_midi = {
        "C0": 12, "C#0": 13, "D0": 14, "D#0": 15, "E0": 16, "F0": 17, "F#0": 18, "G0": 19, "G#0": 20, "A0": 21,
        "A#0": 22, "B0": 23,
        "C1": 24, "C#1": 25, "D1": 26, "D#1": 27, "E1": 28, "F1": 29, "F#1": 30, "G1": 31, "G#1": 32, "A1": 33,
        "A#1": 34, "B1": 35,
        "C2": 36, "C#2": 37, "D2": 38, "D#2": 39, "E2": 40, "F2": 41, "F#2": 42, "G2": 43, "G#2": 44, "A2": 45,
        "A#2": 46, "B2": 47,
        "C3": 48, "C#3": 49, "D3": 50, "D#3": 51, "E3": 52, "F3": 53, "F#3": 54, "G3": 55, "G#3": 56, "A3": 57,
        "A#3": 58, "B3": 59,
        "C4": 60, "C#4": 61, "D4": 62, "D#4": 63, "E4": 64, "F4": 65, "F#4": 66, "G4": 67, "G#4": 68, "A4": 69,
        "A#4": 70, "B4": 71,
        "C5": 72, "C#5": 73, "D5": 74, "D#5": 75, "E5": 76, "F5": 77, "F#5": 78, "G5": 79, "G#5": 80, "A5": 81,
        "A#5": 82, "B5": 83,
        "C6": 84, "C#6": 85, "D6": 86, "D#6": 87, "E6": 88, "F6": 89, "F#6": 90, "G6": 91, "G#6": 92, "A6": 93,
        "A#6": 94, "B6": 95,
        "C7": 96, "C#7": 97, "D7": 98, "D#7": 99, "E7": 100, "F7": 101, "F#7": 102, "G7": 103, "G#7": 104, "A7": 105,
        "A#7": 106, "B7": 107,
        "C8": 108, "C#8": 109, "D8": 110, "D#8": 111, "E8": 112, "F8": 113, "F#8": 114, "G8": 115, "G#8": 116,
        "A8": 117, "A#8": 118, "B8": 119}

    return [note_to_midi[note] for note in note_list]


def transposition(keyboard_number):
    while not 1 <= keyboard_number <= 25:
        if keyboard_number > 25:
            keyboard_number = keyboard_number - 12
        elif keyboard_number < 1:
            keyboard_number = keyboard_number + 12
    return keyboard_number


def midi_to_keyboard_id(midi_list):
    keyboard_id = []
    # Define your keyboard range
    first_key_midi = 52  # E3
    for midi in midi_list:
        # Map to your custom keyboard number
        keyboard_number = midi - first_key_midi + 1
        mapped_key = transposition(keyboard_number)
        keyboard_id.append(mapped_key)
    return keyboard_id


def keyboard_id_to_notes(keyboard_id):
    dic_key = {
        1: "E3",
        2: "F3",
        3: "F#3",
        4: "G3",
        5: "G#3",
        6: "A3",
        7: "A#3",
        8: "B3",
        9: "C4",
        10: "C#4",
        11: "D4",
        12: "D#4",
        13: "E4",
        14: "F4",
        15: "F#4",
        16: "G4",
        17: "G#4",
        18: "A4",
        19: "A#4",
        20: "B4",
        21: "C5",
        22: "C#5",
        23: "D5",
        24: "D#5",
        25: "E5"
    }
    return [dic_key[id] for id in keyboard_id]

def keyboard_id_to_midi(keyboard_id):
    return notes_to_midi(keyboard_id_to_notes(keyboard_id))



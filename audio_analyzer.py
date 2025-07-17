import librosa
import os
import numpy as np
import soundfile as sf


def analyze_audio(file_path):
    # Load the audio file using soundfile instead of librosa.load
    y, sr = sf.read(file_path)

    # Remove the mono conversion and analyze the left channel if stereo
    # or use the original signal if mono
    signal = y[:, 0] if len(y.shape) > 1 else y

    # Estimate tempo (BPM)
    tempo, _ = librosa.beat.beat_track(y=signal, sr=sr)

    # Check if tempo is valid (not zero or too low)
    if tempo < 1:
        tempo = 120  # Set a default BPM if detection fails

    # Calculate bar length in seconds
    # Most music has 4 beats per bar
    beats_per_bar = 4
    bar_length = (beats_per_bar * 60) / tempo

    # Round values and ensure we return numbers, not numpy types
    return round(float(tempo)), round(float(bar_length))


def rename_audio_files(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith(".wav"):
            file_path = os.path.join(directory, filename)
            try:
                # Get BPM and bar length
                bpm, bar_len = analyze_audio(file_path)

                # Create new filename
                name_without_ext = os.path.splitext(filename)[0]
                new_filename = f"{name_without_ext}_BPM{bpm}_BAR{bar_len}s.wav"
                new_file_path = os.path.join(directory, new_filename)

                # Rename the file
                os.rename(file_path, new_file_path)
                print(f"Processed: {filename} -> {new_filename}")

            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")


if __name__ == "__main__":
    # Replace with your directory containing WAV files
    directory = "./audio"
    rename_audio_files(directory)

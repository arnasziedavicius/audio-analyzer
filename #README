# Audio File BPM Analyzer

This script analyzes WAV audio files in a directory to detect their tempo (BPM) and bar length, then renames the files to include this information.

## Prerequisites

Before running the script, you need to install the required Python packages:

pip install librosa numpy soundfile

## Usage

1. Place your WAV files in a directory (default is `./audio`)

2. Run the script:
python audio_analyzer.py

The script will:
- Process all WAV files in the specified directory
- Detect the BPM (tempo) and calculate bar length for each file
- Rename files to include this information in the format: `originalname_BPM120_BAR2s.wav`

## Configuration

By default, the script looks for WAV files in an `./audio` directory. To change this:

1. Open `audio_analyzer.py`
2. Modify the `directory` variable at the bottom of the file:
directory = "./your/path/here"

## Output Format

Files will be renamed following this pattern:
- Original filename: `song.wav`
- New filename: `song_BPM120_BAR2s.wav`
  - `BPM120`: The detected tempo in beats per minute
  - `BAR2s`: The length of one bar in seconds

## Error Handling

- If BPM detection fails, a default value of 120 BPM is used
- Any errors during processing are logged to the console
- The script will continue processing remaining files if one file fails

## Notes

- Only processes WAV files
- Converts stereo files to mono for analysis
- Assumes 4 beats per bar (standard time signature)

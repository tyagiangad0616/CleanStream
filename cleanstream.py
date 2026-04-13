import json
import subprocess
import sys

# INPUT HANDLING


# Accept video file from terminal
if len(sys.argv) < 2:
    print("Usage: python3 cleanstream.py <video_file>")
    sys.exit(1)

VIDEO_FILE = sys.argv[1]
OUTPUT_FILE = "output_final_with_subs.webm"
WHISPER_JSON = "whisper_output.json"

# Words to censor
BAD_WORDS = ["fuck", "fucked", "fucker", "motherfucker", "bitch"]



# LOAD WHISPER DATA


def load_whisper_words(json_file):
    """
    Extracts word-level timestamps from Whisper JSON output.
    """
    with open(json_file, "r") as f:
        data = json.load(f)

    words = []
    for segment in data["segments"]:
        for w in segment["words"]:
            words.append({
                "word": w["word"].lower(),
                "start": w["start"],
                "end": w["end"]
            })
    return words



# DETECT BAD WORDS


def detect_bad_words(words):
    """
    Detects profanity words and generates timestamps.
    Uses asymmetric buffering to ensure full word muting.
    """
    timestamps = []

    for w in words:
        text = w["word"]

        for bad in BAD_WORDS:
            if bad in text:
                # Small backward buffer, larger forward buffer
                start = max(0, w["start"] - 0.04)
                end = w["end"] + 0.30

                print(f"Detected: {text} ({start:.2f} → {end:.2f})")
                timestamps.append((start, end))

    return timestamps



# MERGE OVERLAPPING TIMESTAMPS


def merge_timestamps(timestamps):
    """
    Merges overlapping timestamps to avoid fragmented muting.
    """
    if not timestamps:
        return []

    timestamps.sort()
    merged = [timestamps[0]]

    for current in timestamps[1:]:
        last = merged[-1]

        if current[0] <= last[1]:
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)

    return merged



# GENERATE SUBTITLES (SRT)


def generate_srt_from_whisper(words, output_file="subs.srt"):
    """
    Generates SRT subtitles from Whisper word timestamps.
    """
    with open(output_file, "w") as f:
        idx = 1

        for w in words:
            start = w["start"]
            end = w["end"]
            text = w["word"]

            def format_time(t):
                hrs = int(t // 3600)
                mins = int((t % 3600) // 60)
                secs = int(t % 60)
                ms = int((t - int(t)) * 1000)
                return f"{hrs:02}:{mins:02}:{secs:02},{ms:03}"

            f.write(f"{idx}\n")
            f.write(f"{format_time(start)} --> {format_time(end)}\n")
            f.write(f"{text}\n\n")

            idx += 1



# BUILD FFMPEG COMMAND


def build_ffmpeg_command(input_file, output_file, timestamps):
    """
    Creates FFmpeg command to:
    - Overlay subtitles
    - Mute detected profanity segments
    """
    volume_filters = []

    for start, end in timestamps:
        volume_filters.append(
            f"volume=enable='between(t,{start},{end})':volume=0"
        )

    audio_filter = ",".join(volume_filters)

    command = [
        "ffmpeg",
        "-y",
        "-i", input_file,
        "-vf", "subtitles=subs.srt",
        "-af", audio_filter,
        output_file
    ]

    return command



# MAIN PIPELINE


if __name__ == "__main__":

    print(f"\nProcessing video: {VIDEO_FILE}\n")

    # Step 1: Load transcription
    words = load_whisper_words(WHISPER_JSON)

    # Step 2: Generate subtitles
    generate_srt_from_whisper(words)

    # Step 3: Detect profanity
    timestamps = detect_bad_words(words)
    print("Raw:", timestamps)

    # Step 4: Merge timestamps
    timestamps = merge_timestamps(timestamps)
    print("Merged:", timestamps)

    # Step 5: Apply FFmpeg processing
    if timestamps:
        command = build_ffmpeg_command(VIDEO_FILE, OUTPUT_FILE, timestamps)
        subprocess.run(command)
    else:
        print("No profanity detected.")

    print("\nFinal output ready:", OUTPUT_FILE)

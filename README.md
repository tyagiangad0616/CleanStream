CleanStream 🎬

An automated system that detects strong language in video content and temporarily mutes or blocks the scene to make media family friendly.


Problem Statement

Many movies, web series and online videos contain strong language that makes them unsuitable for family viewing. There is no simple automated system that detects and handles such content in real time.


Our Solution

CleanStream detects strong words from subtitles and automatically:

1) Identifies timestamps of inappropriate words
2) Temporarily mutes or blocks those scenes
3) Produces a clean, family-friendly output video  


Technology Used

1) FFmpeg
2) Subtitle (.vtt) processing
3) Shell scripting
4) Git & GitHub Pages (for hosting presentation)


How It Works

1) Extract subtitles from video.
2) Scan subtitles for strong language keywords.
3) Get timestamps of detected words.
4) Use FFmpeg to mute/block those timestamps.
5) Generate final clean video output.


Sample FFmpeg Command Used

```bash
ffmpeg -i input.webm -vf "drawtext=..." output.webm
```


Results

1) Successfully detected strong language from subtitle file.
2) Automatically muted specific timestamps.
3) Generated clean output video (output_final.webm).
4) GitHub-hosted live presentation deployed successfully.



Live Presentation Link

https://tyagiangad0616.github.io/CleanStream/



Future Scope

1) Real-time live streaming censorship
2) AI-based speech-to-text integration
3) Web application version
4) Browser extension for OTT platforms
5) Mobile app implementation



Project Guide

Dr. Bhawani Singh Rathore


Developed By

Angad Tyagi  
Registration ID: 2427030688


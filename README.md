CleanStream  

An AI-based automated system that detects strong language in video content and selectively mutes only those specific words, making media family-friendly without affecting the overall viewing experience.

Problem Statement  

Many movies, web series, and online videos contain strong language that makes them unsuitable for family viewing. Existing solutions either remove entire scenes or require manual editing. There is no efficient automated system that performs precise, word-level censorship while preserving content continuity.

Our Solution  

CleanStream uses an AI-driven pipeline to detect and censor inappropriate language:

- Uses speech-to-text (Whisper) to extract word-level timestamps  
- Identifies profanity using keyword-based detection  
- Applies selective audio muting using FFmpeg  
- Maintains synchronization between audio and video  
- Generates subtitles for visual verification  

Technology Used  

- Python (core processing and automation)  
- OpenAI Whisper (speech-to-text transcription)  
- FFmpeg (video and audio processing)  
- Subtitle generation (SRT format)  
- Git & GitHub Pages (for hosting presentation)  

How It Works  

1. Input video file is processed.  
2. Whisper generates transcript with word-level timestamps.  
3. Extracted words are scanned for profanity.  
4. Accurate timestamps are generated with buffering.  
5. FFmpeg applies selective muting to those segments.  
6. Subtitles are generated and overlaid on the video.  
7. Final clean video is produced.  

Sample FFmpeg Logic Used  

volume=enable='between(t,start,end)':volume=0  

This ensures only specific segments are muted while keeping the rest of the audio intact.

Results  

- Successfully detected profanity using AI-based transcription  
- Achieved word-level censorship instead of full scene removal  
- Maintained proper audio-video synchronization  
- Generated clean output video with subtitles  
- Successfully tested on multiple video samples  

Live Presentation Link  

https://tyagiangad0616.github.io/CleanStream/  

Future Scope  

- Real-time live streaming censorship  
- Context-aware NLP-based detection  
- Web-based interface for user uploads  
- Browser extension for OTT platforms  
- Mobile application implementation  

Project Guide  

Mr Bhawani Singh Rathore  

Developed By  

Angad Tyagi  
Registration No: 2427030688  

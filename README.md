# yt-dlp-server-starter

A simple Flask server to extract audio URLs from YouTube videos using `yt-dlp`.

## Endpoint

POST `/convert`

### Payload
```json
{
  "youtubeUrl": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
}

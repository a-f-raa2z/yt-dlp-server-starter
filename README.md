# 🎿 YouTube to Audio Converter Server (yt-dlp + Flask)

A simple Python Flask server that converts YouTube videos into audio stream URLs using `yt-dlp`.

---

## 💻 Run Locally in 3 Steps

### ✅ Requirements

* Python 3.7 or higher
* `ffmpeg` installed and in your system path (used by `yt-dlp`)

### 📥 Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/yt-dlp-server-starter.git
cd yt-dlp-server-starter
```

### 📅 Step 2: Install Dependencies

```bash
pip install flask yt-dlp
```

> You can skip `requirements.txt` — all packages are installed manually above.

### 🚀 Step 3: Start the Server

```bash
python app.py
```

You should see:

```
 * Running on http://127.0.0.1:5000
```

---

## 🔁 Example Usage

### Endpoint: `POST /convert`

Send a POST request with a YouTube URL to receive the audio stream URL and video title.

#### 🧷 Test with `curl`:

```bash
curl -X POST http://127.0.0.1:5000/convert \
  -H "Content-Type: application/json" \
  -d '{"youtubeUrl": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}'
```

#### ✅ Successful Response

```json
{
  "success": true,
  "title": "Rick Astley - Never Gonna Give You Up (Official Music Video)",
  "audioUrl": "https://.../stream.m4a"
}
```

#### ❌ Error Response

```json
{
  "success": false,
  "error": "yt-dlp error message here..."
}
```

---

## 🫯 Troubleshooting

* `500 Internal Server Error`:

  * Make sure `ffmpeg` is installed
  * The video may be unavailable or restricted
* `curl` returns nothing:

  * Check the server is running at `http://127.0.0.1:5000`
  * Confirm the video is accessible publicly

---

## 🗂 Project Structure

```
yt-dlp-server-starter/
├── app.py       # Flask server
└── README.md    # This file
```

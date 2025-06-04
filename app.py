from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    youtube_url = data.get('youtubeUrl')

    if not youtube_url:
        return jsonify({'success': False, 'error': 'Missing YouTube URL'}), 400

    try:
        print("🚀 Running yt-dlp to get title...")
        result = subprocess.run(
            ['yt-dlp', '--no-playlist', '--no-check-certificate', '--user-agent', 'Mozilla/5.0', '--get-title', youtube_url],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)

        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, result.args, result.stdout, result.stderr)

        title = result.stdout.strip()

        print("🎵 Getting audio URL...")
        audio_result = subprocess.run(
            ['yt-dlp', '--no-playlist', '--no-check-certificate', '--user-agent', 'Mozilla/5.0', '--get-url', '-f', 'bestaudio[ext=m4a]/bestaudio', youtube_url],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print("AUDIO STDOUT:", audio_result.stdout)
        print("AUDIO STDERR:", audio_result.stderr)

        if audio_result.returncode != 0:
            raise subprocess.CalledProcessError(audio_result.returncode, audio_result.args, audio_result.stdout, audio_result.stderr)

        audio_url = audio_result.stdout.strip()

        return jsonify({'success': True, 'title': title, 'audioUrl': audio_url})

    except subprocess.CalledProcessError as e:
        return jsonify({
            'success': False,
            'error': f"yt-dlp failed:\n{e.stderr or e.stdout}"
        }), 500

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
        title = subprocess.check_output(['yt-dlp', '--get-title', youtube_url], text=True).strip()
        audio_url = subprocess.check_output(
            ['yt-dlp', '--get-url', '-f', 'bestaudio[ext=m4a]/bestaudio', youtube_url],
            text=True
        ).strip()

        return jsonify({
            'success': True,
            'title': title,
            'audioUrl': audio_url
        })

    except subprocess.CalledProcessError as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

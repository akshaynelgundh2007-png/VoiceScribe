from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.get_json()
        text = data.get('text', '')
        target_lang = data.get('target_lang', 'hi')
        if not text:
            return jsonify({'success': False, 'text': 'No text to translate'})
        translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
        return jsonify({'success': True, 'text': translated})
    except Exception as e:
        return jsonify({'success': False, 'text': 'Error: ' + str(e)})

if __name__ == '__main__':
    app.run(debug=True)

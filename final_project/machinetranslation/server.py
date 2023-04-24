from flask import Flask, render_template, request
from .translator import english_to_french, french_to_english

app = Flask("My App")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/englishToFrench', methods=['POST'])
def eng_to_fr():
    text = request.form['text']
    translation = english_to_french(text)
    return render_template('result.html', translation=translation)

@app.route('/frenchToEnglish', methods=['POST'])
def fr_to_eng():
    text = request.form['text']
    translation = french_to_english(text)
    return render_template('result.html', translation=translation)

if __name__ == '__main__':
    app.run() 
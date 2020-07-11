#coding: utf-8

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        dna = request.form['dna']
        return transcribe_dna(dna)
    
def transcribe_dna(phrase):
    transcription = ""
    for letter in phrase:
        if letter in "Tt":
            transcription = transcription + "A"
        elif letter in "Aa":
            transcription = transcription + "U"
        elif letter in "Cc":
            transcription = transcription + "G"
        elif letter in "Gg":
            transcription = transcription + "C"
        else:
            transcription = transcription + letter
    return transcription

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')

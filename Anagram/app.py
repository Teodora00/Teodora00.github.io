from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def start():
 return render_template('anagram.html')

@app.route('/words/<string:word>')
def anagram(word):
 anagrams = []
 word = word.upper()
 f = open('words.txt').read()
 for w in f.split():
     if word == sorted(w):
         anagrams.append(w)
 return render_template('anagram.html', words = anagrams, word=word)          

 

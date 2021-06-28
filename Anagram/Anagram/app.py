from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def start():
 return render_template('anagram.html')

@app.route('/words/<string:word>')
def anagram(word):
 anagrams = []
 word = word.upper()
 f = open('words.txt')
 world_list = f.read().splitlines()
 for w in world_list:
     if sorted(word.upper()) == sorted(w):
      anagrams.append(w)
 return render_template('anagram.html', anagrams = anagrams, word=word)          

 

from flask import Flask, render_template

app = Flask (__name__, template_folder='templates')

@app.route('/')
def start():
        return render_template('fizzbuzz.html')


@app.route('/fizzbuzz/<int:number>')
def fizzbuzz(number):
   l = []
   for n in range(1, number + 1):
        if n % 3 == 0 and n % 5 == 0:
            l.append('FizzBuzz')
        elif n % 3 == 0:
            l.append('Fizz')    
        elif  n % 5 == 0:
            l.append('Buzz')
        else:
            l.append(n)
   return render_template('fizzbuzz.html', number = l)

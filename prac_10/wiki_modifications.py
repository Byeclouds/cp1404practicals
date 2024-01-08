# wiki.py

from flask import Flask, render_template

app = Flask(__name__)


def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32


@app.route('/')
def index():
    return 'Welcome to the Wikipedia Summary and Temperature Conversion App!'


@app.route('/wiki/<title>')
def wiki_summary(title):
    try:
        page = wikipedia.page(title, autosuggest=False)
        return render_template('wiki_summary.html', title=page.title, summary=page.summary, url=page.url)
    except wikipedia.DisambiguationError as e:
        return f"Disambiguation Error: {e.options}"


@app.route('/convert/<float:celsius>')
def convert_temperature(celsius):
    fahrenheit = celsius_to_fahrenheit(celsius)
    return f"{celsius} Celsius is equal to {fahrenheit:.2f} Fahrenheit."


if __name__ == '__main__':
    app.run(debug=True)

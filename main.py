import os

import requests
from flask import Flask, send_file, Response, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()

def get_latinized(fact_input):
    url = 'https://hidden-journey-62459.herokuapp.com/piglatinize/'
    response = requests.post(url,fact_input)
    return response.url


@app.route('/')
def home():
    fact = get_fact().strip()
    fact_input = {'input_text': fact}
    latinized_url = get_latinized(fact_input)
    return render_template('index.jinja2', url = latinized_url)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

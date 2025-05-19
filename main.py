import os

from flask import Flask, send_file, render_template

app = Flask(__name__, template_folder="src")

posts = [
    {'title':"Il Futuro dell'AI nel 2024", 'content':"Un'analisi sulle tendenze e le previsioni per l'intelligenza artificiale nell'anno in corso."},
    {'title':"Come iniziare con il Machine Learning", 'content':"Una guida per principianti sui primi passi nel mondo del Machine Learning."},
    {'title':"Discussione: AI Etica e Responsabile", 'content':"Condividi i tuoi Medication sull'importanza di uno sviluppo etico e responsabile dell'AI."}
]

@app.route("/")
def index():
    return render_template('index.html', posts=posts)

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()

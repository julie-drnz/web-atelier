# ---------------------------------------------------------------
#  Mon premier site Web avec Flask
# ---------------------------------------------------------------
#  Ce fichier est le "cerveau" de votre site : c'est lui qui
#  reçoit les demandes des navigateurs et qui fabrique les réponses.
#
#  Vous allez le compléter petit à petit, exercice après exercice.
#  Les consignes sont dans le dossier "exercices/".
# ---------------------------------------------------------------

from flask import Flask

app = Flask(__name__)


# Une "route" associe une adresse (URL) à une fonction Python.
# Ici : quand quelqu'un visite la page d'accueil "/",
# Flask exécute la fonction accueil() et renvoie son résultat au navigateur.
@app.get("/")
def accueil():
    return "Bienvenue sur le site de Juli !"
@app.get("/presentation")
def presentation():
    return """
    <h1>Julie Di renzo</h1>
    <p>Je suis étudiante en <strong>deuxième année</strong>.</p>
    <h2>Ce que j'aime</h2>
    <ul>
        <li>Les jeux vidéo</li>
        <li>Sortir</li>
    </ul>
    <img src="data:image/jpeg;base64,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" width="100">
    """


# ---------------------------------------------------------------
#  Ajoutez vos nouvelles routes ci-dessous 👇
# ---------------------------------------------------------------



# ---------------------------------------------------------------
#  Ne pas modifier : utile seulement pour lancer le site
#  sur votre propre ordinateur (python flask_app.py)
# ---------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

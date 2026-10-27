# 📒 Mon carnet de bord

**Nom :** Di Renzo

**Prénom :** Julie

**Adresse de mon site :** https://julidrnz.pythonanywhere.com

> Modifiez ce fichier directement sur GitHub (icône crayon ✏️) pour répondre aux questions de chaque exercice.
> Écrivez avec vos propres mots : une réponse courte et juste vaut mieux qu'un long copier-coller ! 🙂

---

## 🟢 Exercice 1 — Mon premier déploiement

1. Où se trouve physiquement le code qui fabrique votre page : sur votre ordinateur, sur GitHub ou sur PythonAnywhere ?

   > _Ma réponse : le code qui fabrique la page se situe sur pythonanywhere

2. Pourquoi votre voisin(e) peut-il voir votre site, alors que vous n'avez rien installé sur son ordinateur ?

   > _Ma réponse : car le site web est en ligne sur le serveur de PyhtonAnywhere, n'importe qui peut y avoir accès si ils ont le lien du site web.

---

## 🟢 Exercice 2 — Les URL et les routes

1. Dans l'URL `https://www.google.com/maps`, quel est le nom de domaine ? Quel est le chemin ?

   > _Ma réponse : le nom de domaine est google.com et le chemin est /maps

2. Que veut dire le message *Not Found* ? Qui l'a envoyé : votre navigateur ou le serveur ?

   > _Ma réponse : le message NOT FOUND indique que le serveur n'a pas trouvé la page demandée. c'est le serveur qui renvoie ce message

3. Que se passe-t-il si deux fonctions portent le même nom dans `flask_app.py` ? (Indice : essayez, puis lisez l'Error log.)

   > _Ma réponse : si les deux fct portent le même nom, il affichera que la première. Sur le error.log, on retrouve le message d'erreur indiquant qu'une fct a essayé de s'écrire par dessus la première car elles ont le même nom.

---

## 🔵 Exercice 3 — Le langage HTML

1. Quelle est la différence entre ce que le serveur **envoie** et ce que le navigateur **affiche** ?

   > _Ma réponse : Le serveur envoie le code HTML, et le navigateur va renvoyer/traduire le visuel.

2. À quoi servent les balises `<h1>`, `<p>`, `<ul>` et `<li>` ?

   > _Ma réponse : Les balises servent à définir le texte que l'on souhaite afficher, c'est une forme d'organisation dans le code. 

3. Pourquoi l'image s'affiche-t-elle alors qu'elle n'est pas sur votre serveur ?

   > _Ma réponse : car le serveur récupère le lien html sur le code à l'aide de la balise "img src" suivi du lien de l'image 

---

## 🔵 Exercice 4 — Les templates

1. Pourquoi est-ce une bonne idée de séparer le code Python et le HTML ? (Pensez à une équipe avec un développeur et un graphiste.)

   > _Ma réponse : c'est une bonne idée car c'est d'une part, + lisible. D'autre part, celà permet un meilleur travail d'équipe dans le sens où le graphiste à moins de chance de casser le code du dév et inversement. 

2. Les `{{ prenom }}` sont-ils remplacés par le serveur ou par le navigateur ? Comment l'avez-vous vérifié ?

   > _Ma réponse : c'est le serveur qui remplace les prénoms, on peut le vérifier grâce au code source vu par CTRL + U. On voit que le serveur renvoie déjà les prénoms intégrés dans flask_app.py. On ne voit pas le template avec les {}.

---

## 🔵 Exercice 5 — Le CSS et les liens

1. Quelle est la différence de rôle entre le HTML et le CSS ?

   > _Ma réponse : le html la page en brut et le css c'est l'esthétique/qui donne le style au html

2. Pour afficher votre page `/presentation`, combien de fichiers le navigateur doit-il télécharger ? (Vous pourrez le vérifier à l'exercice suivant !)

   > _Ma réponse : 3 pour moi car il y 'a l'images, le css et le html

3. Pourquoi faut-il parfois faire **Ctrl + F5** pour voir les changements de CSS ?

   > _Ma réponse : Il faut faire CTRL + F5 pour recharger la page, les changements ne se font pas en direct live. 

---

## 🟣 Exercice 6 — Espionner le navigateur

1. Que signifie HTTP ? Qui envoie la **requête** et qui envoie la **réponse** ?

   > _Ma réponse : HTTP signifie HyperText Transfer Protocol, la requête est envoyée par le navigateur et la réponse est envoyée par le serveur.

2. Combien de requêtes votre page `/presentation` a-t-elle déclenchées ? Lesquelles ?

   > _Ma réponse : la requête déclenche 3 demandes pour les 3 fichiers respectifs, l'image le css et l'html.

3. Que signifie le code `200` ? Et le code `404` de la favicon ?

   > _Ma réponse : le code 200 signifie que la page est "OK", 404 donne pas non trouvée dans le navigateur.

4. Pourquoi les modifications faites dans l'onglet Éléments ne sont-elles pas visibles par les autres visiteurs ?

   > _Ma réponse : Car les modifications se font dans le navigateurs, donc uniquement pour nous vu que les modifications ne touchent pas le serveur. 

---

## 🟣 Exercice 7 — Envoyer des informations dans l'URL

1. Dans l'URL `https://www.youtube.com/results?search_query=chat`, quel est le nom du paramètre ? Quelle est sa valeur ?

   > _Ma réponse : le nom du paramètres est search_query et la valeur est chat

2. Pourquoi le serveur plante-t-il avec `a=bonjour` ? Que faudrait-il faire pour l'éviter ?

   > _Ma réponse : Le serveur plante car il ne peut pas convertir le texte en nombre, on ne peut pas l'éviter, le problème de laisser les mots à s'additionner peut juste renvoyer du charabia

3. Pourquoi est-il dangereux d'afficher **tel quel** ce que l'utilisateur envoie ?

   > _Ma réponse : c'est dangereux car il peut glisser des scripts malveillants et tout ce qu'il veut 

---

## 🟣 Exercice 8 — Les formulaires

1. Quelle est la différence visible entre GET et POST ?

   > _Ma réponse : Les données par GET sont visibles dans l'URL tandis que les données de POSTS ne le sont pas. 

2. Pour un formulaire de **recherche**, quelle méthode choisiriez-vous ? Et pour un formulaire de **connexion avec mot de passe** ? Pourquoi ?

   > _Ma réponse : Pour une recherche un formulaire en get est mieux tandis que pour le form de connexion, le post est mieux. L'un est une recherche simple sans informations sensibles donc pas besoin de le cacher dans l'URL tandis que l'autre contient des données confidentielles à cacher. 

3. Les données envoyées en POST sont-elles vraiment « secrètes » ? (Pensez à ce que vous avez vu dans l'onglet Réseau.)

   > _Ma réponse : Non, elles ne sont pas vraiment secrètes, on peut retrouver les données dans le 'payload'. 

---

## 🔴 Exercice 9 — Les codes de statut

1. Quelle est la différence entre une erreur `4xx` et une erreur `5xx` ? Qui est « fautif » dans chaque cas ?

   > _Ma réponse : une erreur 4xx est une erreur du client, il provient d'une mauvaise commande. Une erreur 5xx est une erreur du serveur, elle provient d'un bug ou d'une panne. 

2. Comment fonctionne une redirection ? Qui fait la deuxième requête : le serveur ou le navigateur ?

   > _Ma réponse : C'est le navigateur qui envoie la requête suite à la recherche du client, puis le serveur répond par ok ou non et lui envoie une redirection. Le navigateur envoie alors une deuxième requête (cest donc lui qui fait la 2ème) pour avoir cette redirection. 
3. Donnez un exemple de situation où un vrai site utilise une redirection.

   > _Ma réponse : Gmail qui demande la connexion du client, le client se connecte avec les bons identifiants et est redirigé vers sa boîte mail. 

---

## 🔴 Exercice 10 — Ce que le serveur sait de vous

1. Citez trois informations que le serveur connaît sur vous, sans que vous ayez rien rempli.

   > _Ma réponse : Mon adresse IP, mon navigateur et ma langue 

2. À quoi peut servir l'en-tête `Accept-Language` pour un site comme Wikipédia ?

   > _Ma réponse : pour traduire automatiquement en la langue du système du client 

3. Dans l'Access log, retrouvez une requête qui a reçu un code `404`. Quelle page était demandée ?

   > _Ma réponse : la page demandée était /aaaa

4. Après cet exercice, que pensez-vous de la notion de « navigation anonyme » ?

   > _Ma réponse : Elle n'est pas si anonyme que ça malheureusement, encore la langue et le navigateur pourquoi pas, mais l'adresse ip rend la chose non-anonyme. Un VPN pourrait changer la donne cependant. 

---

## 🔴 Exercice 11 — Le Web des machines : API et JSON

1. Quelle est la différence entre une page HTML et une réponse JSON ? À qui chacune est-elle destinée ?

   > _Ma réponse :_ 

2. Dans la page `/horloge`, quel code s'exécute sur le **serveur** et quel code s'exécute dans le **navigateur** ?

   > _Ma réponse :_ 

3. Citez une application de votre téléphone qui, selon vous, utilise une API. Quelles données échange-t-elle ?

   > _Ma réponse :_ 

---

## 🏁 Pour conclure

En quelques phrases, expliquez à un ami ce qui se passe entre le moment où il tape une adresse dans son navigateur et celui où la page s'affiche :

> _Ma réponse :_ 

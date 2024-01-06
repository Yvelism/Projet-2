# PROGRAMME PERMETTANT D'INTERAGIR AVEC UNE BASE DE DONNEES SQL
# EN RESPECTANT LES REGLES DE LA PEP8 SAUF POUR LES REQUETES SQL


import sqlite3
conn = sqlite3.connect('RepertoireTelephonique.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS REPERTOIRE(numero TEXT, nom TEXT, prenom TEXT, PRIMARY KEY (numero))")
cur.execute("DELETE FROM REPERTOIRE;") # supprime tout de la table REPERTOIRE
conn.commit()
conn.close()



def creerRepertoire():
    """
    Cette fonction crée une base de donnée appelée
    "RepertoireTelephonique" avec une table "REPERTOIRE"
    """
    import sqlite3
# l'instruction suivante permet d'interagir avec une base de données
# (si cette dernière n'existe pas, elle sera créée)
    conn = sqlite3.connect('RepertoireTelephonique.db')
# permet de manipuler la base de données
    cur = conn.cursor()
# execution d'une requete SQL, on créer une table Repertoire
    cur.execute("CREATE TABLE IF NOT EXISTS REPERTOIRE(numero TEXT, nom TEXT, prenom TEXT, PRIMARY KEY (numero))")
    conn.commit()
    cur.close()  # "ferme" l'objet "cursor" et l'objet de type "connection".
    conn.close()


def ajouterContact(num, nom, prenom):
    """
    prend en parametre le numero, le nom et le prenom
    d'un contact a enregistrer dans le répertoire et ajoute celui-ci
    """
    data = (num, nom, prenom)
    import sqlite3
    conn = sqlite3.connect('RepertoireTelephonique.db')
    cur = conn.cursor()
# structure permettant d'intercepter une potentielle erreur
# de type "IntegrityError" lors d'un ajout de contact
    try:
        # les "?" correspondent respectivement aux valeurs "num","nom","prenom"
        cur.execute("INSERT INTO REPERTOIRE(numero,nom,prenom) VALUES(?,?,?)", data)
        conn.commit()
        cur.close()
        conn.close()
    except sqlite3.IntegrityError:
        print("Le numero (", num, ") que vous voulez ajouter est deja dans la base de données")


def supprimerContact(nom, prenom):
    """
    prend en parametre le nom et le prenom d'un contact et le supprime de la base de données
    """
    suppr = (nom, prenom)
    import sqlite3
    conn = sqlite3.connect('RepertoireTelephonique.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM REPERTOIRE WHERE nom = ? AND prenom = ?', suppr)
    conn.commit()
    cur.close()
    conn.close()


def modifierNumero(nouveau, num):
    """
    prend en parametre le nouveau numero et l'ancien numero
    d'un contact que vous voulez modifier dans la base de données
    "RepertoireTelephonique"
    """
    data = (nouveau, num)
    import sqlite3
    conn = sqlite3.connect('RepertoireTelephonique.db')
    cur = conn.cursor()
    cur.execute('UPDATE REPERTOIRE SET numero = ? WHERE numero = ?', data)
    conn.commit()
    cur.close()
    conn.close()


def afficherContact():
    """
    fonction qui renvoie tous les contacts enregistrés dans la base de données
    """
    import sqlite3
    conn = sqlite3.connect('RepertoireTelephonique.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM REPERTOIRE')
    conn.commit()
    # renvoie dans "liste" un tableau contenant le numero, nom et prenom
    # de tous les contacts
    liste = cur.fetchall()
    cur.close()
    conn.close()
    return liste


def afficher_un_contact(nom, prenom):
    data = (nom, prenom)
    import sqlite3
    conn = sqlite3.connect('RepertoireTelephonique.db')
    cur = conn.cursor()
    cur.execute('SELECT numero, nom, prenom FROM REPERTOIRE WHERE nom = ? AND prenom = ?', data)
    conn.commit()
    liste = cur.fetchall()
    cur.close()
    conn.close()
    return liste

# SERIE DE TESTS
# afficher_un_contact('toto','titi')
# supprimerContact('toto','tata')
# ajouterContact(555,'toto','tata')
# modifierNumero(333,222)
# print(afficherContact())
# creerRepertoire()
# ajouterContact(1,'B','Ilyes')
# ajouterContact(2,'B','Ilyes')
# ajouterContact(28,'B','Ilyes')

# PARTIE FLASK


from flask import Flask, render_template # importe flask et ses fonctions
from flask import request

app = Flask(__name__)


@app.route('/') # définit la première page que l'utilisateur voit
def index():
    return render_template("index.html") # ouvre la page html 'index'


@app.route('/ajouter') # formulaire pour ajouter un contact
def ajouter():
    return render_template("ajouter.html")


@app.route('/ajouter_resultat', methods=['POST']) # page vue après l'ajout du contact
def ajouter_resultat():
    creerRepertoire() # crée le repertoire REPERTOIRE avec les valeurs n, p, et t
    result = request.form
    n = result['nom']
    p = result['prenom']
    t = result['telephone']
    ajouterContact(t, n, p) # crée une rangée dans la table SQL avec ces informations
    return render_template("ajouter_resultat.html", nom=n, prenom=p, telephone=t) # affiche page confirmant l'ajout du contact


@app.route('/recherche') # formulaire pour rechercher un contact
def recherche():
    return render_template("recherche.html")


@app.route('/recherche_resultat', methods=['POST']) # résultat de la recherche
def recherche_resultat():
    result = request.form
    n = result['nom'] # prend le nom et le prenom donnée et crée des variables
    p = result['prenom']
    creerRepertoire() # crée le repertoire REPERTOIRE
    liste = afficher_un_contact(n, p) # crée la variable liste qui contient le nom et prénom mais aussi le numéro de téléphone
    return render_template("recherche_resultat.html", liste=liste)

@app.route('/supprimer') # formulaire pour supprimer un contact
def supprimer():
    return render_template("supprimer.html")


@app.route('/supprimer_resultat', methods=['POST']) # résultat de la suppression
def supprimer_resultat():
    result = request.form
    n = result['nom'] # prend le nom et le prenom donnée et crée des variables
    p = result['prenom']
    creerRepertoire() # crée le repertoire REPERTOIRE
    supprimerContact(n, p) # enlève le contact de la table SQL
    return render_template("supprimer_resultat.html", nom=n, prenom=p) # afficher page avec les variables nom et prenom

@app.route('/tutoriel') # formulaire pour voir le tutoriel
def tutoriel():
    return render_template("tutoriel.html")

@app.route('/annuaire') # affiche l'annuaire
def annuaire():
    import sqlite3 # définit la table
    conn = sqlite3.connect('RepertoireTelephonique.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM REPERTOIRE') # tout prendre de la table REPERTOIRE
    conn.commit()
    liste = cur.fetchall() # met tout dans la table dans la variable liste
    cur.close()
    conn.close()
    return render_template("annuaire.html",liste=liste) # affiche la page html

app.run(debug=True)
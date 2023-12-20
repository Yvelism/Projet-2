import sqlite3

#Connexion
connexion = sqlite3.connect('mybase.db')

#Récupération d'un curseur
c = connexion.cursor()

# ---- début des instructions SQL

#Création des tables
c.execute("""
    CREATE TABLE IF NOT EXISTS clients(
    id_client INT,
    prenom TEXT,
    nom TEXT,
    nb_enfant INT,
    nb_adulte INT,
    PRIMARY KEY(id_client));
    """)

c.execute("""
    CREATE TABLE IF NOT EXISTS logement(
    id_logement INT,
    id_ville INT,
    adresse TEXT,
    date DATE,
    services TEXT,
    type_chambre TEXT,
    PRIMARY KEY(id_logement));
    """)

c.execute("""
    CREATE TABLE IF NOT EXISTS lieu(
    id_ville INT,
    pays TEXT,
    ville TEXT,
    PRIMARY KEY(id_ville));
    """)

c.execute("""
    CREATE TABLE IF NOT EXISTS excursions(
    id_activite INT,
    id_ville INT,
    PRIMARY KEY(id_activite));
    """)

c.execute("""
    CREATE TABLE IF NOT EXISTS choix_activite(
    id_client INT,
    id_activite INT,
    date DATE,
    options TEXT,
    PRIMARY KEY(id_client));
    """)

c.execute("""
    CREATE TABLE IF NOT EXISTS commande(
    id_client INT,
    id_logement INT,
    date DATE,
    PRIMARY KEY(id_client, date));
    """)
# ---- fin des instructions SQL

#Validation
connexion.commit()


#Déconnexion
connexion.close()
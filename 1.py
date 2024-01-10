import sqlite3

#Connexion
connexion = sqlite3.connect('monagence.db')

#Récupération d'un curseur
c = connexion.cursor()

# ---- début des instructions SQL
#Création des tables

c.execute(""" CREATE TABLE IF NOT EXISTS client(id_client INT,prenom TEXT,nom TEXT,nb_enfant INT,nb_adulte INT,PRIMARY KEY(id_client));""")

c.execute("""
    CREATE TABLE IF NOT EXISTS logement(
    id_logement INT,
    id_ville INT,
    nom TEXT,
    PRIMARY KEY(id_logement));
    """)
#services TEXT,
#type_chambre TEXT,
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
    nom_act TEXT,
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
    id_ville INT,
    id_logement INT,
    date DATE,
    duree INT,
    PRIMARY KEY(id_client, date));
    """)


#c.execute('''INSERT INTO lieu VALUES (1, 'France', 'Paris')''')
#c.execute('''INSERT INTO lieu VALUES (2, 'Allemagne', 'Munich')''')
#c.execute('''INSERT INTO lieu VALUES (3, 'Italie', 'Rome')''')
#c.execute('''INSERT INTO lieu VALUES (4, 'Angleterre', 'Londre')''')
#c.execute('''INSERT INTO lieu VALUES (5, 'Maroc', 'Igoudman')''')
#c.execute('''INSERT INTO lieu VALUES (6, 'Maroc', 'Marrackech')''')
#c.execute('''INSERT INTO lieu VALUES (7, 'France', 'Nice')''')
#c.execute('''INSERT INTO lieu VALUES (8, 'Allemagne', 'Berlin')''')
#c.execute('''INSERT INTO lieu VALUES (9, 'Angleterre', 'Liverpool')''')
#c.execute('''INSERT INTO lieu VALUES (10, 'Suède', 'Stockholm')''')
#c.execute('''INSERT INTO lieu VALUES (11, 'Suède', 'Kiruna')''')
#c.execute('''INSERT INTO lieu VALUES (12, 'Slovenie', 'Ljubljana')''')
#c.execute('''INSERT INTO lieu VALUES (13, 'Slovenie', 'Piran')''')
#c.execute('''INSERT INTO lieu VALUES (14, 'Autriche', 'Vienne')''')
#c.execute('''INSERT INTO lieu VALUES (15, 'Emirats Arabes Unis', 'Dubai')''')
#c.execute('''INSERT INTO lieu VALUES (16, 'Emirats Arabes Unis', 'Abu Dabi')''')
#c.execute('''INSERT INTO lieu VALUES (17, 'Italie', 'Venise')''')


#c.execute('''INSERT INTO logement VALUES (20, 1, 'Hotel des champs elysee' )''')
#c.execute('''INSERT INTO logement VALUES (21, 7, 'Le Negresco' )''')
#c.execute('''INSERT INTO logement VALUES (22, 2, 'Hotel Vier Jahreszeiten Kempinski Munich' )''')
#c.execute('''INSERT INTO logement VALUES (23, 8, 'Hotel Adlon Kempinski Berlin' )''')
#c.execute('''INSERT INTO logement VALUES (24, 3, 'JK Place Roma' )''')
#c.execute('''INSERT INTO logement VALUES (25, 19, 'Bauer Palazzo' )''')
#c.execute('''INSERT INTO logement VALUES (26, 4, 'The Ritz London' )''')
#c.execute('''INSERT INTO logement VALUES (27, 9, 'Titanic Hotel Liverpool' )''')
#c.execute('''INSERT INTO logement VALUES (28, 6, 'Royal Mansour Marrakech' )''')
#c.execute('''INSERT INTO logement VALUES (29, 5, 'Palais Tadertino ' )''')
#c.execute('''INSERT INTO logement VALUES (30, 10, 'Grand Hôtel Stockholm' )''')
#c.execute('''INSERT INTO logement VALUES (31, 11, 'IceHotel ' )''')
#c.execute('''INSERT INTO logement VALUES (32, 12, 'InterContinental Ljubljana' )''')
#c.execute('''INSERT INTO logement VALUES (33, 13, 'Barbara Piran Beach Hotel' )''')
#c.execute('''INSERT INTO logement VALUES (34, 14, 'Hotel Sacher Wien' )''')
#c.execute('''INSERT INTO logement VALUES (35, 15, 'JW Marriott Marquis Hotel Dubai' )''')
#c.execute('''INSERT INTO logement VALUES (36, 16, 'St. Regis Abu Dhabi' )''')
#c.execute('''INSERT INTO logement VALUES (37, 17, 'Grand Hôtel Stockholm' )''')
#c.execute('''INSERT INTO logement VALUES (38, 18, 'Hotel Garden' )''')

# Paris, France
#c.execute('''INSERT INTO excursions VALUES (1, "Tour Eiffel", 1)''')
#c.execute('''INSERT INTO excursions VALUES (2, "Musée du Louvre", 1)''')
#c.execute('''INSERT INTO excursions VALUES (3, "Croisière sur la Seine", 1)''')

# Nice, France
#c.execute('''INSERT INTO excursions VALUES (4, "Pronemade des Anglais", 7)''')
#c.execute('''INSERT INTO excursions VALUES (5, "Vieux Nice", 7)''')
#c.execute('''INSERT INTO excursions VALUES (6, "Musée d'art moderne et d'art contemporain ", 7)''')
#c.execute('''INSERT INTO excursions VALUES (7, "Parc de la Colline du Château ", 7)''')

#Munich, Allemagne
#c.execute('''INSERT INTO excursions VALUES (8, "Marienplatz ", 2)''')
#c.execute('''INSERT INTO excursions VALUES (9, "Hofbräuhaus", 2)''')
#c.execute('''INSERT INTO excursions VALUES (10, "Deutsches Museum", 2)''')

# Berlin, Allemagne
#c.execute('''INSERT INTO excursions VALUES (11, "Mur de Berlin et East Side Gallery", 8)''')
#c.execute('''INSERT INTO excursions VALUES (12, "Porte de Brandebourg", 8)''')
#c.execute('''INSERT INTO excursions VALUES (13, "Mémorial de l'Holocauste", 8)''')

# Rome, Italie
#c.execute('''INSERT INTO excursions VALUES (14, "Colisée", 3)''')
#c.execute('''INSERT INTO excursions VALUES (15, "Basilique Saint-Pierre et la Cité du Vatican", 3)''')
#c.execute('''INSERT INTO excursions VALUES (16, "Fontaine de Trevi", 3)''')


# Venise, Italie
#c.execute('''INSERT INTO excursions VALUES (17, "Place Saint-Marc", 17)''')
#c.execute('''INSERT INTO excursions VALUES (18, "Basilique Saint-Marc", 17)''')
#c.execute('''INSERT INTO excursions VALUES (19, "Balade en gondole", 17)''')

# Londres, Angleterre
#c.execute('''INSERT INTO excursions VALUES (20, "Le British Museum", 4)''')
#c.execute('''INSERT INTO excursions VALUES (21, "La Tour de Londres", 4)''')
#c.execute('''INSERT INTO excursions VALUES (22, "Le London Eye ", 4)''')

# Liverpool, Angleterre
#c.execute('''INSERT INTO excursions VALUES (23, "Albert Dock", 9)''')
#c.execute('''INSERT INTO excursions VALUES (24, "The Beatles Story", 9)''')
#c.execute('''INSERT INTO excursions VALUES (25, "Cathédrale métropolitaine de Liverpool", 9)''')

# Marrakech, Maroc
#c.execute('''INSERT INTO excursions VALUES (25, "Place Jemaa el-Fna", 6)''')
#c.execute('''INSERT INTO excursions VALUES (26, "Médina de Marrakech", 6)''')
#c.execute('''INSERT INTO excursions VALUES (27, "Jardin Majorelle", 6)''')

# Igoudman, Maroc
#c.execute('''INSERT INTO excursions VALUES (28, "Exploration des dunes de sable", 5)''')
#c.execute('''INSERT INTO excursions VALUES (29, "Observation des étoiles dans le désert", 5)''')
#c.execute('''INSERT INTO excursions VALUES (30, "Rencontre avec les habitants nomades", 5)''')

# Stochkolm, Suède
#c.execute('''INSERT INTO excursions VALUES (31, "Gamla Stan", 10)''')
#c.execute('''INSERT INTO excursions VALUES (32, "Musée Vasa", 10)''')
#c.execute('''INSERT INTO excursions VALUES (33, "Palais Royal de Stockholm", 10)''')

# Kiruna, Suède
#c.execute('''INSERT INTO excursions VALUES (34, "Observation des aurores boréales", 11)''')
#c.execute('''INSERT INTO excursions VALUES (35, "Visite de la mine de fer de Kiruna", 11)''')
#c.execute('''INSERT INTO excursions VALUES (36, "Randonnée autour du lac Luossajärvi", 11)''')

# Ljubljana, Slovenie
#c.execute('''INSERT INTO excursions VALUES (37, "Château de Ljubljana", 12)''')
#c.execute('''INSERT INTO excursions VALUES (38, "Marché central de Ljubljana", 12)''')
#c.execute('''INSERT INTO excursions VALUES (39, "Balade le long de la rivière Ljubljanica", 12)''')

# Piran, Slovenie
#c.execute('''INSERT INTO excursions VALUES (40, "Vieille ville de Piran", 13)''')
#c.execute('''INSERT INTO excursions VALUES (41, "Muraille de Piran", 13)''')
#c.execute('''INSERT INTO excursions VALUES (42, "Promenade le long de la côte", 13)''')

# Vienne, Autriche
#c.execute('''INSERT INTO excursions VALUES (43, "Palais de Schönbrunn", 14)''')
#c.execute('''INSERT INTO excursions VALUES (44, "Cathédrale Saint-Étienne", 14)''')
#c.execute('''INSERT INTO excursions VALUES (45, "Musée d'Histoire de l'Art", 14)''')

# Dubai, Emirats Arab unis
#c.execute('''INSERT INTO excursions VALUES (46, "Souk de l'or", 15)''')
#c.execute('''INSERT INTO excursions VALUES (47, "Ski Dubai Mall of the Emirates", 15)''')
#c.execute('''INSERT INTO excursions VALUES (48, "Dubai Opera", 15)''')

# Abu dabi, Emirats Arab unis
#c.execute('''INSERT INTO excursions VALUES (49, "Corniche d'Abu Dabi", 16)''')
#c.execute('''INSERT INTO excursions VALUES (50, "Qasr Al Watan", 16)''')
#c.execute('''INSERT INTO excursions VALUES (51, "Mangrove National Park", 16)''')


def repertoire_client():
    # Insertion si le compte n'existe pas déjà
    c.execute(""" CREATE TABLE IF NOT EXISTS client(id_client INT,prenom TEXT,nom TEXT,nb_enfant INT,nb_adulte INT,PRIMARY KEY(id_client));""")        
    print("Nouvel utilisateur ajouté avec succès!")
        
def creer_compte(nom,prenom,nb_enfants,nb_adultes):
    newclient = (nom,prenom, nb_enfants,nb_adultes)
    # Vérification si l'utilisateur existe déjà
    try:
        c.execute("SELECT * FROM client WHERE (nom, prenom, nb_enfant, nb_adulte)=(?,?,?,?)", newclient)
    except sqlite3.IntegrityError:
        print("Le compte (", nom, ") que vous voulez ajouter est deja dans la base de données")

'''def destination():
    c.execute("SELECT * FROM lieu")
    destinations = c.fetchall()
    for destination in destinations:
        print(f"ID: {destination[0]}, Pays: {destination[1]}, Ville: {destination[2]}")

    ville= input("Quelle ville choisissez-vous?")
    for destination in destinations:
        if destination[2]==ville:
            idv=destination[0]
    c.execute("SELECT * FROM logement")
    logement=c.fetchall()
    l=[] 
    print("Voici la liste des Hôtels disponibles à", ville)
    for logement in logement :
        if logement[1]==idv :
            print(f"IDlog: {logement[0]}, IDville: {logement[1]}, Nom: {logement[2]}")  
                
def supprimer(ville,client):
    p = "DELETE FROM commande WHERE id_client = '" + client + "' AND date = '"+ commandesupp + "' "
    c.executescript(p)
    print("Vous avez supprimé votre voyage à ", ville, "de la base de données")
def excursion(lieu,ville):
    lieu= input("Dans quelle ville ?")
    ville= input("ID de cette ville ?")
    c.execute("SELECT * FROM excursions WHERE id_ville=?",(ville)) 
    res= c.fetchall()
    print("Vous consultez les excursions disponibles à ",lieu, " :")
    for res in res:
        print(f"IDactivité: {res[0]}, Nom: {res[1]}, IDville: {res[2]}")
def ajout_voyage(id_client,ville,logement,date,duree):
    id_client = input('Votre identifiant client ? ')
    ville = input('Id de la Ville ? ')
    logement= input('ID du logement ?')
    date = input('A quelle date ?(AAAA-MM-JJ) ')
    duree = input('Pour combien de temps ?')
    p = "INSERT INTO commande VALUES ('" + id_client + "','" + ville + "','" +logement +"','" + date + "','" + duree + "')"
    c.executescript(p)
    print("Vous avez ajouté un voyage à votre commande")
def commande():
    c.execute("SELECT * FROM commande")
    tab = c.fetchall()
    for ligne in tab:
        print(f"IDclient:{ligne[0]}, IDville:{ligne[1]}, IDlogement:{ligne[2]}, Date:{ligne[3]}, Duree:{ligne[4]}")
    '''        


# ---- fin des instructions SQL

#Validation
connexion.commit()


#Déconnexion
connexion.close()


##PARTIE FLASK 
from flask import Flask, render_template # importe flask et ses fonctions
from flask import request

app = Flask(__name__) #Création d'une instance de l'application Flask,
#avec __name__ utilisé pour définir le point de démarrage de l'application

@app.route('/')# définit la première page que l'utilisateur voit
def index():
    return render_template('index.html') # ouvre la page html 'interface'

if __name__ == '__main__': #vérifie si le script est exécuté directement 
    #(plutôt que d'être importé en tant que module).
    app.run(debug=True) # il lance l'application Flask en mode débogagennb 

@app.route('/creer_compte') # formulaire pour ajouter un compte client
def creer_compte():
    return render_template("creer_compte.html")
    
@app.route('/compte_ajoute', methods=['POST'])
def compte_ajoute():
    repertoire_client()
    nom = request.form.get('nom')
    prenom = request.form.get('prenom')
    nb_enfants = request.form.get('nb_enfants')
    nb_adultes = request.form.get('nb_adultes')
    # Insére le compte client dans la base de données SQLite
    creer_compte(nb_adultes,nb_enfants, nom, prenom) # crée une rangée dans la table SQL avec ces informations
    return render_template("compte_ajoute.html", nom, prenom, nb_adultes)
app.run(debug=True)
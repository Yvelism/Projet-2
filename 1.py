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
    id_ville INT
    id_logement INT,
    date DATE,
    duree INT,
    PRIMARY KEY(id_client, date));
    """)


#c.execute('''INSERT INTO lieu VALUES (1, 'France', 'Paris')''')
#c.execute('''INSERT INTO lieu VALUES (2, 'Allemagne', 'Munich')''')
#c.execute('''INSERT INTO lieu VALUES (3, 'Italie', 'Rome')''')
#c.execute('''INSERT INTO lieu VALUES (4, 'Angleterre', 'Londre')''')
#c.execute('''INSERT INTO logement VALUES (20, 1, 'Hotel des champs elysee' )''')
#c.execute('''INSERT INTO lieu VALUES (5, 'Maroc', 'Igoudman')''')
#c.execute('''INSERT INTO lieu VALUES (6, 'Maroc', 'Marrackech')''')
#c.execute('''INSERT INTO lieu VALUES (7, 'France', 'Nice')''')
#c.execute('''INSERT INTO lieu VALUES (8, 'Allemagne', 'Berlin')''')
#c.execute('''INSERT INTO lieu VALUES (9, 'Angleterre', 'Liverpool')''')
#c.execute('''INSERT INTO lieu VALUES (10, 'Suède', 'Stockholm')''')
#c.execute('''INSERT INTO lieu VALUES (11, 'Suède', 'Kiruna')''')
#c.execute('''INSERT INTO lieu VALUES (12, 'Slovenie', 'Ljublijana')''')
#c.execute('''INSERT INTO lieu VALUES (13, 'Slovenie', 'Piran')''')
#c.execute('''INSERT INTO lieu VALUES (14, 'Autriche', 'Vienne')''')
#c.execute('''INSERT INTO lieu VALUES (15, 'Emirats Arabes Unis', 'Dubai')''')
#c.execute('''INSERT INTO lieu VALUES (16, 'Emirats Arabes Unis', 'Abou Dabi')''')
#c.execute('''INSERT INTO lieu VALUES (17, 'Suède', 'Stockholm')''')
#c.execute('''INSERT INTO lieu VALUES (18, 'Suède', 'Malmö')''')
c.execute('''INSERT INTO lieu VALUES (19, 'Italie', 'Venise')''')
mettez vos villes /villages 

#c.execute('''INSERT INTO logement VALUES (20, 1, 'Hotel des champs elysee' )''')
c.execute('''INSERT INTO logement VALUES (21, 7, 'Le Negresco' )''')
c.execute('''INSERT INTO logement VALUES (22, 2, 'Hotel Vier Jahreszeiten Kempinski Munich' )''')
c.execute('''INSERT INTO logement VALUES (23, 8, 'Hotel Adlon Kempinski Berlin' )''')
c.execute('''INSERT INTO logement VALUES (24, 3, 'JK Place Roma' )''')
c.execute('''INSERT INTO logement VALUES (25, 19, 'Bauer Palazzo' )''')
c.execute('''INSERT INTO logement VALUES (26, 4, 'The Ritz London' )''')
c.execute('''INSERT INTO logement VALUES (27, 9, 'Titanic Hotel Liverpool' )''')
c.execute('''INSERT INTO logement VALUES (28, 5, 'Royal Mansour Marrakech' )''')
c.execute('''INSERT INTO logement VALUES (29, 6, 'Palais Tadertino ' )''')
c.execute('''INSERT INTO logement VALUES (30, 10, 'Grand Hôtel Stockholm' )''')
c.execute('''INSERT INTO logement VALUES (31, 11, 'IceHotel ' )''')
c.execute('''INSERT INTO logement VALUES (32, 12, 'InterContinental Ljubljana' )''')
c.execute('''INSERT INTO logement VALUES (33, 13, 'Barbara Piran Beach Hotel' )''')
c.execute('''INSERT INTO logement VALUES (34, 14, 'Hotel Sacher Wien' )''')
c.execute('''INSERT INTO logement VALUES (35, 15, 'JW Marriott Marquis Hotel Dubai' )''')
c.execute('''INSERT INTO logement VALUES (36, 16, 'St. Regis Abu Dhabi' )''')
c.execute('''INSERT INTO logement VALUES (37, 17, 'Grand Hôtel Stockholm' )''')
c.execute('''INSERT INTO logement VALUES (38, 18, 'Hotel Garden' )''')

continuer = True

while continuer :
    print("Bonjour, Que voulez-vous faire ?")
    print("1. Choisir une destination")
    print("2. Consulter la liste des destinations")
    print("3. Supprimer une selection")
    print("4. Choisir une excursion")
    print("5. Selectionner un hotel")
    print("6. Consulter votre commande")
    print("7. Quitter")
    choix = int(input("Votre choix :"))

    if choix == 1:
        id_client = input('Votre identifiant client ? ')
        ville1 = input('Ville ? ')
        ville2= str(c.executescript("SELECT id_ville FROM lieu WHERE ville LIKE ' "+ ville1 +"'"))
        #logement1= input('Quel logement ?')
        #logement2= c.executescript("SELECT id_logement FROM logement WHERE nom LIKE ' "+ logement1 +"'")
        date = input('A quelle date ? ')
        duree = input('pour combien de temps ?')
        p = "INSERT INTO commande VALUES ('" + id_client + "','" + ville2 + "','" +"logement" +"','" + date + "','" + duree + "')"
        c.executescript(p)
        print("Vous avez ajouté un voyage à", ville1,"à votre commande")

    elif choix == 2 :
        nom = input('Nom ? ')
        prenom = input('Prénom ? ')
        note = input('Note ? ')
        p = "UPDATE bulletin SET note = " + note + " WHERE prenom = '"+ prenom + "' AND " + "nom = '"+ nom+ "'"
        c.executescript(p)
        print("Vous avez changé la note de ", nom, prenom,"en", note)

    elif choix == 3 :
        nom = input('Nom ? ')
        prenom = input('Prénom ? ')
        p = "DELETE FROM bulletin WHERE nom = '" + nom + "' AND prenom = '"+ prenom + "' "
        c.executescript(p)
        print("Vous avez supprimé ", nom, prenom,"de la base de données")

    elif choix == 4 :
        c.execute("SELECT MAX(note), prenom , nom FROM bulletin")
        res= c.fetchall()
        print("L'élève ayant la meilleure note est", res[0][1],res[0][2],"avec la note", res[0][0])

    elif choix == 5 :
        c.execute("SELECT MIN(note), prenom , nom FROM bulletin")
        res= c.fetchall()
        print("L'élève ayant la moins bonne note est", res[0][1],res[0][2],"avec la note", res[0][0])

    elif choix == 6:
        c.execute("SELECT prenom , nom, note FROM bulletin")
        tab = c.fetchall()
        for element in tab:
            print(element[0],"|",element[1],"|",element[2])


    elif choix == 7:
        print("Merci d'avoir utilisé l'application de notes")
        continuer = False

    else:
        print("Votre choix doit être compris entre 1 et 7")


# ---- fin des instructions SQL

#Validation
connexion.commit()


#Déconnexion
connexion.close()

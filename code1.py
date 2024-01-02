import sqlite3

#Connexion
connexion = sqlite3.connect('mybase.db')

#Récupération d'un curseur
c = connexion.cursor()

# ---- début des instructions SQL

#Création des tables
c.execute("""
    CREATE TABLE IF NOT EXISTS client(
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
#c.execute('''INSERT INTO lieu VALUES (5, 'Maroc', 'Igoudman')''')
#c.execute('''INSERT INTO lieu VALUES (6, 'Maroc', 'Marrackech')''')
#c.execute('''INSERT INTO lieu VALUES (7, 'France', 'Nice')''')
#c.execute('''INSERT INTO lieu VALUES (8, 'Allemagne', 'Berlin')''')
#c.execute('''INSERT INTO lieu VALUES (9, 'Angleterre', 'Liverpool')''')
#c.execute('''INSERT INTO lieu VALUES (10, 'Suède', 'Stockholm')''')#
#c.execute('''INSERT INTO lieu VALUES (11, 'Suède', 'Kiruna')''')
#c.execute('''INSERT INTO lieu VALUES (12, 'Slovenie', 'Ljublijana')''')
#c.execute('''INSERT INTO lieu VALUES (13, 'Slovenie', 'Piran')''')
#c.execute('''INSERT INTO lieu VALUES (14, 'Autriche', 'Vienne')''')
#c.execute('''INSERT INTO lieu VALUES (15, 'Emirats Arabes Unis', 'Dubai')''')
#c.execute('''INSERT INTO lieu VALUES (16, 'Emirats Arabes Unis', 'Abou Dabi')''')
#c.execute('''INSERT INTO lieu VALUES (17, 'Italie', 'Venise')''')


#c.execute('''INSERT INTO logement VALUES (20, 1, 'Hotel des champs elysee' )''')
#c.execute('''INSERT INTO logement VALUES (21, 7, 'Le Negresco' )''')
#c.execute('''INSERT INTO logement VALUES (22, 2, 'Hotel Vier Jahreszeiten Kempinski Munich' )''')
#c.execute('''INSERT INTO logement VALUES (23, 8, 'Hotel Adlon Kempinski Berlin' )''')
#c.execute('''INSERT INTO logement VALUES (24, 3, 'JK Place Roma' )''')
#c.execute('''INSERT INTO logement VALUES (25, 19, 'Bauer Palazzo' )''')
#c.execute('''INSERT INTO logement VALUES (26, 4, 'The Ritz London' )''')
#c.execute('''INSERT INTO logement VALUES (27, 9, 'Titanic Hotel Liverpool' )''')
#c.execute('''INSERT INTO logement VALUES (28, 5, 'Royal Mansour Marrakech' )''')
#c.execute('''INSERT INTO logement VALUES (29, 6, 'Palais Tadertino ' )''')
#c.execute('''INSERT INTO logement VALUES (30, 10, 'Grand Hôtel Stockholm' )''')
#c.execute('''INSERT INTO logement VALUES (31, 11, 'IceHotel ' )''')
#c.execute('''INSERT INTO logement VALUES (32, 12, 'InterContinental Ljubljana' )''')
#c.execute('''INSERT INTO logement VALUES (33, 13, 'Barbara Piran Beach Hotel' )''')
#c.execute('''INSERT INTO logement VALUES (34, 14, 'Hotel Sacher Wien' )''')
#c.execute('''INSERT INTO logement VALUES (35, 15, 'JW Marriott Marquis Hotel Dubai' )''')
#c.execute('''INSERT INTO logement VALUES (36, 16, 'St. Regis Abu Dhabi' )''')
#c.execute('''INSERT INTO logement VALUES (37, 17, 'Grand Hôtel Stockholm' )''')
#c.execute('''INSERT INTO logement VALUES (38, 18, 'Hotel Garden' )''')

continuer = True

while continuer :
    print("Bonjour, Que voulez-vous faire ?")
    print("1. Créer un compte client")
    print("2. Consulter la liste des destinations et des hôtels")
    print("3. Supprimer une selection")
    print("4. Choisir une excursion")
    print("5. Chosir un voyage")
    print("6. Consulter les commandes")
    print("7. Quitter")
    choix = int(input("Votre choix :"))

    if choix ==1:
        nom = input('Nom ? ')
        prenom = input('Prénom ? ')
        nb_enfants = input('Pour combien denfants ? ')
        nb_adultes = input('Pour combien dadultes ? ')
        newclient = (nom,prenom, nb_enfants,nb_adultes)
        # Vérification si l'utilisateur existe déjà
        c.execute("SELECT * FROM client WHERE (nom, prenom, nb_enfant, nb_adulte)=(?, ?,?,?)", newclient)
        existe_deja = c.fetchone()

        if not existe_deja:
            # Insertion si le compte n'existe pas déjà
            c.execute("INSERT INTO client (nom, prenom, nb_enfant, nb_adulte) VALUES (?, ?,?,?)", newclient)
            print("Nouvel utilisateur ajouté avec succès!")
        else:
            print("L'utilisateur existe déjà.")

    elif choix == 2 :
        c.executescript("SELECT * FROM lieu")
        l=c.fetchall
        print(l)
        ville= input("Quelle ville choisissez-vous?")
        cville=c.executescript("SELECT id_ville FROM lieu WHERE ville LIKE '"+ville+"'")
        p = "SELECT * FROM logement WHERE id_ville = 'cville'"
        c.executescript(p)
        print("Voici la liste des Hotels disponibles à", ville)

    elif choix == 3 :
        client = input('Quel est votre identifiant client ? ')
        ville = input("Quelle est la destination du voyage que vous souhaitez supprimer ?")
        commandesupp = input('Quelle est la date du voyage que vous souhaitez supprimer ? ')
        p = "DELETE FROM commande WHERE id_client = '" + client + "' AND date = '"+ commandesupp + "' "
        c.executescript(p)
        print("Vous avez supprimé votre voyage à ", ville, "de la base de données")

    elif choix == 4 :
        ville= input("Dans quelle ville ?")
        cville=c.executescript("SELECT id_ville FROM lieu WHERE ville LIKE '"+ville+"'")
        c.execute("SELECT * FROM excursions WHERE id_ville="+cville+'"') 
        res= c.fetchall()
        print("Vous consultez les excursions disponibles à", ville,":", res)

    elif choix == 5:
            id_client = input('Votre identifiant client ? ')
            ville1 = input('Ville ? ')
            c.executescript("SELECT id_ville FROM lieu WHERE ville LIKE ' "+ ville1 +"'")
            ville2= input('Code de cette ville ?')
            logement1= input('Quel logement ?')
            c.executescript("SELECT id_logement FROM logement WHERE nom LIKE ' "+ logement1 +"'")
            logement2= input("Code du logement?")
            date = input('A quelle date ?(AAAA-MM-JJ) ')
            duree = input('Pour combien de temps ?')
            p = "INSERT INTO commande VALUES ('" + id_client + "','" + ville2 + "','" +"logement" +"','" + date + "','" + duree + "')"
            c.executescript(p)
            print("Vous avez ajouté un voyage à", ville1,"à votre commande")

    elif choix == 6:
        c.execute("SELECT * FROM commande")
        tab = c.fetchall()
        print(tab)


    elif choix == 7:
        print("Merci d'avoir utilisé notre agence de voyage")
        continuer = False

    else:
        print("Votre choix doit être compris entre 1 et 7")


# ---- fin des instructions SQL

#Validation
connexion.commit()


#Déconnexion
connexion.close()

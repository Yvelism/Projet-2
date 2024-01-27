<!doctype html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <title>Voici les excursions a votre nom</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css2.css') }}">
</head>
<header>
  <h2>Voici les excursions a votre nom</h2>
</header>

<section>
    <nav>
        <form action="{{ url_for('creer_compte') }}">
            <input type="submit" value="Créer un compte client" />
        </form>
        <form action="{{ url_for('affichedestinations') }}">
            <input type="submit" value="Consulter les destinations " />
        </form>
        <form action="{{ url_for('afficheExcursion') }}">
            <input type="submit" value="Consulter les excursions " />
        </form>
        <form action="{{ url_for('affichelogement') }}">
            <input type="submit" value="Consulter les Hotels " />
        </form>
        <form action="{{ url_for('ajoutvoyage') }}">
            <input type="submit" value="Ajouter un voyage " />
        </form>
        <form action="{{ url_for('ajoutExcursion') }}">
            <input type="submit" value="Ajouter une excursion au voyage" />
        </form>
        <form action="{{ url_for('consultervoyage') }}">
            <input type="submit" value="Consulter les voyages à votre nom" />
        </form>
        <form action="{{ url_for('consulterExcursion') }}">
            <input type="submit" value="Consulter les exursions à votre nom" />
        </form>
        <form action="{{ url_for('supprimer') }}">
            <input type="submit" value="Supprimer un voyage" />
        </form>
        <form action="{{ url_for('supprimerCompte') }}">
            <input type="submit" value="Supprimer votre compte client" />
        </form>
    </nav>
    <article>
    <?php

        // Connexion à la base de données
        $chemin_absolu = realpath('monagence.db');
        $db = new PDO('sqlite:' . $chemin_absolu);
        // Requête SQL pour récupérer les données
        $query = $db->query('SELECT * FROM excursions WHERE id_client = :(id_client)');
        $data = $query->fetchAll(PDO::FETCH_ASSOC);
    ?>

    <table>
        <tr>
            <th>id_activite</th>
            <th>nom_activite</th>
            <th>id_ville</th>
        </tr>
        
    <?php foreach ($data as $row): ?>
        <tr>
            <td><?php echo $row['id_activite']; ?></td>
            <td><?php echo $row['nom_act']; ?></td>
            <td><?php echo $row['nom_act']; ?></td>
        </tr>
    <?php endforeach; ?>
        </table>
    
    <a href="{{ url_for('index') }}"> <button class="btn">Retour</button></a>
    </article>
</section>
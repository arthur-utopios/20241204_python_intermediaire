SELECT
	prenom,
	nom
FROM
	artiste;
	
SELECT * FROM artiste;

SELECT prenom, artiste_id, nom, date_naissance FROM artiste;

SELECT
	prenom AS p,
	nom n
FROM 
	artiste;
	
SELECT
	prenom,
	nom
FROM
	artiste
WHERE
	prenom = 'John';
	
SELECT
	prenom,
	nom,
	date_naissance
FROM
	artiste
WHERE
	LENGTH(nom) > 5
	AND
	date_naissance > '1960-01-01';
	
SELECT
	titre, 
	date_sortie
FROM
	disque
WHERE
	titre LIKE '%er%'
	
SELECT
	DISTINCT prenom, nom
FROM
	artiste;
	
-- Opérateur IN
SELECT
	artiste_id, prenom, nom
FROM
	artiste
WHERE
	artiste_id IN 
	(SELECT 
		artiste_id 
	FROM 
		groupe_artiste 
	WHERE 
		groupe_id = (SELECT groupe_id FROM groupe WHERE nom = 'Nirvana'))
		
SELECT
	*
FROM
	artiste AS a
JOIN
	groupe_artiste AS ga ON a.artiste_id = ga.artiste_id
JOIN
	groupe AS g ON ga.groupe_id = g.groupe_id;

SELECT
	a.prenom, a.nom
FROM
	groupe_artiste AS ga
JOIN
	artiste AS a ON a.artiste_id = ga.artiste_id
JOIN
	groupe AS g ON ga.groupe_id = g.groupe_id;



SHOW COLUMNS FROM disque;	

SELECT
	titre, date_sortie
FROM
	disque
WHERE
	date_sortie BETWEEN '1960-01-01' AND '1991-09-24';
	
SELECT
	titre, date_sortie
FROM
	disque
WHERE
	date_sortie BETWEEN '1960-01-01' AND '1991-09-24'
ORDER BY
	date_sortie;
	
SELECT
	titre, date_sortie
FROM
	disque
WHERE
	date_sortie BETWEEN '1960-01-01' AND '1991-09-24'
ORDER BY
	date_sortie DESC;
	
SELECT
	prenom,
	nom
FROM
	artiste
ORDER BY
	prenom,
	nom DESC;
	
-- Durée des albums par rapport au disque
SELECT
	d.titre AS disque,
	SUM(s.duree) AS duree_disque
FROM
	disque AS d
JOIN
	single_disque ON single_disque.disque_id = d.disque_id
JOIN
	single AS s ON single_disque.single_id = s.single_id
-- permet de regrouper la somme des durées de single par disque	
GROUP BY
	d.titre
-- filtre après regroupement
HAVING
	SUM(s.duree) > 800
ORDER BY
	duree_disque DESC;
	
SELECT
	titre,
	duree
FROM
	single
ORDER BY
	duree DESC
LIMIT
	3;

-- On peut gérer le décalage en le précisant avant la limite
SELECT
	titre,
	duree
FROM
	single
ORDER BY
	duree DESC
LIMIT
	3, 1;

SELECT
	g.nom AS groupe,
	d.titre AS album,
	s.titre AS single,
	s.duree
FROM
	single AS s
JOIN
	single_disque ON single_disque.single_id = s.single_id
JOIN
	disque AS d ON single_disque.disque_id = d.disque_id
JOIN
	groupe AS g ON d.groupe_id = g.groupe_id
ORDER BY
	g.nom,
	d.titre,
	s.titre;
	
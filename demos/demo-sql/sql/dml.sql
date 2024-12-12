-- Ajouter des enregistrements en base de données
INSERT INTO
	artiste
	(prenom, nom, date_naissance)
VALUES
	('Paul', 'McCartney', NULL);
	
INSERT INTO
	artiste
	(prenom, nom, date_naissance)
VALUES
	('John', 'Lenon', '1940-10-09'),
	('George', 'Harisson', '1943-02-25'),
	('Ringo', 'Starr', '1940-07-07');

DELETE FROM
	artiste
WHERE
	artiste_id = 4;

UPDATE
	artiste
SET
	date_naissance = '1942-06-18'
WHERE
	artiste_id = 1;

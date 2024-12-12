BEGIN;

-- Je créé le label pour mon groupe
INSERT INTO
	label
	(nom, date_creation)
VALUES
	('Domino Recording Company', '1993-02-24');

SELECT * FROM label;

-- Récupération du dernier ID généré par la fonction d'AUTO_INCREMENT
SELECT LAST_INSERT_ID();

-- Création du nouveau groupe avec l'ID du label créé précédemment
INSERT
	groupe
	(nom, date_creation, label_id)
VALUES
	('Arctic Monkeys', '2002-06-12', LAST_INSERT_ID());

SELECT * FROM groupe;

-- Valider la transaction
COMMIT;

-- Annuler la transaction
ROLLBACK;

BEGIN;
SELECT * FROM label;

INSERT INTO
	label
	(nom)
VALUES
	('Virgin Records');
	
SELECT * FROM label;

INSERT INTO
	groupe
	(nom, date_creation, label_id)
VALUES
	('Massive Attack', '1988-10-14', LAST_INSERT_ID())

ROLLBACK;

SELECT * FROM groupe;
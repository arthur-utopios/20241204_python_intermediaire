-- Création d'une base de données en définissant son encodage
CREATE DATABASE IF NOT EXISTS
	demo_rock
	CHARACTER SET utf8mb4
	COLLATE utf8mb4_general_ci;

-- Se déplacer sur la base de données
USE demo_rock;

-- Création d'une table avec toutes ses colonnes et ses contraintes
CREATE TABLE label(
	label_id INT PRIMARY KEY AUTO_INCREMENT,
	nom VARCHAR(50) NOT NULL,
	date_creation DATETIME DEFAULT NOW()
);

-- Afficher toutes les tables de la base de données
SHOW TABLES;

-- Afficher le détail des colonnes d'une table
SHOW COLUMNS FROM label;

CREATE TABLE single(
	single_id INT PRIMARY KEY AUTO_INCREMENT,
	titre VARCHAR(255) NOT NULL,
	duree INT NOT NULL
);

CREATE TABLE artiste(
	artiste_id INT PRIMARY KEY AUTO_INCREMENT,
	prenom VARCHAR(50) NOT NULL,
	nom VARCHAR(50) NOT NULL,
	date_naissance DATETIME
);

-- Permet de renommer un objet de la base de données
-- RENAME TABLE artist TO artiste;

-- alternative, supprimer et recréer
-- DROP TABLE artiste;

CREATE TABLE groupe(
	groupe_id INT PRIMARY KEY AUTO_INCREMENT,
	nom VARCHAR(100) NOT NULL,
	date_creation DATE NOT NULL
);

-- Ajout d'une colonne après la création de la table
ALTER TABLE groupe
	ADD COLUMN label_id INT NOT NULL,
	-- 1. On donne un nom à notre contrainte: ici fk_label_id
	-- 2. On précise la colonne qui va accueillir la clé étrangère
	-- 3. On lui dit à quelle clé primaire de quelle table elle fait référence
	ADD CONSTRAINT fk_label_id FOREIGN KEY(label_id) REFERENCES label(label_id);

CREATE TABLE disque(
	disque_id INT PRIMARY KEY AUTO_INCREMENT,
	titre VARCHAR(200) NOT NULL,
	date_sortie DATE NOT NULL,
	groupe_id INT NOT NULL,
	CONSTRAINT fk_groupe_id FOREIGN KEY(groupe_id) REFERENCES groupe(groupe_id)
);

CREATE TABLE single_disque(
	disque_id INT NOT NULL,
	single_id INT NOT NULL,
	PRIMARY KEY(disque_id, single_id),
	CONSTRAINT fk_disque_id FOREIGN KEY(disque_id) REFERENCES disque(disque_id),
	CONSTRAINT fk_single_id FOREIGN KEY(single_id) REFERENCES single(single_id)
);

-- Autre syntaxe, mais moins recommandée
CREATE TABLE groupe_artiste(
	groupe_artiste_id INT PRIMARY KEY AUTO_INCREMENT,
	groupe_id INT NOT NULL,
	artiste_id INT NOT NULL,
	-- Les foreign key doivent avoir un nom unique par rapport à la base de données
	CONSTRAINT fk_groupe_artiste_groupe_id FOREIGN KEY(groupe_id) REFERENCES groupe(groupe_id),
	CONSTRAINT fk_groupe_artiste_artiste_id FOREIGN KEY(artiste_id) REFERENCES artiste(artiste_id)
);


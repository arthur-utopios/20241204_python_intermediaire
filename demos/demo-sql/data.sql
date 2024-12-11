USE demo_rock;

-- Insertion dans la table label
INSERT INTO label (nom) VALUES 
('Atlantic Records'), 
('Capitol Records'), 
('Columbia Records'), 
('Island Records'), 
('Warner Bros. Records');

-- Insertion dans la table single
INSERT INTO single (titre, duree) VALUES 
('Bohemian Rhapsody', 354), 
('Stairway to Heaven', 482), 
('Hotel California', 390), 
('Imagine', 183), 
('Smells Like Teen Spirit', 301);

-- Insertion dans la table artiste
INSERT INTO artiste (prenom, nom, date_naissance) VALUES 
('Freddie', 'Mercury', '1946-09-05'), 
('Robert', 'Plant', '1948-08-20'), 
('Don', 'Henley', '1947-07-22'), 
('John', 'Lennon', '1940-10-09'), 
('Kurt', 'Cobain', '1967-02-20');

-- Insertion dans la table groupe
INSERT INTO groupe (nom, date_creation, label_id) VALUES 
('Queen', '1970-01-01', 1), 
('Led Zeppelin', '1968-01-01', 2), 
('Eagles', '1971-01-01', 3), 
('The Beatles', '1960-01-01', 4), 
('Nirvana', '1987-01-01', 5);

-- Insertion dans la table disque
INSERT INTO disque (titre, date_sortie, groupe_id) VALUES 
('A Night at the Opera', '1975-11-21', 1), 
('Led Zeppelin IV', '1971-11-08', 2), 
('Hotel California', '1976-12-08', 3), 
('Abbey Road', '1969-09-26', 4), 
('Nevermind', '1991-09-24', 5);

-- Insertion dans la table single_disque
INSERT INTO single_disque (disque_id, single_id) VALUES 
(1, 1), 
(2, 2), 
(3, 3), 
(4, 4), 
(5, 5);

-- Insertion dans la table groupe_artiste
INSERT INTO groupe_artiste (groupe_id, artiste_id) VALUES 
(1, 1), 
(2, 2), 
(3, 3), 
(4, 4), 
(5, 5);


-- Insertion dans la table artiste avec les membres manquants
INSERT INTO artiste (prenom, nom, date_naissance) VALUES 
('Brian', 'May', '1947-07-19'), 
('Roger', 'Taylor', '1949-07-26'), 
('John', 'Deacon', '1951-08-19'), 
('Jimmy', 'Page', '1944-01-09'), 
('John', 'Paul Jones', '1946-01-03'), 
('John', 'Bonham', '1948-05-31'), 
('Glenn', 'Frey', '1948-11-06'), 
('Joe', 'Walsh', '1947-11-20'), 
('Ringo', 'Starr', '1940-07-07'), 
('Paul', 'McCartney', '1942-06-18'), 
('George', 'Harrison', '1943-02-25'), 
('Krist', 'Novoselic', '1965-05-16'), 
('Dave', 'Grohl', '1969-01-14');

-- Insertion dans la table groupe_artiste avec les membres manquants
INSERT INTO groupe_artiste (groupe_id, artiste_id) VALUES 
(1, 6), -- Brian May
(1, 7), -- Roger Taylor
(1, 8), -- John Deacon
(2, 9), -- Jimmy Page
(2, 10), -- John Paul Jones
(2, 11), -- John Bonham
(3, 12), -- Glenn Frey
(3, 13), -- Joe Walsh
(4, 14), -- Ringo Starr
(4, 15), -- Paul McCartney
(4, 16), -- George Harrison
(5, 17), -- Krist Novoselic
(5, 18); -- Dave Grohl

-- Insertion dans la table single avec des morceaux supplémentaires
INSERT INTO single (titre, duree) VALUES 
('We Will Rock You', 122), 
('We Are the Champions', 179), 
('Black Dog', 296), 
('Rock and Roll', 223), 
('Life in the Fast Lane', 285), 
('Desperado', 223), 
('Come Together', 259), 
('Something', 182), 
('Lithium', 257), 
('In Bloom', 255);

-- Insertion dans la table single_disque pour lier les singles aux albums
INSERT INTO single_disque (disque_id, single_id) VALUES 
(1, 6), -- We Will Rock You
(1, 7), -- We Are the Champions
(2, 8), -- Black Dog
(2, 9), -- Rock and Roll
(3, 10), -- Life in the Fast Lane
(3, 11), -- Desperado
(4, 12), -- Come Together
(4, 13), -- Something
(5, 14), -- Lithium
(5, 15); -- In Bloom
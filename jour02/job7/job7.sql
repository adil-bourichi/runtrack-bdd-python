CREATE DATABASE entreprise;

USE entreprise;

CREATE TABLE employes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255),
    prenom VARCHAR(255),
    salaire DECIMAL(10, 2),
    id_service INT
);

INSERT INTO employes (nom, prenom, salaire, id_service) VALUES
('Doe', 'John', 3000.00, 1),
('Smith', 'Alice', 2500.50, 2),
('Garcia', 'Maria', 3500.00, 1),
('Dupont', 'Luc', 2800.00, 3),
('Kim', 'Jin', 3200.75, 2),
('Baker', 'Tom', 2700.00, 3);



SELECT * FROM employes WHERE salaire > 3000;



CREATE TABLE services (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nom VARCHAR(255)
);

INSERT INTO services (nom)
VALUES ('Ressources Humaines'), ('Marketing'), ('Comptabilité'), ('Informatique');


ALTER TABLE employes ADD COLUMN new_column VARCHAR(255);



UPDATE employes SET id_service = 1 WHERE id IN (1, 2);
UPDATE employes SET id_service = 2 WHERE id IN (3, 4);
UPDATE employes SET id_service = 3 WHERE id = 5;
UPDATE employes SET id_service = 4 WHERE id = 6;



SELECT e.nom, e.prenom, s.nom AS service
FROM employes e
JOIN services s ON e.id_service = s.id;




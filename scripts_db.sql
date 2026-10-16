
CREATE DATABASE taskboard_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE USER 'taskboard_user'@'localhost' IDENTIFIED BY 'Evaluacion2';

GRANT ALL PRIVILEGES ON taskboard_db.* TO 'taskboard_user'@'localhost';

FLUSH PRIVILEGES;
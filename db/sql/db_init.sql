CREATE DATABASE ecsd;
USE ecsd;

CREATE USER 'ecsdadmin'@'%' IDENTIFIED BY 'secretpassbruh';
GRANT ALL ON *.* TO 'ecsdadmin'@'%';

CREATE TABLE versionTable(version TEXT);
INSERT INTO versionTable (version) VALUES ('000');
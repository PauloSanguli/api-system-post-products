use `exercise`;
DROP TABLE `account_admin`;
CREATE TABLE `account_admin` (
	`id` BIGINT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    `username` VARCHAR(40) NOT NULL,
    `password` VARCHAR(100) UNIQUE NOT NULL ,
    `email` VARCHAR(50) UNIQUE DEFAULT NULL        
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `account_admin`(`username`, `password`, `email`) VALUES("Osvaldo Victor", "Idicionario", "osvaldovictor@gmail.com");

SELECT * FROM `account_admin`;
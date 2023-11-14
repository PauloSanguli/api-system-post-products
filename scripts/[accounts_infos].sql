use `exercise`;
DROP TABLE `account_info`;
CREATE TABLE `account_info` (
	`user_id` INT NOT NULL,#foreign key, need configuration
    `password` VARCHAR(30) NOT NULL,
    `username` VARCHAR(40) NOT NULL,
    `email` VARCHAR(30) NOT NULL,
    `date_born` DATE DEFAULT NULL,
    `phone_number` VARCHAR(16) UNIQUE DEFAULT NULL,
    `date_add` DATETIME DEFAULT NOW(),
    `img_perfil` BLOB DEFAULT NULL    
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

SELECT * FROM `account_info`;

ALTER TABLE `account_info` ADD COLUMN (`check_acess` BOOLEAN DEFAULT TRUE NOT NULL);
ALTER TABLE `account_info` ADD COLUMN (`n_posts` INTEGER DEFAULT 0 );
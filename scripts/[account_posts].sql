use `exercise`;
DROP TABLE `posts`;
CREATE TABLE `posts` (
    `post_id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	`user_id` INT NOT NULL,#foreign key, need configuration
    `title_article` VARCHAR(50) NOT NULL,
    `content_text` VARCHAR(500) NOT NULL,
    `content_img` BLOB DEFAULT NULL,
    `date_posted` DATETIME DEFAULT NOW(),
    `price` DOUBLE NOT NULL,
    `show_post` BOOLEAN DEFAULT TRUE NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

SELECT * FROM `posts`;
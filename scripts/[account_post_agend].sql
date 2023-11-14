-- Active: 1691238524811@@localhost@3306@exercise
use `exercise`;
drop table `account_post_agend`;
CREATE TABLE `account_post_agend` (
    `user_id` BIGINT NOT NULL,  #foreign key need config
    `post_id` BIGINT PRIMARY KEY AUTO_INCREMENT,
    `title_article` VARCHAR(50) NOT NULL,
    `content_text` VARCHAR(500) NOT NULL,
    `content_img` BLOB DEFAULT NULL,
    `date_posted` DATETIME DEFAULT NOW(),
    `price` DOUBLE NOT NULL,
    `show_post` BOOLEAN DEFAULT TRUE NOT NULL,
    `date_agend` DATE NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


INSERT INTO `account_post_agend`(user_id, title_article, content_text, price, date_agend, time_agend) VALUES(123456792, "Escutador", "Para ouvir música com privacidade",1200, "2023-09-11", "22:00");
select * from `account_post_agend`;
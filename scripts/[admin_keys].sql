use `exercise`;
drop table `admin`;

CREATE TABLE `admin` (
	`name` VARCHAR(50) NOT NULL,
    `id` VARCHAR(40) DEFAULT("id_admin"),
    `accounts_password` VARCHAR(40) DEFAULT ("accounts_password"),
    `admin_password` VARCHAR(40) DEFAULT("admin_password")
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

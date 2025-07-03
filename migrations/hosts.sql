CREATE TABLE
  `hosts` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `hostname` VARCHAR(50) NOT NULL,
    `ipv4` VARCHAR(20) DEFAULT NULL,
    `arch` VARCHAR(20) DEFAULT NULL,
    `processor` VARCHAR(70) DEFAULT NULL,
    `so` VARCHAR(50) DEFAULT NULL,
    `distribution` VARCHAR(50) DEFAULT NULL,
    `mem_total` VARCHAR(20) DEFAULT NULL,
    `mem_free` VARCHAR(20) DEFAULT NHostsULL,
    `up_time` VARCHAR(10) DEFAULT NULL,
    `mac_address` VARCHAR(20) DEFAULT NULL,
    `created_at` VARCHAR(50) DEFAULT NULL,
    `updated_at` VARCHAR(50),
    PRIMARY KEY (`id`),
    UNIQUE KEY `hostname` (`hostname`),
    CONSTRAINT `hosts_ibfk_1` FOREIGN KEY (`hostname`) REFERENCES `hosts_aditional_infos` (`hostname`)
  ) ENGINE = InnoDB AUTO_INCREMENT = 5 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;
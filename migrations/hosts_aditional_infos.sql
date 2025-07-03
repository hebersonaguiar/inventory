CREATE TABLE
  `hosts_aditional_infos` (
    `hostname` varchar(50) NOT NULL,
    `env` varchar(20) DEFAULT NULL,
    `url` varchar(100) DEFAULT NULL,
    `is_internal` varchar(20) DEFAULT NULL,
    `notes` TEXT DEFAULT NULL,
    `midleware` varchar(50) DEFAULT NULL,
    `app_language` varchar(30) DEFAULT NULL,
    `app_system` varchar(20) DEFAULT NULL,
    `location` varchar(20) DEFAULT NULL,
    PRIMARY KEY (`hostname`),
    UNIQUE KEY `hostname` (`hostname`)
  ) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;
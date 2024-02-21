CREATE TABLE `ko_article` (
  `page_id` int NOT NULL,
  `page_title` varchar(255) NOT NULL,
  `page_text` text NOT NULL,
  `pronunciation` varchar(255) NOT NULL,
  `romanization` text NOT NULL,
  PRIMARY KEY (`page_id`),
  UNIQUE KEY `idko_article_UNIQUE` (`page_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

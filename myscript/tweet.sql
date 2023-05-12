use weibo;

DROP TABLE IF EXISTS `tweet_userprofile`;
CREATE TABLE `tweet_userprofile` (
  `_id` varchar(45) NOT NULL,
  `mblogid` varchar(45) DEFAULT NULL,
  `created_at` varchar(45) DEFAULT NULL,
  `geo` varchar(45) DEFAULT NULL,
  `ip_location` varchar(45) DEFAULT NULL,
  `reposts_count` varchar(45) DEFAULT NULL,
  `comments_count` varchar(45) DEFAULT NULL,
  `attitudes_count` varchar(45) DEFAULT NULL,
  `source` varchar(45) DEFAULT NULL,
  `content` varchar(600) DEFAULT NULL,
  `pic_urls` varchar(600) DEFAULT NULL,
  `pic_num` int DEFAULT NULL,
  `isLongText` varchar(45) DEFAULT NULL,
  `url` varchar(60) DEFAULT NULL,
  `crawl_time` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

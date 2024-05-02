-- `beachpark-history`.musics definition

CREATE TABLE `musics` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `artist` varchar(200) DEFAULT NULL,
  `track` varchar(200) DEFAULT NULL,
  `raw` varchar(200) DEFAULT NULL,
  `datetime_played` timestamp NULL DEFAULT NULL,
  `created` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `musics_unique` (`artist`,`track`,`datetime_played`)
) ENGINE=InnoDB AUTO_INCREMENT=99 DEFAULT CHARSET=latin1;
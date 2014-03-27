CREATE TABLE `user` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `screen_name` varchar(15) CHARACTER SET ucs2 NOT NULL DEFAULT '',
    `type` char(1) NOT NULL DEFAULT '',
    `uid` varchar(15) NOT NULL DEFAULT '',
    `session_id` varchar(16) DEFAULT NULL,
    `session_expire_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
    PRIMARY KEY (`id`),
    UNIQUE KEY `user_name` (`uid`)
);

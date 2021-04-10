drop Database ipl;
CREATE Database ipl;
use ipl;

CREATE TABLE `team` (
  `name` varchar(255) PRIMARY KEY,
  `owner` varchar(255),
  `captain` varchar(255),
  `matches` int,
  `wins` int,
  `winrate` decimal(4,3),
  `home_stadium` varchar(255)
);

CREATE TABLE `coaches` (
  `team_name` varchar(255),
  `coach_name` varchar(255),
  PRIMARY KEY (`team_name`, `coach_name`)
);

CREATE TABLE `player` (
  `player_id` INT NOT NULL,
  `name` varchar(255),
  `nationality` varchar(255),
  `team_name` varchar(255),
  PRIMARY KEY(`player_id`)
);

CREATE TABLE `match` (
  `date` date,
  `time` time,
  `venue` varchar(255),
  `home_team` varchar(255),
  `away_team` varchar(255),
  `audience` int,
  `result` int, -- 0 for draw, 1 for win by home_team, 2 for win by away_team
  PRIMARY KEY (`date`, `time`)
);

CREATE TABLE `stadium` (
  `name` varchar(255) PRIMARY KEY,
  `city` varchar(255)
);

CREATE TABLE `umpire` (
  `umpire_id` INT NOT NULL,
  `name` varchar(255),
  `salary` int,
  PRIMARY KEY(`umpire_id`)
);

CREATE TABLE `ground_staff` (
  `works_on` varchar(255),
  `name` varchar(255),
  `role` varchar(255),
  PRIMARY KEY(`works_on`,`name`)
);

CREATE TABLE `team_management` (
  `works_for` varchar(255),
  `name` varchar(255),
  `role` varchar(255),
  PRIMARY KEY(`works_for`,`name`)
);

CREATE TABLE `bowler` (
  `player_id` int,
  `wickets` int,
  `economy` int,
  PRIMARY KEY(`player_id`)
);

CREATE TABLE `batsman` (
  `player_id` int,
  `runs` int,
  `average` int,
  PRIMARY KEY(`player_id`)
);

CREATE TABLE `wicketkeeper` (
  `player_id` int,
  `stumps` int,
  `caughts` int,
  -- `dismissals` int,
  PRIMARY KEY(`player_id`)
);

CREATE TABLE `game` (
  `home_team` varchar(255),
  `away_team` varchar(255),
  `umpire_id` int,
  `stadium_name` varchar(255),
  PRIMARY KEY(`home_team`,`away_team`,`umpire_id`,`stadium_name`)
);

ALTER TABLE `team` ADD FOREIGN KEY (`home_stadium`) REFERENCES `stadium` (`name`);

ALTER TABLE `coaches` ADD FOREIGN KEY (`team_name`) REFERENCES `team` (`name`);

ALTER TABLE `player` ADD FOREIGN KEY (`team_name`) REFERENCES `team` (`name`);

ALTER TABLE `ground_staff` ADD FOREIGN KEY (`works_on`) REFERENCES `stadium` (`name`);
ALTER TABLE `team_management` ADD FOREIGN KEY (`works_for`) REFERENCES `team` (`name`);

ALTER TABLE `bowler` ADD FOREIGN KEY (`player_id`) REFERENCES `player` (`player_id`);
ALTER TABLE `batsman` ADD FOREIGN KEY (`player_id`) REFERENCES `player` (`player_id`);
ALTER TABLE `wicketkeeper` ADD FOREIGN KEY (`player_id`) REFERENCES `player` (`player_id`);

ALTER TABLE `game` ADD FOREIGN KEY (`home_team`) REFERENCES `team` (`name`);
ALTER TABLE `game` ADD FOREIGN KEY (`away_team`) REFERENCES `team` (`name`);
ALTER TABLE `game` ADD FOREIGN KEY (`umpire_id`) REFERENCES `umpire` (`umpire_id`);
ALTER TABLE `game` ADD FOREIGN KEY (`stadium_name`) REFERENCES `stadium` (`name`);

-- -- populate database
INSERT INTO `stadium` VALUES ("M Chinnaswamy Stadium","Banglore");
INSERT INTO `stadium` VALUES ("M A Chidambaram Stadium","Chennai");
INSERT INTO `stadium` VALUES ("Feroz Shah Kotla","Delhi");
INSERT INTO `stadium` VALUES ("Wankhede","Mumbai");
-- INSERT INTO `stadium` VALUES ("Sardar Patel","Ahmedabad");
-- INSERT INTO `stadium` VALUES ("Eden Gardens","Kolkata");

INSERT INTO `team` VALUES ("RCB","Vijay Malya","Virat Kohli",210, 0 ,0.55,"M Chinnaswamy Stadium");
INSERT INTO `team` VALUES ("CSK","N Srinivason","Ms Dhoni",220, 3 ,0.75,"M A Chidambaram Stadium");
INSERT INTO `team` VALUES ("DC","Parth Jindal","Iyer",200, 0 ,0.60,"Feroz Shah Kotla");
INSERT INTO `team` VALUES ("MI","Mukesh Ambani","Rohit Sharma",222, 4 ,0.78,"Wankhede");

INSERT INTO `coaches` VALUES ("RCB","Anil Kumble");
INSERT INTO `coaches` VALUES ("CSK","Stephan Fleming");
INSERT INTO `coaches` VALUES ("DC","Saurav Ganguly");

INSERT INTO `player` VALUES (1,"Rohit Sharma","India","MI");
INSERT INTO `player` VALUES (2,"Ms Dhoni","India","CSK");
INSERT INTO `player` VALUES (3,"Virat Kohli","India","RCB");
INSERT INTO `player` VALUES (4,"KL Rahul","India","DC");
INSERT INTO `player` VALUES (5,"Ashok","India","MI");
INSERT INTO `player` VALUES (6,"Virat Singh","India","CSK");

INSERT INTO `match` VALUES ("2011-5-2","8:00","M A Chidambaram Stadium","CSK","MI",45000,1);
INSERT INTO `match` VALUES ("2011-5-18","4:00","Firoz Shah Kotla","DC","RCB",100000,2);
INSERT INTO `match` VALUES ("2011-5-2","6:00","M A Chidambaram Stadium","CSK","MI",45000,0);
INSERT INTO `match` VALUES ("2011-5-19","4:00","Eden Gardens","KKR","MI",10000,1);
INSERT INTO `match` VALUES ("2011-5-20","8:00","Eden Gardens","KKR","CSK",10000,2);
INSERT INTO `match` VALUES ("2011-5-21","4:00","Mohali Stadium","KXIP","MI",40000,0);
INSERT INTO `match` VALUES ("2011-5-22","8:00","Eden Gardens","KKR","SRH",10000,1);
INSERT INTO `match` VALUES ("2011-5-23","8:00","Feroz shah kotla","DC","RCB",250000,2);
INSERT INTO `match` VALUES ("2011-5-24","4:00","Eden Gardens","KKR","RCB",10000,1);

INSERT INTO `umpire` VALUES (1,"Simon Tuffel", 150000); 
INSERT INTO `umpire` VALUES (2,"S Ravi", 120000);
-- INSERT INTO `umpire` VALUES (3,"Manu Nayyar",100000);

INSERT INTO `ground_staff` VALUES ("M Chinnaswamy Stadium","Vijay","Pitch Curater");
INSERT INTO `ground_staff` VALUES ("Wankhede","Suresh","Ground Curater");

INSERT INTO `team_management` VALUES ("CSK","Shankar","Manager");
INSERT INTO `team_management` VALUES ("DC","Mallika","Manager");

INSERT INTO `bowler` VALUES (1,95,6.75);
INSERT INTO `bowler` VALUES (4,72,5.12);
INSERT INTO `batsman` VALUES (3,5500,32.30);
INSERT INTO `batsman` VALUES (6,3800,29.80);
INSERT INTO `wicketkeeper` VALUES (2,72,30);
INSERT INTO `wicketkeeper` VALUES (5,42,23);

INSERT INTO `game` VALUES ("DC","MI",1,"Feroz Shah Kotla");
INSERT INTO `game` VALUES ("RCB","CSK",2,"M Chinnaswamy Stadium");

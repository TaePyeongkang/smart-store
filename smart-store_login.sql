-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: 10.10.21.119    Database: smart-store
-- ------------------------------------------------------
-- Server version	8.0.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login` (
  `이름` varchar(45) DEFAULT NULL,
  `아이디` varchar(45) DEFAULT NULL,
  `비밀번호` varchar(45) DEFAULT NULL,
  `연락처` varchar(45) DEFAULT NULL,
  `주소` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES ('asd','asd','asd','asd','asd'),('임영효','ynyh','123','123','123'),('임영효','ynyh','123','123','123'),('임영효','ynyh','123','123','123'),('asdf','asd','asdf','asdf','asdf'),('asd','asd','asd','asd','asd'),('asd','asd','asd','asdasd','asd'),('asd','as','asd','asd','asd'),('asd','asd','asd','asd','asd'),('asd','asd','asd','asd','asd'),('qwe','asd','asd','asd','asd'),('asd','asd','asd','asd','asd'),('asd','asd','asd','asd','asd'),('asd','asda','asd','asd','asd'),('asd','asdas','asd','asd','asd'),('asd','asdasd','asd','asd','asd'),('123','asdfasd','a','asd','asd'),('asd','asd123','asd','asd','asd'),('asdasda','asd213123','a','a','a'),('asd','asdassss','asd','asd','asd'),('123','123123','123','123','123'),('asd','asdasdasdasda','asd','asd','asd'),('asda','asd','a','dasd','asdas');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-19 18:37:56

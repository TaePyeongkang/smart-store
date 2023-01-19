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
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory` (
  `메뉴` text,
  `원재료명` text,
  `재고량` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES ('돼지국밥','돼지고기',4200),('돼지국밥','월계수 잎',21),('돼지국밥','양파',2730),('돼지국밥','마늘',210),('돼지국밥','대파',1050),('돼지국밥','청양고추',420),('돼지국밥','부추',210),('돼지국밥','생강',420),('돼지국밥','다진 마늘',210),('돼지국밥','멸치 액젓',21),('돼지국밥','후추',10),('돼지국밥','사골육수',2100),('돼지국밥','고춧가루',21),('돼지국밥','간장',10),('돼지국밥','매실액',10),('순대국밥','순대',5000),('순대국밥','월계수 잎',25),('순대국밥','양파',3250),('순대국밥','마늘',250),('순대국밥','대파',1250),('순대국밥','청양고추',500),('순대국밥','부추',250),('순대국밥','생강',500),('순대국밥','다진 마늘',250),('순대국밥','멸치 액젓',25),('순대국밥','후추',13),('순대국밥','사골육수',2500),('순대국밥','고춧가루',25),('순대국밥','간장',13),('순대국밥','매실액',13),('머리국밥','머리고기',3200),('머리국밥','월계수 잎',16),('머리국밥','양파',2080),('머리국밥','마늘',160),('머리국밥','대파',800),('머리국밥','청양고추',320),('머리국밥','부추',160),('머리국밥','생강',320),('머리국밥','다진 마늘',160),('머리국밥','멸치 액젓',16),('머리국밥','후추',8),('머리국밥','사골육수',1600),('머리국밥','고춧가루',16),('머리국밥','간장',8),('머리국밥','매실액',8),('내장국밥','내장',5000),('내장국밥','월계수 잎',25),('내장국밥','양파',3250),('내장국밥','마늘',250),('내장국밥','대파',1250),('내장국밥','청양고추',500),('내장국밥','부추',250),('내장국밥','생강',500),('내장국밥','다진 마늘',250),('내장국밥','멸치 액젓',25),('내장국밥','후추',13),('내장국밥','사골육수',2500),('내장국밥','고춧가루',25),('내장국밥','간장',13),('내장국밥','매실액',13);
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
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

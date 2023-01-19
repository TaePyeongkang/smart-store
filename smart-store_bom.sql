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
-- Table structure for table `bom`
--

DROP TABLE IF EXISTS `bom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bom` (
  `메뉴` text,
  `원재료명` text,
  `hs code` text,
  `원산지` text,
  `소모량` double DEFAULT NULL,
  `단가` double DEFAULT NULL,
  `가격` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bom`
--

LOCK TABLES `bom` WRITE;
/*!40000 ALTER TABLE `bom` DISABLE KEYS */;
INSERT INTO `bom` VALUES ('돼지국밥','돼지고기','0203.29-9000','국산',200,15,3000),('돼지국밥','월계수 잎','0910.99-1000','미상',1,24,24),('돼지국밥','양파','0710.80-1000','미상',130,4,520),('돼지국밥','마늘','0710.80-2000','미상',10,2.5,25),('돼지국밥','대파','0710.80-9010','미상',50,10,500),('돼지국밥','청양고추','0709.60-9000','미상',20,10,200),('돼지국밥','부추','0710.80-9090','미상',10,1.5,15),('돼지국밥','생강','2006.00-9090','미상',20,2,40),('돼지국밥','다진 마늘','0703.20-1000','미상',10,2.5,25),('돼지국밥','멸치 액젓','1603.00-4000','미상',1,4,4),('돼지국밥','후추','2103.90-9030','미상',0.5,50,25),('돼지국밥','사골육수','2104.10-1000','미상',100,4,400),('돼지국밥','고춧가루','0904.22-0000','미상',1,14,14),('돼지국밥','간장','2103.10-0000','미상',0.5,3,2),('돼지국밥','매실액','1302.19-9099','미상',0.5,12,6),('순대국밥','돼지고기','0203.29-9000','국산',200,5,1000),('순대국밥','월계수 잎','0910.99-1000','미상',1,24,24),('순대국밥','양파','0710.80-1000','미상',130,4,520),('순대국밥','마늘','0710.80-2000','미상',10,2.5,25),('순대국밥','대파','0710.80-9010','미상',50,10,500),('순대국밥','청양고추','0709.60-9000','미상',20,10,200),('순대국밥','부추','0710.80-9090','미상',10,1.5,15),('순대국밥','생강','2006.00-9090','미상',20,2,40),('순대국밥','다진 마늘','0703.20-1000','미상',10,2.5,25),('순대국밥','멸치 액젓','1603.00-4000','미상',1,4,4),('순대국밥','후추','2103.90-9030','미상',0.5,50,25),('순대국밥','사골육수','2104.10-1000','미상',100,4,400),('순대국밥','고춧가루','0904.22-0000','미상',1,14,14),('순대국밥','간장','2103.10-0000','미상',0.5,3,2),('순대국밥','매실액','1302.19-9099','미상',0.5,12,6),('머리국밥','돼지고기','0203.29-9000','국산',200,12.5,2500),('머리국밥','월계수 잎','0910.99-1000','미상',1,24,24),('머리국밥','양파','0710.80-1000','미상',130,4,520),('머리국밥','마늘','0710.80-2000','미상',10,2.5,25),('머리국밥','대파','0710.80-9010','미상',50,10,500),('머리국밥','청양고추','0709.60-9000','미상',20,10,200),('머리국밥','부추','0710.80-9090','미상',10,1.5,15),('머리국밥','생강','2006.00-9090','미상',20,2,40),('머리국밥','다진 마늘','0703.20-1000','미상',10,2.5,25),('머리국밥','멸치 액젓','1603.00-4000','미상',1,4,4),('머리국밥','후추','2103.90-9030','미상',0.5,50,25),('머리국밥','사골육수','2104.10-1000','미상',100,4,400),('머리국밥','고춧가루','0904.22-0000','미상',1,14,14),('머리국밥','간장','2103.10-0000','미상',0.5,3,2),('머리국밥','매실액','1302.19-9099','미상',0.5,12,6),('내장국밥','돼지고기','0203.29-9000','국산',200,10,2000),('내장국밥','월계수 잎','0910.99-1000','미상',1,24,24),('내장국밥','양파','0710.80-1000','미상',130,4,520),('내장국밥','마늘','0710.80-2000','미상',10,2.5,25),('내장국밥','대파','0710.80-9010','미상',50,10,500),('내장국밥','청양고추','0709.60-9000','미상',20,10,200),('내장국밥','부추','0710.80-9090','미상',10,1.5,15),('내장국밥','생강','2006.00-9090','미상',20,2,40),('내장국밥','다진 마늘','0703.20-1000','미상',10,2.5,25),('내장국밥','멸치 액젓','1603.00-4000','미상',1,4,4),('내장국밥','후추','2103.90-9030','미상',0.5,50,25),('내장국밥','사골육수','2104.10-1000','미상',100,4,400),('내장국밥','고춧가루','0904.22-0000','미상',1,14,14),('내장국밥','간장','2103.10-0000','미상',0.5,3,2),('내장국밥','매실액','1302.19-9099','미상',0.5,12,6);
/*!40000 ALTER TABLE `bom` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-18 16:08:52

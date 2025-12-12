-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: localhost    Database: rttm
-- ------------------------------------------------------
-- Server version	8.0.44

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
-- Table structure for table `attack_recommendation`
--

DROP TABLE IF EXISTS `attack_recommendation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attack_recommendation` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tool_name` varchar(255) DEFAULT NULL,
  `attack_type` varchar(255) DEFAULT NULL,
  `os_windows` tinyint(1) DEFAULT '0',
  `os_linux` tinyint(1) DEFAULT '0',
  `os_android` tinyint(1) DEFAULT '0',
  `os_ios` tinyint(1) DEFAULT '0',
  `os_macos` tinyint(1) DEFAULT '0',
  `open_ports` varchar(255) DEFAULT NULL,
  `description` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attack_recommendation`
--

LOCK TABLES `attack_recommendation` WRITE;
/*!40000 ALTER TABLE `attack_recommendation` DISABLE KEYS */;
INSERT INTO `attack_recommendation` VALUES (1,'nmap','reconnaissance',1,1,1,1,1,'21,22,80,443','Network scanner used for reconnaissance and port discovery'),(2,'theHarvester','reconnaissance',1,1,1,0,0,NULL,'Email, subdomain and employee enumeration'),(3,'sqlmap','web exploitation',1,1,0,0,0,'80,443','Automated SQL injection and database takeover tool'),(4,'hydra','password attack',1,1,1,0,0,'21,22,23,25,80','Brute force tool for multiple protocols (FTP, SSH, Telnet, HTTP)'),(5,'burpsuite','web exploitation',1,1,0,0,0,'80,443','Web vulnerability scanner & interception proxy'),(6,'msfconsole','exploitation',1,1,1,0,0,NULL,'Metasploit framework for exploitation and payload delivery');
/*!40000 ALTER TABLE `attack_recommendation` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-12-12 20:18:05

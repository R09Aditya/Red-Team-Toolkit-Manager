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
-- Table structure for table `toolkit_inventory`
--

DROP TABLE IF EXISTS `toolkit_inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `toolkit_inventory` (
  `tid` int NOT NULL AUTO_INCREMENT,
  `tool_name` varchar(100) NOT NULL,
  `tool_type` varchar(50) DEFAULT NULL,
  `description` text,
  `version` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`tid`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `toolkit_inventory`
--

LOCK TABLES `toolkit_inventory` WRITE;
/*!40000 ALTER TABLE `toolkit_inventory` DISABLE KEYS */;
INSERT INTO `toolkit_inventory` VALUES (1,'Nmap','Network Scanner','Network discovery and security auditing tool','7.93'),(2,'Metasploit','Exploitation Framework','Framework for developing and executing exploit code','6.2.29'),(3,'Burp Suite','Web Vulnerability Scanner','Web application security testing tool','2025.9'),(4,'John the Ripper','Password Cracker','Fast password cracking tool','1.9.0'),(5,'Wireshark','Packet Analyzer','Network protocol analyzer for troubleshooting and analysis','4.0.9'),(6,'Hydra','Brute Force Tool','Password brute forcing tool for various protocols','9.4'),(7,'Aircrack-ng','Wireless Security','Wi-Fi network security testing and cracking tool','1.8'),(8,'SQLmap','SQL Injection Tool','Automatic SQL injection and database takeover tool','1.7.7'),(9,'Nikto','Web Scanner','Web server scanner to detect vulnerabilities','2.1.6'),(10,'SET (Social-Engineer Toolkit)','Social Engineering','Tool for social engineering attacks and testing','8.1.0'),(11,'Nmap','Network Scanner','Network discovery and security auditing tool','7.93'),(12,'Metasploit','Exploitation Framework','Framework for developing and executing exploit code','6.2.29'),(13,'Burp Suite','Web Vulnerability Scanner','Web application security testing tool','2025.9'),(14,'John the Ripper','Password Cracker','Fast password cracking tool','1.9.0'),(15,'Wireshark','Packet Analyzer','Network protocol analyzer for troubleshooting and analysis','4.0.9'),(16,'Hydra','Brute Force Tool','Password brute forcing tool for various protocols','9.4'),(17,'Aircrack-ng','Wireless Security','Wi-Fi network security testing and cracking tool','1.8'),(18,'SQLmap','SQL Injection Tool','Automatic SQL injection and database takeover tool','1.7.7'),(19,'Nikto','Web Scanner','Web server scanner to detect vulnerabilities','2.1.6'),(20,'SET (Social-Engineer Toolkit)','Social Engineering','Tool for social engineering attacks and testing','8.1.0'),(21,'Maltego','Reconnaissance','Graphical link analysis tool for gathering OSINT','4.6.0'),(22,'Recon-ng','Reconnaissance','Web reconnaissance framework with modules for data collection','5.1.0'),(23,'Fierce','DNS Scanner','Domain reconnaissance and subdomain scanning tool','1.0'),(24,'Dirb','Directory Scanner','Web content scanner to discover hidden paths','2.22'),(25,'Gobuster','Directory Scanner','Tool for brute forcing URIs and directories','3.1.0'),(26,'Hashcat','Password Cracker','Advanced password recovery tool supporting GPU acceleration','6.2.6'),(27,'Responder','Network Analysis','LLMNR, NBT-NS and MDNS poisoner for Windows networks','2.3.0'),(28,'Impacket','Network Tools','Collection of Python classes for working with network protocols','0.9.24'),(29,'Ettercap','Network Sniffer','Comprehensive suite for man-in-the-middle attacks','0.8.3'),(30,'OWASP ZAP','Web Vulnerability Scanner','Open-source web application security scanner','2.12.0'),(31,'Skipfish','Web Scanner','Web application security reconnaissance tool','2.10b'),(32,'Cain & Abel','Password Cracker','Password recovery tool for Microsoft OS','4.9.56'),(33,'Netcat','Network Utility','Utility for reading/writing network connections','1.11'),(34,'Hping3','Network Scanner','TCP/IP packet assembler and analyzer','3.0.0'),(35,'BeEF','Browser Exploitation Framework','Framework for exploiting browser vulnerabilities','0.5.4'),(36,'Nikto2','Web Scanner','Improved web server vulnerability scanner','2.1.7'),(37,'WPScan','CMS Scanner','WordPress vulnerability scanner','3.8.0'),(38,'CMSmap','CMS Scanner','Automated vulnerability scanner for CMS platforms','0.8'),(39,'OpenVAS','Vulnerability Scanner','Comprehensive vulnerability scanning and management tool','22.4'),(40,'Airgeddon','Wireless Security','Multi-use bash script for Wi-Fi security auditing','1.6'),(41,'Reaver','Wireless Security','WPS PIN brute force attack tool','1.6.5'),(42,'Wifite','Wireless Security','Automated wireless auditing tool','2.5'),(43,'Bettercap','Network Manipulation','MITM framework for network attacks','2.32'),(44,'Cuckoo Sandbox','Malware Analysis','Automated malware analysis system','2.0'),(45,'Volatility','Memory Analysis','Memory forensics framework','2.6'),(46,'Radare2','Reverse Engineering','Open-source reverse engineering framework','5.6'),(47,'Ghidra','Reverse Engineering','Software reverse engineering suite developed by NSA','10.2'),(48,'Frida','Dynamic Instrumentation','Dynamic instrumentation toolkit for developers, reverse-engineers','15.1'),(49,'Immunity Debugger','Reverse Engineering','Windows debugger for malware analysis','1.85'),(50,'OllyDbg','Debugger','32-bit assembler level analysing debugger for Windows','2.01'),(51,'Binwalk','Firmware Analysis','Firmware analysis tool for extracting embedded files','2.3.3'),(52,'JohnWick','Password Cracker','Custom test password tool','1.0'),(53,'AirSnort','Wireless Security','Tool for decrypting WEP keys','0.2'),(54,'Netdiscover','Network Scanner','Active/passive network reconnaissance tool','0.7'),(55,'SQLninja','SQL Injection Tool','SQL injection automation tool for MS SQL Server','0.9.8'),(56,'Metagoofil','Reconnaissance','Information gathering tool to extract metadata of public documents','2.2'),(57,'OWASP Dependency Check','Vulnerability Scanner','Detect publicly disclosed vulnerabilities in project dependencies','7.4.4'),(58,'Snort','IDS/IPS','Network intrusion detection and prevention system','2.9.21'),(59,'Tcpdump','Packet Analyzer','Command-line packet analyzer','4.99'),(60,'Social-Engineer Toolkit','Social Engineering','Toolkit for social engineering attacks','8.1.0'),(61,'Responder-ng','Network Analysis','Advanced responder for network poisoning','1.0'),(62,'Ettercap-ng','Network Sniffer','Updated suite for MITM attacks','0.9');
/*!40000 ALTER TABLE `toolkit_inventory` ENABLE KEYS */;
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

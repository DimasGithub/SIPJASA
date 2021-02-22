-- MySQL dump 10.13  Distrib 8.0.19, for Linux (x86_64)
--
-- Host: localhost    Database: sijasaku
-- ------------------------------------------------------
-- Server version	8.0.19-0ubuntu5

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (4,'Admin'),(3,'Banned'),(1,'Customer'),(2,'Provider');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=193 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(6,1,6),(7,1,7),(8,1,8),(9,1,9),(10,1,10),(11,1,11),(12,1,12),(13,1,13),(14,1,14),(15,1,15),(16,1,16),(17,1,17),(18,1,18),(19,1,19),(20,1,20),(21,1,21),(22,1,22),(23,1,23),(24,1,24),(25,1,25),(26,1,26),(27,1,27),(28,1,28),(29,1,29),(30,1,30),(31,1,31),(32,1,32),(33,1,33),(34,1,34),(35,1,35),(36,1,36),(37,1,37),(38,1,38),(39,1,39),(40,1,40),(41,1,41),(42,1,42),(43,1,43),(44,1,44),(45,1,45),(46,1,46),(47,1,47),(48,1,48),(49,2,1),(50,2,2),(51,2,3),(52,2,4),(53,2,5),(54,2,6),(55,2,7),(56,2,8),(57,2,9),(58,2,10),(59,2,11),(60,2,12),(61,2,13),(62,2,14),(63,2,15),(64,2,16),(65,2,17),(66,2,18),(67,2,19),(68,2,20),(69,2,21),(70,2,22),(71,2,23),(72,2,24),(73,2,25),(74,2,26),(75,2,27),(76,2,28),(77,2,29),(78,2,30),(79,2,31),(80,2,32),(81,2,33),(82,2,34),(83,2,35),(84,2,36),(85,2,37),(86,2,38),(87,2,39),(88,2,40),(89,2,41),(90,2,42),(91,2,43),(92,2,44),(93,2,45),(94,2,46),(95,2,47),(96,2,48),(97,3,1),(98,3,2),(99,3,3),(100,3,4),(101,3,5),(102,3,6),(103,3,7),(104,3,8),(105,3,9),(106,3,10),(107,3,11),(108,3,12),(109,3,13),(110,3,14),(111,3,15),(112,3,16),(113,3,17),(114,3,18),(115,3,19),(116,3,20),(117,3,21),(118,3,22),(119,3,23),(120,3,24),(121,3,25),(122,3,26),(123,3,27),(124,3,28),(125,3,29),(126,3,30),(127,3,31),(128,3,32),(129,3,33),(130,3,34),(131,3,35),(132,3,36),(133,3,37),(134,3,38),(135,3,39),(136,3,40),(137,3,41),(138,3,42),(139,3,43),(140,3,44),(141,3,45),(142,3,46),(143,3,47),(144,3,48),(145,4,1),(146,4,2),(147,4,3),(148,4,4),(149,4,5),(150,4,6),(151,4,7),(152,4,8),(153,4,9),(154,4,10),(155,4,11),(156,4,12),(157,4,13),(158,4,14),(159,4,15),(160,4,16),(161,4,17),(162,4,18),(163,4,19),(164,4,20),(165,4,21),(166,4,22),(167,4,23),(168,4,24),(169,4,25),(170,4,26),(171,4,27),(172,4,28),(173,4,29),(174,4,30),(175,4,31),(176,4,32),(177,4,33),(178,4,34),(179,4,35),(180,4,36),(181,4,37),(182,4,38),(183,4,39),(184,4,40),(185,4,41),(186,4,42),(187,4,43),(188,4,44),(189,4,45),(190,4,46),(191,4,47),(192,4,48);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add user profile',7,'add_userprofile'),(26,'Can change user profile',7,'change_userprofile'),(27,'Can delete user profile',7,'delete_userprofile'),(28,'Can view user profile',7,'view_userprofile'),(29,'Can add bukajasa',8,'add_bukajasa'),(30,'Can change bukajasa',8,'change_bukajasa'),(31,'Can delete bukajasa',8,'delete_bukajasa'),(32,'Can view bukajasa',8,'view_bukajasa'),(33,'Can add postingjasa',9,'add_postingjasa'),(34,'Can change postingjasa',9,'change_postingjasa'),(35,'Can delete postingjasa',9,'delete_postingjasa'),(36,'Can view postingjasa',9,'view_postingjasa'),(37,'Can add scorejasa',10,'add_scorejasa'),(38,'Can change scorejasa',10,'change_scorejasa'),(39,'Can delete scorejasa',10,'delete_scorejasa'),(40,'Can view scorejasa',10,'view_scorejasa'),(41,'Can add pesan',11,'add_pesan'),(42,'Can change pesan',11,'change_pesan'),(43,'Can delete pesan',11,'delete_pesan'),(44,'Can view pesan',11,'view_pesan'),(45,'Can add report',12,'add_report'),(46,'Can change report',12,'change_report'),(47,'Can delete report',12,'delete_report'),(48,'Can view report',12,'view_report'),(49,'Can add lapor',13,'add_lapor'),(50,'Can change lapor',13,'change_lapor'),(51,'Can delete lapor',13,'delete_lapor'),(52,'Can view lapor',13,'view_lapor');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (6,'pbkdf2_sha256$180000$7DUz5HJTQPeV$Hon1a5MdbnWDucOLvQjuu5rsFyPRZNg1JcqKomjR9DY=','2020-12-22 05:28:15.905448',0,'rizky','Rizky Kamal','Ikhsani','rizkykamalikhsani@gmail.com',0,1,'2020-10-12 15:53:12.137525'),(19,'pbkdf2_sha256$180000$KT8780ONrOwK$v1OlqOdYzmVl2LYuBamCRBfkr6sJVRPsxeZEjx9+kC8=','2020-12-22 12:03:14.842149',0,'septimellianas','septi','melliana s','septimellianasari2.sms21@gmail.com',0,1,'2020-12-17 04:51:40.162644'),(20,'pbkdf2_sha256$180000$wb2JICS3I2KL$Uc/fzRQ39KyDhznyPeD2keUcR8RWlEDEbGSUs3ESBtM=','2020-12-19 11:34:32.985070',1,'superadmin','','','superadmin@sipjasa.com',1,1,'2020-12-18 02:14:45.774763'),(21,'pbkdf2_sha256$180000$ltE145AAkRmU$V0hDNoEhltbst/RRbiqOp4275fwALY9fNRnBE7/44cM=','2020-12-22 06:28:30.992062',0,'admin','admin','sipjasa','admin@sipjasa.com',0,1,'2020-12-18 02:26:07.000000'),(22,'pbkdf2_sha256$180000$Q7Dp9teKYYMy$gwgNCTT3r8E3g+2kOx2XZZLPbZnAfsUgTI6rWM8eH9k=','2020-12-19 15:49:40.064687',0,'atun','Ida','Supriyatun','dim.dim10032000@gmail.com',0,1,'2020-12-18 02:34:51.297385'),(23,'pbkdf2_sha256$180000$a6mNnHSeuED1$atpUOZ8H6VE0+kNSLoNI62B/nqfPBJh9Bdsg22QfUpY=','2020-12-21 01:59:46.509297',0,'deni','Deni','Dwi Saputra','siswabiasa@merahputih.id',0,1,'2020-12-18 09:33:36.232619'),(25,'pbkdf2_sha256$180000$e2qnqQM04Wb2$rAaKFF1qxCNykvPdyBXZRWlhh6PCHWikXv803FYjxxU=','2020-12-22 11:58:08.787242',0,'studioweb','studio','web','kontak@studioweb.co.id',0,1,'2020-12-20 13:06:25.767899'),(26,'pbkdf2_sha256$180000$BtDVqaOyljB0$7wOXvDMDopl+cwIvzW4hh5ldTElUZjS1ZlVaO7yH9ww=','2020-12-20 14:40:49.129330',0,'iza','Laelatul','Iza Nur Anisa','laelatuliza@gmail.com',0,1,'2020-12-20 14:38:24.945452');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (7,6,2),(20,19,1),(22,21,4),(23,22,2),(26,23,3),(27,25,2),(28,26,1);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (6,'2020-12-18 02:15:58.231861','7','teguh',3,'',4,20),(7,'2020-12-18 02:16:07.649956','11','sutrisno',3,'',4,20),(8,'2020-12-18 02:16:21.780845','5','septi',3,'',4,20),(9,'2020-12-18 02:16:32.714214','8','saidi',3,'',4,20),(10,'2020-12-18 02:16:41.814981','17','adam',3,'',4,20),(11,'2020-12-18 02:16:54.041665','16','adit',3,'',4,20),(12,'2020-12-18 02:17:19.041303','4','admin',3,'',4,20),(13,'2020-12-18 02:17:42.544380','14','atun',3,'',4,20),(14,'2020-12-18 02:17:55.484628','2','dim',3,'',4,20),(15,'2020-12-18 02:18:07.205231','12','ronal',3,'',4,20),(16,'2020-12-18 02:18:15.609912','13','chesa',3,'',4,20),(17,'2020-12-18 02:18:23.509894','3','dima',3,'',4,20),(18,'2020-12-18 02:18:32.144198','9','iza',3,'',4,20),(19,'2020-12-18 02:18:45.056265','18','rizki',3,'',4,20),(20,'2020-12-18 02:18:55.452976','10','rafa',3,'',4,20),(21,'2020-12-18 02:19:04.007329','1','su',3,'',4,20),(22,'2020-12-18 02:19:18.142015','15','joni',3,'',4,20),(23,'2020-12-18 02:27:20.523365','21','admin',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,20),(24,'2020-12-19 11:34:48.182133','24','rizki',3,'',4,20);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(11,'order','pesan'),(8,'provider','bukajasa'),(9,'provider','postingjasa'),(10,'provider','scorejasa'),(7,'register','userprofile'),(13,'report','lapor'),(12,'report','report'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-10-12 04:58:32.855312'),(2,'auth','0001_initial','2020-10-12 04:58:36.588965'),(3,'admin','0001_initial','2020-10-12 04:58:50.147299'),(4,'admin','0002_logentry_remove_auto_add','2020-10-12 04:58:53.637047'),(5,'admin','0003_logentry_add_action_flag_choices','2020-10-12 04:58:53.784883'),(6,'contenttypes','0002_remove_content_type_name','2020-10-12 04:58:56.373912'),(7,'auth','0002_alter_permission_name_max_length','2020-10-12 04:58:58.141328'),(8,'auth','0003_alter_user_email_max_length','2020-10-12 04:58:58.696636'),(9,'auth','0004_alter_user_username_opts','2020-10-12 04:58:58.870397'),(10,'auth','0005_alter_user_last_login_null','2020-10-12 04:59:00.173294'),(11,'auth','0006_require_contenttypes_0002','2020-10-12 04:59:00.285306'),(12,'auth','0007_alter_validators_add_error_messages','2020-10-12 04:59:00.431362'),(13,'auth','0008_alter_user_username_max_length','2020-10-12 04:59:02.168948'),(14,'auth','0009_alter_user_last_name_max_length','2020-10-12 04:59:03.753174'),(15,'auth','0010_alter_group_name_max_length','2020-10-12 04:59:04.050039'),(16,'auth','0011_update_proxy_permissions','2020-10-12 04:59:04.168278'),(17,'provider','0001_initial','2020-10-12 04:59:04.917730'),(18,'provider','0002_auto_20200928_1440','2020-10-12 04:59:10.056224'),(19,'provider','0003_bukajasa_jenis_jasa','2020-10-12 04:59:10.799986'),(20,'provider','0004_auto_20200928_1607','2020-10-12 04:59:12.384889'),(21,'provider','0005_auto_20200928_1757','2020-10-12 04:59:14.418973'),(22,'provider','0006_auto_20201001_1716','2020-10-12 04:59:18.243724'),(23,'provider','0007_scorejasa','2020-10-12 04:59:18.883804'),(24,'order','0001_initial','2020-10-12 04:59:21.377256'),(25,'order','0002_auto_20201002_1355','2020-10-12 04:59:21.923390'),(26,'order','0003_pesan_kecamatan_order','2020-10-12 04:59:22.698988'),(27,'order','0004_pesan_akun_pemesan','2020-10-12 04:59:23.554108'),(28,'order','0005_pesan_catatan_order','2020-10-12 04:59:25.540833'),(29,'order','0006_pesan_gambar_order','2020-10-12 04:59:26.242846'),(30,'order','0007_pesan_akun_provider','2020-10-12 04:59:27.135473'),(31,'order','0008_auto_20201008_0758','2020-10-12 04:59:31.080985'),(32,'order','0009_pesan_telp_order','2020-10-12 04:59:31.951851'),(33,'register','0001_initial','2020-10-12 04:59:32.915768'),(34,'register','0002_auto_20200918_1754','2020-10-12 04:59:35.830974'),(35,'register','0003_auto_20200918_1801','2020-10-12 04:59:37.723742'),(36,'register','0004_auto_20200918_1803','2020-10-12 04:59:37.833683'),(37,'register','0005_auto_20201007_0233','2020-10-12 04:59:37.945291'),(38,'register','0006_userprofile_no_telp','2020-10-12 04:59:38.763069'),(39,'register','0007_remove_userprofile_no_telp','2020-10-12 04:59:40.200977'),(40,'report','0001_initial','2020-10-12 04:59:40.966903'),(41,'report','0002_auto_20201007_0354','2020-10-12 04:59:41.225695'),(42,'report','0003_report_datetime_report','2020-10-12 04:59:42.108083'),(43,'sessions','0001_initial','2020-10-12 04:59:42.939708'),(44,'provider','0008_auto_20201012_0514','2020-10-12 05:14:45.068834'),(45,'provider','0009_postingjasa_keterangan','2020-10-12 16:04:22.796576'),(46,'provider','0010_auto_20201013_0700','2020-10-13 07:00:50.763787'),(47,'provider','0011_auto_20201013_0703','2020-10-13 07:03:53.234124'),(48,'provider','0012_auto_20201013_0712','2020-10-13 07:13:01.282050'),(49,'provider','0013_scorejasa_kode_pesan','2020-10-13 14:03:16.103485'),(50,'register','0008_auto_20201016_1120','2020-10-16 11:20:27.339798'),(51,'order','0010_auto_20201211_1200','2020-12-11 12:00:38.946394'),(52,'provider','0014_auto_20201211_1200','2020-12-11 12:00:41.869078'),(53,'report','0004_auto_20201211_1200','2020-12-11 12:00:41.974206'),(54,'provider','0015_auto_20201212_1300','2020-12-12 13:00:32.181519'),(55,'provider','0016_auto_20201220_2103','2020-12-20 14:03:59.515069'),(56,'order','0011_auto_20201222_1220','2020-12-22 05:20:51.918240'),(57,'order','0011_auto_20201222_1233','2020-12-22 05:33:45.744864'),(58,'order','0012_pesan_providertelp','2020-12-22 05:41:46.157486'),(59,'report','0005_report_telp_reported','2020-12-22 05:47:16.068105'),(60,'report','0006_auto_20201222_1247','2020-12-22 05:47:45.913780'),(61,'order','0012_auto_20201222_1650','2020-12-22 09:50:47.812468'),(62,'report','0007_auto_20201222_1638','2020-12-22 09:50:51.860468'),(63,'report','0008_auto_20201222_1716','2020-12-22 10:16:44.039467');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('16s3rwy0pl5xb1sgbv48i44xn2fy0lex','NjI5NmRlNWFlNTE4NTFiYmIxMjBhNzQyYzU2YjJmZjIxNTJhZDkxNjp7Il9hdXRoX3VzZXJfaWQiOiIyNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZGZmN2QzYmYxNWZlM2Q3YzcxMTRmODVhMTg3ZGM1NTkzYWMwMjc3OCJ9','2021-01-05 09:54:12.425610'),('2t3oz78uhc2xsc8c8s3hicw7h0udumwg','YWQ0ZWZjZTQ2MjU1MjRjMTg3NWQwMjlhMTI3MzIzMGU3Y2Y3N2ZmYjp7Il9hdXRoX3VzZXJfaWQiOiIxOSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODkwYjJlYjYyYTM4MjY2ZTY2YzIzOGYxZGMxNzVlNzcxYjRjODg2MiJ9','2020-12-31 10:22:57.548994'),('9kfk1jju999r4f86eqt5y99hjw24phya','YjQ0YjE3ZGVhMjRkY2MxM2UyNzIzNmZlZDZlNzg4NzU4MmU2MjhjZjp7fQ==','2020-12-30 07:05:58.924236'),('arzuu63rpdms3izsber9yaewwjic9dku','YjQ0YjE3ZGVhMjRkY2MxM2UyNzIzNmZlZDZlNzg4NzU4MmU2MjhjZjp7fQ==','2020-12-30 07:06:11.793102'),('ik4a4oytpqyeothaqsfhqhz7gbg9fmb1','NzhmNWFhMmM0MTY3YzE0MWQ1MTg5YmFlNWY4MTAzM2NhZGVmZTA0MTp7Il9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyMTdmMDNhOWFlZTRjNjA0MTI3NGE0MDgyZWQ1MTE4MzQyOWE4ODYxIn0=','2020-10-26 17:12:45.870330'),('k5snwwg4d2ll81kpxu6zsxrr2975xqqj','YzJlZDYyZTY5NGZlMDVjYWY4YWFkMDU2ZDEyMzA5YzBkNGYxYWFlZTp7Il9hdXRoX3VzZXJfaWQiOiIxOSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiOTRhZjA0NzlmYmY1NWFiMjBlMGJiNjNhNjg3YzllNWExN2MzOWM4MiJ9','2021-01-05 12:03:14.963974'),('zevorcovgn3dk30nj1f4mj6z91au0q21','MWExNDI1MjFiM2ZiYzcwY2ZkN2QyMTQ3NDU2MjhiNjkwNDA5MGJhNDp7ImFsZXJ0X2xvZ2luIjp0cnVlfQ==','2020-11-01 15:37:47.303566');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_pesan`
--

DROP TABLE IF EXISTS `order_pesan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_pesan` (
  `id` int NOT NULL AUTO_INCREMENT,
  `kode` char(32) NOT NULL,
  `nama_order` varchar(30) NOT NULL,
  `alamat_order` longtext NOT NULL,
  `jasa_order_id` int NOT NULL,
  `jumlah_order` int NOT NULL,
  `total_order` int NOT NULL,
  `tanggal_order` datetime(6) NOT NULL,
  `status` varchar(20) NOT NULL,
  `nama_jasa` varchar(25) NOT NULL,
  `kecamatan_order` varchar(30) NOT NULL,
  `akun_pemesan` varchar(25) NOT NULL,
  `catatan_order` longtext NOT NULL,
  `gambar_order` varchar(100) NOT NULL,
  `akun_provider` varchar(25) NOT NULL,
  `telp_order` varchar(15) NOT NULL,
  `providertelp` varchar(12) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `kode` (`kode`),
  KEY `order_pesan_jasa_order_id_9e4b9f27` (`jasa_order_id`),
  CONSTRAINT `order_pesan_jasa_order_id_9e4b9f27_fk_provider_postingjasa_id` FOREIGN KEY (`jasa_order_id`) REFERENCES `provider_postingjasa` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_pesan`
--

LOCK TABLES `order_pesan` WRITE;
/*!40000 ALTER TABLE `order_pesan` DISABLE KEYS */;
INSERT INTO `order_pesan` VALUES (13,'fdfcf907d2bd4264b469d6b374dd4294','septi','JL. Banda rt 01 rw 03, desa cibelok',27,1,71000,'2020-12-17 05:10:51.121583','Selesai','Rizki Desain','Taman','septimellianas','pesan 3 buah vector manusia half body','avatar/WhatsApp_Image_2020-12-14_at_13.55.121.jpeg','rizky','082326849247',''),(16,'6e88f8529fb64418adbeb4e0a90edbee','septi melliana s','JL. Banda rt 01 rw 03, desa cibelok',26,1,20000,'2020-12-17 05:18:14.663987','Diproses','Rizki Desain','Taman','septimellianas','yang bagus ya','avatar/WhatsApp_Image_2020-12-14_at_13.57.14.jpeg','rizky','082326849247',''),(17,'f69605b245b849959b5e5e9330446b1b','septi','JL. Banda rt 01 rw 03, desa cibelok',29,1,284000,'2020-12-17 05:19:33.211919','Diproses','Rizki Desain','Taman','septimellianas','semangat','avatar/WhatsApp_Image_2020-12-14_at_14.15.00.jpeg','rizky','082326849247',''),(23,'c0c7fff3ff704fe8a787c80cdfa7d68e','deni dwi s','Desa. plataran RT 03 / RW 01',24,1,71000,'2020-12-19 10:05:59.695448','Diproses','Rizki Desain','Moga','deni','saya pesan desain vector untuk kuciing gambar saya kirim via whatsapp','avatar/WhatsApp_Image_2020-12-14_at_13.55.12.jpeg','rizky','085290627706',''),(26,'06f799e2f5b64e4bb193bac01af64346','Deni dwi s','Desa Plakaran RT 04 RW 01',34,1,100000,'2020-12-19 15:34:09.892829','Selesai','Mobil Atun Berkah','Moga','deni','Sewa mobil pick up satu hari','avatar/WhatsApp_Image_2020-12-09_at_10.33.211_WKONLDb.jpeg','atun','082326849247',''),(27,'40572b4dea5d4c67ab561a5118423c87','iza nur anisa','Dusun Genting Desa Walangsanga',41,1,2000000,'2020-12-20 14:43:21.511693','Pending','Studio Web','Moga','iza','saya mau kursus','avatar/landing-page-editor.png','studioweb','082317646717',''),(29,'e023f93e3abe46ad9957e7097c12fed1','asdasd','asdasd',25,1,142000,'2020-12-22 05:42:16.472239','Pending','Rizki Desain','Randudongkal','septimellianas','asdasd','avatar/WhatsApp_Image_2020-12-14_at_13.55.12_vS5L5ji.jpeg','rizky','085290627706','085713599724'),(30,'b5bd0e91a82441fe952a1dcf4c02352b','pesan website','jl masjid',37,1,2000000,'2020-12-22 09:53:19.240411','Diterima','Studio Web','Randudongkal','septimellianas','asdasd','avatar/www.studioweb.co.id_paket_jasa-pembuatan-toko-online_.png','studioweb','082326849247','087733527474'),(31,'b23757f7207a4e7384e07ed1bd0bbe55','septi','asdasd',35,1,2000,'2020-12-22 12:03:52.829879','Pending','Mobil Atun Berkah','Pulosari','septimellianas','asdasd','avatar/WhatsApp_Image_2020-12-09_at_10.33.211_Nb0kyfN.jpeg','atun','087716288171','082324811221');
/*!40000 ALTER TABLE `order_pesan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `provider_bukajasa`
--

DROP TABLE IF EXISTS `provider_bukajasa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `provider_bukajasa` (
  `nama_jasa` varchar(25) NOT NULL,
  `pemilik_jasa` varchar(25) NOT NULL,
  `email_jasa` varchar(25) NOT NULL,
  `alamat` longtext NOT NULL,
  `no_telp` varchar(20) NOT NULL,
  `deskripsi_jasa` longtext NOT NULL,
  `user_id` int NOT NULL,
  `kecamatan` varchar(25) NOT NULL,
  PRIMARY KEY (`nama_jasa`),
  KEY `provider_bukajasa_user_id_db15b4a2` (`user_id`),
  CONSTRAINT `provider_bukajasa_user_id_db15b4a2_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `provider_bukajasa`
--

LOCK TABLES `provider_bukajasa` WRITE;
/*!40000 ALTER TABLE `provider_bukajasa` DISABLE KEYS */;
INSERT INTO `provider_bukajasa` VALUES ('Mobil Atun Berkah','Ida supriyatun','atunida35@gmail.com','Jl. Masjid baitu taman','082324811221','Mobil Atun Berkah\r\nmemberikan jasa pelayanan berupa :\r\n> angkut pasir\r\n> angkut padi\r\n> angkut batu\r\n> angkut barang pasar\r\n> antar jemput rombongan\r\n> dan sewa mobil pick up',22,'Randudongkal'),('Rizki Desain','Rizky kamal ikhsani','rizkykamalikh@gmail.com','Jl. Karang asem desa bantarbolang','085713599724','Rizki desain adalah jasa layanan pembuatan desain yang meliputi : \r\n>Desain Logo\r\n>Desain Vector\r\n>Desain Baju\r\n>Desain Logo\r\n*revisi desain bebas',6,'Bantarbolang'),('Studio Web','Hermanto','kontak@studioweb.co.id','Jl. Raya Gili Tugel-Kreo KM 1 Rt. 039 Rw. 005, Desa Cibuyur, Kecamatan Warungpring, Kranding Wetan, Cibuyur, Warungpring, Kabupaten Pemalang, Jawa Tengah 52358','087733527474','JASA DIGITAL MARKETING PROFESIONAL\r\nSiap Membantu Kamu Dalam Pembuatan website, Jasa SEO & Maintenance Web, Google Ads, Jasa Pembuatan Logo Usaha, Jasa Cuctomer Service',25,'Randudongkal');
/*!40000 ALTER TABLE `provider_bukajasa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `provider_postingjasa`
--

DROP TABLE IF EXISTS `provider_postingjasa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `provider_postingjasa` (
  `id` int NOT NULL AUTO_INCREMENT,
  `jasa` varchar(50) NOT NULL,
  `harga_jasa` int NOT NULL,
  `satuan_jasa` varchar(10) NOT NULL,
  `jenis_jasa` varchar(30) NOT NULL,
  `status_jasa` varchar(10) NOT NULL,
  `upload_foto` varchar(100) NOT NULL,
  `nama_jasa_id` varchar(25) NOT NULL,
  `keterangan` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `provider_postingjasa_nama_jasa_id_37b35130_fk_provider_` (`nama_jasa_id`),
  CONSTRAINT `provider_postingjasa_nama_jasa_id_37b35130_fk_provider_` FOREIGN KEY (`nama_jasa_id`) REFERENCES `provider_bukajasa` (`nama_jasa`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `provider_postingjasa`
--

LOCK TABLES `provider_postingjasa` WRITE;
/*!40000 ALTER TABLE `provider_postingjasa` DISABLE KEYS */;
INSERT INTO `provider_postingjasa` VALUES (24,'Vector pet halfbody',71000,'QTY','Desain','Ada','avatar/WhatsApp_Image_2020-12-14_at_13.55.12.jpeg','Rizki Desain','pembuat vector hewan halfbody dengan harga Rp.71.000 \r\nbebas revisi desain'),(25,'Vector pet full body',142000,'QTY','Desain','Ada','avatar/WhatsApp_Image_2020-12-14_at_13.55.12_vS5L5ji.jpeg','Rizki Desain','Vector pet full body harga Rp. 142.000 dengan revisian desain bebas.'),(26,'Jasa pembuatan desain baju',20000,'QTY','Desain','Ada','avatar/WhatsApp_Image_2020-12-14_at_13.57.14.jpeg','Rizki Desain','Desain jasa pembuatan desain baju dengan harga Rp. 20.000 dengan revisian desain bebas'),(27,'Vector manusia halfbody',71000,'QTY','Desain','Ada','avatar/WhatsApp_Image_2020-12-14_at_13.55.121.jpeg','Rizki Desain','Vector manusia halfbody desain  harga Rp. 71.000 dengan revisian bebas'),(28,'Vector manusia fullbody',142000,'QTY','Desain','Ada','avatar/WhatsApp_Image_2020-12-14_at_13.55.121_yrtuyOm.jpeg','Rizki Desain','Vector manusia fullbody desain dengan harga Rp. 142.000\r\n*revisi desain bebas'),(29,'Jasa desain logo',284000,'QTY','Desain','Ada','avatar/WhatsApp_Image_2020-12-14_at_14.15.00.jpeg','Rizki Desain','Jasa desain logo dengan harga Rp. 284.000\r\n*revisi desain bebas'),(30,'Jasa Angkut pasir',30000,'KM','Transportasi','Ada','avatar/WhatsApp_Image_2020-12-09_at_10.33.211_85PSzZO.jpeg','Mobil Atun Berkah','Jasa Angkut pasir lokasi angkut pasir desa gembyang\r\nharga sudah termasuk jasa penurunan pasir ke lokasi pemesanan\r\n*belum termasuk harga pasir\r\nuntuk pembelian pasir tergantung jenis pasir'),(31,'Angkut batu krikil',30000,'KM','Transportasi','Ada','avatar/WhatsApp_Image_2020-12-09_at_10.33.211_6lDdchu.jpeg','Mobil Atun Berkah','Jasa angkut batu krikil lokasi pengambilan batu desa gembyang\r\nharga sudah termasuk harga penurunan batu krikil ke tempat pemesanan\r\n*harga belum termasuk pembelian batu krikil.'),(32,'Angkut hasil pertanian',25000,'KM','Transportasi','Ada','avatar/WhatsApp_Image_2020-12-09_at_10.33.211_BqY9NKJ.jpeg','Mobil Atun Berkah','Angkut hasil pertanian berupa:\r\n> angkut panen padi\r\n> angkut panen jagung\r\n> angkut panen umbi umbian\r\n> dan jenis hasil pertanian yang lain\r\n* harga sudah termasuk angkut dan penurunan ke tempat lokasi pemesanan'),(33,'Angkut barang pasar randudongkal ke rumah',5000,'KM','Transportasi','Ada','avatar/WhatsApp_Image_2020-12-09_at_10.33.211_Lc7zqLR.jpeg','Mobil Atun Berkah','Angkut barang pasar dari pasar randudongkal ke lokasi pemesanan\r\nharga sudah termasuk angkut dan penurunan barang'),(34,'Sewa mobil pick up',100000,'HARI','Transportasi','Ada','avatar/WhatsApp_Image_2020-12-09_at_10.33.211_WKONLDb.jpeg','Mobil Atun Berkah','Sewa mobil pick up harga Rp. 100.000 dengan ketentuan bensin sudah terisi full.'),(35,'Antar jemput rombongan',2000,'KM','Transportasi','Ada','avatar/WhatsApp_Image_2020-12-09_at_10.33.211_Nb0kyfN.jpeg','Mobil Atun Berkah','Antar jemput rombongan Rp. 2000 /km per orang\r\nminimal untuk antar jemput orang 10 penumpang'),(36,'jasa angkut buah',5000,'KM','Transportasi','Ada','avatar/WhatsApp_Image_2020-12-09_at_10.33.211_2J9mhuh.jpeg','Mobil Atun Berkah','jasa angkut buah'),(37,'Pembuatan website toko online',2000000,'QTY','Teknologi','Ada','avatar/www.studioweb.co.id_paket_jasa-pembuatan-toko-online_.png','Studio Web','Pembuat Toko Online Rp. 2.000.000\r\n> Disk space besar\r\n> Template Modern\r\n> Bandwith Unlimite\r\n> Gratis Domain & Hosting 1 Tahun\r\n> FREE SSL 1 Tahun\r\n> Desain Responsive dan Seo Friendly\r\n> Feature Live Chat\r\n> Free logo dan banner\r\n> Garansi Hacker \r\n> Gratis submit search engine'),(38,'Pembuatan website company profile',5000000,'QTY','Teknologi','Ada','avatar/www.studioweb.co.id_paket_jasa-pembuatan-toko-online__BGKPpXD.png','Studio Web','Pembuat Toko Online Rp. 2.000.000\r\n> Disk space besar\r\n> Template custom\r\n> Bandwith Unlimited\r\n> Gratis Domain & Hosting 1 Tahun\r\n> FREE SSL 1 Tahun\r\n> Desain Responsive dan Seo Friendly\r\n> Free logo dan banner\r\n> Garansi Hacker \r\n> Gratis submit search engine'),(39,'Pembuatan website personal',3000000,'QTY','Teknologi','Ada','avatar/www.studioweb.co.id_paket_jasa-pembuatan-toko-online__SJdPLuX.png','Studio Web','Pembuat Toko Online Rp. 3.000.000\r\n> Disk space besar\r\n> Template Modern\r\n> Bandwith Unlimite\r\n> Gratis Domain & Hosting 1 Tahun\r\n> FREE SSL 1 Tahun\r\n> Desain Responsive dan Seo Friendly\r\n> Feature Live Chat\r\n> Free logo dan banner\r\n> Garansi Hacker \r\n> Gratis submit search engine'),(40,'Kursus online membuat website landing page',399000,'BULAN','Pendidikan','Ada','avatar/download.jpeg','Studio Web','FREE SUPPORT 30 HARI\r\nBelajar Melalui Online\r\nMateri dalam bentuk Artikel dan Video\r\nBelum Termasuk Domain dan hosting untuk praktek\r\nGaransi Bisa Membuat Landing Page'),(41,'kursus langsung membuat website landing page',2000000,'BULAN','Pendidikan','Ada','avatar/landing-page-editor.png','Studio Web','FREE SUPPORT 1 BULAN\r\nJika peserta 2-8 orang Ada Harga Diskon\r\nWaktu Kursus 8 Jam\r\nSudah Termasuk Makan 1 Kali, coffee dan snack\r\nSudah Termasuk Domain dan hosting untuk praktek'),(42,'Jasa Google ads paket eksekutif',6300000,'BULAN','Teknologi','Ada','avatar/ads2.png','Studio Web','Budget Iklan Per Hari Rp. 200.000\r\nFree Riset dan analisa Keyword Potensial\r\nGoogle Search dan Google Display network (GDN)\r\nFree pembuatan copywriting/desain iklan teks\r\nBelum Termasuk Biaya Pembuatan Banner Iklan Jika mau Menggunakan Iklan Google display network\r\nLaporan Iklan maksimal 4 kali'),(43,'Jasa google ads paket joss gandos',5000000,'BULAN','Teknologi','Sibuk','avatar/ads1.png','Studio Web','Budget Iklan Per Hari Rp. 150.000\r\nGRATIS Biaya untuk Analisa dan Seleksi Keyword-Keyword Potensial bila Anda belum punya daftar keyword yang potensial.\r\nGRATIS Biaya Analisa dan Seleksi Keyword Terbaik\r\nLaporan Iklan Anda maksimal 2 X (Dua kali)\r\nMaksimal dibuatkan copywriting/desain iklan teks 3');
/*!40000 ALTER TABLE `provider_postingjasa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `provider_scorejasa`
--

DROP TABLE IF EXISTS `provider_scorejasa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `provider_scorejasa` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nilai` double NOT NULL,
  `jasa` varchar(50) NOT NULL,
  `nama_pelanggan` varchar(30) NOT NULL,
  `nama_jasa_id` varchar(25) NOT NULL,
  `kode_pesan` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `provider_scorejasa_nama_jasa_id_4d51e586_fk_provider_` (`nama_jasa_id`),
  CONSTRAINT `provider_scorejasa_nama_jasa_id_4d51e586_fk_provider_` FOREIGN KEY (`nama_jasa_id`) REFERENCES `provider_bukajasa` (`nama_jasa`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `provider_scorejasa`
--

LOCK TABLES `provider_scorejasa` WRITE;
/*!40000 ALTER TABLE `provider_scorejasa` DISABLE KEYS */;
INSERT INTO `provider_scorejasa` VALUES (12,4,'Pembutan Desain Vector','Saidi','Rizki Desain','dc85e3f4-fa5d-4fa2-a71f-6773828e8434'),(16,5,'Vector manusia halfbody','septi','Rizki Desain','fdfcf907-d2bd-4264-b469-d6b374dd4294'),(17,3,'Sewa mobil pick up','Deni','Mobil Atun Berkah','bd408d7b-200e-4f43-9e1a-51f72537d839'),(19,4,'Vector pet halfbody','deni dwi s','Rizki Desain','c0c7fff3-ff70-4fe8-a787-c80cdfa7d68e'),(20,5,'Sewa mobil pick up','Deni dwi s','Mobil Atun Berkah','06f799e2-f5b6-4e4b-b193-bac01af64346'),(21,3,'Vector manusia halfbody','septi','Rizki Desain','e4bc86ce-a090-4558-b851-6626a48fc3bd');
/*!40000 ALTER TABLE `provider_scorejasa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `register_userprofile`
--

DROP TABLE IF EXISTS `register_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `register_userprofile` (
  `id` int NOT NULL AUTO_INCREMENT,
  `dob` date NOT NULL,
  `gender` varchar(10) NOT NULL,
  `status` varchar(10) NOT NULL,
  `profile_photo` varchar(100) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `register_userprofile_user_id_26b433c2_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `register_userprofile`
--

LOCK TABLES `register_userprofile` WRITE;
/*!40000 ALTER TABLE `register_userprofile` DISABLE KEYS */;
INSERT INTO `register_userprofile` VALUES (5,'2000-09-22','Laki-Laki','Provider','rizki.jpg',6),(18,'2000-05-30','Laki-Laki','Customer','avatar/2018-06-24_02.16.44_2_1.jpg',19),(19,'2000-02-20','Laki-Laki','Customer','avatar/user.png',21),(20,'1975-08-05','Perempuan','Provider','avatar/WhatsApp_Image_2020-12-09_at_10.33.21_a8e1Fbx.jpeg',22),(21,'2001-01-06','Laki-Laki','Customer','avatar/WhatsApp_Image_2020-12-18_at_14.46.09.jpeg',23),(23,'2019-09-19','Laki-Laki','Provider','avatar/logo.png',25),(24,'2000-01-24','Perempuan','Customer','avatar/WhatsApp_Image_2020-12-20_at_21.24.40.jpeg',26);
/*!40000 ALTER TABLE `register_userprofile` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-23 10:57:04

-- MySQL dump 10.13  Distrib 5.7.15, for Linux (x86_64)
--
-- Host: localhost    Database: website
-- ------------------------------------------------------
-- Server version	5.7.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_58c48ba9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_51277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add permission list',6,'add_permissionlist'),(17,'Can change permission list',6,'change_permissionlist'),(18,'Can delete permission list',6,'delete_permissionlist'),(19,'Can add role list',7,'add_rolelist'),(20,'Can change role list',7,'change_rolelist'),(21,'Can delete role list',7,'delete_rolelist'),(22,'Can add user',8,'add_user'),(23,'Can change user',8,'change_user'),(24,'Can delete user',8,'delete_user'),(25,'Can add project',9,'add_project'),(26,'Can change project',9,'change_project'),(27,'Can delete project',9,'delete_project'),(28,'Can add cluster',10,'add_cluster'),(29,'Can change cluster',10,'change_cluster'),(30,'Can delete cluster',10,'delete_cluster'),(31,'Can add pm',11,'add_pm'),(32,'Can change pm',11,'change_pm'),(33,'Can delete pm',11,'delete_pm'),(34,'Can add vm',12,'add_vm'),(35,'Can change vm',12,'change_vm'),(36,'Can delete vm',12,'delete_vm'),(37,'Can add vlan',13,'add_vlan'),(38,'Can change vlan',13,'change_vlan'),(39,'Can delete vlan',13,'delete_vlan'),(40,'Can add vlan group',14,'add_vlangroup'),(41,'Can change vlan group',14,'change_vlangroup'),(42,'Can delete vlan group',14,'delete_vlangroup'),(43,'Can add storage group',15,'add_storagegroup'),(44,'Can change storage group',15,'change_storagegroup'),(45,'Can delete storage group',15,'delete_storagegroup'),(46,'Can add storage',16,'add_storage'),(47,'Can change storage',16,'change_storage'),(48,'Can delete storage',16,'delete_storage'),(49,'Can add software',17,'add_software'),(50,'Can change software',17,'change_software'),(51,'Can delete software',17,'delete_software'),(52,'Can add domain',18,'add_domain'),(53,'Can change domain',18,'change_domain'),(54,'Can delete domain',18,'delete_domain');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cluster`
--

DROP TABLE IF EXISTS `cluster`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cluster` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `clustername` varchar(30) NOT NULL,
  `platform` varchar(30) NOT NULL,
  `vcaddress` char(39) NOT NULL,
  `ttstorage` int(11) NOT NULL,
  `systorage` int(11) NOT NULL,
  `ttcore` int(11) NOT NULL,
  `sycore` int(11) NOT NULL,
  `ttmem` int(11) NOT NULL,
  `symem` int(11) NOT NULL,
  `remark` varchar(200) DEFAULT NULL,
  `storagegroup_id` int(11) NOT NULL,
  `vlangroup_id` int(11) NOT NULL,
  `usedcore` int(11) NOT NULL,
  `usedmem` int(11) NOT NULL,
  `usedstorage` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `clustername` (`clustername`),
  UNIQUE KEY `cluster_storagegroup_id_52270001_uniq` (`storagegroup_id`),
  UNIQUE KEY `cluster_vlangroup_id_181419aa_uniq` (`vlangroup_id`),
  CONSTRAINT `cluster_storagegroup_id_52270001_fk_storagegroup_id` FOREIGN KEY (`storagegroup_id`) REFERENCES `storagegroup` (`id`),
  CONSTRAINT `cluster_vlangroup_id_181419aa_fk_vlangroup_id` FOREIGN KEY (`vlangroup_id`) REFERENCES `vlangroup` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cluster`
--

LOCK TABLES `cluster` WRITE;
/*!40000 ALTER TABLE `cluster` DISABLE KEYS */;
INSERT INTO `cluster` VALUES (1,'DMZ01','VSPHERE','22.188.18.231',32768,32568,256,248,3072,3056,'',9,1,8,16,200),(2,'DMZ02','VSPHERE','22.188.18.231',20480,20480,768,768,6144,6144,'',10,2,0,0,0),(3,'PT01','VSPHERE','61.0.128.194',32768,32768,640,640,4096,4096,'',5,9,0,0,0),(4,'PT02','VSPHERE','61.0.128.194',24576,24576,384,384,2048,2048,'',6,10,0,0,0),(5,'UAT01','VSPHERE','22.188.18.231',16384,15584,320,288,2560,2464,'',1,3,32,96,800),(6,'UAT02','VSPHERE','22.188.18.231',32768,32768,448,448,3072,3072,'',2,4,0,0,0),(7,'UAT03','Hyper-V','61.0.128.200',28672,28672,384,384,2048,2048,'',3,5,0,0,0),(8,'UAT04','Hyper-V','61.0.128.200',28672,28672,384,384,3072,3072,'',4,6,0,0,0),(9,'PRIVATE01','VSPHERE','22.188.18.231',24576,24276,448,436,6144,6120,'',7,7,12,24,300),(10,'PRIVATE02','VSPHERE','22.188.18.231',40960,40960,384,384,4096,4096,'',8,8,0,0,0);
/*!40000 ALTER TABLE `cluster` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_5151027a_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_1c5f563_fk_user_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_5151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_1c5f563_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_3ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(10,'ProjectManage','cluster'),(11,'ProjectManage','pm'),(9,'ProjectManage','project'),(12,'ProjectManage','vm'),(18,'ResourceManage','domain'),(17,'ResourceManage','software'),(16,'ResourceManage','storage'),(15,'ResourceManage','storagegroup'),(13,'ResourceManage','vlan'),(14,'ResourceManage','vlangroup'),(5,'sessions','session'),(6,'UserManage','permissionlist'),(7,'UserManage','rolelist'),(8,'UserManage','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'UserManage','0001_initial','2016-11-09 10:48:08'),(2,'ResourceManage','0001_initial','2016-11-09 10:48:09'),(3,'ProjectManage','0001_initial','2016-11-09 10:48:11'),(4,'ProjectManage','0002_auto_20161108_1120','2016-11-09 10:48:12'),(5,'ProjectManage','0003_auto_20161108_1229','2016-11-09 10:48:13'),(6,'ProjectManage','0004_auto_20161109_0850','2016-11-09 10:48:13'),(7,'ResourceManage','0002_auto_20161108_1120','2016-11-09 10:48:14'),(8,'ResourceManage','0003_auto_20161109_0850','2016-11-09 10:48:14'),(9,'contenttypes','0001_initial','2016-11-09 10:48:15'),(10,'admin','0001_initial','2016-11-09 10:48:15'),(11,'contenttypes','0002_remove_content_type_name','2016-11-09 10:48:15'),(12,'auth','0001_initial','2016-11-09 10:48:16'),(13,'auth','0002_alter_permission_name_max_length','2016-11-09 10:48:16'),(14,'auth','0003_alter_user_email_max_length','2016-11-09 10:48:16'),(15,'auth','0004_alter_user_username_opts','2016-11-09 10:48:16'),(16,'auth','0005_alter_user_last_login_null','2016-11-09 10:48:16'),(17,'auth','0006_require_contenttypes_0002','2016-11-09 10:48:16'),(18,'sessions','0001_initial','2016-11-09 10:48:16');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('4zl1k4zapx7de35x1awvy3mmd4e3p77o','MWRhODExNTI5NjliNjBlZTFhODA4MmFlOWZhNGY4ZTliY2IzMDFjNTp7Il9hdXRoX3VzZXJfaGFzaCI6Ijk3YzA3Y2I1YjI3YmViMzAyOTQyMzlkY2EyMGJjYzIwNTZjOTk1Y2MiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-11-23 13:20:48'),('bgy1bpn5ua5q6lemeaqym003kf0rh43h','NTRjYTVlMTkzM2FlOWQ4NmE3Mjk2Zjg5M2Y3YWQ4ZTQxODgzZWUwYzp7fQ==','2016-11-23 10:48:47'),('nyy27bsulpjuypj87s85d0qipoam4osa','MWRhODExNTI5NjliNjBlZTFhODA4MmFlOWZhNGY4ZTliY2IzMDFjNTp7Il9hdXRoX3VzZXJfaGFzaCI6Ijk3YzA3Y2I1YjI3YmViMzAyOTQyMzlkY2EyMGJjYzIwNTZjOTk1Y2MiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-11-23 10:48:56'),('yag2pqfssi1196i3z1v4kic3gkp0gy3j','MWRhODExNTI5NjliNjBlZTFhODA4MmFlOWZhNGY4ZTliY2IzMDFjNTp7Il9hdXRoX3VzZXJfaGFzaCI6Ijk3YzA3Y2I1YjI3YmViMzAyOTQyMzlkY2EyMGJjYzIwNTZjOTk1Y2MiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-11-23 12:52:22');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `domain`
--

DROP TABLE IF EXISTS `domain`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `domain` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domainname` varchar(30) NOT NULL,
  `DNS` char(39) NOT NULL,
  `remark` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `domainname` (`domainname`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `domain`
--

LOCK TABLES `domain` WRITE;
/*!40000 ALTER TABLE `domain` DISABLE KEYS */;
INSERT INTO `domain` VALUES (1,'uat.bocuat.org','22.188.152.254',''),(2,'dmzint.bocuat.org','26.184.15.254',''),(3,'dmzpv.bocuat.org','26.184.135.254',''),(4,'pt.bocuat.org','22.188.144.254','');
/*!40000 ALTER TABLE `domain` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permissionlist`
--

DROP TABLE IF EXISTS `permissionlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `permissionlist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `url` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permissionlist`
--

LOCK TABLES `permissionlist` WRITE;
/*!40000 ALTER TABLE `permissionlist` DISABLE KEYS */;
INSERT INTO `permissionlist` VALUES (1,'install','/install/'),(2,'project','/project/'),(3,'resource','/resource/'),(4,'accounts','/accounts/');
/*!40000 ALTER TABLE `permissionlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pm`
--

DROP TABLE IF EXISTS `pm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pm` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pmname` varchar(30) NOT NULL,
  `sn` varchar(30) DEFAULT NULL,
  `role` varchar(30) DEFAULT NULL,
  `type` varchar(30) DEFAULT NULL,
  `cpu` int(11) DEFAULT NULL,
  `memory` int(11) DEFAULT NULL,
  `disk` int(11) DEFAULT NULL,
  `os` varchar(30) DEFAULT NULL,
  `eth` int(11) DEFAULT NULL,
  `hba` int(11) DEFAULT NULL,
  `ip` char(39) NOT NULL,
  `ilo_ip` char(39) NOT NULL,
  `mask` char(39) DEFAULT NULL,
  `gateway` char(39) DEFAULT NULL,
  `jiguihao` varchar(30) DEFAULT NULL,
  `jiguiwei` varchar(30) DEFAULT NULL,
  `hba_wwn` varchar(30) DEFAULT NULL,
  `position` varchar(30) DEFAULT NULL,
  `ttstorage` int(11) DEFAULT NULL,
  `systorage` int(11) DEFAULT NULL,
  `sycore` int(11) DEFAULT NULL,
  `symem` int(11) DEFAULT NULL,
  `remark` varchar(30) DEFAULT NULL,
  `cluster_id` int(11) DEFAULT NULL,
  `domain_id` int(11) DEFAULT NULL,
  `project_id` int(11) DEFAULT NULL,
  `soft_id` int(11) DEFAULT NULL,
  `storagegroup_id` int(11) DEFAULT NULL,
  `vlangroup_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `pmname` (`pmname`),
  KEY `pm_cluster_id_6dbdb5e8_fk_cluster_id` (`cluster_id`),
  KEY `pm_domain_id_43a4cc1d_fk_domain_id` (`domain_id`),
  KEY `pm_b098ad43` (`project_id`),
  KEY `pm_aca54406` (`soft_id`),
  KEY `pm_b22ccbed` (`storagegroup_id`),
  KEY `pm_17e18949` (`vlangroup_id`),
  CONSTRAINT `pm_cluster_id_6dbdb5e8_fk_cluster_id` FOREIGN KEY (`cluster_id`) REFERENCES `cluster` (`id`),
  CONSTRAINT `pm_domain_id_43a4cc1d_fk_domain_id` FOREIGN KEY (`domain_id`) REFERENCES `domain` (`id`),
  CONSTRAINT `pm_project_id_37aeb4f_fk_project_id` FOREIGN KEY (`project_id`) REFERENCES `project` (`id`),
  CONSTRAINT `pm_soft_id_71e8753b_fk_software_id` FOREIGN KEY (`soft_id`) REFERENCES `software` (`id`),
  CONSTRAINT `pm_storagegroup_id_3f35de0d_fk_storagegroup_id` FOREIGN KEY (`storagegroup_id`) REFERENCES `storagegroup` (`id`),
  CONSTRAINT `pm_vlangroup_id_53e8ac64_fk_vlangroup_id` FOREIGN KEY (`vlangroup_id`) REFERENCES `vlangroup` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pm`
--

LOCK TABLES `pm` WRITE;
/*!40000 ALTER TABLE `pm` DISABLE KEYS */;
INSERT INTO `pm` VALUES (1,'UAT01SZ01','123DF78G9','物理集群宿主机','IBM ',64,512,100,'ESXI5.5',4,2,'22.188.18.100','22.188.19.100','255.255.255.0','22.188.18.1','45','GG8','','2C',NULL,NULL,NULL,NULL,'',5,NULL,NULL,NULL,NULL,NULL),(2,'UAT01SZ02','123DF78G8','物理集群宿主机','IBM ',128,1024,100,'ESXI5.5',4,2,'22.188.18.101','22.188.19.101','255.255.255.0','22.188.18.1','46','GG8','','2C',NULL,NULL,NULL,NULL,'',5,NULL,NULL,NULL,NULL,NULL),(3,'UAT01SZ03','123DF78G7','物理集群宿主机','IBM ',128,1024,100,'ESXI5.5',4,2,'22.188.18.102','22.188.19.102','255.255.255.0','22.188.18.1','46','GG6','','2C',NULL,NULL,NULL,NULL,'',5,NULL,NULL,NULL,NULL,NULL),(4,'UAT02SZ01','223DF78G7','物理集群宿主机','IBM ',64,1024,100,'ESXI5.5',4,2,'22.188.18.103','22.188.19.103','255.255.255.0','22.188.18.1','47','GG5','','2C',NULL,NULL,NULL,NULL,'',6,NULL,NULL,NULL,NULL,NULL),(5,'UAT02SZ02','223DF78G8','物理集群宿主机','IBM ',128,1024,100,'ESXI5.5',4,2,'22.188.18.104','22.188.19.104','255.255.255.0','22.188.18.1','47','GG4','','2C',NULL,NULL,NULL,NULL,'',6,NULL,NULL,NULL,NULL,NULL),(6,'UAT02SZ03','323DF78G8','物理集群宿主机','IBM ',256,1024,100,'ESXI5.5',4,2,'22.188.18.105','22.188.19.105','255.255.255.0','22.188.18.1','48','GG4','','2C',NULL,NULL,NULL,NULL,'',6,NULL,NULL,NULL,NULL,NULL),(7,'PT01SZ01','323DF78G1','物理集群宿主机','IBM ',256,1024,100,'ESXI5.5',4,2,'22.188.18.106','22.188.19.106','255.255.255.0','22.188.18.1','48','GG3','','2C',NULL,NULL,NULL,NULL,'',3,NULL,NULL,NULL,NULL,NULL),(8,'PT01SZ02','323DF78G2','物理集群宿主机','IBM ',256,1024,100,'ESXI5.5',4,2,'22.188.18.107','22.188.19.107','255.255.255.0','22.188.18.1','48','GG2','','2C',NULL,NULL,NULL,NULL,'',3,NULL,NULL,NULL,NULL,NULL),(9,'PT01SZ03','333DF78G5','物理集群宿主机','IBM ',128,2048,100,'ESXI5.5',4,2,'22.188.18.108','22.188.19.108','255.255.255.0','22.188.18.1','49','GG2','','2C',NULL,NULL,NULL,NULL,'',3,NULL,NULL,NULL,NULL,NULL),(10,'PV01SZ01','333DF78G5','物理集群宿主机','IBM ',128,2048,100,'ESXI5.5',4,2,'22.188.18.109','22.188.19.109','255.255.255.0','22.188.18.1','50','GG2','','2C',NULL,NULL,NULL,NULL,'',9,NULL,NULL,NULL,NULL,NULL),(11,'PV01SZ02','333DF78G6','物理集群宿主机','IBM ',64,2048,100,'ESXI5.5',4,2,'22.188.18.110','22.188.19.110','255.255.255.0','22.188.18.1','52','GG2','','2C',NULL,NULL,NULL,NULL,'',9,NULL,NULL,NULL,NULL,NULL),(12,'PV01SZ03','333DF78G8','物理集群宿主机','IBM ',256,2048,100,'ESXI5.5',4,2,'22.188.18.111','22.188.19.111','255.255.255.0','22.188.18.1','50','GG2','','2C',NULL,NULL,NULL,NULL,'',9,NULL,NULL,NULL,NULL,NULL),(13,'DMZ01SZ01','433DF78G8','物理集群宿主机','IBM ',128,2048,100,'ESXI6.0',4,2,'22.188.18.112','22.188.19.112','255.255.255.0','22.188.18.1','51','GG2','','2C',NULL,NULL,NULL,NULL,'',1,NULL,NULL,NULL,NULL,NULL),(14,'DMZ01SZ02','433DF78G6','物理集群宿主机','IBM ',128,1024,100,'ESXI6.0',4,2,'22.188.18.113','22.188.19.113','255.255.255.0','22.188.18.1','51','GG1','','2C',NULL,NULL,NULL,NULL,'',1,NULL,NULL,NULL,NULL,NULL),(15,'UAT03SZ01','433DF78G6','物理集群宿主机','IBM ',128,1024,100,'WINDOW SERVER 2012R2',4,2,'22.188.18.114','22.188.19.114','255.255.255.0','22.188.18.1','51','GG1','','2C',NULL,NULL,NULL,NULL,'',7,NULL,NULL,NULL,NULL,NULL),(16,'UAT03SZ02','433DF78G4','物理集群宿主机','IBM ',256,1024,100,'WINDOW SERVER 2012R2',4,2,'22.188.18.115','22.188.19.115','255.255.255.0','22.188.18.1','52','GG1','','2C',NULL,NULL,NULL,NULL,'',7,NULL,NULL,NULL,NULL,NULL),(17,'UAT04SZ01','443DF78G4','物理集群宿主机','IBM ',128,1024,100,'WINDOW SERVER 2012R2',4,2,'22.188.18.116','22.188.19.116','255.255.255.0','22.188.18.1','52','GG2','','2C',NULL,NULL,NULL,NULL,'',8,NULL,NULL,NULL,NULL,NULL),(18,'UAT04SZ02','444DF78G4','物理集群宿主机','IBM ',256,2048,100,'WINDOW SERVER 2012R2',4,2,'22.188.18.117','22.188.19.117','255.255.255.0','22.188.18.1','52','GG3','','2C',NULL,NULL,NULL,NULL,'',8,NULL,NULL,NULL,NULL,NULL),(19,'DMZ02SZ01','445DF78G4','物理集群宿主机','IBM ',256,2048,100,'ESXI5.5',4,2,'22.188.18.118','22.188.19.118','255.255.255.0','22.188.18.1','53','GG3','','2C',NULL,NULL,NULL,NULL,'',2,NULL,NULL,NULL,NULL,NULL),(20,'DMZ02SZ02','445DF78G6','物理集群宿主机','IBM ',256,2048,100,'ESXI5.5',4,2,'22.188.18.119','22.188.19.119','255.255.255.0','22.188.18.1','54','GG4','','2C',NULL,NULL,NULL,NULL,'',2,NULL,NULL,NULL,NULL,NULL),(21,'DMZ02SZ03','445DF78G5','物理集群宿主机','IBM ',256,2048,100,'ESXI5.5',4,2,'22.188.18.120','22.188.19.120','255.255.255.0','22.188.18.1','53','GG4','','2C',NULL,NULL,NULL,NULL,'',2,NULL,NULL,NULL,NULL,NULL),(22,'PV02SZ01','445DF78G9','物理集群宿主机','IBM ',256,2048,100,'ESXI5.5',4,2,'22.188.18.121','22.188.19.121','255.255.255.0','22.188.18.1','55','GG4','','2C',NULL,NULL,NULL,NULL,'',10,NULL,NULL,NULL,NULL,NULL),(23,'PV02SZ02','446DF78G9','物理集群宿主机','IBM ',128,2048,100,'ESXI5.5',4,2,'22.188.18.122','22.188.19.122','255.255.255.0','22.188.18.1','54','GG3','','2C',NULL,NULL,NULL,NULL,'',10,NULL,NULL,NULL,NULL,NULL),(24,'PT02SZ01','326DF78G1','物理集群宿主机','IBM ',256,1024,100,'ESXI5.5',4,2,'22.188.18.123','22.188.19.123','255.255.255.0','22.188.18.1','23','GG3','','2C',NULL,NULL,NULL,NULL,'',4,NULL,NULL,NULL,NULL,NULL),(25,'PT02SZ02','326DF78G2','物理集群宿主机','IBM ',128,1024,100,'ESXI5.5',4,2,'22.188.18.124','22.188.19.124','255.255.255.0','22.188.18.1','24','GG3','','2C',NULL,NULL,NULL,NULL,'',4,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `pm` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `project` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `env` varchar(30) DEFAULT NULL,
  `projectname` varchar(30) NOT NULL,
  `shortname` varchar(30) DEFAULT NULL,
  `starttime` datetime DEFAULT NULL,
  `endtime` datetime DEFAULT NULL,
  `finishtime` datetime DEFAULT NULL,
  `reason` varchar(200) DEFAULT NULL,
  `batch` varchar(10) DEFAULT NULL,
  `remark` varchar(200) DEFAULT NULL,
  `createuser_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `project_createuser_id_4f13f0f5_fk_user_id` (`createuser_id`),
  CONSTRAINT `project_createuser_id_4f13f0f5_fk_user_id` FOREIGN KEY (`createuser_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project`
--

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
INSERT INTO `project` VALUES (1,'T1','中银易商','EZUC','2016-11-09 02:30:00','2016-11-18 09:30:00','2016-11-16 09:30:00','','P606','',2),(2,'T4','网银特色云平台（湖南）','CSP','2016-11-08 02:30:00','2016-11-19 02:30:00','2016-11-14 09:30:00','','P701','',4);
/*!40000 ALTER TABLE `project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rolelist`
--

DROP TABLE IF EXISTS `rolelist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rolelist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rolelist`
--

LOCK TABLES `rolelist` WRITE;
/*!40000 ALTER TABLE `rolelist` DISABLE KEYS */;
INSERT INTO `rolelist` VALUES (1,'admin'),(2,'user');
/*!40000 ALTER TABLE `rolelist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rolelist_permission`
--

DROP TABLE IF EXISTS `rolelist_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rolelist_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rolelist_id` int(11) NOT NULL,
  `permissionlist_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `rolelist_id` (`rolelist_id`,`permissionlist_id`),
  KEY `rolelist_permiss_permissionlist_id_7859adb0_fk_permissionlist_id` (`permissionlist_id`),
  CONSTRAINT `rolelist_permiss_permissionlist_id_7859adb0_fk_permissionlist_id` FOREIGN KEY (`permissionlist_id`) REFERENCES `permissionlist` (`id`),
  CONSTRAINT `rolelist_permission_rolelist_id_d5476a7_fk_rolelist_id` FOREIGN KEY (`rolelist_id`) REFERENCES `rolelist` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rolelist_permission`
--

LOCK TABLES `rolelist_permission` WRITE;
/*!40000 ALTER TABLE `rolelist_permission` DISABLE KEYS */;
INSERT INTO `rolelist_permission` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,2,1),(6,2,2),(7,2,3);
/*!40000 ALTER TABLE `rolelist_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `software`
--

DROP TABLE IF EXISTS `software`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `software` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `softwarename` varchar(30) NOT NULL,
  `version` varchar(30) NOT NULL,
  `platform` varchar(30) NOT NULL,
  `arch` varchar(10) NOT NULL,
  `doc` varchar(100) DEFAULT NULL,
  `path` varchar(100) DEFAULT NULL,
  `type` varchar(30) NOT NULL,
  `remark` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `software`
--

LOCK TABLES `software` WRITE;
/*!40000 ALTER TABLE `software` DISABLE KEYS */;
INSERT INTO `software` VALUES (1,'apache','2.2.15','Linux','X86_64','','','中间件',''),(2,'jboss','6.4','All','X86_64','','','中间件',''),(3,'was','8.5.5.8','All','X86_64','','','中间件',''),(4,'oracle','11.2.0.4','Linux','X86_64','','','数据库',''),(5,'mysql','5.6.27','Linux','X86_64','','','数据库',''),(6,'sqlserver','2014','Window','X86_64','','','数据库',''),(7,'mongodb','3.2.3','Linux','X86_64','','','数据库',''),(8,'gpfs','3.5.0.22','Linux','X86_64','','','中间件',''),(9,'rhel6.7','6.7','Linux','X86_64','','','操作系统','');
/*!40000 ALTER TABLE `software` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `storage`
--

DROP TABLE IF EXISTS `storage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `storage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `storagename` varchar(100) NOT NULL,
  `storagesize` int(11) NOT NULL,
  `storagetype` varchar(30) NOT NULL,
  `raidtype` varchar(30) NOT NULL,
  `remark` varchar(200) DEFAULT NULL,
  `storagegroup_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `storagename` (`storagename`),
  KEY `storage_b22ccbed` (`storagegroup_id`),
  CONSTRAINT `storage_storagegroup_id_169541e_fk_storagegroup_id` FOREIGN KEY (`storagegroup_id`) REFERENCES `storagegroup` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `storage`
--

LOCK TABLES `storage` WRITE;
/*!40000 ALTER TABLE `storage` DISABLE KEYS */;
INSERT INTO `storage` VALUES (1,'UAT01-HW-001-RAID5',8192,'HUAWEI','RAID5','',1),(2,'UAT01-HW-002-RAID5',8192,'HUAWEI','RAID5','',1),(3,'UAT02-EMC-001-RAID10',16384,'EMC','RAID1+0','',2),(4,'UAT02-EMC-002-RAID10',16384,'EMC','RAID1+0','',2),(5,'UAT03-HDS-001-RAID1',4096,'HDS','RAID1','',3),(6,'UAT03-HDS-002-RAID1',8192,'HDS','RAID1','',3),(7,'UAT03-HDS-003-RAID1',16384,'HDS','RAID1','',3),(8,'UAT04-HW-001-RAID1',8192,'HUAWEI','RAID1','',4),(9,'UAT04-HW-002-RAID1',4096,'HUAWEI','RAID1','',4),(10,'UAT04-HW-003-RAID5',16384,'HUAWEI','RAID5','',4),(11,'PT01-HW-001-RAID10',16384,'HUAWEI','RAID1+0','',5),(12,'PT01-HW-002-RAID10',16384,'HUAWEI','RAID1+0','',5),(13,'PT02-HW-001-RAID10',16384,'HUAWEI','RAID1+0','',6),(14,'PT02-HW-002-RAID10',8192,'HUAWEI','RAID1+0','',6),(15,'PV01-EMC-001-RAID10',16384,'EMC','RAID1+0','',7),(16,'PV01-EMC-002-RAID10',4096,'EMC','RAID1+0','',7),(17,'PV01-EMC-003-RAID10',4096,'EMC','RAID1+0','',7),(18,'PV02-EMC-001-RAID5',16384,'EMC','RAID5','',8),(19,'PV02-EMC-002-RAID5',8192,'EMC','RAID5','',8),(20,'PV02-EMC-003-RAID1',16384,'EMC','RAID1','',8),(21,'DMZ01-HDS-001-RAID10',16384,'HDS','RAID1+0','',9),(22,'DMZ01-HDS-002-RAID10',16384,'HDS','RAID1+0','',9),(23,'DMZ02-HDS-001-RAID5',4096,'HDS','RAID5','',10),(24,'DMZ02-HDS-002-RAID5',16384,'HDS','RAID5','',10);
/*!40000 ALTER TABLE `storage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `storagegroup`
--

DROP TABLE IF EXISTS `storagegroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `storagegroup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `storagegroupname` varchar(30) NOT NULL,
  `remark` varchar(200) DEFAULT NULL,
  `systorage` int(11) NOT NULL,
  `ttstorage` int(11) NOT NULL,
  `usedstorage` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `storagegroupname` (`storagegroupname`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `storagegroup`
--

LOCK TABLES `storagegroup` WRITE;
/*!40000 ALTER TABLE `storagegroup` DISABLE KEYS */;
INSERT INTO `storagegroup` VALUES (1,'UAT01','UAT01存储组',15584,16384,800),(2,'UAT02','UAT02存储组',32768,32768,0),(3,'UAT03','UAT03存储组',28672,28672,0),(4,'UAT04','UAT04存储组',28672,28672,0),(5,'PT01','PT01存储组',32768,32768,0),(6,'PT02','PT02存储组',24576,24576,0),(7,'PRIVATE01','PRIVATE01专线存储组',24276,24576,300),(8,'PRIVATE02','PRIVATE02专线存储组',40960,40960,0),(9,'DMZ01','DMZ01存储组',32568,32768,200),(10,'DMZ02','DMZ02存储组',20480,20480,0);
/*!40000 ALTER TABLE `storagegroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `username` varchar(40) NOT NULL,
  `email` varchar(255) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `nickname` varchar(64) DEFAULT NULL,
  `sex` varchar(2) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `user_84566833` (`role_id`),
  CONSTRAINT `user_role_id_16e9a8c3_fk_rolelist_id` FOREIGN KEY (`role_id`) REFERENCES `rolelist` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'pbkdf2_sha256$20000$7YXaeYAD6ckQ$HFS067xbS0zd9qf21YWM9QD66byCWCbtUHU0v5e2ZUU=','2016-11-09 13:20:48','admin','admin@boc.com',1,1,'管理员','男',1),(2,'pbkdf2_sha256$20000$Gb6dN3ttde6p$UwX2xZU5TC0UnItlW+XxQWGfSSI0fE8fveL8MEbap6k=',NULL,'pengyc','pengyc@boc.com',1,0,'彭远春','男',1),(3,'pbkdf2_sha256$20000$DFFz8vEH7e9W$LOVX055hp1KIhgqLr/mi4jrpShDfw5Sog/zRnGZdDcA=',NULL,'shixy','shixy@boc.com',1,0,'施小燕','女',2),(4,'pbkdf2_sha256$20000$k8AmJhNiAy7E$lRmS5DVaEzkBF7Kn6hhuu7Ak4bxtC6CUhd3Qab52uHs=',NULL,'hangqr','hangqr@boc.com',1,0,'杭启荣','男',2),(5,'pbkdf2_sha256$20000$7UVfDaQUXRAU$INjn2ph4GNPsYMSoP3TOnVfItyNBTSP3qIBdUSDfJt0=',NULL,'zhanghao','zhanghao@boc.com',1,0,'张皓','男',2);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vlan`
--

DROP TABLE IF EXISTS `vlan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vlan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vlanname` char(39) NOT NULL,
  `startip` int(11) NOT NULL,
  `endip` int(11) NOT NULL,
  `gateway` char(39) NOT NULL,
  `mask` char(39) NOT NULL,
  `remark` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `vlanname` (`vlanname`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vlan`
--

LOCK TABLES `vlan` WRITE;
/*!40000 ALTER TABLE `vlan` DISABLE KEYS */;
INSERT INTO `vlan` VALUES (1,'22.188.41.0',16,254,'22.188.41.1','255.255.255.0','内网网段'),(2,'22.188.42.0',16,254,'22.188.42.1','255.255.255.0','内网网段'),(3,'22.188.43.0',16,254,'22.188.43.1','255.255.255.0','内网网段'),(4,'22.188.44.0',16,254,'22.188.44.1','255.255.255.0','内网网段'),(5,'26.184.15.0',16,253,'26.184.15.1','255.255.255.0','DMZ网段'),(6,'26.184.17.0',16,254,'26.184.17.1','255.255.255.0','DMZ网段'),(7,'26.184.135.0',16,253,'26.184.135.1','255.255.255.0','专线区网段'),(8,'26.184.136.0',16,254,'26.184.136.1','255.255.255.0','专线区网段'),(9,'22.188.143.0',16,254,'22.188.143.0','255.255.255.0','PT网段'),(10,'22.188.144.0',16,253,'22.188.144.1','255.255.255.0','PT网段');
/*!40000 ALTER TABLE `vlan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vlangroup`
--

DROP TABLE IF EXISTS `vlangroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vlangroup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vlangroupname` varchar(30) NOT NULL,
  `remark` varchar(200) DEFAULT NULL,
  `syip` int(11) NOT NULL,
  `ttip` int(11) NOT NULL,
  `usedip` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `vlangroupname` (`vlangroupname`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vlangroup`
--

LOCK TABLES `vlangroup` WRITE;
/*!40000 ALTER TABLE `vlangroup` DISABLE KEYS */;
INSERT INTO `vlangroup` VALUES (1,'DMZ01','DMZ01网段',0,0,0),(2,'DMZ02','DMZ02网段',0,0,0),(3,'UAT01','UAT01网段',0,0,0),(4,'UAT02','UAT02网段',0,0,0),(5,'UAT03','UAT03网段',0,0,0),(6,'UAT04','UAT04网段',0,0,0),(7,'PRIVATE01','PRIVATE01专线网段组',0,0,0),(8,'PRIVATE02','PRIVATE02专线网段组',0,0,0),(9,'PT01','PT01网段组',0,0,0),(10,'PT02','PT02网段',0,0,0);
/*!40000 ALTER TABLE `vlangroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vlangroup_vlan`
--

DROP TABLE IF EXISTS `vlangroup_vlan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vlangroup_vlan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vlangroup_id` int(11) NOT NULL,
  `vlan_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `vlangroup_id` (`vlangroup_id`,`vlan_id`),
  KEY `vlangroup_vlan_vlan_id_3c63ccf7_fk_vlan_id` (`vlan_id`),
  CONSTRAINT `vlangroup_vlan_vlan_id_3c63ccf7_fk_vlan_id` FOREIGN KEY (`vlan_id`) REFERENCES `vlan` (`id`),
  CONSTRAINT `vlangroup_vlan_vlangroup_id_4349c665_fk_vlangroup_id` FOREIGN KEY (`vlangroup_id`) REFERENCES `vlangroup` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vlangroup_vlan`
--

LOCK TABLES `vlangroup_vlan` WRITE;
/*!40000 ALTER TABLE `vlangroup_vlan` DISABLE KEYS */;
INSERT INTO `vlangroup_vlan` VALUES (1,1,5),(2,1,6),(3,2,6),(4,3,1),(5,3,2),(6,4,2),(7,4,3),(10,5,3),(11,5,4),(12,6,4),(14,7,7),(13,7,8),(15,8,8),(16,9,9),(17,9,10),(18,10,10);
/*!40000 ALTER TABLE `vlangroup_vlan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vm`
--

DROP TABLE IF EXISTS `vm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vm` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vmname` varchar(30) NOT NULL,
  `role` varchar(30) DEFAULT NULL,
  `batch` varchar(30) DEFAULT NULL,
  `env` varchar(30) DEFAULT NULL,
  `os` varchar(30) NOT NULL,
  `cpu` int(11) DEFAULT NULL,
  `mem` int(11) DEFAULT NULL,
  `disk` int(11) DEFAULT NULL,
  `ip` char(39) NOT NULL,
  `mask` char(39) DEFAULT NULL,
  `gateway` char(39) DEFAULT NULL,
  `admin` varchar(30) DEFAULT NULL,
  `appuser` varchar(30) DEFAULT NULL,
  `remark` varchar(200) DEFAULT NULL,
  `cluster_id` int(11) DEFAULT NULL,
  `domain_id` int(11) DEFAULT NULL,
  `pm_id` int(11) DEFAULT NULL,
  `project_id` int(11) DEFAULT NULL,
  `soft_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `vmname` (`vmname`),
  KEY `vm_cluster_id_1a04efba_fk_cluster_id` (`cluster_id`),
  KEY `vm_domain_id_6e2bd34b_fk_domain_id` (`domain_id`),
  KEY `vm_pm_id_762aa674_fk_pm_id` (`pm_id`),
  KEY `vm_project_id_72c22df1_fk_project_id` (`project_id`),
  KEY `vm_soft_id_67e491f3_fk_software_id` (`soft_id`),
  CONSTRAINT `vm_cluster_id_1a04efba_fk_cluster_id` FOREIGN KEY (`cluster_id`) REFERENCES `cluster` (`id`),
  CONSTRAINT `vm_domain_id_6e2bd34b_fk_domain_id` FOREIGN KEY (`domain_id`) REFERENCES `domain` (`id`),
  CONSTRAINT `vm_pm_id_762aa674_fk_pm_id` FOREIGN KEY (`pm_id`) REFERENCES `pm` (`id`),
  CONSTRAINT `vm_project_id_72c22df1_fk_project_id` FOREIGN KEY (`project_id`) REFERENCES `project` (`id`),
  CONSTRAINT `vm_soft_id_67e491f3_fk_software_id` FOREIGN KEY (`soft_id`) REFERENCES `software` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vm`
--

LOCK TABLES `vm` WRITE;
/*!40000 ALTER TABLE `vm` DISABLE KEYS */;
INSERT INTO `vm` VALUES (1,'T1REZUCWEB01','WEB服务器','P606','T1','RHEL6.7',4,8,100,'22.188.41.186','255.255.255.0','22.188.41.1','root','ezuc',NULL,5,1,NULL,1,1),(2,'T1REZUCWEB02','WEB服务器','P606','T1','RHEL6.7',4,8,100,'22.188.41.187','255.255.255.0','22.188.41.1','root','ezuc',NULL,5,1,NULL,1,1),(3,'T1REZUCDB01','数据库服务器','P606','T1','RHEL6.7',4,8,100,'22.188.41.188','255.255.255.0','22.188.41.1','root','ezuc',NULL,5,1,NULL,1,4),(4,'T1REZUCDB02','数据库服务器','P606','T1','RHEL6.7',4,8,100,'22.188.41.189','255.255.255.0','22.188.41.1','root','ezuc',NULL,5,1,NULL,1,4),(5,'T1REZUCQZ02','前置机','P606','T1','RHEL6.7',4,8,100,'26.184.15.200','255.255.255.0','26.184.15.1','root','ezuc',NULL,1,2,NULL,1,1),(6,'T1REZUCQZ01','前置机','P606','T1','RHEL6.7',4,8,100,'26.184.135.200','255.255.255.0','26.184.135.1','root','ezuc',NULL,9,3,NULL,1,1),(7,'T4RCSPQZ01','前置机','P701','T4','RHEL6.7',4,8,100,'26.184.135.201','255.255.255.0','26.184.135.1','root','bochn',NULL,9,3,NULL,2,1),(8,'T4RCSPQZ02','前置机','P701','T4','RHEL6.7',4,8,100,'26.184.135.202','255.255.255.0','26.184.135.1','root','bochn',NULL,9,3,NULL,2,1),(9,'T4RCSPQZ03','前置机','P701','T4','RHEL6.7',4,8,100,'26.184.15.201','255.255.255.0','26.184.15.1','root','bochn',NULL,1,2,NULL,2,1),(10,'T4RCSPWEB01','WEB服务器','P701','T4','RHEL6.7',4,16,100,'22.188.41.190','255.255.255.0','22.188.41.1','root','bochn',NULL,5,1,NULL,2,1),(11,'T4RCSPWEB02','WEB服务器','P701','T4','RHEL6.7',4,16,100,'22.188.41.191','255.255.255.0','22.188.41.1','root','bochn',NULL,5,1,NULL,2,1),(12,'T4RCSPAPP01','应用服务器','P701','T4','RHEL6.7',4,16,100,'22.188.41.192','255.255.255.0','22.188.41.1','root','bochn',NULL,5,1,NULL,2,2),(13,'T4RCSPAPP02','应用服务器','P701','T4','RHEL6.7',4,16,100,'22.188.41.193','255.255.255.0','22.188.41.1','root','bochn',NULL,5,1,NULL,2,2),(14,'T4RCSPAPP03','应用服务器','P701','T4','RHEL6.7',4,12,100,'22.188.41.194','255.255.255.0','22.188.41.1','root','bochn',NULL,5,1,NULL,2,2),(15,'T4RCSPAPP04','应用服务器','P701','T4','RHEL6.7',4,12,100,'22.188.41.195','255.255.255.0','22.188.41.1','root','bochn',NULL,5,1,NULL,2,2);
/*!40000 ALTER TABLE `vm` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-11-10  0:43:30

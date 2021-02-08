CREATE SCHEMA IF NOT EXISTS `online_courses` DEFAULT CHARACTER SET utf8 ;
USE `online_courses` ;

CREATE TABLE IF NOT EXISTS `online_courses`.`locale` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `locale` VARCHAR(45) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '')
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `online_courses`.`content_type` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `name` VARCHAR(90) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '')
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `online_courses`.`permissions` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `name` VARCHAR(45) NOT NULL COMMENT '',
  `content_type_id` INT(11) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  INDEX `fk_permissions_content_type1_idx` (`content_type_id` ASC)  COMMENT '',
  CONSTRAINT `fk_permissions_content_type1`
    FOREIGN KEY (`content_type_id`)
    REFERENCES `online_courses`.`content_type` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `online_courses`.`user_group` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '')
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `online_courses`.`user_group_has_permissions` (
  `user_group_id` INT(11) NOT NULL COMMENT '',
  `permissions_id` INT(11) NOT NULL COMMENT '',
  PRIMARY KEY (`user_group_id`, `permissions_id`)  COMMENT '',
  INDEX `fk_user_group_has_permissions_permissions1_idx` (`permissions_id` ASC)  COMMENT '',
  INDEX `fk_user_group_has_permissions_user_group1_idx` (`user_group_id` ASC)  COMMENT '',
  CONSTRAINT `fk_user_group_has_permissions_user_group1`
    FOREIGN KEY (`user_group_id`)
    REFERENCES `online_courses`.`user_group` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_group_has_permissions_permissions1`
    FOREIGN KEY (`permissions_id`)
    REFERENCES `online_courses`.`permissions` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `online_courses`.`course` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `startdate` DATETIME NOT NULL COMMENT '',
  `enddate` DATETIME NOT NULL COMMENT '',
  `description` VARCHAR(1000) NOT NULL COMMENT '',
  `structure` VARCHAR(1000) NOT NULL COMMENT '',
  `stuff` INT(11) NOT NULL COMMENT '',
  `locale_id` INT(11) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  INDEX `fk_course_user_group1_idx` (`stuff` ASC)  COMMENT '',
  INDEX `fk_course_locale1_idx` (`locale_id` ASC)  COMMENT '',
  CONSTRAINT `fk_course_locale1`
    FOREIGN KEY (`locale_id`)
    REFERENCES `online_courses`.`locale` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_course_user_group1`
    FOREIGN KEY (`stuff`)
    REFERENCES `online_courses`.`user_group` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `online_courses`.`module` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `name` VARCHAR(45) NOT NULL COMMENT '',
  `start_date` DATETIME NOT NULL COMMENT '',
  `soft_deadline` DATETIME NOT NULL COMMENT '',
  `hard_deadline` DATETIME NOT NULL COMMENT '',
  `course_id` INT(11) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  INDEX `fk_module_course1_idx` (`course_id` ASC)  COMMENT '',
  CONSTRAINT `fk_module_course1`
    FOREIGN KEY (`course_id`)
    REFERENCES `online_courses`.`course` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `online_courses`.`lesson` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `max_grade` INT(11) NOT NULL COMMENT '',
  `content` VARCHAR(1000) NOT NULL COMMENT '',
  `module_id` INT(11) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  INDEX `fk_lesson_module1_idx` (`module_id` ASC)  COMMENT '',
  CONSTRAINT `fk_lesson_module1`
    FOREIGN KEY (`module_id`)
    REFERENCES `online_courses`.`module` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `online_courses`.`task` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `state` VARCHAR(45) NOT NULL COMMENT '',
  `condition` VARCHAR(1024) NOT NULL COMMENT '',
  `created` DATETIME NOT NULL COMMENT '',
  `updated` DATETIME NOT NULL COMMENT '',
  `solution` VARCHAR(1000) NULL DEFAULT NULL COMMENT '',
  `lesson_id` INT(11) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  INDEX `fk_task_lesson1_idx` (`lesson_id` ASC)  COMMENT '',
  CONSTRAINT `fk_task_lesson1`
    FOREIGN KEY (`lesson_id`)
    REFERENCES `online_courses`.`lesson` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `online_courses`.`user` (
  `first_name` VARCHAR(45) NOT NULL COMMENT '',
  `last_name` VARCHAR(45) NOT NULL COMMENT '',
  `email` VARCHAR(70) NOT NULL COMMENT '',
  `password` VARCHAR(140) NOT NULL COMMENT '',
  `is_stuff` TINYINT(1) NOT NULL COMMENT '',
  `is_active` TINYINT(1) NOT NULL COMMENT '',
  `last_login` DATETIME NOT NULL COMMENT '',
  `date_joined` DATETIME NOT NULL COMMENT '',
  PRIMARY KEY (`email`)  COMMENT '')
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `online_courses`.`submission` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `created_at` DATETIME NOT NULL COMMENT '',
  `completed_at` DATETIME NOT NULL COMMENT '',
  `content` VARCHAR(1000) NOT NULL COMMENT '',
  `task_id` INT(11) NOT NULL COMMENT '',
  `user_email` VARCHAR(70) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  INDEX `fk_submission_task1_idx` (`task_id` ASC)  COMMENT '',
  INDEX `fk_submission_user1_idx` (`user_email` ASC)  COMMENT '',
  CONSTRAINT `fk_submission_task1`
    FOREIGN KEY (`task_id`)
    REFERENCES `online_courses`.`task` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_submission_user1`
    FOREIGN KEY (`user_email`)
    REFERENCES `online_courses`.`user` (`email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `online_courses`.`assessment` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `score` INT(11) NOT NULL COMMENT '',
  `scored_at` DATETIME NOT NULL COMMENT '',
  `feedback` VARCHAR(1000) NOT NULL COMMENT '',
  `submission_id` INT(11) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  INDEX `fk_assessment_submission1_idx` (`submission_id` ASC)  COMMENT '',
  CONSTRAINT `fk_assessment_submission1`
    FOREIGN KEY (`submission_id`)
    REFERENCES `online_courses`.`submission` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `online_courses`.`certificate` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `created` DATETIME NOT NULL COMMENT '',
  `modified` DATETIME NOT NULL COMMENT '',
  `name` VARCHAR(300) NOT NULL COMMENT '',
  `description` VARCHAR(300) NOT NULL COMMENT '',
  `is_active` TINYINT(1) NOT NULL COMMENT '',
  `course_id` INT(11) NOT NULL COMMENT '',
  `user_email` VARCHAR(70) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  INDEX `fk_certificate_course1_idx` (`course_id` ASC)  COMMENT '',
  INDEX `fk_certificate_user1_idx` (`user_email` ASC)  COMMENT '',
  CONSTRAINT `fk_certificate_course1`
    FOREIGN KEY (`course_id`)
    REFERENCES `online_courses`.`course` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_certificate_user1`
    FOREIGN KEY (`user_email`)
    REFERENCES `online_courses`.`user` (`email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `online_courses`.`country` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '')
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `online_courses`.`city` (
  `id` INT(11) NOT NULL COMMENT '',
  `country_id` INT(11) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  INDEX `fk_city_country1_idx` (`country_id` ASC)  COMMENT '',
  CONSTRAINT `fk_city_country1`
    FOREIGN KEY (`country_id`)
    REFERENCES `online_courses`.`country` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `online_courses`.`city_translate` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `translate` VARCHAR(45) NOT NULL COMMENT '',
  `city_id` INT(11) NOT NULL COMMENT '',
  `locale_id` INT(11) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  INDEX `fk_city_translate_city1_idx` (`city_id` ASC)  COMMENT '',
  INDEX `fk_city_translate_locale1_idx` (`locale_id` ASC)  COMMENT '',
  CONSTRAINT `fk_city_translate_city1`
    FOREIGN KEY (`city_id`)
    REFERENCES `online_courses`.`city` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_city_translate_locale1`
    FOREIGN KEY (`locale_id`)
    REFERENCES `online_courses`.`locale` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `online_courses`.`comment` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `content` VARCHAR(1000) NOT NULL COMMENT '',
  `replied_to` INT(11) NULL DEFAULT NULL COMMENT '',
  `raiting` INT(11) NOT NULL COMMENT '',
  `task_id` INT(11) NOT NULL COMMENT '',
  `user_email` VARCHAR(70) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  INDEX `fk_comment_task1_idx` (`task_id` ASC)  COMMENT '',
  INDEX `fk_comment_user1_idx` (`user_email` ASC)  COMMENT '',
  CONSTRAINT `fk_comment_task1`
    FOREIGN KEY (`task_id`)
    REFERENCES `online_courses`.`task` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comment_user1`
    FOREIGN KEY (`user_email`)
    REFERENCES `online_courses`.`user` (`email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `online_courses`.`country_translate` (
  `id` INT(11) NOT NULL COMMENT '',
  `translate` VARCHAR(45) NOT NULL COMMENT '',
  `country_id` INT(11) NOT NULL COMMENT '',
  `locale_id` INT(11) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  INDEX `fk_country translate_country1_idx` (`country_id` ASC)  COMMENT '',
  INDEX `fk_country translate_locale1_idx` (`locale_id` ASC)  COMMENT '',
  CONSTRAINT `fk_country translate_country1`
    FOREIGN KEY (`country_id`)
    REFERENCES `online_courses`.`country` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_country translate_locale1`
    FOREIGN KEY (`locale_id`)
    REFERENCES `online_courses`.`locale` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `online_courses`.`education_level` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '')
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `online_courses`.`education_level_translate` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `translate` VARCHAR(45) NOT NULL COMMENT '',
  `education_level_id` INT(11) NOT NULL COMMENT '',
  `locale_id` INT(11) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  INDEX `fk_education_level_translation_education_level1_idx` (`education_level_id` ASC)  COMMENT '',
  INDEX `fk_education_level_translate_locale1_idx` (`locale_id` ASC)  COMMENT '',
  CONSTRAINT `fk_education_level_translate_locale1`
    FOREIGN KEY (`locale_id`)
    REFERENCES `online_courses`.`locale` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_education_level_translation_education_level1`
    FOREIGN KEY (`education_level_id`)
    REFERENCES `online_courses`.`education_level` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `online_courses`.`gender` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '')
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `online_courses`.`gender_translate` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `translate` VARCHAR(45) NOT NULL COMMENT '',
  `gender_id` INT(11) NOT NULL COMMENT '',
  `locale_id` INT(11) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  INDEX `fk_gender_translation_gender1_idx` (`gender_id` ASC)  COMMENT '',
  INDEX `fk_gender_translate_locale1_idx` (`locale_id` ASC)  COMMENT '',
  CONSTRAINT `fk_gender_translate_locale1`
    FOREIGN KEY (`locale_id`)
    REFERENCES `online_courses`.`locale` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_gender_translation_gender1`
    FOREIGN KEY (`gender_id`)
    REFERENCES `online_courses`.`gender` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `online_courses`.`notification` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `message` VARCHAR(1000) NOT NULL COMMENT '',
  `url` VARCHAR(100) NULL DEFAULT NULL COMMENT '',
  `is_viewed` TINYINT(1) NOT NULL COMMENT '',
  `is_emailed` TINYINT(1) NOT NULL COMMENT '',
  `created` DATETIME NOT NULL COMMENT '',
  `user_email` VARCHAR(70) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  INDEX `fk_notification_user1_idx` (`user_email` ASC)  COMMENT '',
  CONSTRAINT `fk_notification_user1`
    FOREIGN KEY (`user_email`)
    REFERENCES `online_courses`.`user` (`email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `online_courses`.`student_module` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `module_id` INT(11) NOT NULL COMMENT '',
  `state` VARCHAR(45) NOT NULL COMMENT '',
  `grade` INT(11) NOT NULL COMMENT '',
  `modified` DATETIME NOT NULL COMMENT '',
  `max_grade` INT(11) NOT NULL COMMENT '',
  `user_email` VARCHAR(70) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  INDEX `fk_student_module_module1_idx` (`module_id` ASC)  COMMENT '',
  INDEX `fk_student_module_user1_idx` (`user_email` ASC)  COMMENT '',
  CONSTRAINT `fk_student_module_module1`
    FOREIGN KEY (`module_id`)
    REFERENCES `online_courses`.`module` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_student_module_user1`
    FOREIGN KEY (`user_email`)
    REFERENCES `online_courses`.`user` (`email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `online_courses`.`user_group_translate` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `translate` VARCHAR(45) NOT NULL COMMENT '',
  `user_group_id` INT(11) NOT NULL COMMENT '',
  `locale_id` INT(11) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  INDEX `fk_user_group_translate_user_group1_idx` (`user_group_id` ASC)  COMMENT '',
  INDEX `fk_user_group_translate_locale1_idx` (`locale_id` ASC)  COMMENT '',
  CONSTRAINT `fk_user_group_translate_locale1`
    FOREIGN KEY (`locale_id`)
    REFERENCES `online_courses`.`locale` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_group_translate_user_group1`
    FOREIGN KEY (`user_group_id`)
    REFERENCES `online_courses`.`user_group` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `online_courses`.`user_profile` (
  `username` VARCHAR(45) NOT NULL COMMENT '',
  `birthday` DATETIME NULL DEFAULT NULL COMMENT '',
  `biography` VARCHAR(700) NULL DEFAULT NULL COMMENT '',
  `gender_id` INT(11) NOT NULL COMMENT '',
  `education_level_id` INT(11) NOT NULL COMMENT '',
  `country_id` INT(11) NULL DEFAULT NULL COMMENT '',
  `locale_id` INT(11) NOT NULL COMMENT '',
  `city_id` INT(11) NULL DEFAULT NULL COMMENT '',
  `user_email` VARCHAR(70) NOT NULL COMMENT '',
  INDEX `fk_user_profile_gender1_idx` (`gender_id` ASC)  COMMENT '',
  INDEX `fk_user_profile_education_level1_idx` (`education_level_id` ASC)  COMMENT '',
  INDEX `fk_user_profile_country1_idx` (`country_id` ASC)  COMMENT '',
  INDEX `fk_user_profile_locale1_idx` (`locale_id` ASC)  COMMENT '',
  INDEX `fk_user_profile_city1_idx` (`city_id` ASC)  COMMENT '',
  PRIMARY KEY (`username`)  COMMENT '',
  INDEX `fk_user_profile_user1_idx` (`user_email` ASC)  COMMENT '',
  CONSTRAINT `fk_user_profile_city1`
    FOREIGN KEY (`city_id`)
    REFERENCES `online_courses`.`city` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_profile_country1`
    FOREIGN KEY (`country_id`)
    REFERENCES `online_courses`.`country` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_profile_education_level1`
    FOREIGN KEY (`education_level_id`)
    REFERENCES `online_courses`.`education_level` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_profile_gender1`
    FOREIGN KEY (`gender_id`)
    REFERENCES `online_courses`.`gender` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_profile_locale1`
    FOREIGN KEY (`locale_id`)
    REFERENCES `online_courses`.`locale` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_profile_user1`
    FOREIGN KEY (`user_email`)
    REFERENCES `online_courses`.`user` (`email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `online_courses`.`wiki` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `created` DATETIME NOT NULL COMMENT '',
  `modified` DATETIME NOT NULL COMMENT '',
  `text` VARCHAR(1000) NULL DEFAULT NULL COMMENT '',
  `user_group_id` INT(11) NOT NULL COMMENT '',
  `course_id` INT(11) NOT NULL COMMENT '',
  `user_email` VARCHAR(70) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  INDEX `fk_wiki_user_group1_idx` (`user_group_id` ASC)  COMMENT '',
  INDEX `fk_wiki_course1_idx` (`course_id` ASC)  COMMENT '',
  INDEX `fk_wiki_user1_idx` (`user_email` ASC)  COMMENT '',
  CONSTRAINT `fk_wiki_course1`
    FOREIGN KEY (`course_id`)
    REFERENCES `online_courses`.`course` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_wiki_user_group1`
    FOREIGN KEY (`user_group_id`)
    REFERENCES `online_courses`.`user_group` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_wiki_user1`
    FOREIGN KEY (`user_email`)
    REFERENCES `online_courses`.`user` (`email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `online_courses`.`user_has_user_group` (
  `user_email` VARCHAR(70) NOT NULL COMMENT '',
  `user_group_id` INT(11) NOT NULL COMMENT '',
  PRIMARY KEY (`user_email`, `user_group_id`)  COMMENT '',
  INDEX `fk_user_has_user_group_user_group1_idx` (`user_group_id` ASC)  COMMENT '',
  INDEX `fk_user_has_user_group_user1_idx` (`user_email` ASC)  COMMENT '',
  CONSTRAINT `fk_user_has_user_group_user1`
    FOREIGN KEY (`user_email`)
    REFERENCES `online_courses`.`user` (`email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_has_user_group_user_group1`
    FOREIGN KEY (`user_group_id`)
    REFERENCES `online_courses`.`user_group` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `online_courses`.`user_has_course` (
  `user_email` VARCHAR(70) NOT NULL COMMENT '',
  `course_id` INT(11) NOT NULL COMMENT '',
  PRIMARY KEY (`user_email`, `course_id`)  COMMENT '',
  INDEX `fk_user_has_course_course1_idx` (`course_id` ASC)  COMMENT '',
  INDEX `fk_user_has_course_user1_idx` (`user_email` ASC)  COMMENT '',
  CONSTRAINT `fk_user_has_course_user1`
    FOREIGN KEY (`user_email`)
    REFERENCES `online_courses`.`user` (`email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_has_course_course1`
    FOREIGN KEY (`course_id`)
    REFERENCES `online_courses`.`course` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

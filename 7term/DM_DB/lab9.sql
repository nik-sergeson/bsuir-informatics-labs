drop database if exists `migrations_online_courses`;
create schema `migrations_online_courses` default character set utf8 ;

CREATE TABLE IF NOT EXISTS `migrations_online_courses`.`user` (
  `email` VARCHAR(70) NOT NULL COMMENT '',
  `password` VARCHAR(140) NOT NULL COMMENT '',
  `is_stuff` TINYINT(1) NOT NULL COMMENT '',
  `is_active` TINYINT(1) NOT NULL COMMENT '',
  `last_login` DATETIME NOT NULL COMMENT '',
  `date_joined` DATETIME NOT NULL COMMENT '',
  PRIMARY KEY (`email`)  COMMENT '')
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `migrations_online_courses`.`locale` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `locale` VARCHAR(45) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '')
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `migrations_online_courses`.`gender` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `old_id` INT(11) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '')
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `migrations_online_courses`.`gender_translate` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `translate` VARCHAR(45) NOT NULL COMMENT '',
  `gender_id` INT(11) NOT NULL COMMENT '',
  `locale_id` INT(11) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  INDEX `fk_gender_translation_gender1_idx` (`gender_id` ASC)  COMMENT '',
  INDEX `fk_gender_translate_locale1_idx` (`locale_id` ASC)  COMMENT '',
  CONSTRAINT `fk_gender_translate_locale1`
    FOREIGN KEY (`locale_id`)
    REFERENCES `migrations_online_courses`.`locale` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_gender_translation_gender1`
    FOREIGN KEY (`gender_id`)
    REFERENCES `migrations_online_courses`.`gender` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `migrations_online_courses`.`education_level` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `old_id` INT(11) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '')
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `migrations_online_courses`.`education_level_translate` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `translate` VARCHAR(45) NOT NULL COMMENT '',
  `education_level_id` INT(11) NOT NULL COMMENT '',
  `locale_id` INT(11) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  INDEX `fk_education_level_translation_education_level1_idx` (`education_level_id` ASC)  COMMENT '',
  INDEX `fk_education_level_translate_locale1_idx` (`locale_id` ASC)  COMMENT '',
  CONSTRAINT `fk_education_level_translate_locale1`
    FOREIGN KEY (`locale_id`)
    REFERENCES `migrations_online_courses`.`locale` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_education_level_translation_education_level1`
    FOREIGN KEY (`education_level_id`)
    REFERENCES `migrations_online_courses`.`education_level` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `migrations_online_courses`.`user_profile` (
  `username` VARCHAR(45) NOT NULL COMMENT '',
  `first_name` VARCHAR(45) NOT NULL COMMENT '',
  `last_name` VARCHAR(45) NOT NULL COMMENT '',
  `birthday` DATETIME NULL DEFAULT NULL COMMENT '',
  `biography` VARCHAR(700) NULL DEFAULT NULL COMMENT '',
  `gender_id` INT(11) NOT NULL COMMENT '',
  `education_level_id` INT(11) NOT NULL COMMENT '',
  `locale_id` INT(11) NOT NULL COMMENT '',
  `user_email` VARCHAR(70) NOT NULL COMMENT '',
  INDEX `fk_user_profile_gender1_idx` (`gender_id` ASC)  COMMENT '',
  INDEX `fk_user_profile_education_level1_idx` (`education_level_id` ASC)  COMMENT '',
  INDEX `fk_user_profile_locale1_idx` (`locale_id` ASC)  COMMENT '',
  PRIMARY KEY (`username`)  COMMENT '',
  INDEX `fk_user_profile_user1_idx` (`user_email` ASC)  COMMENT '',
  CONSTRAINT `fk_user_profile_education_level1`
    FOREIGN KEY (`education_level_id`)
    REFERENCES `migrations_online_courses`.`education_level` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_profile_gender1`
    FOREIGN KEY (`gender_id`)
    REFERENCES `migrations_online_courses`.`gender` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_profile_locale1`
    FOREIGN KEY (`locale_id`)
    REFERENCES `migrations_online_courses`.`locale` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_profile_user1`
    FOREIGN KEY (`user_email`)
    REFERENCES `migrations_online_courses`.`user` (`email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;



insert into migrations_online_courses.user(email, password, is_stuff, is_active, last_login, date_joined) select email, password, is_stuff, is_active, last_login, date_joined from online_courses.user;
insert into migrations_online_courses.locale(locale) select locale from online_courses.locale;
insert into migrations_online_courses.gender(old_id) select id from online_courses.gender;
insert into migrations_online_courses.gender_translate(translate, gender_id, locale_id) select src_gen_transl.translate, dst_gen.id, dst_loc.id from online_courses.gender_translate as src_gen_transl inner join migrations_online_courses.gender as dst_gen on src_gen_transl.gender_id=dst_gen.old_id inner join migrations_online_courses.locale as dst_loc on dst_loc.locale=(select locale from online_courses.locale where id=src_gen_transl.locale_id);
insert into migrations_online_courses.education_level(old_id) select id from online_courses.education_level;
insert into migrations_online_courses.education_level_translate(translate, education_level_id, locale_id) select src_edu_transl.translate, dst_edu.id, dst_loc.id from online_courses.education_level_translate as src_edu_transl inner join migrations_online_courses.education_level as dst_edu on src_edu_transl.education_level_id=dst_edu.old_id inner join migrations_online_courses.locale as dst_loc on dst_loc.locale=(select locale from online_courses.locale where id=src_edu_transl.locale_id);
insert into migrations_online_courses.user_profile(username, first_name, last_name, birthday, biography, gender_id, education_level_id, locale_id, user_email) select src_prof.username, src_usr.first_name, src_usr.last_name, src_prof.birthday, src_prof.biography, dst_gender.id, dst_edu.id, dst_locale.id, src_prof.user_email from online_courses.user_profile as src_prof inner join online_courses.user as src_usr on src_prof.user_email=src_usr.email inner join migrations_online_courses.gender as dst_gender on dst_gender.old_id=src_prof.gender_id inner join migrations_online_courses.education_level as dst_edu on dst_edu.old_id=src_prof.education_level_id inner join migrations_online_courses.locale as dst_locale on dst_locale.locale=(select locale from online_courses.locale where id=src_prof.locale_id);
alter table migrations_online_courses.education_level drop column old_id;
alter table migrations_online_courses.gender drop column old_id;



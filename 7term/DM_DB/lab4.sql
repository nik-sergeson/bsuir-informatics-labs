use online_courses;

SET SQL_SAFE_UPDATES=0;
delete from user_has_user_group;
delete from user_group_translate;
delete from user_group_has_permissions;
delete from user_group;
delete from permissions;
delete from content_type;
delete from user_profile;
delete from education_level_translate;
delete from education_level;
delete from gender_translate;
delete from gender;
delete from user;
delete from locale;

insert into locale(locale) values('EN');
insert into locale(locale) values('RU');
insert into locale(locale) values('BLR');
insert into user(first_name, last_name, email, password, is_stuff, is_active, last_login, date_joined)
values('test', 'user', 'test1@user.com', 'test', 0, 1, now(), now());
insert into user(first_name, last_name, email, password, is_stuff, is_active, last_login, date_joined)
values('test', 'user', 'test2@user.com', 'test', 0, 1, now(), now());
insert into user(first_name, last_name, email, password, is_stuff, is_active, last_login, date_joined)
values('test', 'user', 'test3@user.com', 'test', 0, 1, now(), now());
insert into user(first_name, last_name, email, password, is_stuff, is_active, last_login, date_joined)
values('test', 'user', 'test4@user.com', 'test', 0, 1, now(), now());
insert into user(first_name, last_name, email, password, is_stuff, is_active, last_login, date_joined)
values('test', 'user', 'test5@user.com', 'test', 0, 1, now(), now());
insert into gender values();
insert into gender_translate(translate, gender_id, locale_id) values('Male', (select id from gender limit 1), (select id from locale where locale='EN'));
insert into education_level values();
insert into education_level_translate(translate, education_level_id, locale_id) values('Master', (select id from education_level limit 1),  (select id from locale where locale='EN'));
insert into user_profile(username, birthday, biography, gender_id, education_level_id, country_id ,
locale_id, city_id, user_email) values('test1', now(), NULL,  (select id from gender limit 1),  (select education_level_id from education_level_translate where translate='Master'  limit 1), NULL, (select id from locale where locale='EN'), NULL, 'test1@user.com');
insert into user_profile(username, birthday, biography, gender_id, education_level_id, country_id ,
locale_id, city_id, user_email) values('test2', now(), NULL,  (select id from gender limit 1),  (select education_level_id from education_level_translate where translate='Master'  limit 1), NULL, (select id from locale where locale='EN'), NULL, 'test2@user.com');
insert into user_profile(username, birthday, biography, gender_id, education_level_id, country_id ,
locale_id, city_id, user_email) values('test3', now(), NULL,  (select id from gender limit 1),  (select education_level_id from education_level_translate where translate='Master'  limit 1), NULL, (select id from locale where locale='EN'), NULL, 'test3@user.com');
insert into user_profile(username, birthday, biography, gender_id, education_level_id, country_id ,
locale_id, city_id, user_email) values('test4', now(), NULL,  (select id from gender limit 1),  (select education_level_id from education_level_translate where translate='Master'  limit 1), NULL, (select id from locale where locale='EN'), NULL, 'test4@user.com');
insert into user_profile(username, birthday, biography, gender_id, education_level_id, country_id ,
locale_id, city_id, user_email) values('test5', now(), NULL,  (select id from gender limit 1),  (select education_level_id from education_level_translate where translate='Master'  limit 1), NULL, (select id from locale where locale='EN'), NULL, 'test5@user.com');
insert into content_type(name) values('courses');
insert into content_type(name) values('permissions');
insert into permissions(name, content_type_id) values('edit', (select id from content_type where name='courses'));
insert into permissions(name, content_type_id) values('edit', (select id from content_type where name='permissions'));
insert into permissions(name, content_type_id) values('view', (select id from content_type where name='courses'));
insert into user_group values();
insert into user_group values();
insert into user_group values();
insert into user_group_translate(translate, user_group_id, locale_id) values('admin', (select id from user_group limit 0,1), (select id from locale where locale='EN'));
insert into user_group_translate(translate, user_group_id, locale_id) values('stuff', (select id from user_group limit 1,1), (select id from locale where locale='EN'));
insert into user_group_translate(translate, user_group_id, locale_id) values('user', (select id from user_group limit 2,1), (select id from locale where locale='EN'));
insert into user_group_has_permissions(user_group_id, permissions_id) values((select user_group_id from user_group_translate where translate='admin' limit 1), (select id from permissions where name='edit' and content_type_id=(select id from content_type where name='permissions')));
insert into user_group_has_permissions(user_group_id, permissions_id) values((select user_group_id from user_group_translate where translate='stuff' limit 1), (select id from permissions where name='edit' and content_type_id=(select id from content_type where name='courses')));
insert into user_group_has_permissions(user_group_id, permissions_id) values((select user_group_id from user_group_translate where translate='user' limit 1), (select id from permissions where name='view' and content_type_id=(select id from content_type where name='courses')));
insert into user_has_user_group( user_email, user_group_id) values('test1@user.com', (select user_group_id from user_group_translate where translate='admin'));
insert into user_has_user_group( user_email, user_group_id) values('test2@user.com', (select user_group_id from user_group_translate where translate='admin'));
insert into user_has_user_group( user_email, user_group_id) values('test3@user.com', (select user_group_id from user_group_translate where translate='admin'));
insert into user_has_user_group( user_email, user_group_id) values('test4@user.com', (select user_group_id from user_group_translate where translate='stuff'));
insert into user_has_user_group( user_email, user_group_id) values('test5@user.com', (select user_group_id from user_group_translate where translate='user'));


update user_profile set birthday='2009-12-31', biography='Test bio';


delete from user_has_user_group where user_email='test5@user.com';
delete from user_profile where user_email='test5@user.com';
delete from user where email='test5@user.com';


select first_name, last_name, last_login from user where email='test1@user.com';
select birthday, biography from user_profile where user_email='test1@user.com';
select translate from gender_translate where gender_id=(select gender_id from user_profile where user_email='test1@user.com');
select translate from education_level_translate where education_level_id=(select education_level_id from user_profile where user_email='test1@user.com');
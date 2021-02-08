use online_courses;

select birthday,count(*) as count from user_profile group by birthday;
select birthday, group_concat(username separator ' - ') as usernames from user_profile group by birthday;


select education_level_id, group_concat(username separator ' - ') as usernames from user_profile group by education_level_id having count(*)>2;
select education_level_id, group_concat(username separator ' - ') as usernames from user_profile group by education_level_id having education_level_id=5;


select * from user where email in (select user_email from user_has_user_group where user_group_id=(select user_group_id from user_group_has_permissions where permissions_id=(select id from permissions where name='edit' and content_type_id=(select id from content_type where name='courses'))));
select username from user_profile where education_level_id=(select education_level_id from education_level_translate where translate='Master') and gender_id=(select gender_id from gender_translate where translate='Male');
use online_courses;

select upper(username) from user_profile where user_email='test1@user.com';
select substr(email from 6) from user;


select mod(id, 2) from user_group;


select birthday, date_format(date_add(birthday,INTERVAL 45 DAY),'%b %d %Y %h:%i %p') as formatted from user_profile where user_email='test1@user.com';


select convert(birthday, char) as char_date from user_profile;


select convert(length(upper(substr(email from 4))), char) from user;
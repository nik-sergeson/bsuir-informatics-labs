use online_courses;

select * from user where email=(select user_email from user_profile where username='test1');


select * from user where email= any(select user_email from user_has_user_group where user_group_id=(select user_group_id from user_group_translate where translate='admin'));


select * from user where (first_name, last_name)=any(select first_name, last_name from user where is_stuff=1);

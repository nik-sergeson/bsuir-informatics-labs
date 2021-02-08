INSERT INTO skills (ID, name, description) VALUES (skills_seq.nextval, 'C#', 'C#');
INSERT INTO skills (ID, name, description) VALUES (skills_seq.nextval, 'Java', 'Java');
INSERT INTO skills (ID, name, description) VALUES (skills_seq.nextval, 'Python', 'Python');
INSERT INTO skills (ID, name, description) VALUES (skills_seq.nextval, 'Ocaml', 'Ocaml');
INSERT INTO skills (ID, name, description) VALUES (skills_seq.nextval, 'HTML', 'HTML');

INSERT INTO companies (ID, name, description, employee_number) VALUES (companies_seq.nextval, 'Yandex', 'Yandex', 100);
INSERT INTO companies (ID, name, description, employee_number) VALUES (companies_seq.nextval, 'Facebook', 'Facebook', 100);
INSERT INTO companies (ID, name, description, employee_number) VALUES (companies_seq.nextval, 'Twitter', 'Twitter', 100);
INSERT INTO companies (ID, name, description, employee_number) VALUES (companies_seq.nextval, 'Google', 'Google', 100);
INSERT INTO companies (ID, name, description, employee_number) VALUES (companies_seq.nextval, 'IBM', 'IBM', 100);

INSERT INTO employees (ID, first_name, second_name, lang_level, country, company_id) VALUES (employees_seq.nextval, 'John', 'Smith', 'A1', 'England',1);
INSERT INTO employees (ID, first_name, second_name, lang_level, country, company_id) VALUES (employees_seq.nextval, 'John', 'Smith', 'A2', 'England',2);
INSERT INTO employees (ID, first_name, second_name, lang_level, country, company_id) VALUES (employees_seq.nextval, 'John', 'Smith', 'B1', 'England',3);
INSERT INTO employees (ID, first_name, second_name, lang_level, country, company_id) VALUES (employees_seq.nextval, 'John', 'Smith', 'B2', 'England',4);
INSERT INTO employees (ID, first_name, second_name, lang_level, country, company_id) VALUES (employees_seq.nextval, 'John', 'Smith', 'C1', 'England',5);

INSERT INTO contacts (ID, first_id, second_id) VALUES (contacts_seq.nextval, 1, 2);
INSERT INTO contacts (ID,first_id, second_id) VALUES (contacts_seq.nextval,1, 3);
INSERT INTO contacts (ID,first_id, second_id) VALUES (contacts_seq.nextval,1, 4);
INSERT INTO contacts (ID,first_id, second_id) VALUES (contacts_seq.nextval,2, 4);
INSERT INTO contacts (ID,first_id, second_id) VALUES (contacts_seq.nextval,3, 4);

INSERT INTO accounts (ID, profile_id,email, password, is_stuff, is_active,last_login,date_joined) VALUES (employees_seq.nextval, 1, 'mail1@example.com', '1234', 0,1,TO_DATE('2003/05/03 21:02:44', 'yyyy/mm/dd hh24:mi:ss'), TO_DATE('2003/05/03 21:02:44', 'yyyy/mm/dd hh24:mi:ss'));
INSERT INTO accounts (ID, profile_id,email, password, is_stuff, is_active,last_login,date_joined) VALUES (employees_seq.nextval, 2, 'mail2@example.com', '1234', 0,1,TO_DATE('2003/05/03 21:02:44', 'yyyy/mm/dd hh24:mi:ss'), TO_DATE('2003/05/03 21:02:44', 'yyyy/mm/dd hh24:mi:ss'));
INSERT INTO accounts (ID, profile_id,email, password, is_stuff, is_active,last_login,date_joined) VALUES (employees_seq.nextval, 3, 'mail3@example.com', '1234', 0,1,TO_DATE('2003/05/03 21:02:44', 'yyyy/mm/dd hh24:mi:ss'), TO_DATE('2003/05/03 21:02:44', 'yyyy/mm/dd hh24:mi:ss'));
INSERT INTO accounts (ID, profile_id,email, password, is_stuff, is_active,last_login,date_joined) VALUES (employees_seq.nextval, 4, 'mail4@example.com', '1234', 0,1,TO_DATE('2003/05/03 21:02:44', 'yyyy/mm/dd hh24:mi:ss'), TO_DATE('2003/05/03 21:02:44', 'yyyy/mm/dd hh24:mi:ss'));
INSERT INTO accounts (ID, profile_id,email, password, is_stuff, is_active,last_login,date_joined) VALUES (employees_seq.nextval, 5, 'mail5@example.com', '1234', 0,1,TO_DATE('2003/05/03 21:02:44', 'yyyy/mm/dd hh24:mi:ss'), TO_DATE('2003/05/03 21:02:44', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO jobs (ID, title, description, salary,company_id) VALUES (jobs_seq.nextval, 'Developer needed1', 'Developer needed', 100,1);
INSERT INTO jobs (ID, title, description, salary,company_id) VALUES (jobs_seq.nextval, 'Developer needed2', 'Developer needed', 200,2);
INSERT INTO jobs (ID, title, description, salary,company_id) VALUES (jobs_seq.nextval, 'Developer needed3', 'Developer needed', 300,3);
INSERT INTO jobs (ID, title, description, salary,company_id) VALUES (jobs_seq.nextval, 'Developer needed4', 'Developer needed', 400,4);
INSERT INTO jobs (ID, title, description, salary,company_id) VALUES (jobs_seq.nextval, 'Developer needed5', 'Developer needed', 500,5);

INSERT INTO jobskills (ID,first_id, second_id) VALUES (jobskills_seq.nextval, 1, 2);
INSERT INTO jobskills (ID,first_id, second_id) VALUES (jobskills_seq.nextval, 1, 3);
INSERT INTO jobskills (ID,first_id, second_id) VALUES (jobskills_seq.nextval, 1, 4);
INSERT INTO jobskills (ID,first_id, second_id) VALUES (jobskills_seq.nextval, 2, 4);
INSERT INTO jobskills (ID,first_id, second_id) VALUES (jobskills_seq.nextval, 3, 4);
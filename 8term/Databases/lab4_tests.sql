INSERT INTO companies (ID, name, description, employee_number) VALUES (companies_seq.nextval, 'Mozilla', 'Mozilla', 100);
INSERT INTO companies (ID, name, description, employee_number) VALUES (companies_seq.nextval, 'Baidu', 'Baidu', 100);
INSERT INTO companies (ID, name, description, employee_number) VALUES (companies_seq.nextval, 'Samsung', 'Samsung', 100);
INSERT INTO companies (ID, name, description, employee_number) VALUES (companies_seq.nextval, 'Intel', 'Intel', 100);
INSERT INTO companies (ID, name, description, employee_number) VALUES (companies_seq.nextval, 'BSUIR', 'BSUIR', 100);
SELECT * from inserted_companies;

UPDATE companies set description='MRTI' where name='BSUIR';
UPDATE companies set description='Developers of firefox' where name='Mozilla';
UPDATE companies set description='Developers of google.com' where name='Google';
select * from companies_operation;

create table test1(
test_row varchar2(10) NOT NULL);
create table test2(
test_row varchar2(10) NOT NULL);
drop table test1;
drop table test2;
select * from created_objects;
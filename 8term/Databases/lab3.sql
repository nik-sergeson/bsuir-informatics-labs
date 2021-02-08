CREATE OR REPLACE PACKAGE lab3 AS

  PROCEDURE task3(skill IN varchar2) ;
  PROCEDURE task2(in_salary IN number, skill IN varchar2);
  FUNCTION task1(in_salary IN number) RETURN varchar2;
END lab3;
/
CREATE PACKAGE BODY lab3 AS

  FUNCTION task1(in_salary IN number) RETURN varchar2
  IS
    title varchar2(50);
  BEGIN
    SELECT title into title FROM (SELECT * FROM jobs where salary>in_salary ) WHERE ROWNUM = 1;
    RETURN title;
  END;

  PROCEDURE task2(in_salary IN number, skill IN varchar2) 
  IS
  jtitle varchar2(50);
  CURSOR cur_jobs IS
    select title from JOBS where id in(select first_id from jobskills where second_id=(select id from skills where name=skill)) and salary>in_salary;
  BEGIN
    OPEN cur_jobs;
    LOOP
      FETCH cur_jobs INTO jtitle;
      EXIT WHEN cur_jobs%NOTFOUND;
      dbms_output.put_line(jtitle);
    END LOOP;
    CLOSE cur_jobs;
  END;

  PROCEDURE task3(skill IN varchar2) 
  IS
  ctitle varchar2(50);
  CURSOR cur_companies IS
    select name from companies where id in (select company_id from(select * from jobs where id in(select first_id from jobskills where second_id=(select id from skills where name=skill)) order by salary));
  BEGIN
    OPEN cur_companies;
      LOOP
        FETCH cur_companies INTO ctitle;
        EXIT WHEN cur_companies%NOTFOUND;
        dbms_output.put_line(ctitle);
    END LOOP;
    CLOSE cur_companies;
  END;
END lab3;
/
DECLARE
  job_title varchar2(50);
BEGIN
  job_title:=lab3.task1(400);
  dbms_output.Put_line(job_title);
  lab3.task2(200, 'Ocaml');
  lab3.task3('Ocaml');
END;
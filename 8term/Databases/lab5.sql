CREATE OR REPLACE TRIGGER username_unique
BEFORE INSERT
  ON accounts
  FOR EACH ROW
DECLARE
  row_quantity number(10);
  useremail_exc exception;
BEGIN
  select count(*) into row_quantity from accounts where email=:new.email;
  if(row_quantity>0) then
    raise useremail_exc;
  end if;
exception
  when useremail_exc then
    RAISE_APPLICATION_ERROR(-20001,'User email must be unique');
END; 
/
CREATE OR REPLACE PACKAGE lab5 AS
  procedure create_status_table;
  procedure create_jobs_migrate;
  procedure TestLab5;
END lab5;
/
CREATE PACKAGE BODY lab5 AS
  procedure create_status_table IS
  begin
    execute immediate 'CREATE TABLE status( ID number(10) NOT NULL,name varchar2(50) NOT NULL,CONSTRAINT status_pk PRIMARY KEY (ID))';
    execute immediate 'insert into status(ID, name) values(1,'''||'opened'||''')';
    execute immediate 'insert into status(ID, name) values(2,'''||'closed'||''')';
    EXCEPTION
      WHEN OTHERS THEN
        IF SQLCODE = -955 THEN
          execute immediate('ALTER TABLE jobs_migrate DROP CONSTRAINT fk_status_job_migrate');
          execute immediate 'DROP TABLE status';
          execute immediate 'CREATE TABLE status( ID number(10) NOT NULL,name varchar2(50) NOT NULL,CONSTRAINT status_pk PRIMARY KEY (ID))';
          execute immediate 'insert into status(ID, name) values(1,'''||'opened'||''')';
          execute immediate 'insert into status(ID, name) values(2,'''||'closed'||''')';
        END IF;
  end;

  procedure create_jobs_migrate IS
  begin 
    execute immediate 'CREATE TABLE jobs_migrate
    ( ID number(10) NOT NULL,
      title varchar2(50) NOT NULL,
      description varchar2(250) NOT NULL,
      salary number(10) NOT NULL,
      company_id number(10) NOT NULL,
      status_id number(10) NOT NULL,
      CONSTRAINT jobs_migrate_pk PRIMARY KEY (ID),
      CONSTRAINT fk_company_job_migrate
        FOREIGN KEY (company_id)
        REFERENCES companies(ID),
      CONSTRAINT fk_status_job_migrate
        FOREIGN KEY (status_id)
        REFERENCES status(ID))';
    EXCEPTION
      WHEN OTHERS THEN
        IF SQLCODE = -955 THEN
          execute immediate 'DROP TABLE jobs_migrate';
          execute immediate 'CREATE TABLE jobs_migrate
          ( ID number(10) NOT NULL,
            title varchar2(50) NOT NULL,
            description varchar2(250) NOT NULL,
            salary number(10) NOT NULL,
            company_id number(10) NOT NULL,
            status_id number(10) NOT NULL,
            CONSTRAINT jobs_migrate_pk PRIMARY KEY (ID),
            CONSTRAINT fk_company_job_migrate
              FOREIGN KEY (company_id)
              REFERENCES companies(ID),
            CONSTRAINT fk_status_job_migrate
              FOREIGN KEY (status_id)
              REFERENCES status(ID))';
              END IF;
  end;

  procedure TestLab5 IS
    ID number(10);
    title varchar2(50);
    description varchar2(250);
    salary number(10);
    company_id number(10);
    CURSOR cur_jobs IS
      select * from jobs;
  BEGIN
    LAB5.CREATE_STATUS_TABLE;
    LAB5.CREATE_JOBS_MIGRATE;
    OPEN cur_jobs;
    LOOP
      FETCH cur_jobs INTO ID,title ,description,salary,company_id;
      EXIT WHEN cur_jobs%NOTFOUND;
      execute immediate 'insert into jobs_migrate(ID,title, description,salary,company_id,status_id) values('||ID||','''||title||''','''||description||''','||salary||','||company_id||',1)';
    END LOOP;
    CLOSE cur_jobs;
  exception
    when invalid_cursor then
       dbms_output.put_line('Invalid cursor operation');
    when rowtype_mismatch then
       dbms_output.put_line('Check types of columns in migrate table');
  END;   
END lab5;
/
BEGIN
lab5.TestLab5();
END;
/
select * from jobs_migrate;
INSERT INTO accounts (ID, profile_id,email, password, is_stuff, is_active,last_login,date_joined) VALUES (employees_seq.nextval, 1, 'mail1@example.com', '1234', 0,1,TO_DATE('2003/05/03 21:02:44', 'yyyy/mm/dd hh24:mi:ss'), TO_DATE('2003/05/03 21:02:44', 'yyyy/mm/dd hh24:mi:ss'));
CREATE TABLE created_objects(
  ID number(10) NOT NULL,
  object_name VARCHAR2(30)NOT NULL,
  object_type VARCHAR2(30)NOT NULL,
  WHEN_CREATED DATE NOT NULL,
  WHO_CREATED VARCHAR2(30)NOT NULL,
  CONSTRAINT created_objects_pk PRIMARY KEY (ID)
);

CREATE TABLE inserted_companies(
  ID number(10) NOT NULL,
  name varchar2(50) NOT NULL,
  CONSTRAINT inserted_company_pk PRIMARY KEY (ID)
);

CREATE TABLE companies_operation(
  ID number(10) NOT NULL,
  username varchar2(10) NOT NULL,
  operation_type varchar2(15) NOT NULL,
  operation_date date NOT NULL,
  CONSTRAINT companies_operation_pk PRIMARY KEY (ID)
);

CREATE SEQUENCE ins_companies_seq START WITH 1 INCREMENT BY 1 NOMAXVALUE;
CREATE SEQUENCE companies_operation_seq START WITH 1 INCREMENT BY 1 NOMAXVALUE;
CREATE SEQUENCE obj_creation_seq START WITH 1 INCREMENT BY 1 NOMAXVALUE;

CREATE OR REPLACE TRIGGER company_after_insert
AFTER INSERT
  ON companies
  FOR EACH ROW
BEGIN
  INSERT INTO inserted_companies( id,name ) VALUES ( ins_companies_seq.nextval, :new.name);
END;
/
CREATE OR REPLACE TRIGGER company_delete
AFTER DELETE
  ON companies
  FOR EACH ROW
DECLARE
  v_username varchar2(10);
  cur_date date;
BEGIN
  SELECT user INTO v_username FROM dual;
  cur_date := sysdate;
  INSERT INTO companies_operation( id,username, operation_type, operation_date ) VALUES ( companies_operation_seq.nextval,v_username, 'DELETE', cur_date);
END;
/
CREATE OR REPLACE TRIGGER company_insert
AFTER INSERT
  ON companies
  FOR EACH ROW
DECLARE
  v_username varchar2(10);
  cur_date date;
BEGIN
  SELECT user INTO v_username FROM dual;
  cur_date := sysdate;
  INSERT INTO companies_operation( id,username, operation_type, operation_date ) VALUES ( companies_operation_seq.nextval,v_username, 'INSERT', cur_date);
END;
/
CREATE OR REPLACE TRIGGER company_update
AFTER UPDATE
  ON companies
  FOR EACH ROW
DECLARE
  v_username varchar2(10);
  cur_date date;
BEGIN
  SELECT user INTO v_username FROM dual;
  cur_date := sysdate;
  INSERT INTO companies_operation( id,username, operation_type, operation_date ) VALUES ( companies_operation_seq.nextval,v_username, 'UPDATE', cur_date);
END;
/
CREATE OR REPLACE TRIGGER objects_creation_tr AFTER CREATE ON SCHEMA
BEGIN
  INSERT INTO created_objects VALUES (obj_creation_seq.nextval, SYS.DICTIONARY_OBJ_NAME,SYS.DICTIONARY_OBJ_TYPE,SYSDATE,USER);
END;
/
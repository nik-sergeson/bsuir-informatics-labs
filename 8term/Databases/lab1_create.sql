CREATE TABLE skills
( ID number(10) NOT NULL,
  name varchar2(50) NOT NULL,
  description varchar2(50) NOT NULL,
  CONSTRAINT skill_pk PRIMARY KEY (ID)
);

CREATE TABLE companies
( ID number(10) NOT NULL,
  name varchar2(50) NOT NULL,
  description varchar2(50) NOT NULL,
  employee_number number(10) NOT NULL,
  CONSTRAINT company_pk PRIMARY KEY (ID)
);

CREATE TABLE employees
(  
  ID number(10) NOT NULL,
  first_name varchar2(50) NOT NULL,
  second_name varchar2(50) NOT NULL,
  lang_level varchar2(50) NOT NULL,
  country varchar2(50) NOT NULL,
  company_id number(10) NOT NULL,
  CONSTRAINT employees_pk PRIMARY KEY (ID),
  CONSTRAINT fk_companies
    FOREIGN KEY (company_id)
    REFERENCES companies(ID)
);

CREATE TABLE contacts
(  
  ID number(10) NOT NULL,
  first_id number(10) NOT NULL,
  second_id number(10) NOT NULL,
  CONSTRAINT contact_pk PRIMARY KEY (ID),
  CONSTRAINT fk_first_id
    FOREIGN KEY (first_id)
    REFERENCES employees(ID),
  CONSTRAINT fk_second_id
    FOREIGN KEY (first_id)
    REFERENCES employees(ID)
);

CREATE TABLE accounts
( 
  ID number(10) NOT NULL,
  profile_id number(10) NOT NULL,
  email varchar2(50) NOT NULL,
  password varchar2(150) NOT NULL,
  is_stuff number(1) NOT NULL,
  is_active number(1) NOT NULL,
  last_login date NOT NULL,
  date_joined date NOT NULL,
  CONSTRAINT user_pk PRIMARY KEY (ID),
  CONSTRAINT fk_profile
    FOREIGN KEY (profile_id)
    REFERENCES employees(ID)
);

CREATE TABLE jobs
( ID number(10) NOT NULL,
  title varchar2(50) NOT NULL,
  description varchar2(250) NOT NULL,
  salary number(10) NOT NULL,
  company_id number(10) NOT NULL,
  CONSTRAINT job_pk PRIMARY KEY (ID),
  CONSTRAINT fk_company_job
    FOREIGN KEY (company_id)
    REFERENCES companies(ID)
);

CREATE TABLE jobskills
(  
  ID number(10) NOT NULL,
  first_id number(10) NOT NULL,
  second_id number(10) NOT NULL,
  CONSTRAINT jobskills_pk PRIMARY KEY (ID),
  CONSTRAINT fk_jobskills_first_id
    FOREIGN KEY (first_id)
    REFERENCES jobs(ID),
  CONSTRAINT fk_jobskills_second_id
    FOREIGN KEY (second_id)
    REFERENCES skills(ID)
);

CREATE SEQUENCE skills_seq START WITH 1 INCREMENT BY 1 NOMAXVALUE;
CREATE SEQUENCE companies_seq START WITH 1 INCREMENT BY 1 NOMAXVALUE;
CREATE SEQUENCE employees_seq START WITH 1 INCREMENT BY 1 NOMAXVALUE;
CREATE SEQUENCE accounts_seq START WITH 1 INCREMENT BY 1 NOMAXVALUE;
CREATE SEQUENCE jobs_seq START WITH 1 INCREMENT BY 1 NOMAXVALUE;
CREATE SEQUENCE contacts_seq START WITH 1 INCREMENT BY 1 NOMAXVALUE;
CREATE SEQUENCE jobskills_seq START WITH 1 INCREMENT BY 1 NOMAXVALUE;
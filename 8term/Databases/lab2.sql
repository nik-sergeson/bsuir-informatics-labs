CREATE or replace DIRECTORY USER_DIR AS 'D:\Labs\bsuir-informatics-labs\labs.8term\Databases\text'; 
GRANT READ ON DIRECTORY USER_DIR TO PUBLIC;
/
CREATE OR REPLACE PACKAGE lab2 AS
  TYPE temp IS RECORD (field1 date, field2 number, field3 varchar2(40)); 
  CURSOR c1 IS
    SELECT name FROM companies;

  PROCEDURE TestLab2;
  PROCEDURE TestLab2TextFile;
END lab2;
/

CREATE PACKAGE BODY lab2 AS
  PROCEDURE TestLab2 IS
    Perem1 varchar2(40):= '1000';
    Perem2 number(10,2):= 12345678.12;
    Date1 date:=TO_DATE('07.01.2012', 'dd.mm.yyyy');
    Date2 date:=TO_DATE('23.02.2014', 'dd.mm.yyyy');
    Record1 temp;   
    convert1 numeric(7,2):=12345.12;
    convert2 varchar2(40):='Test string';
    convert3 date:=TO_DATE('07.01.2012', 'dd.mm.yyyy');
    to_convert1 float;
    to_convert2 char(40);
    to_convert3 numeric(20,4);
    avg_value float;
    cursor_index int:=0;
    comp_name companies.name%type;
  BEGIN
    Record1.field1:=TO_DATE('07.01.2012', 'dd.mm.yyyy');
    Record1.field2:=10;
    Record1.field3:='ABC';
    dbms_output.Put_line(Record1.field1);
    dbms_output.Put_line(Record1.field2);
    dbms_output.Put_line(Record1.field3);

    to_convert1:=TO_BINARY_FLOAT(convert1);
    to_convert2:=TO_CHAR(convert2);
    to_convert3:=to_number(to_char(convert3,'yyyymmdd'));
    dbms_output.Put_line(to_convert1);
    dbms_output.Put_line(to_convert2);
    dbms_output.Put_line(to_convert3);

    select avg(employee_number) into avg_value from companies;
    if (avg_value>50 and avg_value<200) then
       dbms_output.Put_line('Average: ' || (avg_value));
    end if;

    open c1;
    LOOP
      FETCH c1 into comp_name;
      EXIT WHEN cursor_index>4;
      if (cursor_index=4) then
        dbms_output.put_line(comp_name);
      end if;
      cursor_index:=cursor_index+1;
    END LOOP;
    close c1;
  END;
  
  PROCEDURE TestLab2TextFile IS
    f_in utl_file.file_type;
    s_in varchar2(32767);
    string varchar2(32767);
    in_length integer;
    cur_pos BINARY_INTEGER := 0;
    in_char char(4);
    next_char char(4);
    spaces_add integer :=0;
    space_quant integer :=0;
    end_cut integer:=0;
  BEGIN
    f_in := utl_file.fopen('USER_DIR','input.txt','R');
    loop
      begin
        utl_file.get_line(f_in,s_in);
        EXCEPTION
          WHEN NO_DATA_FOUND THEN
        EXIT;
      end;
      string:= string || s_in;
    end loop;
    utl_file.fclose(f_in);
    dbms_output.Put_line(string); 
 
    in_length := length(string);
    while (cur_pos < in_length-1)
    loop
      cur_pos := cur_pos + 1;
      in_char := substr(string, cur_pos, 1);
      next_char:=substr(string, cur_pos+1, 1);
      if((in_char='.') or (in_char=',') or (in_char='!') or (in_char='?') or (in_char=':') or (in_char=';')) then
        if(next_char!=' ') then
          string:= concat(concat(substr(string, 0, cur_pos),' '),substr(string, cur_pos+1, in_length-cur_pos-1));
          spaces_add:=spaces_add+1;
          cur_pos:=cur_pos+2;
        end if;
      end if;
    end loop;
    dbms_output.Put_line(string);
    dbms_output.Put_line(spaces_add);
  
    cur_pos:=0;
    while (space_quant<8)
    loop
      cur_pos := cur_pos + 1;
      in_char := substr(string, cur_pos, 1);
      if(in_char=' ') then
        space_quant:=space_quant+1;
        if((space_quant=1) or (space_quant=3) or (space_quant=5) or(space_quant=7)) then
          end_cut:=cur_pos+1;
          while(substr(string, end_cut, 1)!=' ')
          loop
            end_cut:=end_cut+1;
          end loop;
          string:=concat(substr(string, 0, cur_pos), substr(string, end_cut, in_length-end_cut-1));
        end if;
      end if;
    end loop;
    dbms_output.Put_line(string);
  
    string:=replace(string, 'å','ÁÁ');
    string:=replace(string, 'î', 'ÁÁ');
    dbms_output.Put_line(string);
  END;
END lab2;
/
BEGIN  
lab2.TestLab2();
lab2.TestLab2TextFile();
END; 
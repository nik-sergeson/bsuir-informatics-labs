program Project2;
{$APPTYPE CONSOLE}
uses
  SysUtils,
  Windows,
  Unit1 in 'Unit1.pas';

  procedure clear;
  var
    sbi: TConsoleScreenBufferInfo;
    i: integer;
  begin
     GetConsoleScreenBufferInfo(GetStdHandle(STD_OUTPUT_HANDLE),sbi);
     for i := 0 to sbi.dwSize.y do
      writeln;
    end;

  var
    Graph:Tgraph;
    choice,a,b,i:Integer;
    s:string;
  begin
  Graph:=Tgraph.Create;
  choice:=0;
  while choice<>8 do begin
    clear;
    Writeln('1)Read from file');
    Writeln('2)add edge');
    Writeln('3)delete edge');
    Writeln('4)add element');
    Writeln('5)delete element');
    Writeln('6)show matrix');
    Writeln('7)write in file');
    Writeln('8)quit');
    Readln(choice);
    case choice of
      1:begin
          clear;
          Graph.filetomas;
          Writeln('mas entered');
          Readln;
          clear;
        end;
      2:begin
          clear;
          writeln('enter "1stelement 2delement"');
          Readln(a,b);
          Graph.addreb(a,b);
          Writeln('edge created');
          Readln;
          clear;
        end;
      3:begin
          clear;
          writeln('enter "1stelement 2delement"');
          Readln(a,b);
          Graph.delreb(a,b);
          Writeln('edge deleted');
          Readln;
          clear;
        end;
      4:begin
          clear;
          Writeln('enter elements to connect "1stelement 2delement..."');
          Readln(s);
          Graph.addelem(s);
          Writeln('element created');
          readln;
          clear;
        end;
      5:begin
          clear;
          Writeln('enter index of element');
          Readln(a);
          Graph.DelElem(a);
          Writeln('element deleted');
          readln;
          clear;
        end;
      6:begin
        clear;
        write('  1');
        for i:=1 to Graph.Dim-1 do
        write(' ',i+1);
        Writeln;
        for i:=0 to Graph.Dim-1 do  begin
          Graph.MatrixWiev(s,i);
          Writeln(s);
        end;
        Readln;
        end;
      7:begin
        Graph.MasToFile;
        end;
      8:
        choice:=8;
    end;
  end;
  end.

unit Unit1;

interface

uses
  SysUtils;

type
  Tgraph=class(TObject)
  private
    fn:integer;
    fmas:array of array of integer;
    procedure WriteElement(i,j: Integer; Value: Integer);
    function ReadElement(i,j: Integer): Integer;
  public
    procedure filetomas;
    procedure addelem(s:string);
    procedure addreb(a,b:integer);
    procedure delreb(a,b:integer);
    procedure DelElem(a:Integer);
    procedure MatrixWiev(var s:string;i:Integer);
    procedure MasToFile;
    property Data[I,J: Integer]: Integer read ReadElement
                                                      write WriteElement;
     property Dim:integer read fn write fn;
  end;

implementation

  function Tgraph.ReadElement(i,j: Integer): Integer;
     begin
       if (i > 0) and (i <= fn) and (j > 0) and (j <= fn)
       then Result := fmas[i,j]
       else Result := 0
     end;

  procedure Tgraph.WriteElement(i,j: Integer; Value: Integer);
     begin 
       if ((i > 0) and (i <= fn) and (j > 0) and (j <= fn)) then
        fmas[i,j] := Value;
     end;

  procedure Tgraph.filetomas;
  var
    myFile : TextFile;
    i,j,si:Integer;
    s:string;
  begin
    AssignFile(myFile,'1.txt');
    Reset(myFile);
    readln(myfile,s);
    fn:=(length(s) div 2)+1;
    setlength(fmas,fn,fn);
    for j:=0 to fn-1 do begin
      si:=1;
      for i:=0 to fn-1 do begin
        fmas[j,i]:=strtoint(s[si]);
        si:=si+2;
      end;
      readln(myfile,s);
    end;
    CloseFile(myFile);
  end;

  procedure Tgraph.addelem;
  var SSp,ElI,i:integer;
  begin
    inc(fn);
    setlength(fmas,fn,fn);
    for i:=0 to fn-1 do begin
      fmas[fn-1,i]:=0;
      fmas[i,fn-1]:=0;
    end;
    while(Pos(' ',s)<>0) do begin
      SSp:=Pos(' ',s);
      ElI:=StrToInt(Copy(s,1,SSp-1));
      Delete(s,1,SSp);
      fmas[ElI-1,fn-1]:=1;
      fmas[fn-1,ElI-1]:=1;
    end;
    ElI:=StrToInt(Copy(s,1,length(s)));
    fmas[ElI-1,fn-1]:=1;
    fmas[fn-1,ElI-1]:=1;
  end;

  procedure tgraph.addreb;
  begin
    fmas[a-1,b-1]:=1;
    fmas[b-1,a-1]:=1;
  end;

  procedure tgraph.delreb;
  begin
    fmas[a-1,b-1]:=0;
    fmas[b-1,a-1]:=0;
  end;

  procedure Tgraph.DelElem;
  var i,j:Integer;
  begin
    for j:=0 to fn-1 do
      for i:=(a-1) to fn-2 do
        fmas[j,i]:=fmas[j,i+1];
    for i:=(a-1) to fn-2 do
      for j:=0 to fn-1 do
        fmas[i,j]:=fmas[i+1,j];
    Dec(fn);
    SetLength(fmas,fn,fn);
  end;

  procedure Tgraph.MatrixWiev;
  var j:Integer;
  begin
    s:=IntToStr(i+1)+' '+inttostr(fMas[i,0]);
    for j:=1 to fn-1 do
      s:=s+' '+inttostr(fMas[i,j]);
  end;

  procedure Tgraph.MasToFile;
  var i,j:Integer;
    myFile : TextFile;
  begin
    AssignFile(myFile,'1.txt');
    Rewrite(myfile);
    for j:=0 to fn-1 do begin
      for i:=0 to fn-2 do begin
        write(myfile,fmas[j,i]);
        write(myfile,' ');
      end;
      write(myfile,fmas[j,i]);
      Writeln(myfile,'');
    end;
    closefile(myfile);
  end;

end.

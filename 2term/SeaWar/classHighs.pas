unit classHighs;

interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs,classField, StdCtrls, ExtCtrls,classBrain,classShip;
  
  type
  Thighscore=class(tobject)
    myScore:file;
    Size:integer;
    HghName:string;
    Names:array of string;
    Scores:array of integer;
    procedure Open;
    procedure Save;
    procedure Show(memo:tmemo);
    procedure add(score:integer;name:string);
    constructor create;
  end;

implementation

constructor Thighscore.create;
var i:integer;
begin
size:=5;
HghName:='Scores.dat';
setlength(Names,size);
setlength(Scores,size);
for i:=0 to size -1 do begin
names[i]:='';
scores[i]:=0;
end;
end;

procedure  Thighscore.Open;
var i:integer;
begin
i:=0;
AssignFile(MyScore,HghName);
if FileExists(HghName) then
Reset(myScore)
else
Rewrite(myScore);
while not Eof(myScore) do
  begin
    BlockRead(myScore, names[i], sizeof(string));
    BlockRead(myScore, scores[i], sizeof(integer));
    inc(i);
    end;
closefile(myScore);
end;

procedure  Thighscore.Save;
var i:integer;
begin
i:=0;
Rewrite(myScore);
while not Eof(myScore) do
  begin
    Blockwrite(myScore, names[i], sizeof(string));
    Blockwrite(myScore, scores[i], sizeof(integer));
    inc(i);
    end;
closefile(myScore);
end;
procedure  Thighscore.add;
var
i,j:integer;
begin
i:=0;
while(Score<scores[i]) do
        inc(i);
for j:=size-2 downto i do begin
        names[j+1]:=names[j];
        scores[j+1]:=scores[j];
end;
if (i<size ) then begin
         names[i]:=name;
         scores[i]:=score;
end;
end;

procedure Thighscore.Show;
var i:integer;
s:string;
begin
for i:=0 to size-1 do begin
        s:=inttostr(i+1)+' '+inttostr(scores[i])+' '+names[i];
        memo.lines.add(s);
end;
end;
end.


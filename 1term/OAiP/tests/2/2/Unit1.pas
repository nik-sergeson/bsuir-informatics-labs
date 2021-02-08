unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, Grids,unit2;

type
  TForm1 = class(TForm)
    StringGrid1: TStringGrid;
    Edit1: TEdit;
    Button1: TButton;
    Button2: TButton;
    procedure FormCreate(Sender: TObject);
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;
  tsolv:solv;

implementation

{$R *.dfm}

procedure TForm1.FormCreate(Sender: TObject);
var
i:integer;
begin
randomize;
for i:=1 to 10 do begin
stringgrid1.Cells[i,1]:=inttostr(i);
stringgrid1.Cells[i,2]:=inttostr(10-i); end;
tsolv:=solv.create;
end;

procedure TForm1.Button1Click(Sender: TObject);
var i:integer;
begin
for i:=1 to 10 do begin
tsolv.mas[i].i:=strtoint(stringgrid1.Cells[i,1]);
tsolv.mas[i].n:=strtoint(stringgrid1.Cells[i,2]);
end; end;

procedure TForm1.Button2Click(Sender: TObject);
begin
tsolv.key:=strtoint(edit1.text);
tsolv.psk(tsolv.mas,1,10);
if tsolv.mas[tsolv.ans].i=tsolv.key then edit1.text:=inttostr(tsolv.mas[tsolv.ans].n);
end;

end.

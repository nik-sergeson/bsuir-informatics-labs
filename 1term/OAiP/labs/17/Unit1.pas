unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, Grids,unit2;

type
  TForm1 = class(TForm)
    Edit1: TEdit;
    Button1: TButton;
    StringGrid1: TStringGrid;
    Edit2: TEdit;
    Button2: TButton;
    Edit3: TEdit;
    Button3: TButton;
    procedure FormCreate(Sender: TObject);
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure Button3Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;
  stack:sstack;
implementation

{$R *.dfm}

procedure TForm1.FormCreate(Sender: TObject);
begin
stringgrid1.Cells[0,0]:='opp';
stringgrid1.Cells[1,0]:='zn';
stringgrid1.Cells[0,1]:='2';
stringgrid1.Cells[0,2]:='7,2';
stringgrid1.Cells[0,3]:='6,4';
stringgrid1.Cells[0,4]:='3';
stringgrid1.Cells[0,5]:='7,4';
stringgrid1.Cells[0,6]:='6';
stringgrid1.Cells[0,7]:='4,2';
stringgrid1.Cells[1,1]:='y';
stringgrid1.Cells[1,2]:='z';
stringgrid1.Cells[1,3]:='v';
stringgrid1.Cells[1,4]:='a';
stringgrid1.Cells[1,5]:='c';
stringgrid1.Cells[1,6]:='d';
stringgrid1.Cells[1,7]:='u';
stack:=sstack.create;
edit1.Text:='(y-z/v)*a^c/d+u';
edit2.clear;
edit3.clear;
end;

procedure TForm1.Button1Click(Sender: TObject);
var a,b:string;
begin
a:=EDIT1.Text;
stack.obr(a,b);
edit2.Text:=b;

end;

procedure TForm1.Button2Click(Sender: TObject);
begin
edit3.Text:=floattostr(stack.av(edit2.Text));
end;

procedure TForm1.Button3Click(Sender: TObject);
begin
stack.zn['y']:=strtofloat(stringgrid1.Cells[0,1]);
stack.zn['z']:=strtofloat(stringgrid1.Cells[0,2]);
stack.zn['v']:=strtofloat(stringgrid1.Cells[0,3]);
stack.zn['a']:=strtofloat(stringgrid1.Cells[0,4]);
stack.zn['c']:=strtofloat(stringgrid1.Cells[0,5]);
stack.zn['d']:=strtofloat(stringgrid1.Cells[0,6]);
stack.zn['u']:=strtofloat(stringgrid1.Cells[0,7]);
end;

end.

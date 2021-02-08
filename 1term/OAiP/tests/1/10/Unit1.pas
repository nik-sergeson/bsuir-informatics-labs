unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, ExtCtrls, StdCtrls,unit2;

type
  TForm1 = class(TForm)
    Edit1: TEdit;
    Label1: TLabel;
    Edit2: TEdit;
    Label2: TLabel;
    Edit3: TEdit;
    Label3: TLabel;
    Label4: TLabel;
    Edit4: TEdit;
    Edit5: TEdit;
    Label5: TLabel;
    Label6: TLabel;
    Edit6: TEdit;
    Edit7: TEdit;
    Label7: TLabel;
    Image1: TImage;
    procedure Edit7DblClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;

implementation

{$R *.dfm}

procedure TForm1.Edit7DblClick(Sender: TObject);
var x1,x2, x3,y1,y2,y3,h:extended;
begin
x1:=strtofloat(edit1.Text);
y1:=strtofloat(edit2.Text);
x2:=strtofloat(edit3.Text);
y2:=strtofloat(edit4.Text);
x3:=strtofloat(edit5.Text);
y3:=strtofloat(edit6.Text);
h:=strtofloat(edit7.Text);
rec(x1,x2, x3,y1,y2,y3,h,image1);
end;

end.

unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, ExtCtrls,unit2, StdCtrls;

type
  TForm1 = class(TForm)
    Image1: TImage;
    Button1: TButton;
    Button2: TButton;
    Button3: TButton;
    Button4: TButton;
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure Button3Click(Sender: TObject);
    procedure Button4Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;
  ris:tris;

implementation

{$R *.dfm}

procedure TForm1.Button1Click(Sender: TObject);
begin
ris:=tris.create(50,50,50,image1.Canvas);
ris.draw;
image1.Update;
end;

procedure TForm1.Button2Click(Sender: TObject);
begin
ris.moveto(0,5,0);
image1.Update;
end;

procedure TForm1.Button3Click(Sender: TObject);
begin
ris.moveto(-5,0,0);
image1.Update;
end;

procedure TForm1.Button4Click(Sender: TObject);
begin
ris.moveto(5,0,0);
image1.Update;
end;

end.

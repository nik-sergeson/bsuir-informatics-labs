unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, unit2;

type
  TForm1 = class(TForm)
    SaveDialog1: TSaveDialog;
    Button1: TButton;
    OpenDialog1: TOpenDialog;
    procedure Button1Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;
  var
  Form1: TForm1;
  fl:fc;
  flname:string;

implementation

{$R *.dfm}

procedure TForm1.Button1Click(Sender: TObject);
begin
if opendialog1.Execute then begin
flname:=opendialog1.FileName;
assignfile(fl,flname);
reset(fl);
zam(fl,')',']'); // ispravit
seek(fl,0);
zam(fl,'(','[');
closefile(fl);
end;
end;

end.

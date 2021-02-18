unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls,unit2, Buttons;

type
  TForm1 = class(TForm)
    ListBox1: TListBox;
    Button1: TButton;
    Edit1: TEdit;
    BitBtn1: TBitBtn;
    Button2: TButton;
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
  tstack:stack;
  n:integer;

implementation

{$R *.dfm}

procedure TForm1.FormCreate(Sender: TObject);
begin
tstack:=stack.create;
randomize;
end;

procedure TForm1.Button1Click(Sender: TObject);
var i:integer;
begin
listbox1.Clear;
n:=strtoint(edit1.Text);
tstack.dim:=n;
for i:=1 to n do
tstack.add(random(50)-25);
tstack.print(listbox1);
end;

procedure TForm1.Button2Click(Sender: TObject);
begin
listbox1.Clear;
tstack.solution;
tstack.print(listbox1);
//listbox1.Items.Add('f');
end;

procedure TForm1.Button3Click(Sender: TObject);
begin
listbox1.Clear;
tstack.sortslip(tstack);
tstack.print(listbox1);
end;

end.

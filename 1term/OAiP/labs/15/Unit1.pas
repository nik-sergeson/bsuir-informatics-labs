unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls,unit2, Buttons;

type
  TForm1 = class(TForm)
    Button1: TButton;
    ListBox1: TListBox;
    Edit1: TEdit;
    Button2: TButton;
    BitBtn1: TBitBtn;
    Edit2: TEdit;
    Button3: TButton;
    ListBox2: TListBox;
    Button4: TButton;
    Button5: TButton;
    ListBox3: TListBox;
    procedure FormCreate(Sender: TObject);
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure Button3Click(Sender: TObject);
    procedure Button4Click(Sender: TObject);
    procedure Button5Click(Sender: TObject);
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
edit1.Text:='10';
randomize;
edit2.Clear;
end;

procedure TForm1.Button1Click(Sender: TObject);
var i,p,l:integer;
begin
n:=strtoint(edit1.Text);
tstack.dim:=n;
if tstack.sp1<>nil then begin
listbox1.Clear;
tstack.del;
end;
for i:=1 to n do begin
p:=random(40);
tstack.add(p);
listbox1.Items.Add(inttostr(p));
end;
end;

procedure TForm1.Button2Click(Sender: TObject);
var asd:tsel;
begin
tstack.bubl;
listbox1.Clear;
tstack.print(listbox1);
end;

procedure TForm1.Button3Click(Sender: TObject);
var l,i,max,min:integer;
begin
with tstack do begin
max:=sp1^.dig; min:=sp1^.dig;
sp:=sp1;
for i:=2 to n do begin
sp:=sp^.a;
if sp^.dig<min then min:=sp^.dig;
if sp^.dig>max then max:=sp^.dig;
end;
edit2.Text:='минимальное-'+inttostr(min)+' мaксимальное-'+inttostr(max);
end; end;

procedure TForm1.Button4Click(Sender: TObject);
begin
tstack.str(listbox2);
end;

procedure TForm1.Button5Click(Sender: TObject);
begin
tstack.strsort(listbox3);
end;

end.

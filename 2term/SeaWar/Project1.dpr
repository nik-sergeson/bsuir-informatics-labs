program Project1;

uses
  Forms,
  Unit1 in 'Unit1.pas' {Form1},
  classShip in 'classShip.pas',
  classGraph in 'classGraph.pas',
  classBrain in 'classBrain.pas',
  classHighs in 'classHighs.pas';

{$R *.res}

begin
  Application.Initialize;
  Application.CreateForm(TForm1, Form1);
  Application.Run;
end.

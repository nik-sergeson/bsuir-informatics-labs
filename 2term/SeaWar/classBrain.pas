unit classBrain;

interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, Grids;
  
  type
  Tbrain=class(tobject)
    Curx,Cury:Integer;
    procedure Easy(Size:integer);
    constructor create;
  end;

implementation

constructor tbrain.create;
begin
CurX:=0;
Cury:=0;
end;

procedure tbrain.Easy;
begin
CurX:=random(size);
CurY:=random(size);
end;
end.


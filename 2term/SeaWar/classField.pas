unit classField;

interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, Grids,classShip, StdCtrls;

 type
  Tfield=class(tobject)
    Dim,Nship,Move:Integer;
    GmStart:boolean;
    Field:array of array of Tship;
    ShipLeft:array of Integer;
    StrikeTable:array of array of boolean;
    procedure init();
    function AddShip(x,y,Size:integer;right:boolean):boolean;
    function LenCtr(Coor:Integer):Integer;
    function MaxShip:Integer;
    function ifStriked(x,y:integer):boolean;
    function Strike(x,y:integer):boolean;
    function GetHealth(x,y:integer):integer;
    function GetSize(x,y:integer):integer;
    function GetShipX(x,y,Count:integer):integer;
    function GetShipY(x,y,Count:integer):integer;
    constructor create;
    end;

implementation

  constructor tfield.create;
  var i,j:Integer;
  begin
    Nship:=4;
    Move:=0;
    Dim:=10;
    SetLength(Field,Dim,Dim);
    SetLength(StrikeTable,Dim,Dim);
    for i:=0 to Dim-1  do
      for j:=0 to Dim-1  do begin
        Field[i,j]:=nil;
        StrikeTable[i,j]:=false;
      end;
    SetLength(ShipLeft,Nship);
    j:=0;
    for i:=Nship-1 downto 0 do
      begin
        inc(j);
        ShipLeft[i]:=j;
      end;
  end;

  procedure tfield.init();
  var i,j,CtrX,CtrY,CountWay,ShipLength,Count:Integer;
  curway:Byte;
  IsEmpty,SetSh:Boolean;
  Way:set of Byte;
  begin
    j:=0;
    for i:=Nship-1 downto 0 do
      begin
        inc(j);
        ShipLeft[i]:=j;
      end;
    Randomize;
    while(MaxShip>0) do begin
    Way:=[];
    CtrX:=Random(Dim);
    CtrY:=Random(Dim);
    IsEmpty:=True;
    for i:=CtrX-Lenctr(CtrX) to CtrX+Lenctr(Dim-(1+CtrX)) do  begin
      for j:=CtrY-lenctr(CtrY) to CtrY+LenCtr(Dim-(1+CtrY)) do
        if((Field[i,j]=nil)=false) then
        begin
          IsEmpty:=False;
          Break;
        end;
        if(IsEmpty=False) then
          Break;
      end;
    if (IsEmpty=True) then
    begin
      CountWay:=0;
      SetSh:=false;
      while ((CountWay<4)and(SetSh=False)) do begin
        curway:=Random(4)+1;
        while (curway in Way) do
          curway:=Random(4)+1;
        Include(Way,curway);
        ShipLength:=1;
        IsEmpty:=True;
        case curway of
        1:
        begin
          for j:=CtrY-2 to CtrY-MaxShip do begin
            for i:=CtrX-Lenctr(CtrX) to CtrX+Lenctr(Dim-(1+CtrX)) do
             begin
             if (j<0) then
              Break;
             if((Field[i,j]=nil)=false) then begin
              IsEmpty:=False;
              Break;
              end;
             end;
             if(IsEmpty=False) then
              Break;
             if(j<0) then
             begin
             if (CtrY>0) then
             inc(ShipLength);
             Break;
             end;
              Inc(ShipLength);
          end;
          while((ShipLeft[ShipLength-1]=0)and (ShipLength>0)) do
            Dec(ShipLength);
          Inc(CountWay);
          if(ShipLength>0) then
          begin
           Field[CtrX,CtrY]:=Tship.create;
           Field[ctrx,ctry].Health:=shipLength;
           Field[CtrX,Ctry].Size:=Shiplength;
           setlength(Field[CtrX,Ctry].coordinates,ShipLength,2);
           Field[CtrX,Ctry].coordinates[0,0]:=CtrX;
           Field[CtrX,Ctry].coordinates[0,1]:=ctry;
           for Count:=1 to ShipLength-1 do begin
            Field[CtrX,CtrY-Count]:=Field[CtrX,CtrY];
            Field[CtrX,Ctry].coordinates[Count,0]:=CtrX;
            Field[CtrX,Ctry].coordinates[Count,1]:=Ctry-Count;
            end;
            SetSh:=True;
            Dec(ShipLeft[ShipLength-1]);
          end;
        end;
        2:
        begin
          for i:=CtrX+2 to CtrX+MaxShip do begin
            for j:=CtrY-Lenctr(CtrY) to CtrY+Lenctr(Dim-(1+CtrY)) do
             begin
             if (i>Dim-1) then
              Break;
             if((Field[i,j]=nil)=false) then  begin
              IsEmpty:=False;
              Break;
              end;
             end;
             if(IsEmpty=False) then
              Break;
             if(i>Dim-1) then
             begin
             if(CtrX<Dim-1) then
                inc(ShipLength);
             Break;
             end;
              Inc(ShipLength);
          end;
          while((ShipLeft[ShipLength-1]=0)and (ShipLength>0)) do
            Dec(ShipLength);
          Inc(CountWay);
          if(ShipLength>0) then
          begin
           Field[CtrX,CtrY]:=Tship.create;
           Field[ctrx,ctry].Health:=shipLength;
           Field[CtrX,Ctry].Size:=Shiplength;
           setlength(Field[CtrX,Ctry].coordinates,ShipLength,2);
           Field[CtrX,Ctry].coordinates[0,0]:=CtrX;
           Field[CtrX,Ctry].coordinates[0,1]:=ctry;
           for Count:=1 to ShipLength-1 do begin
            Field[CtrX+Count,CtrY]:=Field[ctrx,ctry];
            Field[CtrX,Ctry].coordinates[Count,0]:=CtrX+Count;
            Field[CtrX,Ctry].coordinates[Count,1]:=CtrY;
            end;
           SetSh:=True;
           Dec(ShipLeft[ShipLength-1]);
          end;
        end;
        3:
        begin
          for j:=CtrY+2 to CtrY+MaxShip do begin
            for i:=CtrX-Lenctr(CtrX) to CtrX+Lenctr(Dim-(1+CtrX)) do
             begin
             if (j>Dim-1) then
              Break;
             if((Field[i,j]=nil)=false) then  begin
              IsEmpty:=False;
              Break;
             end;
             end;
             if(IsEmpty=False) then
              Break;
             if(j>Dim-1) then
             begin
             if (CtrY<Dim-1) then
             inc(ShipLength);
             Break;
             end;
              Inc(ShipLength);
          end;
          while((ShipLeft[ShipLength-1]=0)and (ShipLength>0)) do
            Dec(ShipLength);
          Inc(CountWay);
          if(ShipLength>0) then
          begin
           Field[CtrX,CtrY]:=tship.create;
           Field[ctrx,ctry].Health:=shipLength;
           Field[CtrX,Ctry].Size:=Shiplength;
           setlength(Field[CtrX,Ctry].coordinates,ShipLength,2);
           Field[CtrX,Ctry].coordinates[0,0]:=CtrX;
           Field[CtrX,Ctry].coordinates[0,1]:=ctry;
           for Count:=1 to ShipLength-1 do begin
           Field[CtrX,CtrY+Count]:=Field[ctrx,ctry];
           Field[CtrX,Ctry].coordinates[Count,0]:=CtrX;
           Field[CtrX,Ctry].coordinates[Count,1]:=CtrY+Count;
           end;
           SetSh:=True;
           Dec(ShipLeft[ShipLength-1]);
          end;
        end;
        4:
        begin
          for i:=CtrX-2 to CtrX-MaxShip do begin
            for j:=CtrY-Lenctr(CtrY) to CtrY+Lenctr(Dim-(1+CtrY)) do
             begin
             if (i<0) then
              Break;
             if((Field[i,j]=nil)=false) then begin
              IsEmpty:=False;
              Break;
              end;
             end;
             if(IsEmpty=False) then
              Break;
             if(i<0) then
             begin
             if(CtrX>0) then
             inc(ShipLength);
             Break;
             end;
              Inc(ShipLength);
          end;
          while((ShipLeft[ShipLength-1]=0)and (ShipLength>0)) do
            Dec(ShipLength);
          Inc(CountWay);
          if(ShipLength>0) then
          begin
           Field[CtrX,CtrY]:=Tship.create;
           Field[ctrx,ctry].Health:=shipLength;
           Field[CtrX,Ctry].Size:=Shiplength;
           setlength(Field[CtrX,Ctry].coordinates,ShipLength,2);
           Field[CtrX,Ctry].coordinates[0,0]:=CtrX;
           Field[CtrX,Ctry].coordinates[0,1]:=ctry;
           for Count:=1 to ShipLength-1 do begin
                Field[CtrX-Count,CtrY]:=Field[ctrx,ctry];
                Field[CtrX,Ctry].coordinates[Count,0]:=CtrX-Count;
                Field[CtrX,Ctry].coordinates[Count,1]:=CtrY;
            end;
           SetSh:=True;
           Dec(ShipLeft[ShipLength-1]);
          end;
        end;
  end;
  end;
  end;
  end;
  end;

  function tfield.LenCtr(Coor:Integer):Integer;

  begin
	if (Coor>0) then
		Result:=1
	else Result:=0;
  end;

  function Tfield.MaxShip:Integer;
  var i:Integer;
  begin
    for i:=Nship-1 downto 0 do
      if((ShipLeft[i]=0)=false) then
        Break;
    if((i=0) and (ShipLeft[i]=0)) then
      Result:=0
    else
      Result:=i+1;
  end;

function Tfield.AddShip;
var i,j:integer;
res:boolean;
begin
res:=true;
if(right=true) then begin
for i:=x-LenCtr(x) to x+Size+Lenctr(Dim-(x+Size))-1 do begin
  for j:=y-LenCtr(y) to y+Lenctr(Dim-(1+y)) do
      if((Field[i,j]=nil)=false) then begin
        res:=false;
        break;
      end;
  if(res=false) then
    break;
end;
if(res=true) then begin
   Field[x,y]:=Tship.create;
   Field[x,y].Health:=Size;
   Field[x,y].Size:=Size;
   setlength(Field[x,y].coordinates,Size,2);
   Field[x,y].coordinates[0,0]:=x;
   Field[x,y].coordinates[0,1]:=y;
   for i:=1 to size-1 do  begin
      Field[x+i,y]:=Field[x,y];
      Field[x,y].coordinates[i,0]:=x+i;
      Field[x,y].coordinates[i,1]:=y;

end;
end;
end
else
begin
for i:=x-LenCtr(x) to x+Lenctr(Dim-(x+1)) do begin
  for j:=y-LenCtr(y) to y+Lenctr(Dim-(Size+y))+Size-1 do
      if((Field[i,j]=nil)=false) then begin
        res:=false;
        break;
      end;
  if(res=false) then
    break;
end;
if(res=true) then begin
   Field[x,y]:=Tship.create;
   Field[x,y].Health:=Size;
   Field[x,y].Size:=Size;
   setlength(Field[x,y].coordinates,Size,2);
   Field[x,y].coordinates[0,0]:=x;
   Field[x,y].coordinates[0,1]:=y;
   for i:=1 to size-1 do begin
      Field[x,y+i]:=Field[x,y];
      Field[x,y].coordinates[i,0]:=x;
      Field[x,y].coordinates[i,1]:=y+i;
end;
end;
end;
Result:=res;
end;

function tField.ifStriked(x,y:integer):boolean;
begin
if(StrikeTable[x,y]=true) then
        result:=true
else
        result:=false;
end;

function tField.Strike(x,y:integer):boolean;
begin
if(Field[x,y]=nil) then
        result:=false
else begin
        dec(Field[x,y].Health);
        result:=true;
end;
end;

function Tfield.GetHealth(x,y:integer):integer;
begin
result:=Field[x,y].health;
end;

function tfield.GetSize(x,y:integer):integer;
begin
result:=Field[x,y].size;
end;

function Tfield.GetShipX(x,y,Count:integer):integer;
begin
result:=field[x,y].coordinates[Count-1,0];
end;

function Tfield.GetShipY(x,y,Count:integer):integer;
begin
result:=field[x,y].coordinates[Count-1,1];
end;
end.

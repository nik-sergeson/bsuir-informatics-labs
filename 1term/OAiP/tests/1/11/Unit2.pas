unit Unit2;

interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls;
  procedure del(edit1:tedit;me:tmemo);

implementation
 procedure del;
 var s,s1:string;
 n:integer;
 begin
 s:=edit1.Text;
 s:=s+' ';
 while length(s)>0 do begin
 n:=pos(' ',s);
 s1:=copy(s,1,n-1);
   delete(s,1,n);
  if not odd(strtoint(s1)) then
  me.Lines.add(s1);
 end; end;
end.

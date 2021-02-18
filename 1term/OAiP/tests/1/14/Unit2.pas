unit Unit2;

interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls;
 procedure vyv(st:string;me:tmemo);

implementation
   procedure vyv;
   var i,n:integer;
   s1:string;
   begin
   for i:=1 to length(st) do begin
   if st[i]='[' then  begin
   n:=i; inc(n);
   repeat
   s1:=s1+st[n];
    inc(n);
    until st[n]=']' ;
     me.lines.add(s1);
   s1:='';
   end;

   end;end;
end.

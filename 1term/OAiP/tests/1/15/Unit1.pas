unit Unit2;

interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls;
  type fl=file of char;
  procedure kolvo(var file1:fl;x:char);

implementation
   procedure kolvo;
 var  x1:char; n1,n,i,k:integer;
   begin
   n:=0; k:=0;
   while not eof(file1) do begin
   read(file1,x1);
   if x1=x then inc(n);
   end;
   n1:=n;
   while n1>=1 do begin
   n1:=n1 div 10;
   inc(k); end;
   write(file1,x);
   for I:=1 to k do
   write(file1,inttostr(n)[i]);
   end;
end.

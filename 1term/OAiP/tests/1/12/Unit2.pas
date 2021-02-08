unit Unit2;

interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls;
  procedure pod(edit1:tedit);
implementation
  procedure pod;
  var
  s:string;
  a:set of char;
  i,n:integer;
  begin
  a:=[]; s:=edit1.Text;  n:=0;
  for i:=1 to length(s) do begin
  if not (s[i] in a) then begin
  include(a,s[i]); inc(n); end; end;
  edit1.Text:=edit1.Text+' -'+inttostr(n);
  end;
end.

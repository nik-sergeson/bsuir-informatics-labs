unit Unit2;

interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls;
  procedure fun(x0,x1,a,e:extended;memo1:tmemo);
implementation
    procedure fun;
    var x2,d:extended;

    begin
    repeat
    x2:=0.5*(x1+a/x0);
    d:=abs(x2-x1);
    x0:=x1;
    x1:=x2;
    until d<e ;
    memo1.lines.add('limit='+floattostr(x1));
    end;
end.

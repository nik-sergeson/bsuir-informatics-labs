unit Unit2;

interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs;
  type telem=record
  c,w:extended;
    end;
  resh=class(tobject)
  n:  byte;
  s,opts:set of byte;
  wmax,cmax:extended;
  a:array[1..100] of telem;
  procedure pp(i:byte);
  procedure vg(i:integer;wt,oct:extended);
  procedure ms;
  procedure mv;
  procedure ss;
  procedure ran(k:byte);
  end;
implementation
  Procedure resh.pp(i:byte);
	var j,k:byte;
        wt,ct:extended;
	begin
	 for j:=0 to 1 do begin
		if j=0 then Include(s,i)
		       else Exclude(S,i);
	if i<n then   pp(i+1)
	     else begin
	     	wt:=0; ct:=0;
	      	for k:=1 to n do
	     if k in S then begin
         wt:=wt+a[k].w; ct:=ct+a[k].c;end;
	   if (wt<=Wmax) and (ct>Cmax) then
				begin Cmax:=ct;opts:=S; end;
			end;
	 end;
   End;
  ////////////////////////
   procedure resh.vg;
   var ct,wt1,oct1:extended;
   begin
   try
   wt1:=wt+a[i].w;
   if (wt1<=wmax) then begin
   include(s,i);
   if i<n then vg(i+1,wt1,oct)
   else
   if oct>cmax then begin cmax:=oct; opts:=s; end;
   exclude(s,i); end;
   oct1:=oct-a[i].c; except showmessage('tththth'); end;
   if oct1>Cmax then
 if i<n then Vg(i+1,wt,oct1)
    else begin Cmax:=oct1; opts:=S end;

    end;
    //////////////////
    procedure resh.ms;
    var mc0,wt,ct:extended;
     i:integer;
    function maxi:byte;
    var i:integer;
    begin
    mc0:=0;
    for i:=1 to n do begin
    if not(i in s) and (a[i].c>mc0) then begin
    mc0:=a[i].c; maxi:=i; end; end; end;
    begin
    s:=[]; i:=maxi; wt:=0; ct:=0; a[n+1].w:=wmax;
    while wt+a[i].w<wmax do begin
    include(s,i); ct:=ct+a[i].c;
    wt:=wt+a[i].w;
    i:=maxi;
    end;
    opts:=s; cmax:=ct;
     end;
    ///////////////////////////////
    procedure resh.mv;
    var mv0,wt,ct:extended;
    i,l:integer;
    function maxv:byte;
    var i:integer;
    begin
       mv0:=a[1].w;
        for i:=1 to n do begin
    if not(i in s) and (a[i].w<mv0) then begin
    mv0:=a[i].w; maxv:=i; end; end; end;
    begin
    s:=[]; i:=maxv; wt:=0; ct:=0; l:=1;
    while (wt+a[i].w<wmax) and (l<=n) do begin
    include(s,i); inc(l);
    wt:=wt+a[i].w;  ct:=ct+a[i].c;
    i:=maxv;
    end;
    opts:=s;  cmax:=ct;
    end;
    ///////////////////////////////
    procedure resh.ss;
    var ss0,wt,ct:extended;
    i,l:integer;
    function maxss:byte;
     var i:integer;
     begin
       ss0:=0;
   for i:=1 to n do begin
    if not(i in s) and (a[i].c/a[i].w>ss0) then begin
    ss0:=a[i].c/a[i].w; maxss:=i; end; end; end;
    begin
    s:=[]; i:=maxss; wt:=0; ct:=0; l:=1;
    while (wt+a[i].w<wmax) and (l<=n) do begin
    include(s,i); inc(l);
    wt:=wt+a[i].w;  ct:=ct+a[i].c;
    i:=maxss;
    end;
    opts:=s;
     end;
    /////////////////////////////////
    procedure resh.ran;
    var p,l,i:integer;
    wtm,ctm,wt,ct:extended;
    begin
    wtm:=0; ctm:=0;
    for i:=1 to k do begin
     s:=[];  wt:=0; ct:=0; l:=1;
    while (wt+a[i].w<wmax) and (l<=n) do begin
    p:=random(n)+1;
    while p in s do
    p:=random(n)+1;
    include(s,p); inc(l);
    wt:=wt+a[p].w;  ct:=ct+a[p].c; end;
    if (wt>=wtm) and (ct>=ctm) then begin
     wtm:=wt; ctm:=ct; opts:=s; end;  //добавить множнство
    end;
    cmax:=ctm; end;

   end.

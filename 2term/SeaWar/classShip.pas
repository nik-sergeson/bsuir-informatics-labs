unit classShip;

interface
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, Grids;
  
  type
  Tship=class(tobject)
    Size,Health:Integer;
    Coordinates:array of array of integer;
  end;

implementation

end.
 
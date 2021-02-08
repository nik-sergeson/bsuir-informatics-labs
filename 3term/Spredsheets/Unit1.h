//---------------------------------------------------------------------------

#ifndef Unit1H
#define Unit1H
//---------------------------------------------------------------------------
#include <Classes.hpp>
#include <Controls.hpp>
#include <StdCtrls.hpp>
#include <Forms.hpp>
#include <Grids.hpp>
#include <Dialogs.hpp>
#include <ActnCtrls.hpp>
#include <ActnMan.hpp>
#include <ActnMenus.hpp>
#include <ToolWin.hpp>
#include <Menus.hpp>
//---------------------------------------------------------------------------
class TForm1 : public TForm
{
__published:	// IDE-managed Components
        TStringGrid *StringGrid1;
        TScrollBar *ScrollBar1;
        TScrollBar *ScrollBar2;
        TEdit *Edit1;
        TEdit *Edit2;
        TOpenDialog *OpenDialog1;
        TSaveDialog *SaveDialog1;
        TMainMenu *MainMenu1;
        TMenuItem *sccx1;
        TMenuItem *N1;
        TMenuItem *N2;
        TMenuItem *N3;
        TMenuItem *N4;
        TMenuItem *N5;
        TMenuItem *N6;
        TMenuItem *N7;
        TMenuItem *N8;
        TMenuItem *N9;
        TMenuItem *N10;
        TMenuItem *N11;
        TEdit *Edit3;
        TMenuItem *N12;
        void __fastcall FormCreate(TObject *Sender);
        void __fastcall ScrollBar2Change(TObject *Sender);
        void __fastcall StringGrid1SelectCell(TObject *Sender, int ACol,
          int ARow, bool &CanSelect);
        void __fastcall StringGrid1MouseWheelDown(TObject *Sender,
          TShiftState Shift, TPoint &MousePos, bool &Handled);
        void __fastcall StringGrid1MouseWheelUp(TObject *Sender,
          TShiftState Shift, TPoint &MousePos, bool &Handled);
        void __fastcall ScrollBar1Change(TObject *Sender);
        void __fastcall StringGrid1SetEditText(TObject *Sender, int ACol,
          int ARow, const AnsiString Value);
        void __fastcall StringGrid1KeyPress(TObject *Sender, char &Key);
        void __fastcall StringGrid1GetEditText(TObject *Sender, int ACol,
          int ARow, AnsiString &Value);
        void __fastcall N1Click(TObject *Sender);
        void __fastcall N2Click(TObject *Sender);
        void __fastcall Edit2KeyPress(TObject *Sender, char &Key);
        void __fastcall N4Click(TObject *Sender);
        void __fastcall StringGrid1MouseDown(TObject *Sender,
          TMouseButton Button, TShiftState Shift, int X, int Y);
        void __fastcall N5Click(TObject *Sender);
        void __fastcall N7Click(TObject *Sender);
        void __fastcall N9Click(TObject *Sender);
        void __fastcall N10Click(TObject *Sender);
        void __fastcall N11Click(TObject *Sender);
        void __fastcall Edit3KeyPress(TObject *Sender, char &Key);
        void __fastcall StringGrid1DblClick(TObject *Sender);
        void __fastcall N12Click(TObject *Sender);
private:	// User declarations
public:		// User declarations
        __fastcall TForm1(TComponent* Owner);
};
//---------------------------------------------------------------------------
extern PACKAGE TForm1 *Form1;
//---------------------------------------------------------------------------
#endif
 
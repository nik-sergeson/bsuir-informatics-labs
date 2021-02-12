object Form1: TForm1
  Left = 383
  Top = 101
  Width = 928
  Height = 555
  Caption = '='
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'MS Sans Serif'
  Font.Style = []
  Menu = MainMenu1
  OldCreateOrder = False
  OnCreate = FormCreate
  PixelsPerInch = 96
  TextHeight = 13
  object StringGrid1: TStringGrid
    Left = 16
    Top = 40
    Width = 825
    Height = 297
    ColCount = 10
    RowCount = 10
    Options = [goFixedVertLine, goFixedHorzLine, goVertLine, goHorzLine, goRangeSelect, goEditing]
    ScrollBars = ssNone
    TabOrder = 0
    OnDblClick = StringGrid1DblClick
    OnGetEditText = StringGrid1GetEditText
    OnKeyPress = StringGrid1KeyPress
    OnMouseDown = StringGrid1MouseDown
    OnMouseWheelDown = StringGrid1MouseWheelDown
    OnMouseWheelUp = StringGrid1MouseWheelUp
    OnSelectCell = StringGrid1SelectCell
    OnSetEditText = StringGrid1SetEditText
    RowHeights = (
      24
      24
      24
      24
      24
      24
      24
      24
      24
      24)
  end
  object ScrollBar1: TScrollBar
    Left = 16
    Top = 352
    Width = 817
    Height = 25
    PageSize = 0
    TabOrder = 1
    TabStop = False
    OnChange = ScrollBar1Change
  end
  object ScrollBar2: TScrollBar
    Left = 856
    Top = 40
    Width = 25
    Height = 289
    Kind = sbVertical
    PageSize = 0
    TabOrder = 2
    TabStop = False
    OnChange = ScrollBar2Change
  end
  object Edit1: TEdit
    Left = 16
    Top = 8
    Width = 289
    Height = 21
    TabOrder = 3
    Text = 'Edit1'
  end
  object Edit2: TEdit
    Left = 320
    Top = 8
    Width = 521
    Height = 21
    TabOrder = 4
    Text = 'Edit2'
    OnKeyPress = Edit2KeyPress
  end
  object Edit3: TEdit
    Left = 16
    Top = 8
    Width = 289
    Height = 21
    TabOrder = 5
    Text = 'Edit3'
    OnKeyPress = Edit3KeyPress
  end
  object OpenDialog1: TOpenDialog
    Filter = 'MyTable|*.dat'
    Left = 600
    Top = 448
  end
  object SaveDialog1: TSaveDialog
    Filter = 'MyTables|*.dat'
    Left = 632
    Top = 448
  end
  object MainMenu1: TMainMenu
    Left = 672
    Top = 448
    object sccx1: TMenuItem
      Caption = #1060#1072#1081#1083
      object N1: TMenuItem
        Caption = #1054#1090#1082#1088#1099#1090#1100
        OnClick = N1Click
      end
      object N2: TMenuItem
        Caption = #1057#1086#1093#1088#1072#1085#1080#1090#1100
        OnClick = N2Click
      end
      object N11: TMenuItem
        Caption = #1047#1072#1082#1088#1099#1090#1100
        OnClick = N11Click
      end
    end
    object N3: TMenuItem
      Caption = #1055#1088#1072#1074#1082#1072
      object N5: TMenuItem
        Caption = #1050#1086#1087#1080#1088#1086#1074#1072#1090#1100
        OnClick = N5Click
      end
      object N12: TMenuItem
        Caption = #1042#1089#1090#1072#1074#1080#1090#1100
        OnClick = N12Click
      end
      object N4: TMenuItem
        Caption = #1053#1072#1079#1072#1076
        OnClick = N4Click
      end
    end
    object N6: TMenuItem
      Caption = #1042#1099#1088#1086#1074#1085#1103#1090#1100
      object N7: TMenuItem
        Caption = #1055#1086' '#1096#1080#1088#1080#1085#1077
        OnClick = N7Click
      end
    end
    object N8: TMenuItem
      Caption = #1044#1072#1085#1085#1099#1077
      object N9: TMenuItem
        Caption = #1055#1086#1080#1089#1082
        OnClick = N9Click
      end
      object N10: TMenuItem
        Caption = #1057#1086#1088#1090#1080#1088#1086#1074#1082#1072
        OnClick = N10Click
      end
    end
  end
end

package com.lab3.gui;

import com.lab3.timers.TimeCounter;
import org.apache.poi.ss.formula.FormulaParseException;
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import javax.swing.*;
import javax.swing.table.AbstractTableModel;
import java.io.*;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;


public class ExcelTableModel extends AbstractTableModel {
    private ArrayList<String> columnNames;
    private XSSFSheet worksheet;
    private XSSFWorkbook workbook;
    private TimeCounter timerCounter;
    private int rowcount;
    private int colcount;
    private String path;
    private JTextField valuefield;
    private boolean readonlymode;

    public ExcelTableModel(String path, TimeCounter timerCounter, JTextField valuefield) throws IOException {
        columnNames = new ArrayList<String>();
        int defaultcolcount = 20;
        int defaultrowcount = 30;
        FileInputStream is = new FileInputStream(path);
        workbook = new XSSFWorkbook(is);
        worksheet = workbook.getSheetAt(0);
        this.path = path;
        this.timerCounter = timerCounter;
        for (int i = 0; i < 100; i++) {
            columnNames.add(Column(i));
        }
        rowcount = worksheet.getLastRowNum() + 1;
        colcount = 0;
        for (int i = 0; i < rowcount; i++) {
            Row currow = worksheet.getRow(i);
            if (currow == null)
                continue;
            colcount = Math.max(colcount, currow.getLastCellNum());
        }
        rowcount = Math.max(rowcount, defaultrowcount);
        colcount = Math.max(colcount, defaultcolcount);
        this.valuefield = valuefield;
        readonlymode = false;
    }

    public ExcelTableModel(TimeCounter timerCounter, JTextField valuefield) {
        columnNames = new ArrayList<String>();
        this.colcount = 20;
        this.rowcount = 30;
        workbook = new XSSFWorkbook();
        worksheet = workbook.createSheet();
        this.timerCounter = timerCounter;
        for (int i = 0; i < 100; i++) {
            columnNames.add(Column(i));
        }
        this.valuefield = valuefield;
        readonlymode = false;
    }

    public static String Column(int column) {
        --column;
        if (column >= 0 && column < 26)
            return Character.toString((char) ('A' + column));
        else if (column > 25)
            return Column(column / 26 - 1) + Column(column % 26);
        else
            return "";
    }

    public void setPath(String path) {
        this.path = path;
    }

    public void setTimerCounter(TimeCounter timerCounter) {
        this.timerCounter = timerCounter;
    }

    public int getColumnCount() {
        return colcount;
    }

    public void setColumnCount(int columnCount) {
        this.colcount = columnCount;
        if (columnCount > columnNames.size()) {
            for (int i = columnNames.size() - 1; i <= columnCount; i++)
                columnNames.add(Column(i));
        }
        fireTableStructureChanged();
    }

    public int getRowCount() {
        return rowcount;
    }

    public void setRowCount(int rowCount) {
        this.rowcount = rowCount;
        fireTableRowsInserted(rowCount, rowCount);
    }

    public String getColumnName(int col) {
        return columnNames.get(col);
    }

    public void DisplayCellValue(int row, int col) {
        String value = "";
        if (col == 0) {
            this.valuefield.setText("");
            return;
        }
        --col;
        Row xssfrow = worksheet.getRow(row);
        if (xssfrow == null) {
            this.valuefield.setText(value);
            return;
        }
        Cell cell = xssfrow.getCell(col);
        if (cell != null) {
            switch (cell.getCellType()) {
                case Cell.CELL_TYPE_STRING:
                    value = cell.getStringCellValue();
                    break;
                case Cell.CELL_TYPE_FORMULA:
                    value = "=" + cell.getCellFormula();
                    break;
                case Cell.CELL_TYPE_NUMERIC:
                    if (DateUtil.isCellDateFormatted(cell)) {
                        value = cell.getDateCellValue().toString();
                    } else {
                        value = Double.toString(cell.getNumericCellValue());
                    }
                    break;
                case Cell.CELL_TYPE_BLANK:
                    value = "";
                    break;
                case Cell.CELL_TYPE_BOOLEAN:
                    value = Boolean.toString(cell.getBooleanCellValue());
                    break;
            }
        }
        this.valuefield.setText(value);
    }

    public Object getValueAt(int row, int col) {
        if (col == 0)
            return Integer.toString(row + 1);
        --col;
        String value = "";
        Row xssfrow = worksheet.getRow(row);
        if (xssfrow == null)
            return value;
        Cell cell = xssfrow.getCell(col);
        if (cell != null) {
            switch (cell.getCellType()) {
                case Cell.CELL_TYPE_STRING:
                    value = cell.getStringCellValue();
                    break;
                case Cell.CELL_TYPE_FORMULA:
                    FormulaEvaluator evaluator = workbook.getCreationHelper().createFormulaEvaluator();
                    CellValue cellValue = evaluator.evaluate(cell);
                    switch (cellValue.getCellType()) {
                        case Cell.CELL_TYPE_BOOLEAN:
                            value = Boolean.toString(cellValue.getBooleanValue());
                            break;
                        case Cell.CELL_TYPE_NUMERIC:
                            value = Double.toString(cellValue.getNumberValue());
                            break;
                        case Cell.CELL_TYPE_STRING:
                            value = cellValue.getStringValue();
                            break;
                        case Cell.CELL_TYPE_BLANK:
                            break;
                        case Cell.CELL_TYPE_ERROR:
                            value = "Error";
                            break;
                        case Cell.CELL_TYPE_FORMULA:
                            break;
                    }
                    break;
                case Cell.CELL_TYPE_NUMERIC:
                    if (DateUtil.isCellDateFormatted(cell)) {
                        value = cell.getDateCellValue().toString();
                    } else {
                        value = Double.toString(cell.getNumericCellValue());
                    }
                    break;
                case Cell.CELL_TYPE_BLANK:
                    value = "";
                    break;
                case Cell.CELL_TYPE_BOOLEAN:
                    value = Boolean.toString(cell.getBooleanCellValue());
                    break;
            }
        }
        return value;
    }

    public Class getColumnClass(int c) {
        return String.class;
    }

    public boolean isCellEditable(int row, int col) {
        if (readonlymode)
            return false;
        if (col == 0)
            return false;
        --col;
        Row xssfrow = worksheet.getRow(row);
        if (xssfrow == null)
            return true;
        Cell cell = xssfrow.getCell(col);
        if (cell != null && cell.getCellType() == Cell.CELL_TYPE_FORMULA)
            return false;
        return true;
    }


    public void setValueAt(Object value, int row, int col) {
        if (timerCounter != null)
            timerCounter.Reset();
        if (readonlymode)
            return;
        if (col == 0)
            return;
        --col;
        String cellvalue = (String) value;
        if (worksheet.getRow(row) == null)
            worksheet.createRow(row);
        worksheet.getRow(row).createCell(col);
        if (cellvalue == "True")
            worksheet.getRow(row).getCell(col).setCellValue(true);
        else if (cellvalue == "False")
            worksheet.getRow(row).getCell(col).setCellValue(false);
        else {
            try {
                double dval = Double.parseDouble(cellvalue);
                worksheet.getRow(row).getCell(col).setCellValue(dval);
            } catch (NumberFormatException ex) {
                SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");
                try {
                    Date date = dateFormat.parse(cellvalue.trim());
                    worksheet.getRow(row).getCell(col).setCellValue(date);
                } catch (ParseException pe) {
                    if (cellvalue.length() != 0 && cellvalue.charAt(0) == '=') {
                        try {
                            worksheet.getRow(row).getCell(col).setCellFormula(cellvalue.substring(1));
                        } catch (FormulaParseException fex) {
                            worksheet.getRow(row).getCell(col).setCellValue("Error");
                        }
                    } else
                        worksheet.getRow(row).getCell(col).setCellValue(cellvalue);
                }
            }
        }
    }

    public void Save() throws IOException {
        if (workbook != null) {
            FileOutputStream out = new FileOutputStream(new File(path));
            workbook.write(out);
        }
    }

    public boolean isReadonlymode() {
        return readonlymode;
    }

    public void setReadonlymode(boolean readonlymode) {
        this.readonlymode = readonlymode;
    }

    public void Refresh() throws IOException {
        int defaultcolcount = 20;
        int defaultrowcount = 30;
        FileInputStream is = new FileInputStream(path);
        workbook = new XSSFWorkbook(is);
        worksheet = workbook.getSheetAt(0);
        rowcount = worksheet.getLastRowNum() + 1;
        colcount = 0;
        for (int i = 0; i < rowcount; i++) {
            Row currow = worksheet.getRow(i);
            if (currow == null)
                continue;
            colcount = Math.max(colcount, currow.getLastCellNum());
        }
        rowcount = Math.max(rowcount, defaultrowcount);
        colcount = Math.max(colcount, defaultcolcount);
        fireTableDataChanged();
    }
}
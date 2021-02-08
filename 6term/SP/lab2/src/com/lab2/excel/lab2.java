package com.lab2.excel;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import java.io.*;


public class lab2 {
    public static void main(String[] args){
        try {
            XSSFWorkbook workbook = new XSSFWorkbook();
            XSSFSheet sheet = workbook.createSheet("Test");
            Row row = sheet.createRow(0);
            Cell cell = row.createCell(0);
            cell.setCellValue(1);
            cell=row.createCell(1);
            cell.setCellValue(2);
            cell=row.createCell(2);
            cell.setCellFormula("A1+B1");
            FileOutputStream out = new FileOutputStream(new File("D:\\Labs\\labs.6term\\SP\\lab2\\src\\lab2.xlsx"));
            workbook.write(out);
            out.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        Thread writer1=new Thread(new excel(1));
        Thread writer2=new Thread(new excel(2));
        writer1.start();
        writer2.start();
    }
}

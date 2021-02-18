package com.lab2.excel;

import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.*;


public class excel implements Runnable {

    private int id;

    public excel(int id){
        this.id=id;
    }

    public void run(){
        try {
            FileInputStream file = new FileInputStream(new File("D:\\Labs\\labs.6term\\SP\\lab2\\src\\thread_excel.xlsx"));
            XSSFWorkbook workbook = new XSSFWorkbook(file);
            XSSFSheet sheet = workbook.getSheetAt(0);
            Cell cell = sheet.getRow(0).getCell(0);
            cell.setCellValue("thread" + Integer.toString(id));
            file.close();
            Thread.sleep(1000);
            FileOutputStream out = new FileOutputStream(new File("D:\\Labs\\labs.6term\\SP\\lab2\\src\\thread_excel.xlsx"));
            workbook.write(out);
            out.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

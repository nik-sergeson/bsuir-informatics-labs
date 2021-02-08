package com.lab3.gui;

import javax.swing.*;
import java.io.*;


public class NotepadModel {
    private String path;
    private String text;
    private boolean readonlymode;
    private JTextPane editorpane;

    public NotepadModel(String path, JTextPane editorpane) throws IOException {
        this.path=path;
        this.editorpane=editorpane;
        readonlymode=false;
        editorpane.setEnabled(!readonlymode);
        File infile=new File(path);
        FileInputStream fis=new FileInputStream(infile);
        byte[] data=new byte[(int) infile.length()+1];
        fis.read(data);
        text=new String(data);
        fis.close();
    }

    public NotepadModel(JTextPane editorpane) {
        text=new String();
        this.editorpane=editorpane;
    }

    public void setPath(String path){
        this.path=path;
    }

    public String GetText(){
        return text;
    }

    public void SetText(String text){this.text=text;}

    public void Save() throws IOException {
        FileOutputStream fos = new FileOutputStream(path);
        byte[] data = text.getBytes();
        fos.write(data);
    }

    public boolean isReadonlymode() {
        return readonlymode;
    }

    public void setReadonlymode(boolean readonlymode) {
        editorpane.setEnabled(!readonlymode);
        this.readonlymode = readonlymode;
    }

    public void UpdateView(){
        editorpane.setText(this.text);
    }

    public void UpdateModel(){
        this.text=editorpane.getText();
    }

    public void Refresh() throws IOException {
        File infile=new File(path);
        FileInputStream fis=new FileInputStream(infile);
        byte[] data=new byte[(int) infile.length()+1];
        fis.read(data);
        text=new String(data);
        fis.close();
        editorpane.setText(text);
    }
}

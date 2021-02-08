/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.lab8.utils;

import java.io.ByteArrayOutputStream;
import java.io.CharArrayWriter;
import java.io.File;
import java.io.InputStream;
import javax.xml.transform.Source;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.stream.StreamResult;
import javax.xml.transform.stream.StreamSource;


public class XSLTUtil {
    private String xsltPath;
    
    public XSLTUtil(String xsltPath) {
        this.xsltPath = xsltPath;
    }
    
     public ByteArrayOutputStream toHtmlStream(Source inXml) {
        TransformerFactory factory = TransformerFactory.newInstance();
        Source styleSource = new StreamSource(new File(this.xsltPath));
        Transformer transformer = null;
        try {
            transformer = factory.newTransformer(styleSource);
            ByteArrayOutputStream htmlData = new ByteArrayOutputStream();
            transformer.transform(inXml,  new StreamResult(htmlData));
            return htmlData;
        } catch (TransformerException ex) {
           ex.printStackTrace();
        }
        return null;
    }
}

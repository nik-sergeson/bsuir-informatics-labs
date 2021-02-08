package com.nik.training_courses.renders;

import com.nik.training_courses.models.TextContent;
import javafx.scene.layout.Pane;
import javafx.scene.layout.VBox;
import javafx.scene.text.Text;


public class TextContentRender {
    public Pane render(TextContent content){
        Text text=new Text(content.getText());
        Text name=new Text(content.getName());
        VBox vBox=new VBox(name, text);
        vBox.setSpacing(15);
        return vBox;
    }
}

package com.nik.training_courses.renders;

import com.nik.training_courses.models.ImageContent;
import javafx.scene.control.Label;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.Pane;
import javafx.scene.layout.VBox;
import javafx.scene.text.Text;

import java.io.File;



public class ImageContentRender {
    public Pane render(ImageContent content){
        Text name=new Text(content.getName());
        Image imageF=new Image(new File(content.getSource()).toURI().toString());
        ImageView imageView=new ImageView(imageF);
        imageView.setFitHeight(150);
        imageView.setFitWidth(150);
        VBox vBox=new VBox(name, imageView);
        vBox.setSpacing(15);
        return vBox;
    }
}

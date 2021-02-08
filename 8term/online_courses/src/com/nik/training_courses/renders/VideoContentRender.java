package com.nik.training_courses.renders;

import com.nik.training_courses.models.VideoContent;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.Pane;
import javafx.scene.layout.VBox;
import javafx.scene.media.Media;
import javafx.scene.media.MediaPlayer;
import javafx.scene.media.MediaView;
import javafx.scene.text.Text;

import java.io.File;


public class VideoContentRender {
    public Pane render(VideoContent content){
        Text name=new Text(content.getName());
        Media media = new Media(new File(content.getSource()).toURI().toString());
        MediaPlayer mediaPlayer = new MediaPlayer(media);
        MediaView mediaView=new MediaView(mediaPlayer);
        mediaView.setFitWidth(300);
        mediaView.setFitHeight(150);
        VBox vBox=new VBox(name, mediaView);
        vBox.setSpacing(15);
        return vBox;
    }
}

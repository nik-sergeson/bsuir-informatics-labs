package com.nik.training_courses.controllers.content;

import com.nik.training_courses.Screens;
import com.nik.training_courses.models.VideoContent;
import com.screensframework.ControlledScreen;
import com.screensframework.ScreensController;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.media.Media;
import javafx.scene.media.MediaPlayer;
import javafx.scene.media.MediaView;
import javafx.stage.FileChooser;
import javafx.stage.Stage;

import java.io.File;


public class VideoController implements ControlledScreen{
    protected ScreensController screensController;
    protected VideoContent editingVideoContent;
    protected Stage stage;
    protected String videoPath;
    protected  final FileChooser fileChooser = new FileChooser();

    @FXML
    private TextField name;

    @FXML
    private Button backButton;

    @FXML
    private MediaView video;

    @FXML
    private Button saveButton;

    @FXML
    private Button openButton;


    @FXML
    private Button playButton;

    @FXML
    void backButtonClicked(ActionEvent event) {
        screensController.setUpdatableScreen(Screens.SUBSECTION_VIEW, editingVideoContent.getParent());
        video.getMediaPlayer().stop();
        editingVideoContent=null;
    }

    @FXML
    void saveButtonClicked(ActionEvent event) {
        editingVideoContent.setName(name.getText());
        editingVideoContent.setSource(videoPath);
        editingVideoContent.save();
        screensController.setUpdatableScreen(Screens.SUBSECTION_VIEW, editingVideoContent.getParent());
        this.video.getMediaPlayer().stop();
        editingVideoContent=null;
    }

    @FXML
    void openButtonClicked(ActionEvent event) {
        File file = fileChooser.showOpenDialog(stage);
        videoPath=file.getAbsolutePath();
        Media media = new Media(file.toURI().toString());
        MediaPlayer mediaPlayer = new MediaPlayer(media);
        video.setMediaPlayer(mediaPlayer);
    }

    public VideoController(Stage stage){
        this.stage=stage;
    }

    @Override
    public void setScreenParent(ScreensController screenPage) {
        screensController=screenPage;
    }

    public void setViewValues(VideoContent videoContent){
        name.setText(videoContent.getName());
        videoPath=videoContent.getSource();
        if(new File(videoPath).exists()) {
            Media media = new Media(new File(videoPath).toURI().toString());
            MediaPlayer mediaPlayer = new MediaPlayer(media);
            video.setMediaPlayer(mediaPlayer);
        }
    }

    @FXML
    void playButtonClicked(ActionEvent event) {
        if(video.getMediaPlayer()!=null)
            video.getMediaPlayer().play();
    }

}

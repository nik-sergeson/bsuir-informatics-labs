package com.nik.training_courses.controllers.content;

import com.nik.training_courses.Screens;
import com.nik.training_courses.models.ImageContent;
import com.screensframework.ControlledScreen;
import com.screensframework.ScreensController;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.stage.FileChooser;
import javafx.stage.Stage;

import java.io.File;


public class ImageController implements ControlledScreen {
    protected ScreensController screensController;
    protected ImageContent editingImageContent;
    protected String imagePath;
    protected Stage stage;
    protected  final FileChooser fileChooser = new FileChooser();

    @FXML
    private ImageView image;

    @FXML
    private TextField name;

    @FXML
    private Button backButton;

    @FXML
    private Button saveButton;

    @FXML
    private Button openButton;

    @FXML
    void openButtonClicked(ActionEvent event) {
        File file = fileChooser.showOpenDialog(stage);
        imagePath=file.getAbsolutePath();
        Image imageF=new Image(new File(imagePath).toURI().toString());
        this.image.setImage(imageF);
    }

    @Override
    public void setScreenParent(ScreensController screenPage) {
        screensController=screenPage;
    }

    @FXML
    void saveButtonClicked(ActionEvent event) {
        editingImageContent.setName(name.getText());
        editingImageContent.setSource(imagePath);
        editingImageContent.save();
        screensController.setUpdatableScreen(Screens.SUBSECTION_VIEW, editingImageContent.getParent());
        editingImageContent=null;
    }

    @FXML
    void backButtonClicked(ActionEvent event) {
        screensController.setUpdatableScreen(Screens.SUBSECTION_VIEW, editingImageContent.getParent());
        editingImageContent=null;
    }

    public void setViewValues(ImageContent imageContent){
        name.setText(imageContent.getName());
        imagePath=imageContent.getSource();
        if(new File(imagePath).exists()) {
            Image imageF = new Image(new File(imagePath).toURI().toString());
            this.image.setImage(imageF);
        }
    }

    public ImageController(Stage stage){
        this.stage=stage;
    }
}

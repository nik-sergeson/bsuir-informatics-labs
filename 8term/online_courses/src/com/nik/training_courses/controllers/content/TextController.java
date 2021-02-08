package com.nik.training_courses.controllers.content;

import com.nik.training_courses.Screens;
import com.nik.training_courses.models.TextContent;
import com.screensframework.ControlledScreen;
import com.screensframework.ScreensController;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;


public class TextController implements ControlledScreen {
    protected ScreensController screensController;
    protected TextContent editingText;

    @FXML
    private TextField name;

    @FXML
    private Button backButton;

    @FXML
    private TextArea text;

    @FXML
    private Button saveButton;

    @FXML
    void backButtonClicked(ActionEvent event) {
        screensController.setUpdatableScreen(Screens.SUBSECTION_VIEW, editingText.getParent());
        editingText=null;
    }

    @FXML
    void saveButtonClicked(ActionEvent event) {
        editingText.setName(name.getText());
        editingText.setText(text.getText());
        editingText.save();
        screensController.setUpdatableScreen(Screens.SUBSECTION_VIEW, editingText.getParent());
        editingText=null;
    }

    @Override
    public void setScreenParent(ScreensController screenPage) {
        screensController=screenPage;
    }

    public void setViewValues(TextContent textContent){
        name.setText(textContent.getName());
        text.setText(textContent.getText());
    }
}

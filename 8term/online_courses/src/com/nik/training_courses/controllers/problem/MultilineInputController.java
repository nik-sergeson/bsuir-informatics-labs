package com.nik.training_courses.controllers.problem;

import com.nik.training_courses.Screens;
import com.nik.training_courses.models.MultilineInputProblem;
import com.screensframework.ControlledScreen;
import com.screensframework.ScreensController;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;


public class MultilineInputController implements ControlledScreen {
    protected ScreensController screensController;
    protected MultilineInputProblem editingProblem;

    @FXML
    private TextArea answer;

    @FXML
    private Button backButton;

    @FXML
    private TextField name;

    @FXML
    private TextArea description;

    @FXML
    private Button saveButton;

    @FXML
    void backButtonClicked(ActionEvent event) {
        screensController.setUpdatableScreen(Screens.SUBSECTION_VIEW, editingProblem.getParent());
        editingProblem=null;
    }

    @FXML
    void saveButtonClicked(ActionEvent event) {
        editingProblem.setCorrectAnswer(answer.getText());
        editingProblem.setName(name.getText());
        editingProblem.setDescription(description.getText());
        editingProblem.save();
        screensController.setUpdatableScreen(Screens.SUBSECTION_VIEW, editingProblem.getParent());
        editingProblem=null;
    }

    @Override
    public void setScreenParent(ScreensController screenPage) {
        screensController=screenPage;
    }

    void setViewValues(MultilineInputProblem problem){
        answer.setText(problem.getCorrectAnswer());
        name.setText(problem.getName());
        description.setText(problem.getDescription());
    }

}

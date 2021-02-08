package com.nik.training_courses.controllers;

import com.nik.training_courses.Screens;
import com.nik.training_courses.models.SubSection;
import com.screensframework.ControlledScreen;
import com.screensframework.ScreensController;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.CheckBox;
import javafx.scene.control.TextField;


public class SubsectionSettingsController implements ControlledScreen {
    protected SubSection editingSubSection;
    protected ScreensController screensController;

    @FXML
    protected CheckBox hideFromStudents;

    @FXML
    protected TextField name;

    @FXML
    protected Button backButton;

    @FXML
    protected Button saveButton;

    @FXML
    void backButtonClicked(ActionEvent event) {
        screensController.setUpdatableScreen(Screens.SECTION_VIEW, editingSubSection.getParent());
        editingSubSection=null;
    }

    @FXML
    void saveButtonClicked(ActionEvent event) {
        editingSubSection.setName(name.getText());
        editingSubSection.setHideFromStudents(hideFromStudents.isSelected());
        editingSubSection.save();
        screensController.setUpdatableScreen(Screens.SECTION_VIEW, editingSubSection.getParent());
        editingSubSection=null;
    }

    @Override
    public void setScreenParent(ScreensController screenPage) {
        screensController=screenPage;
    }

    public void setViewValues(SubSection subSection){
        name.setText(subSection.getName());
        hideFromStudents.setSelected(subSection.isHideFromStudents());
    }
}

package com.nik.training_courses.controllers;

import com.nik.training_courses.Screens;
import com.nik.training_courses.models.Section;
import com.screensframework.ControlledScreen;
import com.screensframework.ScreensController;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.CheckBox;
import javafx.scene.control.DatePicker;
import javafx.scene.control.TextField;

import java.time.Instant;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.util.Date;


public class SectionSettingsController implements ControlledScreen {
    protected ScreensController screensController;
    protected Section editingSection;

    @FXML
    protected DatePicker hardDeadline;

    @FXML
    protected CheckBox hideFromStudents;

    @FXML
    protected DatePicker releaseDate;

    @FXML
    protected Button backButton;

    @FXML
    private DatePicker softDeadline;

    @FXML
    protected Button saveButton;

    @FXML
    private TextField name;

    @FXML
    void backButtonClicked(ActionEvent event) {
        screensController.setUpdatableScreen(Screens.SECTION_VIEW, editingSection);
        editingSection=null;
    }

    @FXML
    void saveButtonClicked(ActionEvent event) {
        Instant instant = hardDeadline.getValue().atStartOfDay().atZone(ZoneId.systemDefault()).toInstant();
        editingSection.setHardDeadline(Date.from(instant));
        instant = releaseDate.getValue().atStartOfDay().atZone(ZoneId.systemDefault()).toInstant();
        editingSection.setSoftDeadline(Date.from(instant));
        instant = softDeadline.getValue().atStartOfDay().atZone(ZoneId.systemDefault()).toInstant();
        editingSection.setSoftDeadline(Date.from(instant));
        editingSection.setHideFromStudents(hideFromStudents.isSelected());
        editingSection.setName(name.getText());
        editingSection.save();
        screensController.setUpdatableScreen(Screens.COURSE_VIEW, editingSection.getParent());
        editingSection=null;
    }

    public void setViewValues(Section section){
        LocalDate softDln = LocalDateTime.ofInstant(Instant.ofEpochMilli(section.getSoftDeadline().getTime()), ZoneId.systemDefault()).toLocalDate();
        LocalDate hardDln = LocalDateTime.ofInstant(Instant.ofEpochMilli(section.getHardDeadline().getTime()), ZoneId.systemDefault()).toLocalDate();
        LocalDate release = LocalDateTime.ofInstant(Instant.ofEpochMilli(section.getReleaseDate().getTime()), ZoneId.systemDefault()).toLocalDate();
        hardDeadline.setValue(hardDln);
        softDeadline.setValue(softDln);
        releaseDate.setValue(release);
        hideFromStudents.setSelected(section.isHideFromStudents());
        name.setText(section.getName());
    }

    @Override
    public void setScreenParent(ScreensController screenPage) {
        screensController = screenPage;
    }

    public void initialize(){
    }
}

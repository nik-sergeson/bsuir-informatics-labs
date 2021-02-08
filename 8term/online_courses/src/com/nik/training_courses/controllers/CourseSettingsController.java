package com.nik.training_courses.controllers;

import com.nik.training_courses.Screens;
import com.nik.training_courses.models.Course;
import com.nik.training_courses.models.Language;
import com.screensframework.ControlledScreen;
import com.screensframework.ScreensController;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.*;

import java.time.Instant;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.util.Date;


public class CourseSettingsController implements ControlledScreen {
    protected ScreensController screensController;
    protected Course editingCourse;

    @FXML
    protected DatePicker endDate;

    @FXML
    protected DatePicker enrollmentStartDate;

    @FXML
    protected TextField organization;

    @FXML
    protected Button backButton;

    @FXML
    protected TextArea description;

    @FXML
    protected ChoiceBox<Language> language;

    @FXML
    protected Button saveButton;

    @FXML
    protected DatePicker enrollmentEndDate;

    @FXML
    protected DatePicker startDate;

    @FXML
    protected TextField name;

    @Override
    public void setScreenParent(ScreensController screenPage) {
        screensController=screenPage;
    }

    public void setViewValues(Date startDate, Date endDate, Date enrollmentStartDate, Date enrollmentEndDate, String name, String organization, String description, Language language){
        LocalDate start = LocalDateTime.ofInstant(Instant.ofEpochMilli(startDate.getTime()), ZoneId.systemDefault()).toLocalDate();
        LocalDate end = LocalDateTime.ofInstant(Instant.ofEpochMilli(endDate.getTime()), ZoneId.systemDefault()).toLocalDate();
        LocalDate enrollStart = LocalDateTime.ofInstant(Instant.ofEpochMilli(enrollmentStartDate.getTime()), ZoneId.systemDefault()).toLocalDate();
        LocalDate enrollEnd = LocalDateTime.ofInstant(Instant.ofEpochMilli(enrollmentEndDate.getTime()), ZoneId.systemDefault()).toLocalDate();
        this.startDate.setValue(start);
        this.endDate.setValue(end);
        this.enrollmentStartDate.setValue(enrollStart);
        this.enrollmentEndDate.setValue(enrollEnd);
        this.language.getSelectionModel().select(language);
        this.name.setText(name);
        this.organization.setText(organization);
        this.description.setText(description);
    }

    @FXML
    protected void backButtonClicked(ActionEvent event) {
        screensController.setUpdatableScreen(Screens.MAIN_SCREEN, null);
        editingCourse=null;
    }

    @FXML
    protected void saveButtonClicked(ActionEvent event) {
        Instant instant = startDate.getValue().atStartOfDay().atZone(ZoneId.systemDefault()).toInstant();
        editingCourse.getCourseSettings().setStartDate(Date.from(instant));
        instant = endDate.getValue().atStartOfDay().atZone(ZoneId.systemDefault()).toInstant();
        editingCourse.getCourseSettings().setEndDate(Date.from(instant));
        instant = enrollmentStartDate.getValue().atStartOfDay().atZone(ZoneId.systemDefault()).toInstant();
        editingCourse.getCourseSettings().setEnrollmentStartDate(Date.from(instant));
        instant = enrollmentEndDate.getValue().atStartOfDay().atZone(ZoneId.systemDefault()).toInstant();
        editingCourse.getCourseSettings().setEnrollmentEndDate(Date.from(instant));
        editingCourse.getCourseSettings().setLanguage(language.getValue());
        editingCourse.setName(name.getText());
        editingCourse.getCourseSettings().setOrganization(organization.getText());
        editingCourse.getCourseSettings().setDescription(description.getText());
        editingCourse.save();
        screensController.setUpdatableScreen(Screens.MAIN_SCREEN, null);
        editingCourse=null;
    }

    public void initialize(){
        language.getItems().addAll(Language.values());
    }

}

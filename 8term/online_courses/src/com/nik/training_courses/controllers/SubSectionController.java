package com.nik.training_courses.controllers;

import com.nik.training_courses.Screens;
import com.nik.training_courses.models.*;
import com.screensframework.ControlledScreen;
import com.screensframework.ScreensController;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.ListCell;
import javafx.scene.control.ListView;
import javafx.util.Callback;

import java.util.UUID;


public class SubSectionController implements ControlledScreen, UpdatableController {
    private ScreensController screensController;
    private SubSection currentSubSection;

    @FXML
    private Button deleteButton;

    @FXML
    private Button backButton;

    @FXML
    private ListView<Content> content;

    @FXML
    private ListView<Problem> problems;

    @FXML
    private Button settingsButton;


    @Override
    public void update(CourseStructureItem item) {
        currentSubSection = SubSection.getByID(item.getId());
        update();
    }

    public void update() {
        problems.getItems().clear();
        content.getItems().clear();
        ObservableList<Problem> problems = FXCollections.observableArrayList(currentSubSection.Problems());
        this.problems.setItems(problems);
        ObservableList<Content> contents = FXCollections.observableArrayList(currentSubSection.Content());
        this.content.setItems(contents);
    }

    @Override
    public void setScreenParent(ScreensController screenPage) {
        screensController = screenPage;
    }

    @FXML
    void backButtonClicked(ActionEvent event) {
        screensController.setUpdatableScreen(Screens.SECTION_VIEW, currentSubSection.getParent());
        currentSubSection = null;
    }

    @FXML
    void addImage(ActionEvent event) {
        screensController.setCreationScreen(Screens.IMAGE_CONTENT_CREATE, currentSubSection);
    }

    @FXML
    void addText(ActionEvent event) {
        screensController.setCreationScreen(Screens.TEXT_CONTENT_CREATE, currentSubSection);
    }

    @FXML
    void addVideo(ActionEvent event) {
        screensController.setCreationScreen(Screens.VIDEO_CONTENT_CREATE, currentSubSection);
    }

    @FXML
    void addInput(ActionEvent event) {
        screensController.setCreationScreen(Screens.INPUT_CREATE, currentSubSection);
    }

    @FXML
    void addMultilineInput(ActionEvent event) {
        screensController.setCreationScreen(Screens.MULITLINE_INPUT_CREATE, currentSubSection);
    }

    @FXML
    void addMultipleChoice(ActionEvent event) {
        screensController.setCreationScreen(Screens.MULTIPLE_CHOICE_CREATE, currentSubSection);
    }

    @FXML
    void addSingleChoice(ActionEvent event) {
        screensController.setCreationScreen(Screens.SINGLE_CHOICE_CREATE, currentSubSection);
    }

    @FXML
    void deleteButtonClicked(ActionEvent event) {
        screensController.setUpdatableScreen(Screens.SECTION_VIEW, currentSubSection.getParent());
        currentSubSection.delete();
        currentSubSection = null;
    }

    @FXML
    void settingsButtonClicked(ActionEvent event) {
        screensController.setUpdatableScreen(Screens.SUBSECTION_EDIT, currentSubSection);
    }

    public void initialize() {
        problems.setCellFactory(new Callback<ListView<Problem>,
                                        ListCell<Problem>>() {
                                    @Override
                                    public ListCell<Problem> call(ListView<Problem> list) {
                                        return new ProblemCell();
                                    }
                                }
        );
        content.setCellFactory(new Callback<ListView<Content>,
                                          ListCell<Content>>() {
                                      @Override
                                      public ListCell<Content> call(ListView<Content> list) {
                                          return new ContentCell();
                                      }
                                  }
        );
    }

}

class ProblemCell extends ListCell<Problem> {
    @Override
    public void updateItem(Problem item, boolean empty) {
        super.updateItem(item, empty);
        if (item != null) {
            setGraphic(item.render());
        }
        else {
            setGraphic(null);
        }
    }
}

class ContentCell extends ListCell<Content> {
    @Override
    public void updateItem(Content item, boolean empty) {
        super.updateItem(item, empty);
        if (item != null) {
            setGraphic(item.render());
        }
        else {
            setGraphic(null);
        }
    }
}


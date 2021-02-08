package com.nik.training_courses.controllers;

import com.nik.training_courses.Screens;
import com.nik.training_courses.models.Course;
import com.nik.training_courses.models.CourseStructureItem;
import com.screensframework.ControlledScreen;
import com.screensframework.ScreensController;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.ListCell;
import javafx.scene.control.ListView;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.VBox;
import javafx.scene.text.Text;
import javafx.util.Callback;

import java.util.Arrays;
import java.util.Observable;
import java.util.UUID;


public class CoursewareController implements ControlledScreen, UpdatableController {
    private ScreensController screensController;

    @FXML
    private Button newButton;

    @FXML
    private ListView<Course> courseList;

    public void setScreenParent(ScreensController screenParent) {
        screensController = screenParent;
    }

    @FXML
    void courseClicked(MouseEvent event) {
        screensController.setUpdatableScreen(Screens.COURSE_VIEW, courseList.getSelectionModel().getSelectedItem());
    }

    @FXML
    void newButtonClicked(ActionEvent event) {
        screensController.setCreationScreen(Screens.COURSE_CREATE, null);
    }

    public void initialize() {
        courseList.setCellFactory(new Callback<ListView<Course>,
                                           ListCell<Course>>() {
                                       @Override
                                       public ListCell<Course> call(ListView<Course> list) {
                                           return new CourseCell();
                                       }
                                   }
        );
    }

    @Override
    public void update(CourseStructureItem item) {
        update();
    }

    public void update() {
        courseList.getItems().clear();
        ObservableList<Course> courses=FXCollections.observableArrayList(Course.getAll());
        this.courseList.setItems(courses);
    }
}

class CourseCell extends ListCell<Course> {
    @Override
    public void updateItem(Course item, boolean empty) {
        super.updateItem(item, empty);
        if (item != null) {
            VBox vBox = new VBox();
            vBox.getChildren().addAll(Arrays.asList(new Text(item.getName()), new Text(item.getCourseSettings().getLanguage() +
                    "/" +item.getCourseSettings().getOrganization())));
            setGraphic(vBox);
        }
        else {
            setGraphic(null);
        }
    }
}

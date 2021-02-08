package com.nik.training_courses.controllers;

import com.nik.training_courses.Screens;
import com.nik.training_courses.models.Course;
import com.nik.training_courses.models.CourseStructureItem;
import com.nik.training_courses.models.Section;
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

import java.text.SimpleDateFormat;
import java.util.Arrays;
import java.util.UUID;


public class CourseController implements ControlledScreen, UpdatableController {
    private ScreensController screensController;
    private Course currentCourse;

    @FXML
    private Button addButton;

    @FXML
    private Button backButton;

    @FXML
    private Button deleteButton;

    @FXML
    private Button settingsButton;

    @FXML
    private ListView<Section> sectionList;

    @FXML
    void addButtonClicked(ActionEvent event) {
        screensController.setCreationScreen(Screens.SECTION_CREATE, currentCourse);
    }

    @FXML
    void sectionSelected(MouseEvent event) {
        screensController.setUpdatableScreen(Screens.SECTION_VIEW, sectionList.getSelectionModel().getSelectedItem());
    }

    @FXML
    void backButtonClicked(ActionEvent event) {
        screensController.setUpdatableScreen(Screens.MAIN_SCREEN, null);
        currentCourse=null;
    }

    @FXML
    void deleteButtonClicked(ActionEvent event) {
        currentCourse.delete();
        screensController.setUpdatableScreen(Screens.MAIN_SCREEN, null);
        currentCourse=null;
    }

    @FXML
    void settingsButtonClicked(ActionEvent event) {
        screensController.setUpdatableScreen(Screens.COURSE_EDIT, currentCourse);
    }


    public void setScreenParent(ScreensController screenParent){
        screensController = screenParent;
    }

    public void initialize(){
        sectionList.setCellFactory(new Callback<ListView<Section>,
                                           ListCell<Section>>() {
                                       @Override
                                       public ListCell<Section> call(ListView<Section> list) {
                                           return new SectionCell();
                                       }
                                   }
        );
    }

    @Override
    public void update(CourseStructureItem item) {
        currentCourse=Course.getByID(item.getId());
        update();
    }

    public void update() {
        ObservableList<Section> sections= FXCollections.observableArrayList(currentCourse.getCourseSections());
        this.sectionList.setItems(sections);
    }
}

class SectionCell extends ListCell<Section> {
    @Override
    public void updateItem(Section item, boolean empty) {
        super.updateItem(item, empty);
        VBox vBox = new VBox();
        if (item != null) {
            SimpleDateFormat dt1 = new SimpleDateFormat("yyyy-MM-dd");
            vBox.getChildren().addAll(Arrays.asList(new Text(item.getName()), new Text(dt1.format(item.getSoftDeadline())+
                    "/"+dt1.format(item.getHardDeadline()))));
            setGraphic(vBox);
        }
        else {
            setGraphic(null);
        }
    }
}

package com.nik.training_courses.controllers;

import com.nik.training_courses.Screens;
import com.nik.training_courses.models.CourseStructureItem;
import com.nik.training_courses.models.Section;
import com.nik.training_courses.models.SubSection;
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
import java.util.UUID;


public class SectionController implements ControlledScreen, UpdatableController {
    private ScreensController screensController;
    private Section currentSection;

    @FXML
    private Button deleteButton;

    @FXML
    private Button settingButton;

    @FXML
    private Button backButton;

    @FXML
    private Button addButton;

    @FXML
    private ListView<SubSection> subSectionList;

    @Override
    public void update(CourseStructureItem item) {
        currentSection = Section.getByID(item.getId());
        update();
    }

    public void update() {
        subSectionList.getItems().clear();
        ObservableList<SubSection> subSections= FXCollections.observableArrayList(currentSection.getSubSections());
        this.subSectionList.setItems(subSections);
    }

    @FXML
    void backButtonClicked(ActionEvent event) {
        screensController.setUpdatableScreen(Screens.COURSE_VIEW, currentSection.getParent());
        currentSection=null;
    }

    @Override
    public void setScreenParent(ScreensController screenPage) {
        screensController = screenPage;
    }

    public void initialize() {
        subSectionList.setCellFactory(new Callback<ListView<SubSection>,
                                           ListCell<SubSection>>() {
                                       @Override
                                       public ListCell<SubSection> call(ListView<SubSection> list) {
                                           return new SubsectionCell();
                                       }
                                   }
        );
    }

    @FXML
    void addButtonClicked(ActionEvent event) {
        screensController.setCreationScreen(Screens.SUBSECTION_CREATE, currentSection);
    }

    @FXML
    void deleteButtonClicked(ActionEvent event) {
        screensController.setUpdatableScreen(Screens.COURSE_VIEW, currentSection.getParent());
        currentSection.delete();
        currentSection=null;
    }

    @FXML
    void settingButtonClicked(ActionEvent event) {
        screensController.setUpdatableScreen(Screens.SECTION_EDIT, currentSection);
    }

    @FXML
    void subsectionSelected(MouseEvent event) {
        screensController.setUpdatableScreen(Screens.SUBSECTION_VIEW, subSectionList.getSelectionModel().getSelectedItem());
    }

}

class SubsectionCell extends ListCell<SubSection> {
    @Override
    public void updateItem(SubSection item, boolean empty) {
        super.updateItem(item, empty);
        VBox vBox = new VBox();
        if (item != null) {
            vBox.getChildren().addAll(Arrays.asList(new Text(item.getName()), new Text("Problems: "+item.Problems().size()+
            "  Content :" +item.Content().size())));
            setGraphic(vBox);
        }
        else {
            setGraphic(null);
        }
    }
}

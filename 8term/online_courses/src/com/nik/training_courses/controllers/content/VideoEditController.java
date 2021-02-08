package com.nik.training_courses.controllers.content;

import com.nik.training_courses.controllers.UpdatableController;
import com.nik.training_courses.models.CourseStructureItem;
import com.nik.training_courses.models.VideoContent;
import javafx.stage.Stage;

import java.util.UUID;


public class VideoEditController extends VideoController implements UpdatableController {
    @Override
    public void update(CourseStructureItem item) {
        editingVideoContent= VideoContent.getByID(item.getId());
        update();
    }

    public void update() {
        setViewValues(editingVideoContent);
    }

    public VideoEditController(Stage stage) {
        super(stage);
    }
}
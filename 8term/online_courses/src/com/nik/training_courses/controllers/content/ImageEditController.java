package com.nik.training_courses.controllers.content;

import com.nik.training_courses.controllers.UpdatableController;
import com.nik.training_courses.models.CourseStructureItem;
import com.nik.training_courses.models.ImageContent;
import javafx.stage.Stage;

import java.util.UUID;


public class ImageEditController extends ImageController implements UpdatableController {
    @Override
    public void update(CourseStructureItem item) {
        editingImageContent= ImageContent.getByID(item.getId());
        update();
    }

    public void update() {
        setViewValues(editingImageContent);
    }

    public ImageEditController(Stage stage) {
        super(stage);
    }
}
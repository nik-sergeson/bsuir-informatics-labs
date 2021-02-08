package com.nik.training_courses.controllers.content;

import com.nik.training_courses.controllers.CreationController;
import com.nik.training_courses.models.CourseStructureItem;
import com.nik.training_courses.models.ImageContent;
import com.nik.training_courses.models.SubSection;
import javafx.stage.Stage;


public class ImageCreateController   extends ImageController implements CreationController {
    @Override
    public void setNewItemParent(CourseStructureItem parent) {
        editingImageContent=new ImageContent((SubSection) parent);
        setViewValues(editingImageContent);
    }

    public ImageCreateController(Stage stage) {
        super(stage);
    }
}
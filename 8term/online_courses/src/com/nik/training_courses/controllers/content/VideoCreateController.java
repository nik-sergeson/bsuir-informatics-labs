package com.nik.training_courses.controllers.content;

import com.nik.training_courses.controllers.CreationController;
import com.nik.training_courses.models.CourseStructureItem;
import com.nik.training_courses.models.SubSection;
import com.nik.training_courses.models.VideoContent;
import javafx.stage.Stage;


public class VideoCreateController  extends VideoController implements CreationController {
    @Override
    public void setNewItemParent(CourseStructureItem parent) {
        editingVideoContent=new VideoContent((SubSection) parent);
        setViewValues(editingVideoContent);
    }

    public VideoCreateController(Stage stage) {
        super(stage);
    }
}

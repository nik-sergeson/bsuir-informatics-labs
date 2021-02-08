package com.nik.training_courses.controllers.content;

import com.nik.training_courses.controllers.UpdatableController;
import com.nik.training_courses.models.CourseStructureItem;
import com.nik.training_courses.models.TextContent;

import java.util.UUID;


public class TextEditController extends TextController implements UpdatableController {
    @Override
    public void update(CourseStructureItem item) {
        editingText= TextContent.getByID(item.getId());
        update();
    }

    public void update() {
        setViewValues(editingText);
    }
}
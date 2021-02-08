package com.nik.training_courses.controllers.content;

import com.nik.training_courses.controllers.CreationController;
import com.nik.training_courses.models.CourseStructureItem;
import com.nik.training_courses.models.SubSection;
import com.nik.training_courses.models.TextContent;


public class TextCreateController extends TextController implements CreationController {
    @Override
    public void setNewItemParent(CourseStructureItem parent) {
        editingText = new TextContent((SubSection) parent);
        setViewValues(editingText);
    }
}

package com.nik.training_courses.controllers;

import com.nik.training_courses.models.Course;
import com.nik.training_courses.models.CourseStructureItem;
import com.nik.training_courses.models.Section;


public class SectionCreateController extends SectionSettingsController implements CreationController {
    @Override
    public void setNewItemParent(CourseStructureItem parent) {
        editingSection=new Section((Course) parent);
        setViewValues(editingSection);
    }
}

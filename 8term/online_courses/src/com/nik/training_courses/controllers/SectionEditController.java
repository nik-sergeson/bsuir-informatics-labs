package com.nik.training_courses.controllers;

import com.nik.training_courses.models.CourseStructureItem;
import com.nik.training_courses.models.Section;

import java.util.UUID;


public class SectionEditController extends SectionSettingsController implements UpdatableController {
    @Override
    public void update(CourseStructureItem item) {
        editingSection= Section.getByID(item.getId());
        update();
    }


    public void update() {
        setViewValues(editingSection);
    }
}

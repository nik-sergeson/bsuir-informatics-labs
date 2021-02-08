package com.nik.training_courses.controllers;

import com.nik.training_courses.models.CourseStructureItem;
import com.nik.training_courses.models.SubSection;

import java.util.UUID;


public class SubSectionEditController extends SubsectionSettingsController implements UpdatableController {
    @Override
    public void update(CourseStructureItem item) {
        editingSubSection=SubSection.getByID(item.getId());
        update();
    }

    public void update() {
        setViewValues(editingSubSection);
    }
}

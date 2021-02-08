package com.nik.training_courses.controllers;

import com.nik.training_courses.models.CourseStructureItem;
import com.nik.training_courses.models.Section;
import com.nik.training_courses.models.SubSection;


public class SubSectionCreateController extends SubsectionSettingsController implements CreationController {
    @Override
    public void setNewItemParent(CourseStructureItem parent) {
        editingSubSection=new SubSection("Subsection", (Section) parent);
        setViewValues(editingSubSection);
    }
}

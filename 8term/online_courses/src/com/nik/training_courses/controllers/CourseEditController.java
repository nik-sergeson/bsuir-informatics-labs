package com.nik.training_courses.controllers;

import com.nik.training_courses.models.Course;
import com.nik.training_courses.models.CourseSettings;
import com.nik.training_courses.models.CourseStructureItem;

import java.util.UUID;


public class CourseEditController extends CourseSettingsController implements UpdatableController {
    @Override
    public void update(CourseStructureItem item) {
        editingCourse=Course.getByID(item.getId());
        update();
    }

    public void update() {
        CourseSettings courseSettings=editingCourse.getCourseSettings();
        setViewValues(courseSettings.getStartDate(), courseSettings.getEndDate(), courseSettings.getEnrollmentStartDate(),
                courseSettings.getEnrollmentEndDate(), editingCourse.getName(), courseSettings.getOrganization(),
                courseSettings.getDescription(), courseSettings.getLanguage());
    }
}

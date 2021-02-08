package com.nik.training_courses.controllers;

import com.nik.training_courses.models.Course;
import com.nik.training_courses.models.CourseSettings;
import com.nik.training_courses.models.CourseStructureItem;


public class CourseCreateController extends CourseSettingsController implements CreationController {
    @Override
    public void setNewItemParent(CourseStructureItem parent) {
        editingCourse=new Course("Course", null, new CourseSettings());
        CourseSettings courseSettings=editingCourse.getCourseSettings();
        setViewValues(courseSettings.getStartDate(), courseSettings.getEndDate(), courseSettings.getEnrollmentStartDate(),
                courseSettings.getEnrollmentEndDate(), editingCourse.getName(), courseSettings.getOrganization(),
                courseSettings.getDescription(), courseSettings.getLanguage());
    }
}

package com.nik.training_courses.sql_saver;

import com.nik.training_courses.models.Course;

import java.util.List;


public interface ICourseSaver extends Saver<Course>{
    List<Course> getAll();
}

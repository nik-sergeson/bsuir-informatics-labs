package com.nik.training_courses.sql_saver;


import com.nik.training_courses.models.CourseStructureItem;

import java.util.UUID;

public interface Saver <T extends CourseStructureItem>{
    void create(T item);
    T read(Long id);
    void delete(T item);
    void update(T item);
}

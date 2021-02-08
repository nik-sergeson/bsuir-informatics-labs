package com.nik.training_courses.controllers.problem;

import com.nik.training_courses.controllers.UpdatableController;
import com.nik.training_courses.models.CourseStructureItem;
import com.nik.training_courses.models.MultilineInputProblem;

import java.util.UUID;


public class MultilineInputEditController extends MultilineInputController implements UpdatableController {
    @Override
    public void update(CourseStructureItem item) {
        editingProblem= MultilineInputProblem.getByID(item.getId());
        update();
    }

    public void update() {
        setViewValues(editingProblem);
    }
}
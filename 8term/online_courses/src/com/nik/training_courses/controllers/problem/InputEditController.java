package com.nik.training_courses.controllers.problem;

import com.nik.training_courses.controllers.UpdatableController;
import com.nik.training_courses.models.CourseStructureItem;
import com.nik.training_courses.models.InputProblem;

import java.util.UUID;


public class InputEditController extends InputController implements UpdatableController {
    @Override
    public void update(CourseStructureItem item) {
        editingProblem= InputProblem.getByID(item.getId());
        update();
    }

    public void update() {
        setViewValues(editingProblem);
    }
}

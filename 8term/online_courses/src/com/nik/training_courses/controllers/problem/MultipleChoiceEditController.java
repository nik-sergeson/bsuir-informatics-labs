package com.nik.training_courses.controllers.problem;

import com.nik.training_courses.controllers.UpdatableController;
import com.nik.training_courses.models.CourseStructureItem;
import com.nik.training_courses.models.MultipleChoiceProblem;

import java.util.UUID;


public class MultipleChoiceEditController extends MultipleChoiceController implements UpdatableController {
    @Override
    public void update(CourseStructureItem item) {
        editingProblem= MultipleChoiceProblem.getByID(item.getId());
        update();
    }

    public void update() {
        setViewValues(editingProblem);
    }
}

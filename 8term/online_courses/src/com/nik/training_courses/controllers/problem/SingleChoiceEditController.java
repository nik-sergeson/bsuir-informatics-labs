package com.nik.training_courses.controllers.problem;

import com.nik.training_courses.controllers.UpdatableController;
import com.nik.training_courses.models.CourseStructureItem;
import com.nik.training_courses.models.SingleChoiceProblem;

import java.util.UUID;


public class SingleChoiceEditController extends SingleChoiceController implements UpdatableController {
    @Override
    public void update(CourseStructureItem item) {
        editingProblem=SingleChoiceProblem.getByID(item.getId());
        update();
    }

    public void update() {
        setViewValues(editingProblem);
    }

}

package com.nik.training_courses.controllers.problem;

import com.nik.training_courses.controllers.CreationController;
import com.nik.training_courses.models.CourseStructureItem;
import com.nik.training_courses.models.SingleChoiceProblem;
import com.nik.training_courses.models.SubSection;


public class SingleChoiceCreateController extends SingleChoiceController implements CreationController {
    @Override
    public void setNewItemParent(CourseStructureItem parent) {
        editingProblem=new SingleChoiceProblem((SubSection) parent);
        setViewValues(editingProblem);
    }
}

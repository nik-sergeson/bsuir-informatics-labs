package com.nik.training_courses.controllers.problem;

import com.nik.training_courses.controllers.CreationController;
import com.nik.training_courses.models.CourseStructureItem;
import com.nik.training_courses.models.MultipleChoiceProblem;
import com.nik.training_courses.models.SubSection;


public class MultipleChoiceCreateController extends MultipleChoiceController implements CreationController {
    @Override
    public void setNewItemParent(CourseStructureItem parent) {
        editingProblem=new MultipleChoiceProblem((SubSection) parent);
        setViewValues(editingProblem);
    }
}

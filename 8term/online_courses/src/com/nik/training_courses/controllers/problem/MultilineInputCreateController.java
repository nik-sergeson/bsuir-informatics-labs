package com.nik.training_courses.controllers.problem;

import com.nik.training_courses.controllers.CreationController;
import com.nik.training_courses.models.CourseStructureItem;
import com.nik.training_courses.models.MultilineInputProblem;
import com.nik.training_courses.models.SubSection;


public class MultilineInputCreateController extends MultilineInputController implements CreationController {
    @Override
    public void setNewItemParent(CourseStructureItem parent) {
        editingProblem=new MultilineInputProblem((SubSection) parent);
        setViewValues(editingProblem);
    }
}
package com.nik.training_courses.controllers.problem;

import com.nik.training_courses.controllers.CreationController;
import com.nik.training_courses.models.CourseStructureItem;
import com.nik.training_courses.models.InputProblem;
import com.nik.training_courses.models.SubSection;


public class InputCreateController extends InputController implements CreationController {
    @Override
    public void setNewItemParent(CourseStructureItem parent) {
        editingProblem=new InputProblem((SubSection) parent);
        setViewValues(editingProblem);
    }
}

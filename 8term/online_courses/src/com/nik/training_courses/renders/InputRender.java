package com.nik.training_courses.renders;

import com.nik.training_courses.models.InputProblem;
import javafx.scene.control.Label;
import javafx.scene.layout.Pane;
import javafx.scene.layout.VBox;
import javafx.scene.text.Text;


public class InputRender {
    public Pane render(InputProblem problem){
        Text description=new Text(problem.getDescription());
        Text name=new Text(problem.getName());
        VBox vBox=new VBox(name, description);
        vBox.setSpacing(15);
        return vBox;
    }
}

package com.nik.training_courses.renders;

import com.nik.training_courses.models.SingleChoiceProblem;
import javafx.scene.control.Label;
import javafx.scene.layout.Pane;
import javafx.scene.layout.VBox;
import javafx.scene.text.Text;


public class SingleCnoiceRender {
    public  Pane render(SingleChoiceProblem problem){
        Text description=new Text(problem.getDescription());
        Text name=new Text(problem.getName());
        VBox vBox=new VBox(name, description);
        vBox.setSpacing(15);
        return vBox;
    }
}

package com.nik.training_courses.models;

import com.nik.training_courses.Main;
import com.nik.training_courses.renders.InputRender;
import com.nik.training_courses.renders.MultilineInputRender;
import com.nik.training_courses.sql_saver.Saver;
import javafx.scene.layout.Pane;

import javax.persistence.*;
import java.util.UUID;


@Entity
@Table(name = "multiline_input_problem")
public class MultilineInputProblem extends Problem{
    private String description;
    private String correctAnswer;
    private SubSection parent;
    private static Saver<MultilineInputProblem> saver;
    private static MultilineInputRender render;

    @Column(name = "Description")
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    @Column(name = "Correct_Answer")
    public String getCorrectAnswer() {
        return correctAnswer;
    }

    public void setCorrectAnswer(String correctAnswer) {
        this.correctAnswer = correctAnswer;
    }

    public static void setRender(MultilineInputRender mutlRender) {
        render = mutlRender;
    }

    public static MultilineInputRender getRender() {
        return render;
    }

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "parent_ID")
    public SubSection getParent() {
        return parent;
    }

    public void setParent(SubSection parent) {
        this.parent = parent;
    }

    public MultilineInputProblem(){
        this(null);
    }

    public MultilineInputProblem(SubSection parent){
        super("Input problem", 0);
        this.description="Description";
        this.correctAnswer="Answer";
        this.parent=parent;
    }

    public MultilineInputProblem(String name, int gradingPoints, SubSection parent) {
        super(name, gradingPoints);
        this.description="Description";
        this.correctAnswer="Answer";
        this.parent=parent;
    }

    public MultilineInputProblem(String name, int gradingPoints, String description, String correctAnswer, SubSection parent) {
        super(name, gradingPoints);
        this.description = description;
        this.correctAnswer = correctAnswer;
        this.parent=parent;
    }

    @Override
    public Long ParentID() {
        return parent.getId();
    }

    public static void setSaver(Saver<MultilineInputProblem> saver) {
        MultilineInputProblem.saver = saver;
    }

    public static MultilineInputProblem getByID(Long id){
        return saver.read(id);
    }

    @Override
    public void save() {
        if(!created)
            create();
        else
            saver.update(this);
    }

    private void create(){
        created=true;
        saver.create(this);
        parent.getMultilineInputProblems().add(this);
    }

    @Override
    public void delete() {
        saver.delete(this);
        created =false;
    }


    @Override
    public Pane render() {
        return render.render(this);
    }
}

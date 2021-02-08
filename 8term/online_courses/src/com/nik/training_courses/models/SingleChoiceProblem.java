package com.nik.training_courses.models;

import com.nik.training_courses.Main;
import com.nik.training_courses.renders.SingleCnoiceRender;
import com.nik.training_courses.sql_saver.Saver;
import javafx.scene.effect.Light;
import javafx.scene.layout.Pane;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;


@Entity
@Table(name = "single_choice_problem")
public class SingleChoiceProblem extends Problem{
    private List<String> answers;
    private Integer correctAnswerIndex;
    private String description;
    private SubSection parent;
    private static Saver<SingleChoiceProblem> saver;
    private static SingleCnoiceRender render;

    @ElementCollection
    public List<String> getAnswers() {
        return answers;
    }

    @Column(name = "Correct_Answer")
    public int getCorrectAnswerIndex() {
        return correctAnswerIndex;
    }

    @Column(name = "Description")
    public String getDescription() {
        return description;
    }

    public void setCorrectAnswerIndex(int correctAnswerIndex) {
        this.correctAnswerIndex = correctAnswerIndex;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public static void setRender(SingleCnoiceRender render) {
        SingleChoiceProblem.render = render;
    }

    public void setAnswers(List<String> answers) {
        this.answers = answers;
    }

    public void setCorrectAnswerIndex(Integer correctAnswerIndex) {
        this.correctAnswerIndex = correctAnswerIndex;
    }

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "parent_ID")
    public SubSection getParent() {
        return parent;
    }

    public void setParent(SubSection parent) {
        this.parent = parent;
    }

    @Override
    public Long ParentID() {
        return parent.getId();
    }

    public SingleChoiceProblem(){
        this(null);
    }

    public SingleChoiceProblem(SubSection parent){
        super("Single Choice", 0);
        this.parent=parent;
        this.answers=new ArrayList<>();
        this.correctAnswerIndex=-1;
        this.description="Description";
    }

    public SingleChoiceProblem(String name, int gradingPoints, ArrayList<String> answers, int correctAnswerIndex, String description, SubSection parent) {
        super(name, gradingPoints);
        this.parent=parent;
        this.answers = answers;
        this.correctAnswerIndex = correctAnswerIndex;
        this.description = description;
    }

    public static void setSaver(Saver<SingleChoiceProblem> saver) {
        SingleChoiceProblem.saver = saver;
    }

    public static SingleChoiceProblem getByID(Long id){
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
        parent.getSingleChoiceProblems().add(this);
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

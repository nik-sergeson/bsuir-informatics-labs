package com.nik.training_courses.models;

import com.nik.training_courses.Main;
import com.nik.training_courses.renders.MultipleChoiceRender;
import com.nik.training_courses.sql_saver.Saver;
import javafx.scene.layout.Pane;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;


@Entity
@Table(name = "multiline_choice_problem")
public class MultipleChoiceProblem extends Problem {
    private List<String> answers;
    private List<Integer> correctAnswers;
    private String description;
    private SubSection parent;
    private static Saver<MultipleChoiceProblem> saver;
    private static MultipleChoiceRender render;

    @ElementCollection
    public List<String> getAnswers() {
        return answers;
    }

    @ElementCollection
    public List<Integer> getCorrectAnswers() {
        return correctAnswers;
    }

    public void setAnswers(List<String> answers) {
        this.answers = answers;
    }

    public void setCorrectAnswers(List<Integer> correctAnswers) {
        this.correctAnswers = correctAnswers;
    }

    @Column(name = "Description")
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public static void setRender(MultipleChoiceRender render) {
        MultipleChoiceProblem.render = render;
    }

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "parent_ID")
    public SubSection getParent() {
        return parent;
    }

    public void setParent(SubSection parent) {
        this.parent = parent;
    }

    public MultipleChoiceProblem(){
        this(null);
    }

    public MultipleChoiceProblem(SubSection parent) {
        super("Multiple Choice", 0);
        this.parent=parent;
        this.answers=new ArrayList<>();
        this.correctAnswers=new ArrayList<>();
        this.description="Description";
    }


    public MultipleChoiceProblem(String name, int gradingPoints, ArrayList<String> answers, ArrayList<Integer> correctAnswers, String description, SubSection parent) {
        super(name, gradingPoints);
        this.answers = answers;
        this.correctAnswers = correctAnswers;
        this.description = description;
        this.parent=parent;
    }

    @Override
    public Long ParentID() {
        return parent.getId();
    }

    public static MultipleChoiceProblem getByID(Long id){
        return saver.read(id);
    }

    public static void setSaver(Saver<MultipleChoiceProblem> saver) {
        MultipleChoiceProblem.saver = saver;
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
        parent.getMultipleChoiceProblems().add(this);
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

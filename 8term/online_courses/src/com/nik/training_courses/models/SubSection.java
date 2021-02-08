package com.nik.training_courses.models;

import com.nik.training_courses.Main;
import com.nik.training_courses.sql_saver.Saver;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;


@Entity
@Table(name = "subsections")
public class SubSection extends CourseStructureItem {
    private Boolean hideFromStudents;
    private List<InputProblem> inputProblems;
    private List<MultilineInputProblem> multilineInputProblems;
    private List<SingleChoiceProblem> singleChoiceProblems;
    private List<MultipleChoiceProblem> multipleChoiceProblems;
    private List<TextContent> textContents;
    private List<ImageContent> imageContents;
    private List<VideoContent> videoContents;
    private static Saver<SubSection> saver;
    private Section parent;

    @Column(name = "Hide_From_Students")
    public boolean isHideFromStudents() {
        return hideFromStudents;
    }

    public ArrayList<Problem> Problems(){
        ArrayList<Problem> problems=new ArrayList<Problem>();
        problems.addAll(inputProblems);
        problems.addAll(multilineInputProblems);
        problems.addAll(singleChoiceProblems);
        problems.addAll(multipleChoiceProblems);
        return problems;
    }

    public ArrayList<Content> Content(){
        ArrayList<Content> contents=new ArrayList<>();
        contents.addAll(textContents);
        contents.addAll(videoContents);
        contents.addAll(imageContents);
        return contents;
    }

    public void setHideFromStudents(boolean hideFromStudents) {
        this.hideFromStudents = hideFromStudents;
    }

    @Column(name = "Hide_From_Students")
    public Boolean getHideFromStudents() {
        return hideFromStudents;
    }

    public void setHideFromStudents(Boolean hideFromStudents) {
        this.hideFromStudents = hideFromStudents;
    }

    @OneToMany(mappedBy = "parent", fetch = FetchType.LAZY, cascade=CascadeType.REMOVE)
    public List<InputProblem> getInputProblems() {
        return inputProblems;
    }

    public void setInputProblems(List<InputProblem> inputProblems) {
        this.inputProblems = inputProblems;
    }

    @OneToMany(mappedBy = "parent", fetch = FetchType.LAZY, cascade=CascadeType.REMOVE)
    public List<MultilineInputProblem> getMultilineInputProblems() {
        return multilineInputProblems;
    }

    public void setMultilineInputProblems(List<MultilineInputProblem> multilineInputProblems) {
        this.multilineInputProblems = multilineInputProblems;
    }

    @OneToMany(mappedBy = "parent", fetch = FetchType.LAZY, cascade=CascadeType.REMOVE)
    public List<SingleChoiceProblem> getSingleChoiceProblems() {
        return singleChoiceProblems;
    }

    public void setSingleChoiceProblems(List<SingleChoiceProblem> singleChoiceProblems) {
        this.singleChoiceProblems = singleChoiceProblems;
    }

    @OneToMany(mappedBy = "parent", fetch = FetchType.LAZY, cascade=CascadeType.REMOVE)
    public List<MultipleChoiceProblem> getMultipleChoiceProblems() {
        return multipleChoiceProblems;
    }

    public void setMultipleChoiceProblems(List<MultipleChoiceProblem> multipleChoiceProblems) {
        this.multipleChoiceProblems = multipleChoiceProblems;
    }

    @OneToMany(mappedBy = "parent", fetch = FetchType.LAZY, cascade=CascadeType.REMOVE)
    public List<TextContent> getTextContents() {
        return textContents;
    }

    public void setTextContents(List<TextContent> textContents) {
        this.textContents = textContents;
    }

    @OneToMany(mappedBy = "parent", fetch = FetchType.LAZY, cascade=CascadeType.REMOVE)
    public List<ImageContent> getImageContents() {
        return imageContents;
    }

    public void setImageContents(List<ImageContent> imageContents) {
        this.imageContents = imageContents;
    }

    @OneToMany(mappedBy = "parent", fetch = FetchType.LAZY, cascade=CascadeType.REMOVE)
    public List<VideoContent> getVideoContents() {
        return videoContents;
    }

    public void setVideoContents(List<VideoContent> videoContents) {
        this.videoContents = videoContents;
    }

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "parent_ID")
    public Section getParent() {
        return parent;
    }

    public void setParent(Section parent) {
        this.parent = parent;
    }

    public SubSection(String name, Boolean hideFromStudents, ArrayList<InputProblem> inputProblems, ArrayList<MultilineInputProblem> multilineInputProblems, ArrayList<SingleChoiceProblem> singleChoiceProblems, ArrayList<MultipleChoiceProblem> multipleChoiceProblems, ArrayList<TextContent> textContents, ArrayList<ImageContent> imageContents, ArrayList<VideoContent> videoContents, Section parent) {
        super(name);
        this.hideFromStudents = hideFromStudents;
        this.inputProblems = inputProblems;
        this.multilineInputProblems = multilineInputProblems;
        this.singleChoiceProblems = singleChoiceProblems;
        this.multipleChoiceProblems = multipleChoiceProblems;
        this.textContents = textContents;
        this.imageContents = imageContents;
        this.videoContents = videoContents;
        this.parent = parent;
    }

    public SubSection(String name, Section parent){
        this();
        this.name=name;
        this.parent=parent;
    }

    public SubSection(){
        super("Subsection");
        this.hideFromStudents = false;
        this.inputProblems = new ArrayList<>();
        this.multilineInputProblems = new ArrayList<>();
        this.singleChoiceProblems = new ArrayList<>();
        this.multipleChoiceProblems =new ArrayList<>();
        this.textContents = new ArrayList<>();
        this.imageContents = new ArrayList<>();
        this.videoContents = new ArrayList<>();
        this.parent = null;
    }

    @Override
    public Long ParentID() {
        return parent.getId();
    }

    public static void setSaver(Saver<SubSection> saver) {
        SubSection.saver = saver;
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
        parent.getSubSections().add(this);
    }

    @Override
    public void delete() {
        parent.getSubSections().remove(this);
        saver.delete(this);
        created =false;
    }

    public static SubSection getByID(Long id){
        return saver.read(id);
    }
}

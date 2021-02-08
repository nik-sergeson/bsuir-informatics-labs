package com.nik.training_courses.models;

import com.nik.training_courses.Main;
import com.nik.training_courses.sql_saver.Saver;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.UUID;


@Entity
@Table(name = "sections")
public class Section extends CourseStructureItem {
    private Date releaseDate;
    private Date softDeadline;
    private Date hardDeadline;
    private boolean hideFromStudents;
    private Course parent;
    private List<SubSection> subSections;
    private static Saver<Section> saver;

    @Column(name = "Release_Date")
    public Date getReleaseDate() {
        return releaseDate;
    }

    public void setReleaseDate(Date releaseDate) {
        this.releaseDate = releaseDate;
    }

    @Column(name = "Hide_From_Students")
    public boolean isHideFromStudents() {
        return hideFromStudents;
    }

    public void setHideFromStudents(boolean hideFromStudents) {
        this.hideFromStudents = hideFromStudents;
    }

    @Column(name = "Hard_Deadline")
    public Date getHardDeadline() {
        return hardDeadline;
    }

    public void setHardDeadline(Date hardDeadline) {
        this.hardDeadline = hardDeadline;
    }

    @Column(name = "Soft_Deadline")
    public Date getSoftDeadline() {
        return softDeadline;
    }

    public void setSoftDeadline(Date softDeadline) {
        this.softDeadline = softDeadline;
    }

    @OneToMany(mappedBy = "parent", fetch = FetchType.LAZY, cascade=CascadeType.REMOVE)
    public List<SubSection> getSubSections() {
        return subSections;
    }

    public void setSubSections(List<SubSection> subSections) {
        this.subSections = subSections;
    }


    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "parent_ID")
    public Course getParent() {
        return parent;
    }

    public void setParent(Course parent) {
        this.parent = parent;
    }

    @Override
    public Long ParentID() {
        return parent.getId();
    }

    public Section(){
        this(null);
    }

    public Section(Course parent){
        super("Section");
        this.parent=parent;
        this.releaseDate =new Date();
        this.softDeadline=new Date();
        this.hardDeadline=new Date();
        this.subSections=new ArrayList<SubSection>();
        this.hideFromStudents=false;
    }

    public Section(String name, Date releaseDate, Date softDeadline, Date hardDeadline, boolean hideFromStudents, ArrayList<SubSection> subSections, Course parent) {
        super(name);
        this.parent=parent;
        this.releaseDate = releaseDate;
        this.softDeadline = softDeadline;
        this.hardDeadline = hardDeadline;
        this.hideFromStudents = hideFromStudents;
        this.subSections = subSections;
    }

    public static void setSaver(Saver<Section> saver) {
        Section.saver = saver;
    }

    public static Section getByID(Long id){
       return saver.read(id);
    }

    private void create(){
        created =true;
        saver.create(this);
        parent.getCourseSections().add(this);
    }

    @Override
    public void save(){
        if(!created){
            create();
        }
        else{
            saver.update(this);
        }
    }

    @Override
    public void delete() {
        parent.getCourseSections().remove(this);
        saver.delete(this);
        created=false;
    }
}

package com.nik.training_courses.models;

import com.nik.training_courses.Main;
import com.nik.training_courses.renders.IRendered;

import javax.persistence.Column;
import javax.persistence.MappedSuperclass;


@MappedSuperclass
public abstract class Problem extends CourseStructureItem implements IRendered{
    protected Integer gradingPoints;
    protected Integer position;

    @Column(name = "Grdading_Points")
    public int getGradingPoints() {
        return gradingPoints;
    }

    public void setGradingPoints(int gradingPoints) {
        this.gradingPoints = gradingPoints;
    }

    @Column(name = "Position")
    public Integer getPosition() {
        return position;
    }

    public void setPosition(Integer position) {
        this.position = position;
    }

    public Problem(String name, int gradingPoints, int position) {
        super(name);
        this.gradingPoints = gradingPoints;
        this.position = position;
    }

    public Problem(String name, int gradingPoints) {
        super(name);
        this.gradingPoints = gradingPoints;
        this.position=0;
    }
}

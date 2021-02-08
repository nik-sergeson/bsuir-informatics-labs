package com.nik.training_courses.models;

import com.nik.training_courses.Main;
import com.nik.training_courses.renders.IRendered;

import javax.persistence.Column;
import javax.persistence.MappedSuperclass;


@MappedSuperclass
public abstract class Content extends CourseStructureItem implements IRendered{
    private Integer position;

    @Column(name = "position")
    public Integer getPosition() {
        return position;
    }

    public void setPosition(int position) {
        this.position = position;
    }

    public Content(String name){
        super(name);
        this.position=0;
    }

    public Content(String name, int position) {
        super(name);
        this.position = position;
    }
}

package com.nik.training_courses.models;

import javax.persistence.Column;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.MappedSuperclass;
import java.util.UUID;


@MappedSuperclass
public abstract class CourseStructureItem {
    protected String name;
    protected Long id;
    protected boolean created;

    @Column(name = "Name")
    public String getName() {
        return name;
    }

    @Id
    @GeneratedValue
    @Column(name = "ID")
    public Long getId() {
        return id;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public boolean isCreated() {
        return created;
    }

    public void setCreated(boolean created) {
        this.created = created;
    }

    public CourseStructureItem(String name){
        this.name=name;
        created =false;
    }

    @Override
    public String toString(){
        return name;
    }

    public abstract void save();
    public abstract void delete();
    public abstract Long ParentID();
}

package com.nik.training_courses.models;

import com.nik.training_courses.Main;
import com.nik.training_courses.sql_saver.CourseSaver;
import com.nik.training_courses.sql_saver.ICourseSaver;
import com.nik.training_courses.sql_saver.Saver;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;


@Entity
@Table(name = "courses")
@NamedQuery(name = "course.getAll", query = "SELECT c from Course c")
public class Course extends CourseStructureItem {
    private List<Section> courseSections;
    private CourseSettings courseSettings;
    private List<User> registeredUsers;
    private static ICourseSaver saver;

    @OneToMany(fetch=FetchType.LAZY, mappedBy="parent", cascade=CascadeType.REMOVE)
    public List<Section> getCourseSections() {
        return courseSections;
    }

    @OneToOne(fetch = FetchType.LAZY)
    public CourseSettings getCourseSettings() {
        return courseSettings;
    }

    public void setCourseSections(List<Section> courseSections) {
        this.courseSections = courseSections;
    }

    @ManyToMany(mappedBy="courses", fetch = FetchType.LAZY)
    public List<User> getRegisteredUsers() {
        return registeredUsers;
    }

    public void setRegisteredUsers(List<User> registeredUsers) {
        this.registeredUsers = registeredUsers;
    }

    public Course(){
        super("Course");
        courseSections=new ArrayList<>();
        courseSettings=new CourseSettings();
    }

    public Course(String name, ArrayList<Section> courseSections, CourseSettings courseSettings) {
        super(name);
        this.courseSections = courseSections;
        this.courseSettings = courseSettings;
    }

    public static void setSaver(ICourseSaver saver) {
        Course.saver = saver;
    }

    public static ArrayList<Course> getAll(){
        return (ArrayList<Course>) saver.getAll();
    }

    public void setCourseSettings(CourseSettings courseSettings) {
        this.courseSettings = courseSettings;
    }

    @Override
    public Long ParentID() {
        return null;
    }

    public static Course getByID(Long id){
       return saver.read(id);
    }

    private void create(){
        created =true;
        saver.create(this);
    }

    @Override
    public void save() {
        if(!created) {
            create();
        }
        else
            saver.update(this);
    }

    @Override
    public void delete() {
        saver.delete(this);
        created =false;
    }
}

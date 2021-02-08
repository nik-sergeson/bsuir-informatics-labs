package com.nik.training_courses.sql_saver;

import com.nik.training_courses.models.Course;
import com.nik.training_courses.models.Section;
import org.hibernate.Query;
import org.hibernate.Session;
import org.hibernate.SessionFactory;

import javax.annotation.Resource;
import javax.persistence.EntityManager;
import javax.persistence.Persistence;
import javax.persistence.TypedQuery;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;


public class CourseSaver implements Saver<Course>, ICourseSaver {

    public EntityManager em;

    public CourseSaver(EntityManager em){
        this.em=em;
    }

    public List<Course> getAll(){
        TypedQuery<Course> namedQuery = em.createNamedQuery("course.getAll", Course.class);
        return namedQuery.getResultList();
    }

    public void create(Course course) {
        em.getTransaction().begin();
        em.persist(course.getCourseSettings());
        em.persist(course);
        em.getTransaction().commit();
    }

    public void delete(Course course) {
        em.getTransaction().begin();
        em.remove(course.getCourseSettings());
        em.remove(course);
        em.getTransaction().commit();
    }

    public void update(Course course){
        em.getTransaction().begin();
        em.merge(course);
        em.merge(course.getCourseSettings());
        em.getTransaction().commit();
    }

    public Course read(Long id){
        Course course=em.find(Course.class, id);
        return course;
    }
}

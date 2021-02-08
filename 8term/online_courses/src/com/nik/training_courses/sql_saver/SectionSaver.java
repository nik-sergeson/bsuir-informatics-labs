package com.nik.training_courses.sql_saver;

import com.nik.training_courses.models.Course;
import com.nik.training_courses.models.Section;
import com.nik.training_courses.models.SubSection;

import javax.persistence.EntityManager;
import javax.persistence.TypedQuery;
import java.util.List;
import java.util.UUID;


public class SectionSaver implements Saver<Section> {
    public EntityManager em;

    public SectionSaver(EntityManager em){
        this.em=em;
    }

    public void create(Section section) {
        em.getTransaction().begin();
        em.persist(section);
        em.getTransaction().commit();
    }

    public void delete(Section section) {
        em.getTransaction().begin();
        em.remove(section);
        em.getTransaction().commit();
    }

    public void update(Section section){
        em.getTransaction().begin();
        em.merge(section);
        em.getTransaction().commit();
    }

    public Section read(Long id){
        return em.find(Section.class, id);
    }
}

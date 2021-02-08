package com.nik.training_courses.sql_saver;

import com.nik.training_courses.models.Content;
import com.nik.training_courses.models.Problem;
import com.nik.training_courses.models.Section;
import com.nik.training_courses.models.SubSection;

import javax.persistence.EntityManager;
import java.util.UUID;


public class SubSectionSaver implements Saver<SubSection> {

    public EntityManager em;

    public SubSectionSaver(EntityManager em){
        this.em=em;
    }

    public void create(SubSection subSection) {
        em.getTransaction().begin();
        em.persist(subSection);
        em.getTransaction().commit();
    }

    public void delete(SubSection subSection) {
        em.getTransaction().begin();
        em.remove(subSection);
        em.getTransaction().commit();
    }

    public void update(SubSection subSection){
        em.getTransaction().begin();
        em.merge(subSection);
        em.getTransaction().commit();
    }

    public SubSection read(Long id){
        return em.find(SubSection.class, id);
    }
}

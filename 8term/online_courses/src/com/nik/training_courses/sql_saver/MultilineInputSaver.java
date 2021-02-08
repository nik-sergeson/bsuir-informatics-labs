package com.nik.training_courses.sql_saver;

import com.nik.training_courses.models.MultilineInputProblem;
import com.nik.training_courses.models.Section;

import javax.persistence.EntityManager;
import java.util.UUID;


public class MultilineInputSaver implements Saver<MultilineInputProblem> {
    public EntityManager em;

    public MultilineInputSaver(EntityManager em){
        this.em=em;
    }

    public void create(MultilineInputProblem inputProblem) {
        em.getTransaction().begin();
        em.persist(inputProblem);
        em.getTransaction().commit();
    }

    public void delete(MultilineInputProblem inputProblem) {
        em.getTransaction().begin();
        em.remove(inputProblem);
        em.getTransaction().commit();
    }

    public void update(MultilineInputProblem inputProblem){
        em.getTransaction().begin();
        em.merge(inputProblem);
        em.getTransaction().commit();
    }

    public MultilineInputProblem read(Long id){
        return em.find(MultilineInputProblem.class, id);
    }
}

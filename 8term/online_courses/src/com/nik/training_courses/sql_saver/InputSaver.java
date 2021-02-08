package com.nik.training_courses.sql_saver;

import com.nik.training_courses.models.InputProblem;
import com.nik.training_courses.models.Section;

import javax.persistence.EntityManager;
import java.util.UUID;


public class InputSaver implements Saver<InputProblem> {
    public EntityManager em;

    public InputSaver(EntityManager em){
        this.em=em;
    }

    public void create(InputProblem inputProblem) {
        em.getTransaction().begin();
        em.persist(inputProblem);
        em.getTransaction().commit();
    }

    public void delete(InputProblem inputProblem) {
        em.getTransaction().begin();
        em.remove(inputProblem);
        em.getTransaction().commit();
    }

    public void update(InputProblem inputProblem){
        em.getTransaction().begin();
        em.merge(inputProblem);
        em.getTransaction().commit();
    }

    public InputProblem read(Long id){
        return em.find(InputProblem.class, id);
    }
}

package com.nik.training_courses.sql_saver;

import com.nik.training_courses.models.MultipleChoiceProblem;
import com.nik.training_courses.models.Section;

import javax.persistence.EntityManager;
import java.util.UUID;


public class MultipleChoiceSaver implements Saver<MultipleChoiceProblem> {
    public EntityManager em;

    public MultipleChoiceSaver(EntityManager em){
        this.em=em;
    }

    public void create(MultipleChoiceProblem multipleChoiceProblem) {
        em.getTransaction().begin();
        em.persist(multipleChoiceProblem);
        em.getTransaction().commit();
    }

    public void delete(MultipleChoiceProblem multipleChoiceProblem) {
        em.getTransaction().begin();
        em.remove(multipleChoiceProblem);
        em.getTransaction().commit();
    }

    public void update(MultipleChoiceProblem multipleChoiceProblem){
        em.getTransaction().begin();
        em.merge(multipleChoiceProblem);
        em.getTransaction().commit();
    }

    public MultipleChoiceProblem read(Long id){
        return em.find(MultipleChoiceProblem.class, id);
    }
}

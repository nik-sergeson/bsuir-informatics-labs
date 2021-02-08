package com.nik.training_courses.sql_saver;

import com.nik.training_courses.models.Section;
import com.nik.training_courses.models.SingleChoiceProblem;

import javax.persistence.EntityManager;
import java.util.UUID;


public class SingleChoiceSaver implements Saver<SingleChoiceProblem> {
    public EntityManager em;

    public SingleChoiceSaver(EntityManager em){
        this.em=em;
    }

    public void create(SingleChoiceProblem singleChoiceProblem) {
        em.getTransaction().begin();
        em.persist(singleChoiceProblem);
        em.getTransaction().commit();
    }

    public void delete(SingleChoiceProblem singleChoiceSaver) {
        em.getTransaction().begin();
        em.remove(singleChoiceSaver);
        em.getTransaction().commit();
    }

    public void update(SingleChoiceProblem singleChoiceProblem){
        em.getTransaction().begin();
        em.merge(singleChoiceProblem);
        em.getTransaction().commit();
    }

    public SingleChoiceProblem read(Long id){
        return em.find(SingleChoiceProblem.class, id);
    }
}

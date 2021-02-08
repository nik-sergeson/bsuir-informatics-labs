package com.nik.training_courses.sql_saver;

import com.nik.training_courses.models.Section;
import com.nik.training_courses.models.TextContent;

import javax.persistence.EntityManager;
import java.util.UUID;


public class TextSaver implements Saver<TextContent> {
    public EntityManager em;

    public TextSaver(EntityManager em){
        this.em=em;
    }

    public void create(TextContent textContentection) {
        em.getTransaction().begin();
        em.persist(textContentection);
        em.getTransaction().commit();
    }

    public void delete(TextContent textContent) {
        em.getTransaction().begin();
        em.remove(textContent);
        em.getTransaction().commit();
    }

    public void update(TextContent textContent){
        em.getTransaction().begin();
        em.merge(textContent);
        em.getTransaction().commit();
    }

    public TextContent read(Long id){
        return em.find(TextContent.class, id);
    }
}

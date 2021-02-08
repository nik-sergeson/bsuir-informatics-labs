package com.nik.training_courses.sql_saver;

import com.nik.training_courses.models.ImageContent;
import com.nik.training_courses.models.Section;

import javax.persistence.EntityManager;
import java.util.UUID;


public class ImageSaver implements Saver<ImageContent> {
    public EntityManager em;

    public ImageSaver(EntityManager em){
        this.em=em;
    }

    public void create(ImageContent imageContent) {
        em.getTransaction().begin();
        em.persist(imageContent);
        em.getTransaction().commit();
    }

    public void delete(ImageContent imageContent) {
        em.getTransaction().begin();
        em.remove(imageContent);
        em.getTransaction().commit();
    }

    public void update(ImageContent imageContent){
        em.getTransaction().begin();
        em.merge(imageContent);
        em.getTransaction().commit();
    }

    public ImageContent read(Long id){
        return em.find(ImageContent.class, id);
    }
}

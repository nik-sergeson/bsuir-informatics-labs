package com.nik.training_courses.sql_saver;

import com.nik.training_courses.models.Section;
import com.nik.training_courses.models.VideoContent;

import javax.persistence.EntityManager;
import java.util.UUID;


public class VideoSaver implements Saver<VideoContent> {
    public EntityManager em;

    public VideoSaver(EntityManager em){
        this.em=em;
    }

    public void create(VideoContent videoContent) {
        em.getTransaction().begin();
        em.persist(videoContent);
        em.getTransaction().commit();
    }

    public void delete(VideoContent videoContent) {
        em.getTransaction().begin();
        em.remove(videoContent);
        em.getTransaction().commit();
    }

    public void update(VideoContent videoContent){
        em.getTransaction().begin();
        em.merge(videoContent);
        em.getTransaction().commit();
    }

    public VideoContent read(Long id){
        return em.find(VideoContent.class, id);
    }
}

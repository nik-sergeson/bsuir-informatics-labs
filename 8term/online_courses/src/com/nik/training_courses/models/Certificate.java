package com.nik.training_courses.models;

import javax.persistence.*;
import java.util.Date;


@Entity
@Table(name = "certificates")
public class Certificate {
    private Long ID;
    private Date completeDate;
    private User owner;
    private String description;
    private Course course;
    private Integer score;

    @Id
    @GeneratedValue
    @Column(name = "ID")
    public Long getID() {
        return ID;
    }

    public void setID(Long ID) {
        this.ID = ID;
    }

    @Column(name = "Completed_At")
    public Date getCompleteDate() {
        return completeDate;
    }

    public void setCompleteDate(Date completeDate) {
        this.completeDate = completeDate;
    }

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "User_ID")
    public User getOwner() {
        return owner;
    }

    public void setOwner(User owner) {
        this.owner = owner;
    }

    @Column(name = "Description")
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "Course_ID")
    public Course getCourse() {
        return course;
    }

    public void setCourse(Course course) {
        this.course = course;
    }

    @Column(name = "Score")
    public Integer getScore() {
        return score;
    }

    public void setScore(Integer score) {
        this.score = score;
    }
}

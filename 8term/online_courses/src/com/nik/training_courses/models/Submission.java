package com.nik.training_courses.models;

import javax.persistence.*;
import java.util.Date;


@Entity
@Table(name = "submissions")
public class Submission {
    private Long ID;
    private Date completedAt;
    private Date createdAt;
    private Long taskID;
    private User author;

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
    public Date getCompletedAt() {
        return completedAt;
    }

    public void setCompletedAt(Date completedAt) {
        this.completedAt = completedAt;
    }

    @Column(name = "Created_At")
    public Date getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(Date createdAt) {
        this.createdAt = createdAt;
    }

    @Column(name = "Task_ID")
    public Long getTaskID() {
        return taskID;
    }

    public void setTaskID(Long taskID) {
        this.taskID = taskID;
    }

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "User_ID")
    public User getAuthor() {
        return author;
    }

    public void setAuthor(User author) {
        this.author = author;
    }
}

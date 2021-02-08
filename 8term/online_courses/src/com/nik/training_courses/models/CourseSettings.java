package com.nik.training_courses.models;

import javax.persistence.*;
import java.util.Date;


@Entity
@Table(name = "settings")
public class CourseSettings {
    private Long id;
    private Date startDate;
    private Date endDate;
    private Date enrollmentStartDate;
    private Date enrollmentEndDate;
    private Language language;
    private String image;
    private String description;
    private String organization;

    @Id
    @Column(name = "ID")
    @GeneratedValue
    public Long getId() {
        return id;
    }

    @Column(name = "Start_Date")
    public Date getStartDate() {
        return startDate;
    }


    @Column(name = "End_Date")
    public Date getEndDate() {
        return endDate;
    }

    @Column(name = "Org")
    public String getOrganization() {
        return organization;
    }

    public void setOrganization(String organization) {
        this.organization = organization;
    }

    @Column(name = "Description")
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    @Column(name = "Image")
    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }

    @Enumerated(EnumType.STRING)
    @Column(name = "category_type")
    public Language getLanguage() {
        return language;
    }

    public void setLanguage(Language language) {
        this.language = language;
    }

    @Column(name = "Enrollment_End")
    public Date getEnrollmentEndDate() {
        return enrollmentEndDate;
    }

    public void setEnrollmentEndDate(Date enrollmentEndDate) {
        this.enrollmentEndDate = enrollmentEndDate;
    }

    @Column(name = "Enrollment_Start")
    public Date getEnrollmentStartDate() {
        return enrollmentStartDate;
    }

    public void setEnrollmentStartDate(Date enrollmentStartDate) {
        this.enrollmentStartDate = enrollmentStartDate;
    }

    public void setEndDate(Date endDate) {
        this.endDate = endDate;
    }

    public void setStartDate(Date startDate) {
        this.startDate = startDate;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public CourseSettings(){
        startDate=new Date();
        endDate=new Date();
        enrollmentStartDate=new Date();
        enrollmentEndDate=new Date();
        language=Language.English;
        image="image.jpg";
        description="new course";
        organization="nik";
    }

    public CourseSettings(Date startDate, Date endDate, Date enrollmentStartDate, Date enrollmentEndDate, Language language, String image, String description, String organization) {
        this.startDate = startDate;
        this.endDate = endDate;
        this.enrollmentStartDate = enrollmentStartDate;
        this.enrollmentEndDate = enrollmentEndDate;
        this.language = language;
        this.image = image;
        this.description = description;
        this.organization = organization;
    }
}

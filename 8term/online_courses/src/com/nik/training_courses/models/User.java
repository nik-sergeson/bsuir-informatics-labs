package com.nik.training_courses.models;

import org.hibernate.annotations.Fetch;

import javax.persistence.*;
import java.util.Date;
import java.util.List;


@Entity
@Table(name = "users")
public class User {
    private List<Course> courses;
    private List<Submission> submissions;
    private List<Certificate> certificates;
    private Long ID;
    private String firstName;
    private String lastName;
    private String email;
    private Boolean isStuff;
    private Boolean isActive;
    private Date joined;
    private String username;
    private Date birthday;
    private String country;
    private String education;

    @ManyToMany(fetch = FetchType.LAZY)
    @JoinTable(name="user_courses")
    public List<Course> getCourses() {
        return courses;
    }

    public void setCourses(List<Course> courses) {
        this.courses = courses;
    }

    @Id
    @GeneratedValue
    @Column(name = "ID")
    public Long getID() {
        return ID;
    }

    public void setID(Long ID) {
        this.ID = ID;
    }

    @Column(name = "First_Name")
    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    @Column(name = "Last_Name")
    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    @Column(name = "Email")
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    @Column(name = "Is_Stuff")
    public Boolean getStuff() {
        return isStuff;
    }

    public void setStuff(Boolean stuff) {
        isStuff = stuff;
    }

    @Column(name = "Is_Active")
    public Boolean getActive() {
        return isActive;
    }

    public void setActive(Boolean active) {
        isActive = active;
    }

    @Column(name = "Joined")
    public Date getJoined() {
        return joined;
    }

    public void setJoined(Date joined) {
        this.joined = joined;
    }

    @Column(name = "Username")
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    @Column(name = "Birthday")
    public Date getBirthday() {
        return birthday;
    }

    public void setBirthday(Date birthday) {
        this.birthday = birthday;
    }

    @Column(name = "Country")
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    @Column(name = "Education")
    public String getEducation() {
        return education;
    }

    public void setEducation(String education) {
        this.education = education;
    }

    @OneToMany(fetch=FetchType.LAZY, mappedBy="author", cascade=CascadeType.REMOVE)
    public List<Submission> getSubmissions() {
        return submissions;
    }

    public void setSubmissions(List<Submission> submissions) {
        this.submissions = submissions;
    }

    @OneToMany(fetch=FetchType.LAZY, mappedBy="owner", cascade=CascadeType.REMOVE)
    public List<Certificate> getCertificates() {
        return certificates;
    }

    public void setCertificates(List<Certificate> certificates) {
        this.certificates = certificates;
    }

    public User() {
    }
}

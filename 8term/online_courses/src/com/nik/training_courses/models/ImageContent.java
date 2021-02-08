package com.nik.training_courses.models;

import com.nik.training_courses.Main;
import com.nik.training_courses.renders.ImageContentRender;
import com.nik.training_courses.sql_saver.Saver;
import javafx.scene.layout.Pane;

import javax.persistence.*;
import java.util.UUID;


@Entity
@Table(name = "image_content")
public class ImageContent extends Content {
    private String source;
    private SubSection parent;
    private static Saver<ImageContent> saver;

    private static ImageContentRender render;

    @Column(name = "Source")
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }

    public static void setRender(ImageContentRender render) {
        ImageContent.render = render;
    }

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "parent_ID")
    public SubSection getParent() {
        return parent;
    }

    public void setParent(SubSection parent) {
        this.parent = parent;
    }

    public static ImageContentRender getRender() {
        return render;
    }

    public ImageContent() {
        this(null);
    }

    public ImageContent(SubSection subSection){
        super("Image content");
        this.parent=subSection;
        this.source="D:\\default.jpg";
    }

    @Override
    public Long ParentID() {
        return parent.getId();
    }

    public static void setSaver(Saver<ImageContent> saver) {
        ImageContent.saver = saver;
    }

    public static ImageContent getByID(Long id){
        return saver.read(id);
    }

    @Override
    public void save() {
        if(!created)
            create();
        else
            saver.update(this);
    }

    private void create(){
        created=true;
        saver.create(this);
        parent.getImageContents().add(this);
    }

    @Override
    public void delete() {
        saver.delete(this);
        created =false;
    }

    @Override
    public Pane render() {
        return render.render(this);
    }
}

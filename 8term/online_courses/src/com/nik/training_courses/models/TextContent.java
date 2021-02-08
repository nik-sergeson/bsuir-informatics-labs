package com.nik.training_courses.models;

import com.nik.training_courses.Main;
import com.nik.training_courses.renders.TextContentRender;
import com.nik.training_courses.sql_saver.Saver;
import javafx.scene.layout.Pane;

import javax.persistence.*;
import java.util.UUID;


@Entity
@Table(name = "text_content")
public class TextContent extends Content {
    private String text;
    private SubSection parent;
    private static Saver<TextContent> saver;

    private static TextContentRender render;

    @Column(name = "Text")
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public static void setRender(TextContentRender render) {
        TextContent.render = render;
    }

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "parent_ID")
    public SubSection getParent() {
        return parent;
    }

    public void setParent(SubSection parent) {
        this.parent = parent;
    }

    @Override
    public Long ParentID() {
        return parent.getId();
    }

    public TextContent(){
        this(null);
    }

    public TextContent(SubSection parent){
        super("Text content");
        this.parent=parent;
        text="Text content";
    }

    public static void setSaver(Saver<TextContent> saver) {
        TextContent.saver = saver;
    }

    public static TextContent getByID(Long id){
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
        parent.getTextContents().add(this);
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

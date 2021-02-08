package com.nik.training_courses.models;

import com.nik.training_courses.Main;
import com.nik.training_courses.renders.VideoContentRender;
import com.nik.training_courses.sql_saver.Saver;
import javafx.scene.layout.Pane;

import javax.persistence.*;
import java.util.UUID;


@Entity
@Table(name = "video_contents")
public class VideoContent extends Content {
    private String source;
    private SubSection parent;
    private static Saver<VideoContent> saver;

    private static VideoContentRender render;

    @Column(name = "Source")
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }

    public static void setRender(VideoContentRender render) {
        VideoContent.render = render;
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

    public VideoContent(){
        this(null);
    }

    public VideoContent(SubSection parent){
        super("Video content");
        this.parent=parent;
        this.source="D://intro.mp4";
    }

    public static void setSaver(Saver<VideoContent> saver) {
        VideoContent.saver = saver;
    }

    public static VideoContent getByID(Long id){
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
        parent.getVideoContents().add(this);
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

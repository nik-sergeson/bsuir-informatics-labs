package com.nik.training_courses;

import com.nik.training_courses.controllers.*;
import com.nik.training_courses.controllers.content.*;
import com.nik.training_courses.controllers.problem.*;
import com.nik.training_courses.models.*;
import com.nik.training_courses.renders.*;
import com.nik.training_courses.sql_saver.*;
import com.screensframework.ScreensController;
import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.stage.Stage;
import org.hibernate.Session;

import javax.persistence.EntityManager;
import javax.persistence.Persistence;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Date;


public class Main extends Application {

    public final EntityManager em = Persistence.createEntityManagerFactory("nikpu").createEntityManager();

    @Override
    public void start(Stage primaryStage) throws Exception {
        //buttons should be aprox 90x30
        InputProblem.setRender(new InputRender());
        InputProblem.setSaver(new InputSaver(em));
        MultilineInputProblem.setRender(new MultilineInputRender());
        MultilineInputProblem.setSaver(new MultilineInputSaver(em));
        SingleChoiceProblem.setRender(new SingleCnoiceRender());
        SingleChoiceProblem.setSaver(new SingleChoiceSaver(em));
        MultipleChoiceProblem.setRender(new MultipleChoiceRender());
        MultipleChoiceProblem.setSaver(new MultipleChoiceSaver(em));
        TextContent.setRender(new TextContentRender());
        TextContent.setSaver(new TextSaver(em));
        ImageContent.setRender(new ImageContentRender());
        ImageContent.setSaver(new ImageSaver(em));
        VideoContent.setRender(new VideoContentRender());
        VideoContent.setSaver(new VideoSaver(em));
        Course.setSaver(new CourseSaver(em));
        Section.setSaver(new SectionSaver(em));
        SubSection.setSaver(new SubSectionSaver(em));
        ScreensController mainContainer = new ScreensController();
        mainContainer.addUpdatableScreen(Screens.MAIN_SCREEN, Screens.VIEWS_DIR + Screens.MAIN_SCREEN_FXML, new CoursewareController());
        mainContainer.addUpdatableScreen(Screens.COURSE_VIEW, Screens.VIEWS_DIR + Screens.COURSE_VIEW_FXML, new CourseController());
        mainContainer.addUpdatableScreen(Screens.COURSE_EDIT, Screens.VIEWS_DIR + Screens.COURSE_SETTINGS_FXML, new CourseEditController());
        mainContainer.addCreationScreen(Screens.COURSE_CREATE, Screens.VIEWS_DIR + Screens.COURSE_SETTINGS_FXML, new CourseCreateController());
        mainContainer.addUpdatableScreen(Screens.SECTION_VIEW, Screens.VIEWS_DIR + Screens.SECTION_VIEW_FXML, new SectionController());
        mainContainer.addUpdatableScreen(Screens.SECTION_EDIT, Screens.VIEWS_DIR + Screens.SECTION_SETTINGS_FXML, new SectionEditController());
        mainContainer.addCreationScreen(Screens.SECTION_CREATE, Screens.VIEWS_DIR + Screens.SECTION_SETTINGS_FXML, new SectionCreateController());
        mainContainer.addUpdatableScreen(Screens.SUBSECTION_VIEW, Screens.VIEWS_DIR + Screens.SUBSECTION_VIEW_FXML, new SubSectionController());
        mainContainer.addUpdatableScreen(Screens.SUBSECTION_EDIT, Screens.VIEWS_DIR + Screens.SUBSECTION_SETTINGS_FXML, new SubSectionEditController());
        mainContainer.addCreationScreen(Screens.SUBSECTION_CREATE, Screens.VIEWS_DIR + Screens.SUBSECTION_SETTINGS_FXML, new SubSectionCreateController());
        mainContainer.addUpdatableScreen(Screens.INPUT_EDIT, Screens.VIEWS_DIR + Screens.INPUT_FXML, new InputEditController());
        mainContainer.addCreationScreen(Screens.INPUT_CREATE, Screens.VIEWS_DIR + Screens.INPUT_FXML, new InputCreateController());
        mainContainer.addUpdatableScreen(Screens.MULITLINE_INPUT_EDIT, Screens.VIEWS_DIR + Screens.MULITLINE_INPUT_FXML, new MultilineInputEditController());
        mainContainer.addCreationScreen(Screens.MULITLINE_INPUT_CREATE, Screens.VIEWS_DIR + Screens.MULITLINE_INPUT_FXML, new MultilineInputCreateController());
        mainContainer.addUpdatableScreen(Screens.SINGLE_CHOICE_EDIT, Screens.VIEWS_DIR + Screens.SINGLE_CHOICE_FXML, new SingleChoiceEditController());
        mainContainer.addCreationScreen(Screens.SINGLE_CHOICE_CREATE, Screens.VIEWS_DIR + Screens.SINGLE_CHOICE_FXML, new SingleChoiceCreateController());
        mainContainer.addUpdatableScreen(Screens.MULTIPLE_CHOICE_EDIT, Screens.VIEWS_DIR + Screens.MULTIPLE_CHOICE_FXML, new MultipleChoiceEditController());
        mainContainer.addCreationScreen(Screens.MULTIPLE_CHOICE_CREATE, Screens.VIEWS_DIR + Screens.MULTIPLE_CHOICE_FXML, new MultipleChoiceCreateController());
        mainContainer.addUpdatableScreen(Screens.IMAGE_CONTENT_EDIT, Screens.VIEWS_DIR + Screens.IMAGE_CONTENT_FXML, new ImageEditController(primaryStage));
        mainContainer.addCreationScreen(Screens.IMAGE_CONTENT_CREATE, Screens.VIEWS_DIR + Screens.IMAGE_CONTENT_FXML, new ImageCreateController(primaryStage));
        mainContainer.addUpdatableScreen(Screens.TEXT_CONTENT_EDIT, Screens.VIEWS_DIR + Screens.TEXT_CONTENT_FXML, new TextEditController());
        mainContainer.addCreationScreen(Screens.TEXT_CONTENT_CREATE, Screens.VIEWS_DIR + Screens.TEXT_CONTENT_FXML, new TextCreateController());
        mainContainer.addUpdatableScreen(Screens.VIDEO_CONTENT_EDIT, Screens.VIEWS_DIR + Screens.VIDEO_CONTENT_FXML, new VideoEditController(primaryStage));
        mainContainer.addCreationScreen(Screens.VIDEO_CONTENT_CREATE, Screens.VIEWS_DIR + Screens.VIDEO_CONTENT_FXML, new VideoCreateController(primaryStage));
        mainContainer.setUpdatableScreen(Screens.MAIN_SCREEN, null);
        Group root = new Group();
        root.getChildren().addAll(mainContainer);
        Scene scene = new Scene(root, 700, 650);
        primaryStage.setTitle("Training Courses");
        primaryStage.setScene(scene);
        primaryStage.setResizable(false);
        primaryStage.show();
    }


    public static void main(String[] args) {
        launch(args);
    }
}

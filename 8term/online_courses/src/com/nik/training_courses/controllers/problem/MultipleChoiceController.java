package com.nik.training_courses.controllers.problem;

import com.nik.training_courses.Screens;
import com.nik.training_courses.models.MultipleChoiceProblem;
import com.screensframework.ControlledScreen;
import com.screensframework.ScreensController;
import javafx.beans.property.StringProperty;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;

import java.util.ArrayList;
import java.util.HashMap;


public class MultipleChoiceController  implements ControlledScreen {
    protected ScreensController screensController;
    protected MultipleChoiceProblem editingProblem;
    protected HashMap<StringProperty, CheckBox> answerMap;
    protected ArrayList<StringProperty> answers;
    protected HashMap<Object, HBox> answerRow;

    @FXML
    private VBox answerList;

    @FXML
    private Button backButton;

    @FXML
    private TextArea description;

    @FXML
    private Button saveButton;

    @FXML
    private Button addAnswer;

    @FXML
    void backButtonClicked(ActionEvent event) {
        answerMap.clear();
        answerRow.clear();
        answers.clear();
        screensController.setUpdatableScreen(Screens.SUBSECTION_VIEW, editingProblem.getParent());
        editingProblem=null;
    }

    @FXML
    void saveButtonClicked(ActionEvent event) {
        int answerIndex=0;
        ArrayList<String> stringAnswers=new ArrayList<>();
        ArrayList<Integer> correctAnswers=new ArrayList<>();
        for(StringProperty answer:answers){
            stringAnswers.add(answer.toString());
            if(answerMap.get(answer).isSelected())
                correctAnswers.add(answerIndex);
            answerIndex+=1;
        }
        answers.clear();
        editingProblem.setAnswers(stringAnswers);
        editingProblem.setCorrectAnswers(correctAnswers);
        editingProblem.setDescription(description.getText());
        editingProblem.save();
        answerMap.clear();
        answerRow.clear();
        screensController.setUpdatableScreen(Screens.SUBSECTION_VIEW, editingProblem.getParent());
        editingProblem=null;
    }

    @FXML
    void addAnswerClicked(ActionEvent event) {
        TextField textField=new TextField("Answer");
        CheckBox checkBox=new CheckBox("Answer");
        answerMap.put(textField.textProperty(), checkBox);
        textField.textProperty().addListener(
                new ChangeListener<String>() {
                    @Override
                    public void changed(ObservableValue<? extends String> observable, String oldValue, String newValue) {
                        answerMap.get(observable).setText(newValue);
                    }
                }
        );
        Button button=new Button("Remove");
        button.setOnAction(
                new EventHandler<ActionEvent>() {
                    @Override
                    public void handle(ActionEvent event) {
                        answerList.getChildren().remove(answerRow.get(event.getSource()));
                        answers.remove(event.getSource());
                    }
                }
        );
        HBox hBox=new HBox(textField, checkBox, button);
        answers.add(textField.textProperty());
        hBox.setSpacing(20);
        answerList.getChildren().add(hBox);
        answerRow.put(button, hBox);
    }

    @Override
    public void setScreenParent(ScreensController screenPage) {
        screensController=screenPage;
    }

    public void initialize(){
        answerMap=new HashMap<>();
        answerRow=new HashMap<>();
        answers=new ArrayList<>();
    }

    public void setViewValues(MultipleChoiceProblem problem){
        description.setText(problem.getDescription());
        for(String answer : problem.getAnswers()){
            TextField textField=new TextField(answer);
            CheckBox checkBox=new CheckBox(answer);
            answerMap.put(textField.textProperty(), checkBox);
            textField.textProperty().addListener(
                    new ChangeListener<String>() {
                        @Override
                        public void changed(ObservableValue<? extends String> observable, String oldValue, String newValue) {
                            answerMap.get(observable).setText(newValue);
                        }
                    }
            );
            Button button=new Button("Remove");
            button.setOnAction(
                    new EventHandler<ActionEvent>() {
                        @Override
                        public void handle(ActionEvent event) {
                            answerList.getChildren().remove(answerRow.get(event.getSource()));
                            answers.remove(event.getSource());
                        }
                    }
            );
            HBox hBox=new HBox(textField, checkBox, button);
            answers.add(textField.textProperty());
            hBox.setSpacing(20);
            answerList.getChildren().add(hBox);
            answerRow.put(button, hBox);
        }
    }
}

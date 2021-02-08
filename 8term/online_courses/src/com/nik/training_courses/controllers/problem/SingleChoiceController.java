package com.nik.training_courses.controllers.problem;

import com.nik.training_courses.Screens;
import com.nik.training_courses.models.SingleChoiceProblem;
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


public class SingleChoiceController implements ControlledScreen {
    protected ScreensController screensController;
    protected SingleChoiceProblem editingProblem;
    protected final ToggleGroup radioGroup = new ToggleGroup();
    protected HashMap<StringProperty, RadioButton> answerMap;
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
        ArrayList<String> stringAnswers=new ArrayList<>();
        int answerIndex=0;
        for(StringProperty answer:answers){
            stringAnswers.add(answer.toString());
            if(answerMap.get(answer).isSelected())
                editingProblem.setCorrectAnswerIndex(answerIndex);
            answerIndex+=1;
        }
        answerMap.clear();
        answerRow.clear();
        answers.clear();
        editingProblem.setDescription(description.getText());
        editingProblem.setAnswers(stringAnswers);
        editingProblem.save();
        screensController.setUpdatableScreen(Screens.SUBSECTION_VIEW, editingProblem.getParent());
        editingProblem=null;
    }

    @FXML
    void addAnswerClicked(ActionEvent event) {
        TextField textField=new TextField("Answer");
        RadioButton radioButton=new RadioButton("Answer");
        answerMap.put(textField.textProperty(), radioButton);
        textField.textProperty().addListener(
                new ChangeListener<String>() {
                    @Override
                    public void changed(ObservableValue<? extends String> observable, String oldValue, String newValue) {
                        answerMap.get(observable).setText(newValue);
                    }
                }
        );
        radioButton.setToggleGroup(radioGroup);
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
        HBox hBox=new HBox(textField, radioButton, button);
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

    public void setViewValues(SingleChoiceProblem problem){
        description.setText(problem.getDescription());
        for(String answer : problem.getAnswers()){
            TextField textField=new TextField(answer);
            RadioButton radioButton=new RadioButton(answer);
            answerMap.put(textField.textProperty(), radioButton);
            textField.textProperty().addListener(
                    new ChangeListener<String>() {
                        @Override
                        public void changed(ObservableValue<? extends String> observable, String oldValue, String newValue) {
                            answerMap.get(observable).setText(newValue);
                        }
                    }
            );
            radioButton.setToggleGroup(radioGroup);
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
            HBox hBox=new HBox(textField, radioButton, button);
            answers.add(textField.textProperty());
            hBox.setSpacing(20);
            answerList.getChildren().add(hBox);
            answerRow.put(button, hBox);
        }
    }
}

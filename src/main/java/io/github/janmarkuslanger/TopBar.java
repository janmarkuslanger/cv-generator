package io.github.janmarkuslanger;

import io.github.janmarkuslanger.scene.PersonalInformation;
import javafx.scene.control.Button;
import javafx.scene.control.ToolBar;
import javafx.stage.Stage;

public class TopBar {
    public static ToolBar createTopBar(Stage stage) {
        Button workExperienceButton = new Button("Work Experience");
        Button personalInformationButton = new Button("Personal information");
        Button certificationButton = new Button("Certification");

        personalInformationButton.setOnAction(event -> stage.setScene(
            PersonalInformation.getScene(stage)
        ));

        return new ToolBar(personalInformationButton, workExperienceButton, certificationButton);
    }
}

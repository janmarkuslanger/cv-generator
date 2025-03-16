package io.github.janmarkuslanger.scene;

import io.github.janmarkuslanger.App;
import io.github.janmarkuslanger.Constants;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ToolBar;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;

public class PersonalInformation {
    public static Scene getScene(Stage stage) {

        Button backButton = new Button("Back");
        backButton.setOnAction(event -> stage.setScene(App.getMainScene(stage)));
        ToolBar topbar = new ToolBar(backButton);

        BorderPane layout = new BorderPane(backButton);
        layout.setTop(topbar);
        return new Scene(layout, Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT);
    }
}

package io.github.janmarkuslanger;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;

public class App extends Application {
    @Override
    public void start(Stage primaryStage) {
        primaryStage.setScene(getMainScene(primaryStage));
        primaryStage.setTitle("CV Generator mit Szenenwechsel");
        primaryStage.show();
    }

    public static Scene getMainScene(Stage stage) {
        BorderPane root = new BorderPane();
        root.setTop(TopBar.createTopBar(stage));

        return new Scene(root, Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT);
    }

    public static void main(String[] args) {
        launch(args);
    }
}

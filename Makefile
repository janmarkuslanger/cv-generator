start:
	mvn clean install && java --module-path /opt/javafx/lib --add-modules javafx.controls,javafx.fxml -cp target/cv-generator-1.0-SNAPSHOT.jar io.github.janmarkuslanger.App

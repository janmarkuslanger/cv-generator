package io.github.janmarkuslanger;

import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.File;
import java.io.IOException;
import io.github.janmarkuslanger.model.CvData;

public class JsonManager {
    private static final ObjectMapper mapper = new ObjectMapper();
    private static final String FILE_NAME = "cv-data.json";

    public static void saveData(CvData data) {
        try {
            mapper.writerWithDefaultPrettyPrinter().writeValue(new File(FILE_NAME), data);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static CvData loadData() {
        try {
            return mapper.readValue(new File(FILE_NAME), CvData.class);
        } catch (IOException e) {
            return new CvData();
        }
    }
}

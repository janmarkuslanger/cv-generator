import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonInclude;

@JsonInclude(JsonInclude.Include.NON_NULL)
public class CvData {
    @JsonProperty
    private String firstName;

    @JsonProperty
    private String lastName;
}

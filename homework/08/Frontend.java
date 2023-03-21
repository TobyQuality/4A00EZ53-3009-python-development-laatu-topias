
import java.io.IOException;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;

public class Frontend {
    public static void main(String[] args) throws Exception {
        URL url = new URL("https://tobys-python-cloud.onrender.com/customers");
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("GET");
        conn.setRequestProperty("Accept", "application/json");

        InputStream is = conn.getInputStream();
        byte[] responseBytes = is.readAllBytes();
        String responseBody = new String(responseBytes, StandardCharsets.UTF_8);

        System.out.println(responseBody);
    }
}
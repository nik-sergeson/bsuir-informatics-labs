package files;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;


public class FileHelper {
    public static String fileToString(String path) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(path));
        StringBuilder builder = new StringBuilder();
        String line = reader.readLine();
        while (line != null) {
            builder.append(line);
            line = reader.readLine();
        }
        return builder.toString();
    }
}

package lab1.src;

import files.FileHelper;

import java.io.IOException;
import java.util.HashMap;


public class Lab1 {
    public static void main(String[] args) throws IOException {
        char[] alphabet = {'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С',
                'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я'};
        CaesarCipher cipher = new CaesarCipher(alphabet);
        String encrypted = cipher.encrypt(FileHelper.fileToString(args[0]), 3);
        System.out.println(encrypted);
        HashMap<Character, Double> expectedDestribution = new HashMap<>();
        expectedDestribution.put('А', 0.07998);
        expectedDestribution.put('Б', 0.01592);
        expectedDestribution.put('В', 0.04533);
        expectedDestribution.put('Г', 0.01687);
        expectedDestribution.put('Д', 0.02977);
        expectedDestribution.put('Е', 0.08483);
        expectedDestribution.put('Ё', 0.00013);
        expectedDestribution.put('Ж', 0.0094);
        expectedDestribution.put('З', 0.01641);
        expectedDestribution.put('И', 0.07367);
        expectedDestribution.put('Й', 0.01208);
        expectedDestribution.put('К', 0.03486);
        expectedDestribution.put('Л', 0.04343);
        expectedDestribution.put('М', 0.03203);
        expectedDestribution.put('Н', 0.067);
        expectedDestribution.put('О', 0.10983);
        expectedDestribution.put('П', 0.02804);
        expectedDestribution.put('Р', 0.04746);
        expectedDestribution.put('С', 0.05473);
        expectedDestribution.put('Т', 0.06318);
        expectedDestribution.put('У', 0.02615);
        expectedDestribution.put('Ф', 0.00267);
        expectedDestribution.put('Х', 0.00966);
        expectedDestribution.put('Ц', 0.00486);
        expectedDestribution.put('Ч', 0.0145);
        expectedDestribution.put('Ш', 0.00718);
        expectedDestribution.put('Щ', 0.00361);
        expectedDestribution.put('Ъ', 0.00037);
        expectedDestribution.put('Ы', 0.01898);
        expectedDestribution.put('Ь', 0.01735);
        expectedDestribution.put('Э', 0.00331);
        expectedDestribution.put('Ю', 0.00639);
        expectedDestribution.put('Я', 0.02001);
        String decrtypted = cipher.decrypt(expectedDestribution, encrypted);
        System.out.println(decrtypted);
    }
}
package lab1.src;

import java.util.*;


public class CaesarCipher {
    private Map<Character, Integer> alphabetMap;
    private char[] alphabet;
    private static Comparator<Map.Entry<Character, Double>> EntryComparator
            = new Comparator<Map.Entry<Character, Double>>() {
        public int compare(Map.Entry<Character, Double> obj1, Map.Entry<Character, Double> obj2) {
            return obj1.getValue().compareTo(obj2.getValue());
        }

    };

    public CaesarCipher(char[] alphabet) {
        this.alphabet = new char[alphabet.length];
        this.alphabetMap = new HashMap<>();
        for (int i = 0; i < alphabet.length; i++) {
            if (Character.isLowerCase(alphabet[i])) {
                this.alphabetMap.put(alphabet[i], i);
                this.alphabet[i] = alphabet[i];
            } else {
                this.alphabetMap.put(Character.toLowerCase(alphabet[i]), i);
                this.alphabet[i] = Character.toLowerCase(alphabet[i]);
            }
        }
    }

    public String encrypt(String text, int key) {
        int alphabetLength = alphabet.length;
        StringBuilder encryptedText = new StringBuilder(text);
        for (int i = 0; i < encryptedText.length(); i++) {
            char nextSymbol = Character.toLowerCase(encryptedText.charAt(i));
            if (alphabetMap.containsKey(nextSymbol)) {
                char encryptedSymbol = alphabet[(alphabetMap.get(nextSymbol) + key) % alphabetLength];
                if (Character.isLowerCase(encryptedText.charAt(i)))
                    encryptedText.setCharAt(i, encryptedSymbol);
                else
                    encryptedText.setCharAt(i, Character.toUpperCase(encryptedSymbol));
            }
        }
        return encryptedText.toString();
    }

    public String decrypt(HashMap<Character, Double> expectedDestribution, String text) {
        StringBuilder decryptedText = new StringBuilder(text);
        int letterCount = 0;
        HashMap<Character, Double> textDestribution = new HashMap<>(), updatedExpected = new HashMap<>();
        for (Map.Entry<Character, Double> entry : expectedDestribution.entrySet()) {
            if (Character.isUpperCase(entry.getKey())) {
                updatedExpected.put(Character.toLowerCase(entry.getKey()), entry.getValue());
            }
        }
        expectedDestribution = updatedExpected;
        for (int i = 0; i < text.length(); i++) {
            char letter = Character.toLowerCase(text.charAt(i));
            if (alphabetMap.containsKey(letter)) {
                ++letterCount;
                if (textDestribution.containsKey(letter))
                    textDestribution.put(letter, textDestribution.get(letter) + 1.0 / letterCount);
                else
                    textDestribution.put(letter, 1.0 / letterCount);
            }
        }
        HashMap<Character, Character> letterMapping = generateMapping(new ArrayList<>(expectedDestribution.entrySet()), new ArrayList<>(textDestribution.entrySet()));
        for (int i = 0; i < decryptedText.length(); i++) {
            char currentLetter = decryptedText.charAt(i);
            if (alphabetMap.containsKey(Character.toLowerCase(currentLetter))) {
                if (Character.isLowerCase(currentLetter))
                    decryptedText.setCharAt(i, letterMapping.get(currentLetter));
                else
                    decryptedText.setCharAt(i, Character.toUpperCase(letterMapping.get(Character.toLowerCase(currentLetter))));
            } else
                decryptedText.setCharAt(i, currentLetter);
        }
        return decryptedText.toString();
    }

    public HashMap<Character, Character> generateMapping(ArrayList<Map.Entry<Character, Double>> expectedDestribution, ArrayList<Map.Entry<Character, Double>> sourceDestribution) {
        HashMap<Character, Character> mapping = new HashMap<>();
        double distance1, distance2, distance3 = 0;
        int expectedIndex = 0, sourceIndex = 0;
        Map.Entry<Character, Double> expectedCurrent, sourceCurrent;
        MapEntryComparator comparator = new MapEntryComparator();
        Collections.sort(expectedDestribution, comparator);
        Collections.sort(sourceDestribution, comparator);
        while (sourceIndex < sourceDestribution.size()) {
            expectedCurrent = expectedDestribution.get(expectedIndex);
            sourceCurrent = sourceDestribution.get(sourceIndex);
            if (expectedIndex + 1 < expectedDestribution.size()) {
                distance1 = Math.abs(sourceCurrent.getValue() - expectedCurrent.getValue());
                distance2 = Math.abs(sourceCurrent.getValue() - expectedDestribution.get(expectedIndex + 1).getValue());
                if (sourceIndex + 1 < sourceDestribution.size())
                    distance3 = Math.abs(sourceDestribution.get(sourceIndex + 1).getValue() - expectedDestribution.get(expectedIndex + 1).getValue());
                if (distance1 <= distance2 || sourceDestribution.size() - sourceIndex == expectedDestribution.size() - expectedIndex) {
                    mapping.put(sourceCurrent.getKey(), expectedCurrent.getKey());
                    ++sourceIndex;
                    ++expectedIndex;
                } else if (sourceIndex + 1 >= sourceDestribution.size())
                    ++expectedIndex;
                else if (distance3 <= distance2) {
                    mapping.put(sourceCurrent.getKey(), expectedCurrent.getKey());
                    ++expectedIndex;
                    ++sourceIndex;
                } else {
                    mapping.put(sourceCurrent.getKey(), expectedDestribution.get(expectedIndex + 1).getKey());
                    ++sourceIndex;
                    expectedIndex += 2;
                }
            } else {
                mapping.put(sourceCurrent.getKey(), expectedCurrent.getKey());
                ++sourceIndex;
                ++expectedIndex;
            }
        }
        return mapping;
    }
}

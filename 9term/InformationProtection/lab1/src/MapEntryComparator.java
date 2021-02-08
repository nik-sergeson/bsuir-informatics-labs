package lab1.src;

import java.util.*;


public class MapEntryComparator implements Comparator<Map.Entry<Character, Double>> {
    @Override
    public int compare(Map.Entry<Character, Double> e1, Map.Entry<Character, Double> e2) {
        return e1.getValue().compareTo(e2.getValue());
    }
}
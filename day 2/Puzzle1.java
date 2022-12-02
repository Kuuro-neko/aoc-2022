import java.io.*;
import java.util.Scanner;
import java.util.HashMap;

class Puzzle1 {
    public static void main(String[] args) {
        try {
            File file = new File("input.txt");
            Scanner input = new Scanner(file);
            int score = 0;

            HashMap<Character, Integer> values = new HashMap<Character, Integer>();
            values.put('X', 0);
            values.put('Y', 1);
            values.put('Z', 2);
            values.put('A', 0);
            values.put('B', 1);
            values.put('C', 2);
            
            while (input.hasNextLine()) {
                String line = input.nextLine();
                char opponent = line.charAt(0);
                char me = line.charAt(2);
                score += score(opponent, me, values);
            }
            System.out.println("Puzzle 1 - the score is " + score + "."); // Puzzle 1

        } catch (FileNotFoundException e) {
            System.out.println("File not found");
        }
    }

    static int score(char opponent, char me, HashMap<Character, Integer> values) {
        int score = 0;
        score += values.get(me) + 1;
        if (values.get(opponent) == 0) {
            score += ((values.get(opponent) + values.get(me) + 1) % 3) * 3;
        } else if (values.get(opponent) == 1) {
            score += ((values.get(opponent) + values.get(me) + 2) % 3) * 3;
        } else if (values.get(opponent) == 2) {
            score += ((values.get(opponent) + values.get(me)) % 3) * 3;
        }
        return score;
    }
}
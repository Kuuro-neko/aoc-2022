import java.io.*;
import java.util.Scanner;
import java.util.HashMap;

class Puzzle2 {
    public static void main(String[] args) {
        try {
            File file = new File("input.txt");
            Scanner input = new Scanner(file);
            int score = 0;

            HashMap<Character, Integer> values = new HashMap<Character, Integer>();
            values.put('X', 0); // lose
            values.put('Y', 1); // draw
            values.put('Z', 2); // win
            values.put('A', 0); // rock
            values.put('B', 1); // paper
            values.put('C', 2); // scissors
            
            while (input.hasNextLine()) {
                String line = input.nextLine();
                char opponent = line.charAt(0);
                char game = line.charAt(2);
                score += score(opponent, game, values);
            }
            System.out.println("Puzzle 2 - the score is " + score + ".");

        } catch (FileNotFoundException e) {
            System.out.println("File not found");
        }
    }

    static int score(char opponent, char game, HashMap<Character, Integer> values) {
        int score = 0;
        score += values.get(game) * 3;
        switch(game) {
            case 'X':
                score += (values.get(opponent) + 2) % 3;
                break;
            case 'Y':
                score += values.get(opponent);
                break;
            case 'Z':
                score += (values.get(opponent) + 1) % 3;
                break;
        }
        score ++;
        return score;
    }
}
import java.io.*;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

class Puzzle {
    public static void main(String[] args) {
        try {
            File file = new File("input.txt");
            Scanner input = new Scanner(file);
            List<Integer> list = new ArrayList<Integer>();
            int count = 0;
            while (input.hasNextLine()) {
                String line = input.nextLine();
                if (!line.isEmpty()) {
                    try {
                        list.set(count, Integer.parseInt(line) + list.get(count));
                    } catch (IndexOutOfBoundsException e) {
                        list.add(Integer.parseInt(line));
                    }
                } else {
                    count++;
                }
            }
            int max = 0;
            for(int i : list) {
                if (i > max) {
                    max = i;
                }
            }
            System.out.println("The elf carrying the most calories is carrying " + max + " calories."); // Puzzle 1

            int[] maxes = {0, 0, 0};
            for(int i : list) {
                if (i > maxes[0]) {
                    maxes[2] = maxes[1];
                    maxes[1] = maxes[0];
                    maxes[0] = i;
                } else if (i > maxes[1]) {
                    maxes[2] = maxes[1];
                    maxes[1] = i;
                } else if (i > maxes[2]) {
                    maxes[2] = i;
                }
            }
            System.out.println("The elves carrying the most calories are carrying " + maxes[0] + ", " + maxes[1] + ", and " + maxes[2] + " calories, which is a total of " + (maxes[0] + maxes[1] + maxes[2]) + " calories."); // Puzzle 2
        } catch (FileNotFoundException e) {
            System.out.println("File not found");
        }
    }
}
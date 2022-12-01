import java.io.*;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

class Puzzle1 {
    public static void main(String[] args) {
        try {
            File file = new File("input1.txt");
            Scanner input = new Scanner(file);
            List<Integer> list = new ArrayList<Integer>();
            int count = 0;
            // read each line of the file and add its value to the list if the line is not empty
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
            System.out.println(max);
        } catch (FileNotFoundException e) {
            System.out.println("File not found");
        }
    }
}
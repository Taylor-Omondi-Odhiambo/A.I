import javafx.util.Pair;

import java.util.HashSet;
import java.util.Set;

interface Robot {
   boolean move();

   void turnLeft();

   void turnRight();

   void clean();
}

class Solution {
   //a hashtable to keep track of whether a non-obstacle cell is visited or not.
   Set<Pair<Integer, Integer>> visited = new HashSet();
   Robot robot;

   public void goBack() {
       //Changing robot's direction and moving to the previous cell
       robot.turnRight();
       robot.turnRight();
       robot.move();
       robot.turnRight();
       robot.turnRight();
   }

   public void backtrack(int x, int y, int dir) {
       //Adding the current position to the visited
       visited.add(new Pair(x, y));
       //Cleaning the cell
       robot.clean();

       //Assigning numbers to the clockwise directions:
       //0: 'up', 1: 'right', 2: 'down', 3: 'left'
       for (int i = 0; i < 4; i++) {
           //Intially hold the current X and Y
           int newX = x;
           int newY = y;
           //Specifying the new direction of the robot
           //We use mod 4 because we only have 4 directions
           int newDir = (dir + i) % 4;

           //Checking the directions based on the direction formulas
           //0: 'up', 1: 'right', 2: 'down', 3: 'left'
           if (newDir == 0)
               newX -= 1;
           else if (newDir == 1)
               newY += 1;
           else if (newDir == 2)
               newX += 1;
           else if (newDir == 3)
               newY -= 1;

           //Checks if the next cell is visited and
           //whether the robot can move to the next cell or not.
           //If true, backtrack and find an alternative path
           if (!visited.contains(new Pair(newX, newY)) && robot.move()) {
               //Recursively backtracking to find a new path for the robot
               backtrack(newX, newY, newDir);
               //If there is no empty cell, go back to the previous cell
               goBack();
           }
           //turn the robot in the clockwise direction
           robot.turnRight();
       }
   }

   public void cleanRoom(Robot robot) {
       this.robot = robot;
       backtrack(0, 0, 0);
   }
}
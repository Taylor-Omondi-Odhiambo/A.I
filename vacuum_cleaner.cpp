#include <iostream>
#include <vector>
#include <unordered_set>
#include <thread>
#include <chrono>

// Class implimentation for the vacuum
int r = 0;
class Robot
{
public:
  virtual bool move() = 0;
  virtual void turnLeft() = 0;
  virtual void turnRight() = 0;
  virtual void clean() = 0;
  virtual std::pair<int, int> getPos() = 0;
  virtual int getDirection() = 0;
};

// A bot with a maze, direction and list of visited indexes
class RobotCreate : public Robot
{
private:
  int dir; // up: 0, right: 1, down: 2, left: 3
  int **room;
  std::pair<int, int> pos;

public:
  // create a bot, in a room. Specify the start position and the direction it is facing
  RobotCreate(int **room, std::pair<int, int> startPos) : room(room), pos(startPos), dir(0) {}

  // Returns true if the movement is valid
  bool move() override
  {
    int x = 0, y = 0;
    switch (dir)
    {
    case 0:
      y = -1;
      break;
    case 1:
      x = 1;
      break;
    case 2:
      y = 1;
      break;
    case 3:
      x = -1;
      break;
    }

    int newX = pos.first + x;
    int newY = pos.second + y;

    // Disregard if movement is into an obstacle or out of bounds
    if (newX >= 0 && newX < 16 && newY >= 0 && newY < 16 && room[newX][newY] != 0)
    {
      pos = {newX, newY};
      return true;
    }

    return false;
  }

  void turnLeft() override
  {
    dir = (dir + 3) % 4; // Bounds check
  }

  void turnRight() override
  {
    dir = (dir + 1) % 4; // Bounds check
  }

  void clean() override
  {
    room[pos.first][pos.second] = 2; // Mark as cleaned
  }

  std::pair<int, int> getPos() override
  {
    return pos;
  }

  int getDirection() override
  {
    return dir;
  }
};

// Moves in dfs mode to clean all indexes in the room
class RoomCleaner
{
public:
  // Prints the room state
  static void printRoom(int **room, std::pair<int, int> robotPos, int robotDirection)
  {
    system("clear");
    for (int i = 0; i < 16; i++)
    {
      for (int j = 0; j < 16; j++)
      {
        if (i == robotPos.first && j == robotPos.second)
        {
          char arrow;
          switch (robotDirection)
          {
          case 0:
            arrow = '^';
            break; // Up
          case 1:
            arrow = '>';
            break; // Right
          case 2:
            arrow = 'v';
            break; // Down
          case 3:
            arrow = '<';
            break; // Left
          default:
            arrow = 'R'; // Unknown direction
          }
          // If the bot is in a valid square, it is deemed as cleaned
          std::cout << "\033[42m" << arrow << " \033[0m"; // ANSI_GREEN, aka cleaned
        }
        else if (room[i][j] == 0)
        {
          std::cout << "# "; // Obstacle
        }
        else if (room[i][j] == 1)
        {
          std::cout << "_ "; // Uncleaned path
        }
        else if (room[i][j] == 2)
        {
          std::cout << "\033[42m_ \033[0m"; // ANSI_GREEN Cleaned path
        }
      }
      std::cout << std::endl;
    }

    // Sleep to visualize the steps
    std::this_thread::sleep_for(std::chrono::seconds(1));
  }

  void cleanRoom(RobotCreate &bot, int **room)
  {
    dfs(bot, bot.getPos().first, bot.getPos().second, 0, room);
  }

  void dfs(RobotCreate &bot, int i, int j, int dir, int **room)
  {
    // Index identifier
    // Mark the cell as cleaned
    room[i][j] = 2;
    printRoom(room, bot.getPos(), bot.getDirection());

    if (j == 0 && i == 14)
    {
      r++;
    }

    // Attempt to move in all directions
    for (int n = 0; n < 4; n++)
    {
      if (bot.move())
      {
        int x = bot.getPos().first;
        int y = bot.getPos().second;
        if (room[x][y] == 1)
        {
          // Visit the next branch
          dfs(bot, x, y, dir, room);
          // Return to the previous cell
          bot.turnLeft();
          bot.turnLeft();
          bot.move();
          bot.turnRight();
          bot.turnRight();
        }
      }
      // Rotate 90 degrees
      bot.turnRight();
      dir = (dir + 1) % 4;
    }
  }
};

int main()
{
  int **room = new int *[16];
  for (int i = 0; i < 16; i++)
  {
    room[i] = new int[16];
  }

  // Initialize the room with obstacles
  for (int i = 0; i < 16; i++)
  {
    for (int j = 0; j < 16; j++)
    {
      room[i][j] = 1; // 1: path
    }
  }

  // Adding obstacles
  // Room 1
  room[0][0] = 0; // 0: obstacle
  room[3][3] = 0; // 0: obstacle
  room[0][3] = 0; // 0: obstacle
  room[0][1] = 0; // 0: obstacle
  room[0][2] = 0; // 0: obstacle
  room[1][2] = 0; // 0: obstacle
  room[2][2] = 0; // 0: obstacle

  // Room 2
  int k = 9;
  for (int i = 1; i < 5; i++)
  {
    int j = k;
    while (j < k + 3)
    {
      room[i][j] = 0; // 0: obstacle
      j++;
    }
    k++;
  }

  for (int i = 9; i < 15; i++)
  {
    for (int j = 2; j < 5; j++)
    {
      room[i][j] = 0; // 0: obstacle
    }
  }

  for (int i = 0; i < 16; i++)
  {
    room[7][i] = 0; // Room boundary
    room[i][7] = 0;
  }

  room[7][6] = 1;
  room[7][7] = 1;
  room[7][8] = 1;
  room[6][7] = 1;
  room[7][7] = 1;
  room[8][7] = 1;

  for (int i = 8; i < 16; i++)
  {
    for (int j = 8; j < 16; j++)
    {
      room[i][j] = 2;
    }
  }

  // Initial robot start coordinate
  std::pair<int, int> pos = {7, 7};
  RobotCreate bot(room, pos);

  // Show the room before starting
  RoomCleaner::printRoom(room, bot.getPos(), bot.getDirection());
  //  std::this_thread::sleep_for(std::chrono::seconds(0.5)); // Sleep for 2s before starting

  // Clean the room
  // Step 1: Clean the index the bot starts at
  bot.clean();
  RoomCleaner roomCleaner;
  roomCleaner.cleanRoom(bot, room);

  // Deallocate memory for the room
  for (int i = 0; i < 16; i++)
  {
    delete[] room[i];
  }
  delete[] room;

  return 0;
}

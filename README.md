# Space_Shooter
This is a simple multiplayer game done in Python programming language using Socket programming. The programs are constructed using client server architecture and implemented through Graphical User Interface (GUI) using Pygame.The space-shooter game gives a spaceship to the player to move around and shoot opponents.the player who shoots the opponent to zero health wins the game.

Rules Of The Game:
1. The Spaceship moves using UP,DOWN,LEFT,RIGHT keys and fires Bullets with LEFT_CTRL .
2. The Game: Here,two spaceship spawns in the window and the players can fire bullets at their opponent to decrease their health.
3. When a bullet is fired,the player cannot fire another bullet till the bullet is hit or moves out of the screen.
4. Game Winning condition:the first win to make the opponent’s health zero wins.

Installation Guide<br />
1.clone the repository in your local machine.<br />
```git clone link from the repo```
2.change the directory.<br />
```cd space_shooter```
3.Run this command to install the requirements.<br />
```pip install -r requirements.txt```
4.Run the server.py<br />
![image](https://user-images.githubusercontent.com/90893643/149646956-e68c47e9-09ba-42d0-84d8-77db931dbe9e.png)
5.Run the client.py<br />
![image](https://user-images.githubusercontent.com/90893643/149646964-06232caa-da19-4dbe-b067-0ae2bc01d8e6.png)

Movements:<br />
1.Moving the spaceship with up,down,left,right arrow across the window<br />
![image](https://user-images.githubusercontent.com/90893643/149646992-e18f0807-6730-47d4-9661-a65e5f8d3810.png)
2.Pressing LEFT_CTRL to fire a bullet(the bullet fire sound plays)<br />
![image](https://user-images.githubusercontent.com/90893643/149647001-33a36f10-9fc4-4f27-8ac4-dd4d9f95b081.png)

When one of the player wins:<br />
![image](https://user-images.githubusercontent.com/90893643/149647085-f17eb1c8-b457-4bc0-93f1-6b6784ced710.png)

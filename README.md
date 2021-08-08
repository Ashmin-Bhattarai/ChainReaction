REQUIREMENTS:
1)Python with version 3.6 or greater

Additional Required Python Modules:
	1) Tkinter
	2) Pygames
	3) Pillow

Game Rule:
-There will be several grids appear in a window.
-When a player clicks on the cell of the grid then an orb is formed.
-The color of orb will be different for different players.
-The multiple clicks on the formed orb will increase its number per click.
-If the no. of orb is greater than 1 in corner cell of grid or greater than 2 in edge cell or greater than three in remaining 
 cell then the orb burst out adding each orb to its adjacent cells.
-If the adjacent orb is of another player than that orb will be converted into other player orb by changing its color.
-The player that loses all its orb is out of the game.


--> NOTE: Run Chain_Reaction.py to start the game
--> This program uses port 5555 for online playing. So if any issues arises while playing multiplayer on LAN or on remote server
	please port forward portnumber=5555 and enable this port on firewall as well
--> The source code and precompiled binary file can also be found on github 
     https://github.com/Ashmin-Bhattarai/ChainReaction
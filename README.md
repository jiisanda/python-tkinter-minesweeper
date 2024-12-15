Python Tkinter Minesweeper
===========================

Minesweeper game written in Python using Tkinter GUI library.

<img src="https://i.imgur.com/8JwCyAQ.png" alt="Screenshot on OSX" height="350"/>

Contents:
----------

- */minesweeper.py* - The actual python program
- */images/* - GIF Images ready for usage with Tkinter
- */images/original* - Original PNG images made with GraphicsGale

To Do:
----------
- Have specific number of mines, rather than random
- Highscore table
- Adjustable grid and mine count via UI


Task
----------
Your task is to convert it into a client-server application where two players start **on the same board** and then compete who can solve the board faster.
1. While you don't need a "player ready" UI, if only one client starts it should be impossible to play.
2. Timer should start when both players connected.
3. When a player wins both players' games should be stoped with "Player A/B won". Player A is the client that connected first.

MAKEY MAKEY BREADBOARD QUIZ MANAGEMENT SOFTWARE 
===============================================

https://github.com/liangdrew/makeymakey-buzzers/
===============================================

This application uses Python and Pygame to allow a game master to manage 
team-based quizzes in which buzzers are used (hardware simulated using MakeyMakey
breadboard and accompanying wiring http://makeymakey.com). 

INSTRUCTIONS
============
Press the 'Y' key if the answer provided is correct upon "buzzing in".
Press the 'N' key if the answer provided is incorrect upon "buzzing in".
Press the 'P' key to display game statistics.
Pree the 'ESC' key to exit the program.

HOW TO USE
==========
The MakeyMakey breadboard and wiring must be set up so that when any one of the five circuits are closed, a keyboard input (up, down, left, right, space) is sent to the compiler. Each key corresponds to a team colour (red, blue, green, yellow, black). The first team that "buzzes in" by closing their circuit will have their team colour show up on the program window and a recorded voice-over played which calls out their team colour. Other teams will not be able to buzz-in until the game master presses the 'Y' key or the 'N' key, telling the compiler that the team has either answered correctly or incorrectly. If correct, the team will gain 1 point. If incorrect, the other teams may buzz-in to answer the same question, but the team which answered incorrectly will not be able to buzz-in again until the question provided by the game master is answered correctly by a different team.

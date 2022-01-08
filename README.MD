![](C:\Users\Hello world\PycharmProjects\pythonProject\screenshots\Project image.jpg)

## Inspiration
We once watched a YouTube video by PolyMars where he thought of playing a game of snake using alternative methods, namely **Twitter**. Since then, the Twitter API has a lot more features that made us think of how we can explore the space of alternative ways to play games.

We chose **Connect Four** as it is a game that is easy for multiple players to join and leave at anytime. In addition, one of our team member recently played a basketball version of Connect Four where people would throw balls to place the elements. A part that made that variant of the game fun was the chaotic nature of not always being able to predict how even your own move would turn out, which we believe we can replicate with a voting based option.

## What it does
_Twitter plays Connect Four_ is a Twitter bot that simulates a game of Connect Four by choosing the highest voted choice in a poll. Connect Four is a game where players are required, as the name suggests, to connect four of their pieces either vertically, horizontally or diagonally. The game runs on a fixed timer and checks for the most voted choice every 5 minutes. If more than one choice is tied, a random choice will be picked out of the tied choices.

## How we built it
We made the bot entirely in **python**, and all calls to the **Twitter API** utilizes the **Tweety** Python Library to translate calls. The newer Twitter API v2 was paramount in allowing us to create this with better poll support as well.

## Challenges we ran into
The original design choice was to allow players to vote from every possible choice. However, the reality was that the polls were limited to **4 choices**. A compromise was to keep it to 4 random choices out of the 7 possible roles available. While it made the simulation different from the actual game, it also made voting more focused to fewer choices. We believe it also lends to the overall chaotic theme of the project.

## Accomplishments that we're proud of
As a pair of Information Security students, we are excited at the progress we managed in something outside our usual field of study. We hope to be able to explore more interesting usage of API of various well-known systems.

## What we learned
We started with almost no knowledge of the Twitter API a day ago, and only created a Developer Account for Twitter on the 6th of January. In this hackathon, we were able to learn so much about using an API to create things. Also, using a website API allowed us to focus a lot more on the backend when it is already well packaged in Twitter's UI.

## What's next for Twitter plays Connect Four
The project is mostly done with small avenues to explore such as leaderboards. We hope that this will inspire more similar games that can be played in a _democratic_ fashion on Twitter.
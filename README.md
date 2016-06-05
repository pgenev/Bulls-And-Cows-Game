Bulls and Cows Game - CLI Implementation 

Bulls and Cows (also known as Cows and Bulls or Pigs and Bulls or Bulls and Cleots) is an old code-breaking mind or paper and pencil game for two or more players.
The numerical version of the game is usually played with 4 digits, but can also be played with 3 or any other number of digits.

On a sheet of paper, the players each write a 4-digit secret number. The digits must be all different. Then, in turn, the players try to guess their opponent's number who gives the number of matches. If the matching digits are in their right positions, they are "bulls", if in different positions, they are "cows". Example:

Secret number: 4271
Opponent's try: 1234
Answer: 1 bull and 2 cows. (The bull is "2", the cows are "4" and "1".)

The first one to reveal the other's secret number wins the game. As the first player has a logical advantage, the game can be balanced over multiple games by alternating the right to go first, or over a single game by granting the second player an equal number of guesses, possibly resulting in a tie.

4.Имплементирайте игра на бикове и крави https://en.wikipedia.org/wiki/Bulls_and_Cows

Насоки:
	
	1. Направете клас Game, който да представлява една игра, да
	приема число и да управлява ходовете на играта
	
	2. Направете базов клас Player
	
	3. Наследете класът и направете имплементация, която играе
	сама играта
	
	4. Наследете класът и направете имплементация, която приема
	вход от конзолата и показва колко крави и колко бикове е
	получил играча
	
	5. Имплементирайте запазване и четене на резултати от
	изиграни игри във файл
	
	6. Опитайте се да го направите максимално разплетено от
	конзолата­ т.е. Ако някой реши да вземе вашите класове и да
	ги използва в игра с графичен интерфейс, да не му трябват 2
	седмици да го направи
	
	7. Можете да направите различни режими на игра­ например с
	ограничен брой ходове или казваща само броят на биковете

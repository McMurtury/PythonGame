# PythonGame
**Author: Mark Daniel McMurtury**

**Date: Feburary 2nd 2020**

This is a currently incomplete project that I started a few years ago. I was working to create a role playing fantasy game with turn 
based combat. The project was started before I was enrolled in the University of South Carolina, but because I was enrolled in a Java 
programming class I was able to improve my skills and learn better and cleaner ways of coding. During the summer of 2018 I went back 
and started to rewrite the Python code to make it better and easier to read. However, the free time that I had disappeared when classes
picked back up and I have be unable to return to the project. This is an older example of my work.

## Combat

Combat was developed as a turn based style and the order was determetered on speed. The enemy would randomly select a target from the player's party. In a later version I planned to factor in a hidden value, aggro, which would add more weight to a certain character based on what they did during their turn. High damage or healing would generate a large increase in aggro. Currently there is only one attack option and the battle screen copies the player character twice. This was just to test the scaleablitly of the code, since the idea is to allow for a party of up to four characters. The thumbnail that shows the character in the battle screen slowly fills up with red as it takes damage. 

## Inventory

This is a simple screen that shows the items that the player's party has. The testing of it revolved around some potions. It featured a simple thumbnail and title listed in the inventory, and empty or unavaible otherwise. Later the player would be able to increase the size of the inventory. Clicking on item would cause a larger image to appear at the top and a description of the item to be displayed. 

## Character Creation

Most of this work was done in the Main file, but it would take the player through the process of creating a character. They would have to pick a class out of three options; Warrior, Rogue, and Mage. Another aspect they have to pick is the gender of the character. Following that, they have to distribute the stats points between the following: Magic, Agility, Intellence, Strength, Endurance, and Stamina. These values can not go below 1, and if they wish too they can put all the points into one stat. Currently the amount of points they have is 18. The last step is to input a name for the character. After that, they get a screen that shows them the character that they have created and are asked if they wish to confrim it or change something. 

## Movement Across The Map

This displays the map of the game world along with a player icon. The player would use the qweasdzc keys to move the icon around the map. There are some spots on the map that the player can not move too, such as a large body of water. Later they would be on a ship, and have a chance to move into the ocean, but until then they are landlocked. Reaching a city does break you out of the movement, since at that point you would be given the chance to enter the city or not.
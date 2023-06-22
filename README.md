<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Project: Surreal EscaPY

## Overview

If you happen to know [Zork I: The Great Underground Empire](https://en.wikipedia.org/wiki/Zork) ...congrats! (wow, you must be older than time ). Text-based adventure games like that, have inspired gaming since 1977. Our goal for the first team project ([Aris Goulas](https://github.com/ArisGoulas), [Letícia De Marchi](https://github.com/leticiademarchiferreira), [Matheus Freire](https://github.com/MatheusFreir) was to use our freshly-acquired Python programming skills, in order to develop the game design of a classic game - Escape Room further. We therefore present you with **Surreal EscaPY**!

---

## Game Design

Our development consists of 3 (and a half) features:
- :fearful: Environment thematic customization: _surreal nightmare_ - personalization of the experience (MVP)
- :mag: _"check"_ action addition - gameplay (towards a future "inventory" feature)
- :repeat: Map layout limited _differentiation_ - replayability (towards a future map layout "randomization" feature)
- :hourglass: Player name & _Timer_ - gameplay (towards a future "scoring" feature and a "lose condition" feature)

The modules `time` and `random` were used, and an additional function (explore_self) was implemented.

### Game Map

![Game Map adapted](surreal-escape-plan.jpg)

### Game Narratives

The player is asked to provide a name, and then the game starts in a specific room. They can utilize a menu of three **actions** ("explore", "check", or "examine") in order to move further in the game:
- Explore: indicates to the player the room they currently are, the furniture present and the doors of the room
- Check: informs the player about the keys that the player has collected
- Examine: allows the player to inspect furniture in order to find keys, if applied to doors while in presence of the respective key allows the player to cross through the door if they wish (yes/no option)

The customized rooms, furnitures, doors and keys that the player can encounter in the game are:
- 4+1 rooms: the room of insomnia, diamond room, the room of Alice, the room of reasoning, outside **(victory condition, a timer indicates the duration of the game)**
- 6 furnitures: bed of nails, escritoire desk, steel chest, Red Queen bed, White Knight dresser, bag of problems, 
- 4 doors: veil of darkness, black hole, open mouth, arch of life
- 4 keys: candle-light **(random assignment)**, diamond, small pill **(random assignment)**, large pill **(random assignment based on small pill assignment)**

---

## How to play the Game

1. Clone this repo in your GitHub

2. Launch `surreal-escapy.py` (in command prompt, type `python surreal-escape.py`)

3. If you enjoyed, you might want to ~~take a break~~ spur your nostalgia further by checking some of the (successors of text-based) classic point-and-click adventure PC games I grew up with:
   - [Zak McKracken and the Alien Mindbenders](https://en.wikipedia.org/wiki/Zak_McKracken_and_the_Alien_Mindbenders) 1988
   - [KGB](https://en.wikipedia.org/wiki/KGB_(video_game)) 1992
   - [Gabriel Knight: Sins of the Fathers](https://en.wikipedia.org/wiki/Gabriel_Knight) 1993
   - [Simon the Sorcerer](https://en.wikipedia.org/wiki/Simon_the_Sorcerer) 1993  
   - [Prisoner of Ice](https://en.wikipedia.org/wiki/Prisoner_of_Ice) 1995


<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Project: Surreal EscaPY

## Overview

If you know [Zork I: The Great Underground Empire](https://en.wikipedia.org/wiki/Zork) ...congrats! (wow, you must be older than time ). Text-based adventure games like that, have inspired gaming since 1977. Our goal for the first team project ([Aris Goulas](https://github.com/ArisGoulas), [Letícia De Marchi](https://github.com/leticiademarchiferreira), [Matheus Freire](https://github.com/MatheusFreir) was to use our freshly-acquired Python programming skills, in order to develop the game design of a classic game - Escape Room further. We therefore present you with **Surreal EscaPY**!

---

## Game Design

Our development consists of 3 (and a half) features:
- :fearful: Environment thematic customization: _surreal nightmare_ - personalization of the experience (MVP)
- :mag: _"check"_ action addition - gameplay (towards a future "inventory" feature)
- :repeat: Map layout limited _differentiation_ - replayability (towards a future map layout "randomization" feature)
- :hourglass: Player name & _Timer_ - gameplay (towards a future "scoring" feature and a "lose condition" feature)

### Game Map

![Game Map adapted](surreal-escape-plan.jpg)

### Game Narratives

The player is asked to provide a name, and then starts the game in a specific room. They can utilize a menu of three **actions** ("explore", "check", or "examine") in order to move further in the game:
- Explore: indicates to the player the room they currently are, the furniture present and the doors of the room
- Check: informs the player about the keys that the player has collected
- Examine: allows the player to inspect furniture in order to find keys, if applied to doors while in presence of the respective key allows the player to cross through the door if they wish (yes/no option)

The 5 rooms, 6 furnitures, 4 doors and 4 keys that the player can encounter in the game are:
- rooms: the room of insomnia, diamond room, the room of Alice, the room of reasoning, outside **(victory condition, a timer indicates the duration of the game)**
- furnitures: bed of nails, escritoire desk, steel chest, Red Queen bed, White Knight dresser, bag of problems, 
- doors: veil of darkness, black hole, open mouth, arch of life
- keys: candle-light **(random assignment)**, diamond, small pill **(random assignment)**, large pill **(random assignment based on small pill assignment)**

---


## How to play the Game

1. Clone this repo in your GitHub.

2. Launch `surreal-escapy.py` (in command prompt, type `python surreal-escape.py`)

3. Enjoy!

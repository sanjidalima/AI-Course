🧟 Zombie Escape Game (Human vs AI)

This is a 5x5 grid-based survival game built using **Pygame**. You play as a human (🧑) trying to escape from the zombie (🧟) by reaching the exit at the bottom-right corner. The zombie learns your most frequent movement direction and follows you intelligently — making it an exciting AI-based pursuit game!

---

📦 Requirements

Before running the game, make sure you have:

- Python 3 installed
- Pygame library installed

✅ To install Pygame:
```bash
pip install pygame
▶️ How to Run the Game
Save the code into a file named zombie_escape.py

Open terminal or command prompt

Navigate to the folder containing the file

Run the command:

bash
Copy
Edit
python zombie_escape.py
A window will open to play the game.

🎮 How to Play
The player (🧑) starts at the top-left corner [0,0].

The goal is to reach the green exit at bottom-right [4,4].

A zombie (🧟) starts from the exit and chases you.

Use the following keys to move:

U = Up

D = Down

L = Left

R = Right

Press S to restart the game after it ends.

📢 End Conditions:
You win if you reach the exit safely 🏁

Zombie wins if it catches you 😱

🧠 AI Algorithm Used
The zombie learns and predicts your most frequent move direction (e.g., if you go right often, it follows that direction). This makes the AI dynamic and harder to escape.

Strategy: Frequency-based Movement Prediction

Learning from: Your movement history

Behavior: Pursues based on statistical pattern

🖼️ Screenshots
You can add screenshots like this:

bash
Copy
Edit
/zombie_escape/
├── zombie_escape.py
├── README.md
└── screenshots/
    └── gameplay.png
Then, show it in the README using:

markdown
Copy
Edit
![Gameplay](./screenshots/gameplay.png)
💡 Tips
Try to vary your movement to confuse the zombie.

Avoid repeating the same direction too much.

📜 License
This game is open-source and free to use for educational or modification purposes.

# Images
[Image](https://raw.githubusercontent.com/sanjidalima/AI-Course/refs/heads/main/AI%20Games/Zoombie_escape/Image/Zhombie_Escapde.PNG)

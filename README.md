# 📌 Higher or Lower - Follower Count Game

A simple **Python-based terminal game** where you guess which celebrity or public figure has **more Instagram followers**!

---

## 📖 How to Play

1. The game will display **two celebrities/public figures** and their descriptions.
2. You must guess which one has **more followers** by typing `'A'` or `'B'`.
3. If you guess correctly, your **score increases**, and the next round begins.
4. If you're wrong, the game **ends** and shows your final score.
5. You can choose to **play again** or exit.

---

## 💻 Installation & Setup

```
1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-username/higher-lower-game.git
   cd higher-lower-game
   ```

2. **Install dependencies** (if required):
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the game**:
   ```sh
   python game.py
   ```
```

---

## 🎮 Features

```
✔ **Guess the celebrity with more followers**  
✔ **High Score Tracking** 🏆  
✔ **Looping gameplay** (Play again after losing)  
✔ **Input validation** (Prevents invalid choices)  
✔ **Randomized comparisons** for a fresh experience every time  
```

---

## 🔧 Project Structure

```
/higher-lower-game
│── game.py         # Main game logic
│── game_data.py    # Contains a list of public figures & their follower counts
│── art.py          # ASCII art for visuals
│── README.md       # Game documentation
```

---

## 📌 Example Gameplay

```
____Welcome to the Game!____

Compare A: Cristiano Ronaldo, a Footballer, from Portugal
vs
Against B: Taylor Swift, a Singer, from USA

--------------------------------------------------

Who has more followers? Type 'A' or 'B': A
You're right! Current score: 1

--------------------------------------------------

Compare A: Taylor Swift, a Singer, from USA
vs
Against B: Elon Musk, a Entrepreneur, from USA

Who has more followers? Type 'A' or 'B': B
Sorry, that's wrong. Final score: 1
The correct answer was A.

🏆 High Score: 2

Do you want to play again? (Y/N): Y
```

---

## 🛠 Future Improvements

```
- **Difficulty Levels** (Easy, Medium, Hard)  
- **Leaderboard System** 🏅  
- **Timed Mode** ⏳ (Answer within 5 seconds!)  
- **More data sources** (e.g., Twitter, YouTube subscriber counts)  
```

---

## 📜 License

```
This project is open-source under the **MIT License**.
```

---

## 💡 Credits

```
- Inspired by **Higher or Lower** games  
- Data sourced from `game_data.py`  
- Built with **Python** 🐍  
```

---

### 🚀 Enjoy & Have Fun! 🎉  

# 🎭 Random Name & Question Picker (GUI)

A fun and interactive **Python GUI application** that randomly selects a **name** and a **question** from text files and displays them using a visually appealing interface with a doll character.
Perfect for classrooms, ice-breaker sessions, presentations, and live audience engagement.

---

## 🚀 Features

* 🎲 Randomly picks a **name** from `names.txt`
* ❓ Randomly picks a **question** from `questions.txt`
* 🖼️ Attractive **GUI with doll image** using Tkinter
* 🔁 Generates new name & question on every button click
* 📂 File-based input (easy to modify, no code changes needed)
* 🧠 Simple logic, beginner-friendly, yet impressive for demos

---

## 🛠️ Tech Stack

* **Python 3**
* **Tkinter** – GUI framework
* **Pillow (PIL)** – Image handling
* **Random module** – Random selection logic

---

## 📁 Project Structure

```
Random-Name-Question-Picker/
│
├── main.py            # Main Python GUI application
├── names.txt          # List of names (one per line)
├── questions.txt      # List of questions (one per line)
├── doll.png           # Doll image shown in GUI
└── README.md          # Project documentation
```

---

## 📋 Sample Input Files

### `names.txt`

```
Alice
Bob
Charlie
David
```

### `questions.txt`

```
What is your favorite hobby?
What motivates you every day?
Where do you see yourself in 5 years?
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/random-name-question-picker.git
cd random-name-question-picker
```

### 2️⃣ Install Required Library

```bash
pip install pillow
```

### 3️⃣ Run the Application

```bash
python main.py
```

---

## 🖥️ How It Works

1. The program reads names from `names.txt`
2. It reads questions from `questions.txt`
3. On button click:

   * One random name is selected
   * One random question is selected
4. Both are displayed on the GUI along with the doll image

---

## 🎯 Use Cases

* 👩‍🏫 Classroom activities
* 🎤 Stage events & audience interaction
* 🧑‍💻 Ice-breaker sessions
* 🎓 College project demos
* 🧩 Fun learning applications

---

## 🌟 Future Enhancements

* Add sound effects or animations 🎶
* Prevent repetition until all names/questions are used 🔁
* Export selected name & question to a file 📄
* Full-screen or themed UI 🎨

---

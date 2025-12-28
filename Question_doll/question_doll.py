import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Function to read names and questions from the files and pick random ones
def pick_random_name_and_question():
    # Read names from 'names.txt'
    with open('names.txt', 'r') as name_file:
        names = name_file.readlines()
    
    # Read questions from 'questions.txt'
    with open('questions.txt', 'r') as question_file:
        questions = question_file.readlines()
    
    # Strip any trailing newlines or spaces from each name and question
    names = [name.strip() for name in names]
    questions = [question.strip() for question in questions]
    
    # Select a random name and a random question
    random_name = random.choice(names)
    random_question = random.choice(questions)
    
    # Display the selected name and question in the respective labels
    name_label.config(text="Name: " + random_name)
    question_label.config(text="Question: " + random_question)

# Set up the GUI window
root = tk.Tk()
root.title("Random Name & Question Picker")
root.geometry("400x600")  # Size of the window

# Load and display the doll image
image = Image.open("doll.png")
image = image.resize((200, 200), Image.Resampling.LANCZOS)  # Resize the image to fit in the GUI
photo = ImageTk.PhotoImage(image)

# Create a label to display the doll image
image_label = tk.Label(root, image=photo)
image_label.pack(pady=20)

# Create a label to display the random name
name_label = tk.Label(root, text="", font=("Arial", 18), fg="blue")
name_label.pack(pady=10)

# Create a label to display the random question
question_label = tk.Label(root, text="", font=("Arial", 18), fg="green")
question_label.pack(pady=10)

# Create a button to pick a random name and question
pick_button = tk.Button(root, text="Pick a Random Name and Question", font=("Arial", 14), command=pick_random_name_and_question)
pick_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()

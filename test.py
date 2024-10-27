import tkinter as tk
from tkinter import messagebox

# Define the quiz data
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "London", "Paris", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Jupiter", "Mars", "Venus"],
        "answer": "Jupiter"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["Oxygen", "Gold", "Osmium", "Zinc"],
        "answer": "Oxygen"
    },
    {
        "question": "What is the smallest country in the world?",
        "options": ["Vatican City", "Monaco", "San Marino", "Liechtenstein"],
        "answer": "Vatican City"
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.root.geometry("400x300")

        # Quiz attributes
        self.question_index = 0
        self.score = 0
        self.selected_answer = tk.StringVar()

        # UI setup
        self.question_label = tk.Label(root, text="", font=("Arial", 12))
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for _ in range(4):
            option_button = tk.Radiobutton(root, text="", variable=self.selected_answer, font=("Arial", 10))
            self.option_buttons.append(option_button)
            option_button.pack(anchor="w", padx=20)

        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)

        # Display the first question
        self.display_question()

    def display_question(self):
        """Display the current question and options."""
        if self.question_index < len(quiz_data):
            current_question = quiz_data[self.question_index]
            self.question_label.config(text=current_question["question"])
            self.selected_answer.set("")  # Reset the selected answer
            for idx, option in enumerate(current_question["options"]):
                self.option_buttons[idx].config(text=option, value=option)
        else:
            self.show_score()

    def next_question(self):
        """Check answer and go to the next question."""
        current_question = quiz_data[self.question_index]
        if self.selected_answer.get() == current_question["answer"]:
            self.score += 1
        self.question_index += 1
        self.display_question()

    def show_score(self):
        """Show the final score and end the quiz."""
        messagebox.showinfo("Quiz Completed", f"Your score: {self.score} out of {len(quiz_data)}")
        self.root.quit()

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

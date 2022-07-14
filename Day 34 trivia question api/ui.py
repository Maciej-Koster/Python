from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=1, row=2, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            150,
            100,
            width=280,
            text="pytanie",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        # Button
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_answer)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_answer)

        self.true_button.grid(column=1, row=3)
        self.false_button.grid(column=2, row=3)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=2, row=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="koniec quizu")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_answer(self):
        is_right = self.quiz.check_answer("Ture")
        self.give_feedback(is_right)

    def false_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



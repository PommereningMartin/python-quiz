from tkinter import *
import random

root = Tk()
answer = StringVar(None, 0)
questions_per_cat = {1: [{
    "id": 1,
    "text": "Wieviele Räder hat ein Auto?",
    "possible_answers": [1, 2, 3, 4],
    "correct_answer": 4
}],
    2: [{
        "id": 1,
        "text": "Was bedeutet GmbH?",
        "possible_answers": ['Foo', 'Bar', 'Baz', 'Test'],
        "correct_answer": 'Test'
    }]}

data = {}


class Question:
    label = None
    container = None
    amser_label = None
    cat = None
    answers = []

    def __init__(self, container, cat):
        self.cat = cat
        self.container = container
        self.for_category(container, cat)
        self.answer = StringVar()

    def for_category(self, container, cat):
        print(cat)
        questions = questions_per_cat.get(cat)

        question = questions[random.randrange(0, len(questions))]
        row = 1
        col = 0
        self.label = Label(container, text=question["text"])
        self.label.grid(row=0, column=0)
        print(question['possible_answers'])
        data[question['text']] = question['correct_answer']
        self.cleanup()
        for foo in question['possible_answers']:
            # print(col, row)
            self.answers.append(Radiobutton(container,
                                            text=foo,
                                            value=foo,
                                            variable=answer).grid(row=row, column=col))
            if col == 1:
                col = 0
            else:
                col += 1
            if col == 0:
                row += 1
        Button(self.container, text='Submit Answer', command=lambda: self.check_answer(question['text'])).grid(row=10,
                                                                                                               column=0)

    def cleanup(self):
        if not self.answers:
            for elem in self.answers:
                elem.destroy()

    def check_answer(self, question):
        foo = data.get(question)
        print(foo, "######", answer.get())
        if str(foo) == answer.get():
            self.bar()
            self.amser_label = Label(self.container, text='Correct Answer')
            self.amser_label.grid(row=11, column=0)
        else:
            self.bar()
            self.amser_label = Label(self.container, text='Wrong Answer')
            self.amser_label.grid(row=11, column=0)

    def bar(self):
        if self.amser_label is not None:
            self.amser_label.destroy()
        return


class Quiz:
    root = None
    categoriesList = None
    categoriesFrame = None
    questionFrame = None
    categoriesButtons = []
    question = None

    def __init__(self):
        self.build_window()
        self.categoriesFrame = LabelFrame(root, padx=50, pady=50, text='Categories')
        self.show_categories()
        self.categoriesFrame.grid(row=0, column=0)
        self.questionFrame = LabelFrame(root, padx=50, pady=50, text='Questions')
        self.questionFrame.grid(row=0, column=1)

    def build_window(self):
        root.geometry("800x600")

    @staticmethod
    def run():
        root.mainloop()

    def show_categories(self):
        self.categoriesList = {
            1: {"name": "TECHNIK", "name_label": "Technik", "description": "All about Technik!"},
            2: {"name": "WIRTSCHAFT", "name_label": "Wirtschaft", "description": "All about Wirtschaft!"},
            3: {"name": "SPORT", "name_label": "Sport", "description": "All about Sport!"},
            4: {"name": "INFORMATIK", "name_label": "Informatik", "description": "All about Informatik!"},
        }
        index = 1
        for key in self.categoriesList:
            cat_name = self.categoriesList.get(key)['name']
            button = Button(self.categoriesFrame, text=cat_name,
                            command=lambda a=key: self.create_question_for_category(a))
            button.grid(column=0, row=index)
            index += 1

    def create_question_for_category(self, cat):
        self.question = None
        self.question = Question(self.questionFrame, cat)

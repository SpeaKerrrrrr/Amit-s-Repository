from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.urls import reverse
from .models import Question, Answer
# Home view
def home(request):
    return render(request, 'home.html')

# Registration view
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('home')  # Redirect to a profile page or home
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Log in the user
            return redirect('home')  # Redirect to the profile page or another page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Profile view
def profile(request):
    return render(request, 'profile.html')

# About view
def about(request):
    return render(request, 'about.html')

# Experience level views
def beginner(request):
    return render(request, 'beginner.html')

def intermediate(request):
    return render(request, 'intermediate.html')

def professional(request):
    return render(request, 'professional.html')

def expert(request):
    return render(request, 'expert.html')

# Start Learning view
def start_learning(request):
    return render(request, 'start_learning.html')

def projects_ideas(request):
    return render(request, 'projects_ideas.html')

# Define the questions and answers
beginner_quiz = [
    {
        "question": "What is the output of print('Hello, World!')?",
        "options": ["Hello", "World", "Hello, World!", "Syntax Error"],
        "correct_answer": "Hello, World!"
    },
    {
        "question": "Which of the following is a variable declaration in Python?",
        "options": ["int a = 5", "a = 5", "declare a = 5", "var a = 5"],
        "correct_answer": "a = 5"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/* */", "<!-- -->"],
        "correct_answer": "#"
    },
    {
        "question": "What is the correct file extension for Python files?",
        "options": [".python", ".pyth", ".py", ".pyt"],
        "correct_answer": ".py"
    },
    {
        "question": "Which data type is used to store text?",
        "options": ["int", "float", "str", "bool"],
        "correct_answer": "str"
    },
    {
        "question": "How do you create a list in Python?",
        "options": ["{}", "[]", "()", "<>"],
        "correct_answer": "[]"
    },
    {
        "question": "Which function is used to get input from the user in Python?",
        "options": ["input()", "get()", "read()", "scan()"],
        "correct_answer": "input()"
    },
    {
        "question": "What will be the output of 2 ** 3 in Python?",
        "options": ["6", "8", "9", "5"],
        "correct_answer": "8"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "define", "def", "function"],
        "correct_answer": "def"
    },
    {
        "question": "Which of the following is used to create an infinite loop in Python?",
        "options": ["for", "while", "loop", "repeat"],
        "correct_answer": "while"
    }
]

intermidiate_quiz = [
    {
        "question": "What is the output of the following code:\n```python\nfor i in range(2, 6):\n    print(i**2)\n```",
        "options": ["4 6 8 10", "4 9 16 25", "2 3 4 5", "2 4 6 8"],
        "correct_answer": "4 9 16 25"
    },
    {
        "question": "What is the purpose of the `yield` keyword in Python?",
        "options": ["Returns a value from a function", "Creates a generator object", "Defines a class", "Raises an exception"],
        "correct_answer": "Creates a generator object"
    },
    {
        "question": "What is the output of the following code:\n```python\nmy_list = [1, 2, 3]\nmy_list.append(4)\nprint(my_list)\n```",
        "options": ["[1, 2, 3]", "[2, 3, 4]", "[1, 2, 3, 4]", "Syntax Error"],
        "correct_answer": "[1, 2, 3, 4]"    
    },
    {
        "question": "What is the difference between a list and a tuple in Python?",
        "options": ["Lists are immutable, tuples are mutable", "Lists are mutable, tuples are immutable", "Lists are faster, tuples are slower", "There is no difference"],
        "correct_answer": "Lists are mutable, tuples are immutable"
    },
    {
        "question": "What is the output of the following code:\n```python\nmy_dict = {'a': 1, 'b': 2}\nmy_dict['c'] = 3\nprint(my_dict['b'])\n```",
        "options": ["1", "2", "3", "KeyError"],
        "correct_answer": "2"
    },
    {
        "question": "What is the purpose of the `try-except` block in Python?",
        "options": ["To define a function", "To handle exceptions", "To create a loop", "To define a class"],
        "correct_answer": "To handle exceptions"
    },
    {
        "question": "What is the output of the following code:\n```python\nmy_string = 'Hello, World!'\nprint(my_string[::-1])\n```",
        "options": ["!dlroW ,olleH", "Hello, World!", "dlroW ,olleH", "Syntax Error"],
        "correct_answer": "!dlroW ,olleH"
    },
    {
        "question": "What is the output of the following code:\n```python\nmy_list = [1, 2, 3]\nmy_list.insert(1, 4)\nprint(my_list)\n```",
        "options": ["[1, 4, 2, 3]", "[4, 1, 2, 3]", "[1, 2, 3, 4]", "Syntax Error"],
        "correct_answer": "[1, 4, 2, 3]"
    },
    {
        "question": "What is the output of the following code:\n```python\nmy_list = [1, 2, 3]\nmy_list.remove(2)\nprint(my_list)\n```",
        "options": ["[1, 2, 3]", "[1, 3]", "[2, 3]", "Syntax Error"],
        "correct_answer": "[1, 3]"
    }
]

professional_quiz = [
    {
        "question": "Explain the concept of metaclasses in Python and provide an example of their usage.",
        "options": ["A class that inherits from another class", "A class that creates other classes", "A class that implements a protocol", "A class that defines a custom data type"],
        "correct_answer": "A class that creates other classes"
    },
    {
        "question": "Describe the differences between `try-except`, `try-finally`, and `try-except-finally` blocks in Python.",
        "options": ["Different ways to define functions", "Different ways to create classes", "Different ways to handle exceptions", "Different ways to control the flow of execution"],
        "correct_answer": "Different ways to handle exceptions"
    },
    {
        "question": "Explain the concept of decorators in Python and provide an example of their usage.",
        "options": ["Classes that inherit from other classes", "Functions that modify other functions", "Functions that create new objects", "Functions that raise exceptions"],
        "correct_answer": "Functions that modify other functions"
    },
    {
        "question": "What is the difference between shallow copy and deep copy in Python? Provide an example of each.",
        "options": ["Shallow copy creates a new object with the same references, deep copy creates a new object with new references", "Shallow copy creates a new object with new references, deep copy creates a new object with the same references", "Both create new objects with the same references", "Both create new objects with new references"],
        "correct_answer": "Shallow copy creates a new object with the same references, deep copy creates a new object with new references"
    },
    {
        "question": "Explain the concept of context managers in Python and provide an example of their usage.",
        "options": ["Objects that manage resources", "Functions that modify other functions", "Classes that inherit from other classes", "Functions that create new objects"],
        "correct_answer": "Objects that manage resources"
    },
    {
        "question": "Explain the concept of closures in Python and provide an example of their usage.",
        "options": ["Functions that return other functions", "Functions that modify other functions", "Functions that create new objects", "Functions that raise exceptions"],
        "correct_answer": "Functions that return other functions"
    },
    {
        "question": "What is the difference between a generator function and a regular function in Python?",
        "options": ["Generator functions return iterators, regular functions return values", "Generator functions return values, regular functions return iterators", "There is no difference", "Generator functions are faster, regular functions are slower"],
        "correct_answer": "Generator functions return iterators, regular functions return values"
    },
    {
        "question": "Explain the concept of abstract base classes (ABCs) in Python and provide an example of their usage.",
        "options": ["Classes that cannot be instantiated", "Classes that define a common interface for other classes", "Classes that inherit from other classes", "Classes that raise exceptions"],
        "correct_answer": "Classes that define a common interface for other classes"
    },
    {
        "question": "What is the purpose of the `__slots__` attribute in Python classes?",
        "options": ["To define the class's attributes", "To optimize memory usage", "To create a new instance of the class", "To call the constructor"],
        "correct_answer": "To optimize memory usage"
    }
]

expert_quiz = [
    {
        "question": "Explain the concept of metaclasses in Python and provide an example of their usage to create custom class factories.",
        "options": ["A class that inherits from another class", "A class that implements a protocol", "A class that creates other classes", "A class that defines a custom data type"],
        "correct_answer": "A class that creates other classes"
    },
    {
        "question": "Describe the differences between `try-except`, `try-finally`, and `try-except-finally` blocks in Python, and provide examples of when each is appropriate.",
        "options": ["Different ways to define functions", "Different ways to create classes", "Different ways to handle exceptions", "Different ways to control the flow of execution"],
        "correct_answer": "Different ways to handle exceptions"
    },
    {
        "question": "Explain the concept of decorators in Python and provide an example of using them to create custom context managers.",
        "options": ["Functions that modify other functions", "Classes that inherit from other classes", "Functions that create new objects", "Functions that raise exceptions"],
        "correct_answer": "Functions that modify other functions"
    },
    {
        "question": "What is the difference between shallow copy and deep copy in Python? Provide an example of each and explain when they are appropriate.",
        "options": ["Shallow copy creates a new object with the same references, deep copy creates a new object with new references", "Shallow copy creates a new object with new references, deep copy creates a new object with the same references", "Both create new objects with the same references", "Both create new objects with new references"],
        "correct_answer": "Shallow copy creates a new object with the same references, deep copy creates a new object with new references"
    },
    {
        "question": "Explain the concept of context managers in Python and provide an example of creating a custom context manager for file operations.",
        "options": ["Functions that modify other functions", "Classes that inherit from other classes", "Functions that create new objects", "Objects that manage resources"],
        "correct_answer": "Objects that manage resources"
    },
    {
        "question": "Explain the concept of closures in Python and provide an example of using them to create private functions within a module.",
        "options": ["Functions that modify other functions", "Functions that create new objects", "Functions that return other functions", "Functions that raise exceptions"],
        "correct_answer": "Functions that return other functions"
    },
    {
        "question": "What is the difference between a generator function and a regular function in Python? Provide an example of using a generator function to create an infinite iterator.",
        "options": ["Generator functions return values, regular functions return iterators", "Generator functions return iterators, regular functions return values", "There is no difference", "Generator functions are faster, regular functions are slower"],
        "correct_answer": "Generator functions return iterators, regular functions return values"
    },
    {
        "question": "Explain the concept of abstract base classes (ABCs) in Python and provide an example of using them to enforce a common interface for related classes.",
        "options": ["Classes that cannot be instantiated", "Classes that define a common interface for other classes", "Classes that inherit from other classes", "Classes that raise exceptions"],
        "correct_answer": "Classes that define a common interface for other classes"
    },
    {
        "question": "What is the purpose of the `__slots__` attribute in Python classes? How can it be used to optimize memory usage in large-scale applications?",
        "options": ["To define the class's attributes", "To optimize memory usage", "To create a new instance of the class", "To call the constructor"],
        "correct_answer": "To optimize memory usage"
    }
]

# View for displaying a question

# View for displaying a question

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'beginner_questions.html', {'questions': questions})

# def beginner_questions(request, question, options, solution):
#      context = {'question': question,
#                 'options': options.split(','),
#                 'solution': solution } 
#      return render(request, 'beginner_questions.html', context)


def beginner_questions(request):
    current_index = int(request.GET.get('index', 0))    
    is_last_question = current_index == len(beginner_quiz) - 1
    current_question = beginner_quiz[current_index % len(beginner_quiz)]    
    next_index = (current_index + 1)
    next_question = beginner_quiz[next_index % len(beginner_quiz)]
    
    context = {
        'question': current_question['question'],
        'options': current_question['options'],
        'solution': current_question['correct_answer'],
        'next_question': next_question['question'],
        'next_options': ','.join(next_question['options']),
        'next_solution': next_question['correct_answer'],
        'next_url': reverse('beginner_questions') + f'?index={next_index}',
        'is_last_question': is_last_question,
        'home_url': reverse('home')
    }
    
    return render(request, 'beginner_questions.html', context)

def intermidiate_questions(request):
    current_index = int(request.GET.get('index', 0))    
    is_last_question = current_index == len(intermidiate_quiz) - 1
    current_question = intermidiate_quiz[current_index % len(intermidiate_quiz)]    
    next_index = (current_index + 1)
    next_question = intermidiate_quiz[next_index % len(intermidiate_quiz)]
    
    context = {
        'question': current_question['question'],
        'options': current_question['options'],
        'solution': current_question['correct_answer'],
        'next_question': next_question['question'],
        'next_options': ','.join(next_question['options']),
        'next_solution': next_question['correct_answer'],
        'next_url': reverse('intermidiate_questions') + f'?index={next_index}',
        'is_last_question': is_last_question,
        'home_url': reverse('home')
    }
    
    return render(request, 'intermidiate_questions.html', context)

def professional_questions(request):
    current_index = int(request.GET.get('index', 0))    
    is_last_question = current_index == len(professional_quiz) - 1
    current_question = professional_quiz[current_index % len(professional_quiz)]    
    next_index = (current_index + 1)
    next_question = professional_quiz[next_index % len(professional_quiz)]
    
    context = {
        'question': current_question['question'],
        'options': current_question['options'],
        'solution': current_question['correct_answer'],
        'next_question': next_question['question'],
        'next_options': ','.join(next_question['options']),
        'next_solution': next_question['correct_answer'],
        'next_url': reverse('professional_questions') + f'?index={next_index}',
        'is_last_question': is_last_question,
        'home_url': reverse('home')
    }
    
    return render(request, 'professional_questions.html', context)

def expert_questions(request):
    current_index = int(request.GET.get('index', 0))    
    is_last_question = current_index == len(expert_quiz) - 1
    current_question = expert_quiz[current_index % len(expert_quiz)]    
    next_index = (current_index + 1)
    next_question = expert_quiz[next_index % len(expert_quiz)]
    
    context = {
        'question': current_question['question'],
        'options': current_question['options'],
        'solution': current_question['correct_answer'],
        'next_question': next_question['question'],
        'next_options': ','.join(next_question['options']),
        'next_solution': next_question['correct_answer'],
        'next_url': reverse('expert_questions') + f'?index={next_index}',
        'is_last_question': is_last_question,
        'home_url': reverse('home')
    }
    
    return render(request, 'expert_questions.html', context)

def check_answer(request, question_number):
    questions = Question.objects.all()
    if 1 <= question_number <= questions.count():
        question = questions[question_number - 1]
        correct_answer = question.answers.filter(is_correct=True).first()

        if request.method == 'POST':
            user_answer_id = request.POST.get('answer')
            user_answer = get_object_or_404(Answer, id=user_answer_id)

            next_question = question_number + 1 if question_number < questions.count() else None
            previous_question = question_number - 1 if question_number > 1 else None

            if user_answer.is_correct:
                if next_question:
                    return render(request, 'answer_correct.html', {
                        'next_question': next_question
                    })
                else:
                    return render(request, 'answer_correct.html')
            else:
                return render(request, 'answer_incorrect.html', {
                    'next_question': next_question,
                    'previous_question': previous_question
                })
    else:
        return redirect('beginner')

from flask import Flask, render_template, request, jsonify, redirect, url_for
import json

app = Flask(__name__)

questions = [
    {
        "question": "Ποια ήταν η πρωτεύουσα της αρχαίας Ελλάδας;",
        "options": ["Ναύπλιο", "Σπάρτη", "Αθήνα", "Χανιά"],
        "correct_answer": "Ναύπλιο",
        "reward": 50
    },
    {
        "question": "Ποια ήταν η πρωτεύουσα της αρχαίας Ελλάδας;",
        "options": ["Ναύπλιο", "Σπάρτη", "Αθήνα", "Χανιά"],
        "correct_answer": "Ναύπλιο",
        "reward": "50"
    },
    {
        "question": "Ποιος ήταν ο ιστορικός που περιέγραψε την κατάκτηση της Τροίας στην Ιλιάδα;",
        "options": ["Δημοσθένης", "Θουκυδίδης", "Ηρόδοτος", "Όμηρος"],
        "correct_answer": "Όμηρος",
        "reward": "100"
    },
    {
        "question": "Ποιος είναι ο συνθέτης του εθνικού ύμνου της Ελλάδας;",
        "options": ["Διονύσιος Σολώμος", "Μίκης Θεοδοράκης", "Μάνος Χατζιδάκις", "Νίκος Σκαλκώτας"],
        "correct_answer": "Διονύσιος Σολώμος",
        "reward": "150"
    },
    {
        "question": "Ποια είναι η γνωστή ελληνική γιορτή του καλοκαιριού που γιορτάζεται στις 15 Αυγούστου;",
        "options": ["Αγίου Πνεύματος", "Κοίμηση της Θεοτόκου", "Αγίων Πάντων", "Αγίου Ιωάννη"],
        "correct_answer": "Κοίμηση της Θεοτόκου",
        "reward": "250"
    },
    {
        "question": "Ποιο είναι το ακρωτήριο όπου βρίσκεται ο ναός του Ποσειδώνα;",
        "options": ["Ταίναρο", "Δράστης", "Καβογκρεκό", "Σούνιο"],
        "correct_answer": "Σούνιο",
        "reward": "500"
    },
    {
        "question": "Ποιο είναι το μεγαλύτερο νησί της Ελλάδας;",
        "options": ["Κρήτη", "Ρόδος", "Ευβοία", "Μυτιλήνη"],
        "correct_answer": "Κρήτη",
        "reward": "1.000"
    },
    {
        "question": "Ποιο είναι το εθνικό ζώο της Ελλάδας;",
        "options": ["Γάτα", "Σκίουρος", "Δελφίνι", "Αρκούδα"],
        "correct_answer": "Δελφίνι",
        "reward": "2.000"
    },
    {
        "question": "Ποιος αρχαίος ελληνικός φιλόσοφος είναι γνωστός για την πρότασή του Γνώθι σε αυτόν;",
        "options": ["Σωκράτης", "Πλάτωνας", "Αριστοτέλης", "Ηράκλειτος"],
        "correct_answer": "Σωκράτης",
        "reward": "5.000"
    },
    {
        "question": "Ποια είναι η πόλη-κράτος που διακρίθηκε για την αρχιτεκτονική της που συνδυάζει φυσικό τοπίο και αρχαία μνημεία;",
        "options": ["Πάτρα", "Χανιά", "Αθήνα", "Σαντορίνη"],
        "correct_answer": "Σαντορίνη",
        "reward": "10.000"
    },
    {
        "question": "Ποιος ήταν ο αρχαίος Έλληνας ιατρός που θεωρείται ο πατέρας της ιατρικής;",
        "options": ["Γαληνός", "Ασκληπιάδης", "Ηρόδοτος", "Ιπποκράτης"],
        "correct_answer": "Ιπποκράτης",
        "reward": "20.000"
    },
    {
        "question": "Σύμφωνα με τον μύθο ποιος ξεκίνησε τους Ολυμπιακούς αγώνες;",
        "options": ["Δίας", "Άρης", "Ηρακλής", "Θησέας"],
        "correct_answer": "Ηρακλής",
        "reward": "30.000"
    },
    {
        "question": "Ποιο είναι το αρχιτεκτονικό θαύμα στην Πελοπόννησο που κατασκευάστηκε τον 20ό αιώνα;",
        "options": ["Αρχαίο θέατρο της Κορίνθου", "Οι Μετεώροι", "Οι μεσαιωνικές και βυζαντινές εκκλησίες στη Μονεμβασιά", "Αρχαίο θέατρο της Επιδαύρου"],
        "correct_answer": "Αρχαίο θέατρο της Επιδαύρου",
        "reward": "50.000"
    },
    {
        "question": "Ποιο ήταν το κοινό θέμα των περισσότερων αρχαίων ελληνικών κεραμικών;",
        "options": ["Αθλήματα", "Σκηνές καθημερινής ζωής", "Έρωτας", "Απεικόνιση των μύθων της ελληνικής μυθολογίας"],
        "correct_answer": "Απεικόνιση των μύθων της ελληνικής μυθολογίας",
        "reward": "100.000"
    },
    {
        "question": "Ποιος είναι ο διάσημος μαθηματικός και φυσικός που γεννήθηκε στην Ελλάδα και έζησε στον 3ο αιώνα π.Χ.;",
        "options": ["Θάλης", "Πυθαγόρας", "Αρχιμήδης", "Ευκλείδης"],
        "correct_answer": "Αρχιμήδης",
        "reward": "200.000"
    },
    {
        "question": "Ποιος ήταν ο διάσημος αρχαίος Έλληνας ζωγράφος που ζωγράφισε τα τοιχογραφικά τους τάματα στην πόλη της Πομπηίας;",
        "options": ["Ζεύξις", "Εφήβιος", "Φίλοξενος", "Πολύγνωτος"],
        "correct_answer": "Φίλοξενος",
        "reward": "300.000"
    },
    {
        "question": "Ποιος αρχαίος Έλληνας μαθηματικός θεωρείται ο πατέρας της γεωμετρίας;",
        "options": ["Πυθαγόρας", "Θαλής", "Αρχιμήδης", "Ευκλείδης"],
        "correct_answer": "Ευκλείδης",
        "reward": "400.000"
    },
    {
        "question": "Ποιο ήταν το έργο του Αισχύλου που περιγράφει την επιστροφή του Αγαμέμνονα στην Αργό;",
        "options": ["Πέρσες", "Ορέστεια", "Ευμενίδες", "Χοηφόροι"],
        "correct_answer": "Ορέστεια",
        "reward": "500.000"
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game.html')
def start_game():
    question_number = 1
    question_data = questions[question_number]
    return render_template('start_game.html', question_number=question_number, question=question_data["question"], options=question_data["options"])

@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.get_json()
    question_number = int(data['question_number'])
    answer = data['answer']

    if question_number < len(questions):
        correct_answer = questions[question_number]['correct_answer']
        reward = questions[question_number]['reward']

        if answer == correct_answer:
            if question_number + 1 < len(questions):
                response = {
                    "is_correct": True,
                    "reward": reward,
                    "question_number": question_number + 1
                }
            else:
                response = {
                    "is_correct": True,
                    "reward": reward,
                    "question_number": None,
                    "winner": True
                }
        else:
            response = {
                "is_correct": False,
                "correct_answer": correct_answer
            }
    else:
        response = {
            "is_correct": False,
            "correct_answer": "Invalid question number"
        }

    return jsonify(response)

@app.route('/next_question', methods=['POST'])
def next_question():
    data = request.get_json()
    question_number = int(data['question_number'])

    if question_number < len(questions):
        question_data = questions[question_number]
        response = {
            "question_number": question_number,
            "question": question_data["question"],
            "options": question_data["options"]
        }
    else:
        response = {
            "question_number": None,
            "question": "No more questions",
            "options": []
        }

    return jsonify(response)

@app.route('/rules.html')
def rules():
    return render_template('rules.html')

@app.route('/winner.html')
def winner():
    return render_template('winner.html')

if __name__ == '__main__':
    app.run(debug=True)

import sqlite3

###############################################################
# Database functions
###############################################################

def connect_to_db():
    conn = sqlite3.connect('database.db')
    return conn

def drop_db_table():
    try:
        conn = connect_to_db()
        conn.execute('''DROP TABLE questions''')
        conn.commit()
        print("Questions table dropped successfully")
    except:
        print("Questions table drop failed")
    finally:
        conn.close()

def create_db_table():
    try:
        conn = connect_to_db()
        conn.execute('''
            CREATE TABLE questions (
                question_id INTEGER PRIMARY KEY,
                questionText TEXT NOT NULL,
                answerOptions TEXT NOT NULL
            );
        ''')
        conn.commit()
        print("Questions table created successfully")
    except:
        print("Questions table creation failed")
    finally:
        conn.close()


def insert_quiz_question(questionText):
    inserted_question = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO questions (questionText, answerOptions) VALUES (?, ?)", (questionText['questionText'], repr(questionText['answerOptions'])) )
        conn.commit()
        inserted_question = get_question_by_id(cur.lastrowid)
    except:
        conn().rollback()

    finally:
        conn.close()

    return inserted_question


def get_questions():
    questions = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM questions")
        rows = cur.fetchall()

        # convert row objects to dictionary
        for i in rows:
            questionText = {}
            questionText["question_id"] = i["question_id"]
            questionText["questionText"] = i["questionText"]
            questionText["answerOptions"] = eval(i["answerOptions"])
            questions.append(questionText)

    except:
        questions = []

    return questions


def get_question_by_id(question_id):
    questionText = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM questions WHERE question_id = ?", (question_id,))
        row = cur.fetchone()

        # convert row object to dictionary
        questionText["question_id"] = row["question_id"]
        questionText["questionText"] = row["questionText"]
        questionText["answerOptions"] = eval(row["answerOptions"])
    except:
        questionText = {}

    return questionText


def update_question(questionText):
    updated_question = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("UPDATE questions SET questionText = ?, answerOptions = ? WHERE question_id =?", (questionText["questionText"], repr(questionText["answerOptions"]), questionText["question_id"]))
        conn.commit()
        #return the questionText
        updated_question = get_question_by_id(questionText["question_id"])
    except:
        conn.rollback()
        updated_question = {}
    finally:
        conn.close()

    return updated_question


def delete_question(question_id):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute("DELETE from questions WHERE question_id = ?", (question_id,))
        conn.commit()
        message["status"] = "questionText deleted successfully"
    except:
        conn.rollback()
        message["status"] = "Cannot delete questionText"
    finally:
        conn.close()

    return message
import sqlite3
from internet import check_internet_connection
# from output_module import output
def create_connection():

    connection = sqlite3.connect("memory.db")
    return connection

def get_questions_and_answers():

    con = create_connection()
    cur = con.cursor()

    cur.execute("SELECT * FROM questionsAndAnswers")

    return cur.fetchall()

def insert_question_and_answer(question, answer):
    try:
        con = create_connection()
        cur = con.cursor()
        # insert into tablename values('question', 'answert')
        query = "INSERT INTO questionsAndAnswers values('" + question + "', '" + answer + "')"
        cur.execute(query)
        con.commit()
    except sqlite3.Error as e:
        print(f"Error: {e}")
def get_answer_from_memory(question):
    rows = get_questions_and_answers()
    answer = ""
    for row in rows:
        if row[0].lower() in question.lower():
            answer = row[1]
            break
    return answer

def get_name():
    con = create_connection()
    cur = con.cursor()
    query = "select value from memory where name = 'assistant_name'"
    cur.execute(query)
    return cur.fetchall()[0][0]

def update_name(new_name):
    # Check if new_name is not None before proceeding
    if new_name is not None:
        con = create_connection()
        cur = con.cursor()
        query = "update memory set value = '" + new_name + "' where name = 'assistant_name'"
        cur.execute(query)
        con.commit()
    else:
        print("Error: new_name is None")
def update_last_seen(last_seen_date):
    con = create_connection()
    cur = con.cursor()
    query = "update memory set value = '" + str(last_seen_date) + "' where name = 'last_seen_date'"
    cur.execute(query)
    con.commit()

def get_last_seen():
    con = create_connection()
    cur = con.cursor()
    query = "select value from memory where name = 'last_seen_date'"
    cur.execute(query)
    con.commit()
    return str(cur.fetchall()[0][0])

def turn_on_speech():
    if (check_internet_connection()):

        con = create_connection()
        cur = con.cursor()
        query = "update memory set value = 'on' where name = 'speech'"
        cur.execute(query)
        con.commit()

        return("Ok ,I will speak now!")
    else:
        return ("Hey please turn on internet first.")

def turn_off_speech():
    con = create_connection()
    cur = con.cursor()
    query = "update memory set value = 'off' where name = 'speech'"
    cur.execute(query)
    con.commit()
    return ("Ok I won't speak")
    # return "OK"

def speak_is_on():
    con = create_connection()
    cur = con.cursor()
    query = "select value from memory where name = 'speech'"
    cur.execute(query)
    con.commit()
    ans = str(cur.fetchall()[0][0])

    if ans == "on":
        return True
    else:
        return False







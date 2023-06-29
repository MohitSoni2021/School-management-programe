import pymysql
from prettytable import PrettyTable
conn = pymysql.connect(
        host='localhost',
        user='root', 
        password = "root",
        db='school',
        )

def new_student(first_name, last_name):
    cur = conn.cursor()
    cur.execute(f"insert into class12(first_name, last_name) values ('{first_name}', '{last_name}')")
    conn.commit()
    cur.close()
    
    cur = conn.cursor()
    cur.execute(f"select registeration_no from class12 where first_name = '{first_name}' and last_name = '{last_name}' order by registeration_no desc")
    registeration_no_new_student = cur.fetchall()
    cur.close()
    
    print(registeration_no_new_student[0][0])
    
def show_student_data():
    cur = conn.cursor()
    cur.execute("describe class12")
    column_detail = cur.fetchall()
    cur.close()

    cur = conn.cursor()
    cur.execute("select * from class12")
    student_detail = cur.fetchall()
    cur.close()

    columns = []

    for i in range(len(column_detail)):
        columns.append(column_detail[i][0])

    student = PrettyTable(columns)

    for i in range(len(student_detail)):
        student.add_row(list(student_detail[i]))

    print(student)
    
def delete_admission(registeration_no_student):
    cur = conn.cursor()
    cur.execute(f"delete from class12 where registeration_no = {registeration_no_student}")
    print("Admission cancel sucessfully ......")
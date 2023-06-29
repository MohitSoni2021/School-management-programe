import pymysql
from prettytable import PrettyTable
conn = pymysql.connect(
        host='localhost',
        user='root', 
        password = "root"
        )

def database_checker(database_name, create_database="N"):
    #this function return check if database already present 
    # return uncheck if database not present
    
        cur = conn.cursor()
        cur.execute("show databases")
        fetch_databases = cur.fetchall()
        database_list=[]
        for database in fetch_databases:
                database_list.append(database[0])
                
        check_for_database = ""
        if database_name in database_list:
                check_for_database = "Check"
        else:
                check_for_database = "Uncheck"
                if create_database.capitalize() == "Y":
                    cur = conn.cursor()
                    cur.execute(f"create database {database_name}")
                else:
                    pass
         
        return check_for_database


def table_checker(database_name, table_name):
        cur = conn.cursor()
        cur.execute(f"use {database_name}")
        cur.execute(f"show tables")
        fetch_table = cur.fetchall()
        tables_list = []
        for table in fetch_table:
                tables_list.append(table[0])
                
        check_for_table = ""
        if table_name in tables_list:
                check_for_table = "Check"
        else:
                check_for_table = "Unchecked"
                
        return check_for_table

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
    try:
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
    except Exception as e:
        print("NO DATA PRESENT IN DATABASE...\n\n")
    
def delete_admission(registeration_no_student):
    cur = conn.cursor()
    cur.execute(f"delete from class12 where registeration_no = {registeration_no_student}")
    print("Admission cancel sucessfully ......")
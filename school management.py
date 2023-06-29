import mysqlCommands as MSC

while True:
    main_screen_options = ["Add New Student", "Show all students", "Cancel Admission"]

    for i in range(len(main_screen_options)):
        print(f"{i+1} {main_screen_options[i]}")

    main_screen_user_option = int(input("Enter your option : \t"))

    if main_screen_user_option == 1:
        student_first_name = input("Enter First Name of Student : \t")
        student_last_name = input("Enter Last Name of Student : \t")
        MSC.new_student(student_first_name, student_last_name)
        print("Admission sucessful ...")
        
    elif main_screen_user_option == 2:
        MSC.show_student_data()
        
    else:main_screen_options = ["Add New Student", "Show all students"]

    for i in range(len(main_screen_options)):
        print(f"{i+1} {main_screen_options[i]}")

    main_screen_user_option = int(input("Enter your option : \t"))

    if main_screen_user_option == 1:
        student_first_name = input("Enter First Name of Student : \t")
        student_last_name = input("Enter Last Name of Student : \t")
        MSC.new_student(student_first_name, student_last_name)
        print("Admission sucessful ...")
        
    elif main_screen_user_option == 2:
        MSC.show_student_data()
        
    elif main_screen_user_option == 3:
        registeration_no_student = int(input("Enter registeration to Cancel admission : \t"))
        MSC.delete_admission(registeration_no_student)
        
    else:
        pass
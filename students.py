def students():
    no_of_students= int(input("Total number of students in the class :"))
    print(" ")
    math_students = int(input("Total number of Math students in the class :"))
    print(" ")
    bio_students= int(input("Total number of Bio students in the class :"))
    print(" ")
    
    remaining_students=no_of_students-math_students-bio_students
    print("Remaining Students", remaining_students)
    
    math_bio_students=math_students+bio_students
    print("Total no. of bio and math students is :",math_bio_students)

students()
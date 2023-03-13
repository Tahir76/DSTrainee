def students():
    no_of_students= int(input("Total number of students in the class :"))
    print(" ")
    math_students = int(input("Total number of Math students in the class :"))
    print(" ")
    bio_students= int(input("Total number of Bio students in the class :"))
    print(" ")
    
    without_math_bio=no_of_students-math_students-bio_students
    print("Remaining 1 students are: ", without_math_bio)
    
    with_math_bio=math_students+bio_students
    print("Total no. of bio and math students are :",with_math_bio)

students()
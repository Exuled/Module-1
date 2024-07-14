#grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
#students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#student_grades = {}
#print((grades[0] == 'Aaron'))
#print(list(students)[0])
#A = grades[0]
#B = grades[1]
#J = grades[2]
#K = grades[3]
#S = grades[4]
#print(list(A))
#print(grades[0])
#print(list(students.pop()))
#students = str(students)
#print((students) [1:48])
#print((students)[1])

#Aaron = str(A)
#print(Aaron)

#все это великолепие я делал сам, когда не мог решить задачу
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}


grades_s = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])]
students_s = sorted(students)

dict1 = dict(zip(grades_s, students_s))
print(dict1)








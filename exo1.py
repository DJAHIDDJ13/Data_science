from random import randint

def write_student_marks(filename, nbr_students, nbr_marks):
	f = open(filename, "w")
	f.write(':'.join(['Test'+str(i) for i in range(1, nbr_marks+1)]))
	for i in range(nbr_students+1):
		f.write(':'.join([str(randint(0,20)) for _ in range(nbr_marks)]) + '\r\n')
	f.close()

def read_student_marks(filename):
	f = open(filename, "r")
	res = []
	line = f.readline() # ignore first line
	line = f.readline()
	while line:
		res.append([int(i) for i in line.split(':')])
		line = f.readline()
	f.close()
	return res

def get_weighted_student_averages(students):
	if len(students[0]) != 5:
		return [round(sum(student)/len(student),2) for student in students]
	return [sum([vals[0] * vals[1] for vals in zip(sorted(student), [0.05,0.05,0.3,0.3,0.3])]) for student in students]

def get_test_averages(students):
	len_marks = len(students[0])
	len_students = len(students)
	return [sum([students[j][i] for j in range(len_students)])/len_students for i in range(len_marks)]

def write_average_data(source_file, out_file):
	f = open(filename, "w")

	students = read_student_marks(source_file)
	stud_num = len(students)
	mark_num = len(students[0])
	
	f.write(':'.join(['Test'+str(i) for i in range(1, mark_num + 1)]+['Average\r\n']))

	stud_averages = get_weighted_student_averages(students)
	test_averages = get_test_averages(students)
	
	for i in range(stud_num):
		f.write(':'.join([str(students[i][j]) for j in range(mark_num)]) + ':'+ str(round(stud_averages[i], 2)) + '\r\n')

	f.write(':'.join(['Average'+str(i) for i in range(1, mark_num + 1)]+['Total_average\r\n']))
	f.write(':'.join([str(round(test_averages[i], 2)) for i in range(len(test_averages))]) + ':'+str(round(sum(stud_averages)/len(stud_averages), 2))+'\r\n')
	
	f.close()
student_number = 100000
marks_number = 5
write_student_marks("note.csv", student_number, marks_number)
write_average_data("note.csv", "average.csv")

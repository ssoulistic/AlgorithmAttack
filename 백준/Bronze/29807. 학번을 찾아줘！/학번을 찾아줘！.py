import sys
input=sys.stdin.readline
T=int(input())
grades=list(map(int,input().split()))
grades.extend([0]*(5-T))

student_number=0
if grades[0]>grades[2]:
    student_number+=508*(grades[0]-grades[2])
else:
    student_number+=108*(grades[2]-grades[0])

if grades[1]>grades[3]:
    student_number+=212*(grades[1]-grades[3])
else:
    student_number+=305*(grades[3]-grades[1])

if grades[4]:
    student_number+=grades[4]*707

student_number*=4763
print(student_number)
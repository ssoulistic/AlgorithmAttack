credit_sum=0
grade_sum=0
level={"A+":4.5,"A0":4.0,"B+":3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0.0}
for _ in range(20):
    name,credit,grade=input().split()
    if grade=="P":
        continue
    credit_sum+=float(credit)
    grade_sum+=level[grade]*float(credit)
if credit_sum!=0:
    print(f"{grade_sum/credit_sum:.6f}")
else:
    print(f"{0:.6f}")
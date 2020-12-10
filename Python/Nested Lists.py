#https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    n=5
    input1=["Harry","Berry","Tina","Akriti","Harsh"]
    input2=[37.21,37.21,37.2,41,39]

    grades=[]
    for i in range(int(5)):
        grades.append([input1[i],float(input2[i])])

    x=sorted(set([grade for name, grade in grades]))[1]
    print("\n".join([nm for nm in sorted([grade[0] for grade in grades for n in grade if n==x])]))
# Today small project of  a Total Marks Calculator 
Name=input("What is Your Name?\n")
print("========================")
print("Welcome",Name,"to my Grade Culculator.\n,lets Culculate your Marks Please insert your marks in Below Section of Your each Subject")
print("========================")
English= int(input("tell me the total marks of your English "))
English_obtained= int(input ("your obtained marks in English?"))
Chemistry= int(input("tell me the total marks of your Chemistry "))
Chemistry_obtained= int(input ("your obtained marks in Chemistry?"))
Biology= int(input("tell me the total marks of your Biology "))
Biology_obtained= int(input ("your obtained marks in Biology?"))
Physics= int(input("tell me the total marks of your Physics "))
Physics_obtained= int(input ("your obtained marks in Physics?"))
Maths= int(input ("total marks of Maths?"))
Maths_Obtained = int(input ("Obtained marks in Maths"))
Total_Marks= English + Chemistry+ Biology+ Physics+ Maths
Obtained_Marks= English_obtained + Chemistry_obtained + Biology_obtained + Physics_obtained + Maths_Obtained
print ("============================================")
print ("Hy" ,Name,"This is Your Result, Good luck")
print ("============================================")
print ("English =", English_obtained,"Out of ",English)
print ("English =", Chemistry_obtained,"Out of ",Chemistry)
print ("Biology =", Biology_obtained,"Out of ",Biology)
print ("Physics =", Physics_obtained,"Out of ",Physics)
print ("Maths =", Maths_Obtained,"Out of ",Maths)
print ("Your total Obtained Marks =", Obtained_Marks)
Percentage = Obtained_Marks/Total_Marks * 100
print ("Percentage =" ,Percentage,"%")
if Percentage >= 90:
    print ("A+ Grade")
elif Percentage >= 80 and Percentage <=89:
    print ("A Grade")
elif Percentage >= 70 and Percentage <=79:
    print ("B Grade")
else:
    print("fail")
print ("Thank You for Using My Calculator")
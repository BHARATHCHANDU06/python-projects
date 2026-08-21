#quiz game
print("Welcome")
score = 0
print(" 1.what is the capital of telangana.?")
print("a.hyderabad")
print("b.amaravathi")
print("c.rangaredddy")
print("d.sangareddy")
answer = input("Enter your answer (a/b/c/d): ").lower()
if answer == "a":
 score=score+1
 print("correct")
else:
 print("wrong")
print("2.what is the capital of india.?")
print("a.mumbai")
print("b.delhi")
print("c.hyderabad")
print("d.chennai")
answer = input("Enter your answer (a/b/c/d): ").lower()
if answer == "b":
 score=score+1
 print("correct")
else:
 print("wrong")
print("Quiz Completed!")
print("Your Score:", score, "/2")
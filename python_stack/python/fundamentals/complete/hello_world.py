# # 1. TASK: print "Hello World"
# print("1.")
# print("Hello World" )
# # 2. print "Hello Noelle!" with the name in a variable
# print("2.")
# name = "Noelle"
# print(f"Hello {name}")
# print("Hello",name)	# with a comma
# print("Hello "+name)	# with a +
# # 3. print "Hello 42!" with the number in a variable
# print("3.")
# name = 42
# print("Hello",{name})	# with a comma
# print("Hello " + {name})	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
print("4.")
fave_food1 = "sushi"
fave_food2 = "pizza"
print("{} {}".format(fave_food1,fave_food2)) # with .format()
print(f"{fave_food1} {fave_food2}") # with an f string
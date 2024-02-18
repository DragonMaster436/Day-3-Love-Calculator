# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
cobined_names = name1 + name2
lower_name = cobined_names.lower()


# Count occurrences of each letter in "true" for name1
count_t_name1 = lower_name.count('t')
count_r_name1 = lower_name.count('r')
count_u_name1 = lower_name.count('u')
count_e_name1 = lower_name.count('e')

# Count occurrences of each letter in "true" for name2
count_t_name2 = lower_name.count('l')
count_r_name2 = lower_name.count('o')
count_u_name2 = lower_name.count('v')
count_e_name2 = lower_name.count('e')

# Calculate the total score for each name
score_name1 = count_t_name1 + count_r_name1 + count_u_name1 + count_e_name1
score_name2 = count_t_name2 + count_r_name2 + count_u_name2 + count_e_name2


total = str(score_name1) + str(score_name2)
total_int = int(total)

if total_int <= 10 or total_int >= 90:
    print(f"Your score is {total_int}, you go together like coke and mentos.")
elif total_int >= 40 and total_int <= 50:
    print(f"Your score is {total_int}, you are alright together.")
else:
    print(f"Your score is {total_int}.")
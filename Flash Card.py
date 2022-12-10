'''
Game Discription
This game consists of 3 games
1. You we be shown flags of different countries and you have to guess the name of the country.
For the input purpose, you have to enter the name of city in the input box.
There will be two buttons:
	First one we will pass that if you don't know the answer you can simply pass and move to next flag.
	Second one will be submit button. If you click the second button and the answer is correct a message stating "correct" will be displayed else a message showing " incorrect" will be shown along with the correct answer.
2. You will be given the flag of a country and you have to guess the capital to that country.
	As guessing the capital name of a country is a difficult task you will be given 3 options and you have to choose from one of them. For this purpose we will need check boxes.

3. You will be given two numbers and you have to add the two numbers.
	The numbers given will be in form of images and you have to enter your answer in the entry box. If the answer is correct you have to show a correct message. Else you have to show a incorrect message with correct answer.
We will be using frames for the displaying different contents.
'''
from tkinter import *
from PIL import ImageTk, Image
from random import randint
import random

# Math Menu ===============================================================
# Create flashcard randomization
def math_random():
	#Generate a random number and call the image for that number. The name of the image is same as the number
	

# Create addition answer function
def answer_add():
	



# Create Addition Math Flashcard Function
def add():
	hide_all_frames()
	# Add frame fro addition deleting all previous frames
	add_frame.pack(fill="both", expand=1)
	add_label = Label(add_frame, text="Addition Flashcards", font=("Helvetica", 18)).pack(pady=15)
	# We add a new frame (pic frame inside our new frame)
	pic_frame = Frame(add_frame, width=600, height=600)
	pic_frame.pack()

	#Generate a random number
	global num_1
	global num_2
	num_1 = randint(1, 10)
	num_2 = randint(1, 10)

	# Create 3 labels inside our pic frame, frame
	global add_1
	global add_2
	add_1 = Label(pic_frame)
	add_2 = Label(pic_frame)
	math_sign = Label(pic_frame, text="+", font=("Helvetica", 28))
	# Grid our labels
	add_1.grid(row=0, column=0)
	math_sign.grid(row=0, column=1)
	add_2.grid(row=0, column=2)

	global add_image1
	global add_image2
	card1 = "flashcard/" + str(num_1) + ".jpg"
	card2 = "flashcard/" + str(num_2) + ".jpg"
	add_image1 = ImageTk.PhotoImage(Image.open(card1))
	add_image2 = ImageTk.PhotoImage(Image.open(card2))

	# Put flashcard images on the screen
	add_1.config(image=add_image1)
	add_2.config(image=add_image2)

	# Create answer box and button
	global add_answer
	add_answer = Entry(add_frame, font=("Helvetica", 18))
	add_answer.pack(pady=50)

	add_answer_button = Button(add_frame, text="Answer", command=answer_add)
	add_answer_button.pack()
	# Goto answer_add function
	# Displaying out answer after addition operation
	global answer_message
	answer_message = Label(add_frame, text="", font=("Helvetica", 18))
	answer_message.pack(pady=40)



# Create Radomizing country function
def random_country():
	#Create a list of country names
	





# Create answer function
def country_answer():
	answer = answer_input.get().title()
	# We need to convert the input to this format as our name of the falgs are in this format.
	
	# Determine if our answer is right or wrong!
	

	#Clear the entry box
	

# Create country Flashcard Function
def countries():
	# Hide previous frames
	
	# Show_country label coglobal show_country
	

	# Create answer input box
	


	# Create Button To Randomize country Images
	# This button generates a new flag see here we called the same function again rather than making a new function that generates a new flag.
	# Try substituting random
	rando_button = Button(country_frame, text="Pass", command=countries)
	rando_button.pack(pady=10)

	# Create a Button To Answer the Question
	answer_button = Button(country_frame, text="Answer", command=country_answer)
	answer_button.pack(pady=5)	

	# Create a Label To tell us if we got the answer right or not
	global answer_label
	answer_label = Label(country_frame, text="", font=("Helvetica", 18), bg="white")
	answer_label.pack(pady=15)

# Create country capital answers
def country_capital_answer():
	


# Create country Capital Flashcard Function
def country_capitals():
	# Hide previous frames
	hide_all_frames()
	country_capitals_frame.pack(fill="both", expand=1)
	#my_label = Label(country_capitals_frame, text="Capitals").pack()

	global show_country
	show_country = Label(country_capitals_frame)
	show_country.pack(pady=15)
	# Go through the Capitals text file to see the format
	global our_countries
	our_countries = open("Capitals.txt").read().splitlines()
    # Our_country_capitals is a dictionary that contains key as the country name and value as name of the capital of that country.
	global our_country_capitals
	our_country_capitals ={}
	# Adding the elements in the dictionary
	for i in our_countries:
		a = i.split('-')
		our_country_capitals[a[0].strip()] = a[1].strip()

	# Create empty answer list and counter
	answer_list = []
	count = 1
	global answer 

	# Generate our three random capitals and if last element is remaining we need to store the country name as that would be our answer.
	

		# Add our first selection to a new list
		answer_list.append(our_countries[rando])

		# Remove from old list
		our_countries.remove(our_countries[rando])

		#Shuffle original list
		random.shuffle(our_countries)
		count += 1
	for i in range(3):
		answer_list[i] = answer_list[i].split('-')[0].strip()
	random.shuffle(answer_list)
	print(answer_list)
	# Capital radio stores the value returned by the radio button.
	global capital_radio
	capital_radio = StringVar()
	capital_radio.set(our_country_capitals[answer_list[0]])
	
	# Add A Pass Button
	pass_button = Button(country_capitals_frame, text="Pass", command=country_capitals)
	pass_button.pack(pady=15)

	# Create a button to answer
	capital_answer_button = Button(country_capitals_frame, text="Answer", command=country_capital_answer)
	capital_answer_button.pack(pady=15)

	#Create an answer label
	global answer_label_capitals
	answer_label_capitals = Label(country_capitals_frame, text="", font=("helvetica", 18))
	answer_label_capitals.pack(pady=15)


# Hide all previous frames
def hide_all_frames():
	# Loop thru and destroy all children in previous frames
	for widget in country_frame.winfo_children():
		widget.destroy()
	
	for widget in country_capitals_frame.winfo_children():
		widget.destroy()

	for widget in add_frame.winfo_children():
		widget.destroy()

	add_frame.pack_forget()
	country_frame.pack_forget()
	country_capitals_frame.pack_forget()


root = Tk()
root.title('Flashcards!')
root.geometry("800x600")

# Create our menu


# Create Geography menu items


# Math Flashcard Menu
math_menu = Menu(my_menu)
my_menu.add_cascade(label="Math", menu=math_menu)
math_menu.add_command(label="Addition", command=add)
# Add more arithmetic operations here

# Create our Frames
country_frame = Frame(root, width=500, height=500, bg="white")
country_capitals_frame = Frame(root, width=500, height=500)
# Addition Frame
add_frame = Frame(root, width=500, height=500)
root.mainloop()

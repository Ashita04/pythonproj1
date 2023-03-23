while True:
	print("\nWELCOME TO PYSCOPE\nThis is a Program to know your Horoscope:\n")
	date = int(input("Enter your  birth date: \n"))
	if date > 31:
		print("Please enter the correct date. The date should not exceed 31\n")
		continue
	month = int(input("Enter your birthday month in number format ( for example 1 for January, 2 for February,..... and  12 for December ): \n"))
	if month > 12:
		print("Please enter the correct month. The month should not exceed 12\n")
		continue
	
	if month == 12:
		if (date < 22):
			sign = 'Sagittarius'
		else: 'Capricorn'
	elif month == 1:
		if (date < 20):
			sign = 'Capricorn'
		else: 'Aquarius'
	elif month == 2:
		if (date < 19):
			sign = 'Aquarius'
		else: 'Pisces'
	elif month == 3:
		if (date <=20):
			sign = 'Pisces'
		else: 'Aries'
	elif month == 4:
		if (date <=21):
			sign = 'Aries'
		else: 'Taurus'
	elif month == 5:
		if (date < 21):
			sign = 'Taurus'
		else: 'Gemini'
	elif month == 6:
		if (date < 21):
			sign = 'Gemini'
		else: 'Cancer'
	elif month == 7:
		if (date < 23):
			sign = 'Cancer'
		else: 'Leo'
	elif month == 8:
		if (date < 23):
			sign = 'Leo'
		else: 'Virgo'
	elif month == 9:
		if (date < 23):
			sign = 'Virgo'
		else: 'Libra'
	elif month == 10:
		if (date < 23):
			sign = 'Libra'
		else: 'Scorpio'
	elif month == 11:
		if (date < 22):
			sign = 'Scorpio'
		else: 'Sagittarius'
	print("\nYour Astrological sign is :",sign)

	user=input("\nDo you want to read your horoscope?\nEnter Y to read your scope and N to exit\n")

	if user=='Y':
		print("Here is your horoscope!!!!")

		if sign=="Sagittarius":
			print("\nCurious and energetic, you are the travelers of the zodiac.Your open mind and philosophical view motivates you to wander\n"
      "around the world in search of the meaning of life. Sagittarius is an extrovert, always optimistic, full of enthusiasm, and ready for changes\n"
      "This is a Sun sign of individuals who are often preoccupied with mental work, but when they find grounding\n"
       "they show their ability to transform visions and thoughts into concrete actions and circumstances.\n")
                                                    
		elif sign=='Capricorn':
			print("\nCapricorn is a sign that represents time and responsibility, and its representatives are traditional and often very serious by nature.\n"
       "These individuals possess an inner state of independence that enables significant progress both in their personal and professional lives.\n" 
       "You are masters of self-control and have the ability to lead the way, make solid and realistic plans,\n"
       "and manages many people who work for you at any time. You will learn from your mistakes and get to the top based solely on your experience and expertise.\n")
		elif sign == "Aquarius":
			print("\nAquarius is the sign different from the rest of the zodiac and people born with their Sun in it feel special. This makes you eccentric and energetic in your fight for freedom,\n"
      "or at times shy and quiet, afraid to express your true personality. In both cases you are deep thinker and highly intellectual people  love to fight for idealistic causes.\n" 
      "You are able to see people without prejudice and this makes you truly special. Although you can easily adapt to the energy that surrounds you,\n"
       "Aquarius representatives have a deep need to have some time alone and away from everything in order to restore power.\n")
		elif sign == "Pisces":
			print("\nPisces are very friendly and often find themselves in company of very different people. They are selfless and always willing to help others,\n"
         "a very fine intent for as long as they don’t expect anything much in return. People born with their Sun in Pisces have an intuitive understanding of the life cycle\n"
         "and form incredible emotional relationship with other humans on the basis of natural order and senses guiding them\n")
		elif sign == "Aries":
			print("\nAs the first sign in the zodiac, the presence of Aries always marks the beginning of something energetic and turbulent. You are continuously looking\n"
       "for dynamic, speed and competition, always being the first in everything - from work to social gatherings. Thanks to its ruling planet Mars and\n"
       "the fact it belongs to the element of Fire (just like Leo and Sagittarius),\n"
       "Aries is one of the most active zodiac signs. It is in your nature to take action, sometimes before you think about it\n")
		elif sign == "Taurus":
			print("\nPractical and well-grounded, Taurus is the sign that harvests the fruits of labor. You feel the need to always be surrounded by love and beauty,\n"
       "turned to the material world, hedonism, and physical pleasures. People born with their Sun in Taurus are sensual and tactile, considering touch and\n" 
        "taste the most important of all senses Stable and conservative,\n"
        "this is one of the most reliable signs of the zodiac, ready to endure and stick to their choices until they reach the point of personal satisfaction.\n")
		elif sign == "Gemini":
			print("\nExpressive and quick-witted, Gemini represents two different personalities in one and you will never be sure which one you will face. You are sociable, communicative\n"
		     "and ready for fun, with a tendency to suddenly get serious, thoughtful and restless. You are fascinated with the world itself, extremely curious, with a constant feeling\n"
			  "that there is not enough time to experience everything you want to see.\n")
		elif sign == "Cancer":
			print("\nDeeply intuitive and sentimental, Cancer can be one of the most challenging zodiac signs to get to know. You are very emotional and sensitive, and care deeply\n"
			 "about matters of the family and your home. Cancer is sympathetic and attached to people they keep close.\n" 
			 "Those born with their Sun in Cancer are very loyal and able to empathize with other people's pain and suffering.\n")
		elif sign == "Leo":
			print("\n People born under the sign of Leo are natural born leaders. You are dramatic, creative, self-confident, dominant and extremely difficult to resist,\n" 
			"able to achieve anything you want to in any area of life you commit to. There is a specific strength to a Leo and their king of the jungle status.\n" 
			"Leo often has many friends for they are generous and loyal. Self-confident and attractive, this is a Sun sign capable of uniting different groups of people and\n"
			"leading them as one towards a shared cause, and their healthy sense of humor makes collaboration with other people even easier.\n")
		elif sign == "Virgo":
			print("\nVirgos are always paying attention to the smallest details and their deep sense of humanity makes them one of the most careful signs of the zodiac.\n"
					"Your methodical approach to life ensures that nothing is left to chance, and although you are often tender, your heart might be closed for the outer world.\n" 
					"This is a sign often misunderstood, not because you lack the ability to express, but because you won’t accept your feelings as valid,\n"
					"true, or even relevant when opposed to reason. The symbolism behind the name speaks well of your nature,\n"
					 "born with a feeling you are experiencing everything for the first time.\n")
		elif sign == "Libra":
			print("\nPeople born under the sign of Libra are peaceful, fair, and you hate being alone. Partnership is very important for you, seeking someone with the ability\n"
			 "to be the mirror to yourself. These individuals are fascinated by balance and symmetry, they are in a constant chase for justice and equality, realizing through life that\n"
			 "the only thing that should be truly important to themselves in their own inner core of personality. You are someone ready to do nearly anything to avoid conflict,\n" 
			 "keeping the peace whenever possible\n")
		elif sign == "Scorpio":
			print("\nScorpios are passionate and assertive people with determination and focus you rarely see in other zodiac signs. You will turn to in-depth research to\n"
			 "reach the truth behind anything you find important. Great leaders and guides, Scorpios are resourceful, dedicated and fearless when there is challenge to be overcome.\n" 
			"You will hold on to other people’s secrets, even when you aren’t very fond of them to begin with and do anything you can for those you tie yourself to.\n")
	 

else:
	print("Invalid Input, Please enter the correct input.") 

            




    
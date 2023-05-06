travel=[]
places=[]
numchancepos=0
numchanceneg=0
symptoms=["fever", "constant tiredness", "dry cough", "aches and pains","nasal congestion", "runny nose", "sore throat", "diarrhoea"]
while True:
    print("You are about to start a questionnaire (related to COVID 19) that will provide you with advise as to what your next step should be in terms of testing.")

    print("Please enter either yes or no.")
    abroad=str(input("Have you travelled abroad a few months prior to now? "))
    while True:
        if abroad=="yes" or abroad=="no":
            break
        else:
            while True:
                print("Please enter either yes or no.")
                abroad=str(input("Have you travelled abroad a few months prior to now? "))
                validateabroad=abroad.lower()
                char=int(len(validateabroad))
                if (validateabroad=="yes" or validateabroad=="no") and (char==2 or char==3):
                    travel.append(validateabroad)
                    break

    print("Please enter either yes or no.")
    place=str(input("Have you been to any public gatherings or places where there are large groups of people in the last few weeks? "))        
    if place=="yes":
        location=str(input("Where have you gone? "))
        places.append(location)
    elif place=="no":
        print("Since you haven't travelled abroad or been to any public areas in the last few weeks, you are most likely to not test positive.\n\
        But, you are advised to observe yourself over time and look out for the symptoms that are mentioned above.\n")
        break
    else:
        while True:
            print("Please enter either yes or no.")
            place=str(input("Have you been to any public gatherings or places where there are large groups of people in the last few weeks? "))
            validateplace=place.lower()
            chars=int(len(validateplace))
            if (validateplace=="yes" or validateplace=="no" ) and (chars==2 or chars==3):
                if validateplace=="yes":
                    location=str(input("Where have you gone? "))
                    places.append(location)
                    break
                elif validateplace=="no":
                    print("Since you haven't travelled abroad or been to any public areas in the last few weeks, you are most likely to not test positive.\n\
                    But, you are advised to observe yourself over time and look out for the symptoms that are mentioned above.\n")
                    break
     
    print(symptoms)
    print("Please enter either yes or no.")
    answer=str(input("Do you experience any of the symptoms in the above list?"))
    if answer=="yes" or validateanswer=="yes":
        symptom=str(input("Enter any one of the symptoms you have."))
        while True:
            if symptom in symptoms:
                time=int(input("How many days have you been experiencing these symptoms for? "))
                if time>6:
                    print("We would advise you to visit a testing centre or contact medical professional.")
                    break
                else:
                    print("Keep monitoring yourself for symptoms. If the symptom(s) continues or you seem to become aware of more symptoms, you are advised to visit a testing centre or contact\n\
                    a medical profesional.\n")
                    break
            else:
                print("Your symptom is not an official symptom of COVID 19. If you become aware of any of the symptoms mentioned above, you are advised to visit a medical professional, or ")
                break
            
    elif answer=="no":
        print("Since you do not have any symptoms of COVID-19, you are advised that you don't leave your home and to stay away from areas of\n\
        public gatherings. If you do become aware of any of the symtoms mentioned above, you should visit a medical professional.\n")
        break
    else:
        while True:
            print(symptoms)
            print("Please enter either yes or no.")
            answer=str(input("Do you experience any of the symptoms in the above list? "))
            validateanswer=answer.lower()
            characters=int(len(validateanswer))
            if (validateanswer=="yes" or validateanswer=="no") and (characters==2 or characters==3):
                if validateanswer=="yes":
                    
                    numchancepos=numchancepos+1
                    break
                elif validateanswer=="no":
                    print("Since you do not have any symptoms of COVID-19, you are advised that you don't leave your home and to stay away from areas of\n\
                    public gatherings. If you do become aware of any of the symtoms mentioned above, you should visit a medical professional.\n")
                    numchanceneg=numberchanceneg+1
                    break
            
    


    
    Menu="Would you like to quit the program?\n\
    1.Yes\n\
    2.No\n"
    ToQuitOrNotToQuit=int(input(Menu))
    if ToQuitOrNotToQuit==1:
        break
                
   
menu="Would you like to know the number of people who have a chance of testing positive or negative?(ENTER AN OPTION)\n\
1. Positive\n\
2. Negative\n"
response=int(input(menu))
if response==1:
    print("The number of people who have a chance of testing positive: "+str(numchancepos))
elif response==2:
    print("The number of people who have a chance of testing negative: "+str(numchanceneg))
else:
    print("Please enter either 1 or 2.")
    response=int(input(menu))
print("The places they went to were " +str(places))

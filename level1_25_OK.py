import re
import time
print('Welcome to ALI BABA treasure')
player_1= input('please enter you name: ')
print('Hello', player_1, 'Please open you email immediately')
def intro(): 
    while True:
        try:
            print("Are you opened your email?[Yes/No]")
            open_1 = input('>>> ').lower()
            if open_1 == 'YES'.lower(): 
                print("That's good idea")
                print('Please find the unknown email!!!')
                print('If you find it, please open it')
                print('Are you open it?[Yes/No]')
                
            elif open_1 == 'No'.lower():
                print('**********Game Over**********')
                break
                
            elif open_1 != 'NO'.lower() or open_1 != 'YES'.lower():
                print('Invalid Input')
                continue

            find_1 = input(">>> ").lower()
            if find_1 == 'YES'.lower():
                print("Hello", player_1, "Please read the messeage carefully")
                print("There is ALI BABA treasure in Tongass forest in Alaska state.To get to it you have to take an adventure through the evil forest to reach it ")
                print(" Keep that in your mind, you can lost you life during this adventure and there is no way to back again.")
                print('to reach to the treasure please follow the instructions and answer the questions to survive. if you can not answer the questions, you will die')
                print('Are you accepted this adventure?[Yes/No]')
                
            elif find_1 == 'NO'.lower():
                print('**********Game Over**********')
                break
            elif find_1 != 'NO'.lower() or find_1 != 'YES'.lower():
                print('Invalid Input')
                continue  
            accept_1 = input('>>>').lower()
            if accept_1 == 'YES'.lower():
                print('I will send to you flight ticket from Des Moines to Ted Stevens Anchorage International airport! ')
                print('Please answer the folloing riddles to get it!')
                print('I make two people out of one.  What am I?')
            elif accept_1 == 'NO'.lower():
                print('**********Game Over**********')
                break
            elif accept_1 != 'NO'.lower() or accept_1 != 'YES'.lower():
                print('Invalid Input')
                continue
            ans_1 = input('>>>').lower()
            if ans_1 == 'A MIRROR'.lower():
                print('Right answer')
                
            else:
                print('Wrong Answer')
                print('**********************Start Again*************************')  
                continue
            print('I have two hands, but I can not scratch myself. What am I?')
            ans_2 = input('>>>').lower()
            if ans_2 == 'A CLOCK'.lower():
                print('Right answer')
                print('Your ticket has been sent')
                print('After 3 hours')
                time.sleep(3)
                level_2()
                break                        
            else:
                print('Wrong answer')
                print('**********************Start Again*************************')
                break
        except:
            print('Invalid Input111')
            


def level_2():
    while True: 
        try:
            time.sleep(2)
            print(player_1, 'Welcome in Des Moines airport')
            print(player_1, ' Please check you phone SMS')
            print('Did you open the unknown message?[Yes/No]')
            sms_2 = input('>>> ').lower()
            if sms_2 == 'YES'.lower():
                print('There is no way to turn back again... Good Luck')
                time.sleep(3)
                print('After 4 hours, the plane crashed ')
                print(player_1, "you got SMS say: answer the next question to get parachute to survive yourself")
                print('What has to be broken before it can be used?')
            elif sms_2 == 'NO'.lower():
                print('I will kill you after 1 hour... Bye Bye!')
                break
            elif sms_2 != 'NO'.lower() or sms_2 != 'YES'.lower():
                print('Invalid Input')
                continue
            ans_2_1 = input('>>> ').lower()
            if ans_2_1 == 'AN EGG'.lower():
                print('Right answer')
            else:
                print('Worng answer')
                print('The aircraft will destroy')
                print('GO TO HEAL')
                break
            print('Take off my skin and I won’t cry, but you will, what am I?')
            ans_2_2 = input('>>> ').lower()
            if ans_2_2 == 'ONION'.lower():
                print('Right answer')
                print('you will find the parachute under your seat')
                print('Get it and jump, right away')
                time.sleep(5)
                level_3()
                break
            else: 
                print('Wrong answer')
                print('The aircraft will destroy')
                continue
        except:
            print('Invalid input')

def level_3():
    while True:
        try:
            pattern_3= ['sun']
            print('You servived')
            print('You are in Tongass Forest')
            print(player_1, ' start walking to the east')
            print('How you can determine the east destination?')
            ans_3_1= input('>>> ').lower()
            for answer_3 in pattern_3:
                if re.search (answer_3, ans_3_1):
                    print("Thay's right, start walking now!")
                                      
                elif ans_3_1 != 'SUN'.lower():
                    print("That's wrong, please thinking again!")
                    exit()
                
            print('After 3 hours of walking')
            print(player_1, 'answer the next riddle to get some water to continue your trip')
            print('I have no feet, no hands, no wings, but I climb to the sky. What am I?')
            ans_3_2 = input('>>> ').lower()
           
            if ans_3_2 == 'SMOKE'.lower():
                print('Right answer')
                print('After 2 hours')
                print('You need to build a tent ')
                print('Answer the next riddle to get it...')
                print('What has a neck but no head?')

            else:
                print('Wrong answer')
                print('**********************Start Again*************************')
                continue
            ans_3_3 = input('>>> ').lower()
            if ans_3_3 == 'A BOTTLE'.lower():
                print('Right answer')
                print('You will find the tent after next tree')
                print('Build your tent and take some rest')
                level_4()
                break
            else:
                print('Wrong answer')
                print('**********************Start Again*************************')
                continue
        except:
            print('Invaild input')



def level_4():
    chance_4_1 = 3
    
    print('Good morning', player_1)
    print(player_1, 'Please walk again to the east diraction')
    print(player_1, 'How dare you come to Xing Tian Kingdom')
    print('to servive answer the next riddles')
    print("David's father has three sons : Snap, Crackle and _____")
    while chance_4_1 > 0 :
        ans_4_1 = input('>>> ').lower()
        if ans_4_1 == 'david':
            print('Right answer')
            print('you are not smart enough')
            que_2()
            break
        else:
            print('Wrong answer')
            chance_4_1 -= 1
            print('You have', chance_4_1,'chance')
            continue
            
    
def que_2():
    chance_4_2 = 3


    while chance_4_2 > 0 :
        print('What belongs to you, but other people use it more than you?')
        ans_4_2 = input('>>> ').lower()
        if ans_4_2 == 'my name':
            print('Right answer')
            print('you are not smart but not too much')
            que_3()
            break
        else:
            print('Wrong answer')
            chance_4_2 -= 1
            print('You have', chance_4_2,'chance')
            continue
def que_3():
    chance_4_3 = 3

    print('What goes up but never comes down?')
    while chance_4_3 > 0 :
        ans_4_3 = input('>>> ').lower()
        if ans_4_3 == 'age':
            print('Right answer')
            print('you are smart')
            print('You can walk in my kingdom')
            level_5()
            break
        else:
            print('Wrong answer')
            chance_4_3 -= 1
            print('You have', chance_4_3,'chance')
            continue
    

        

def level_5():
    while True:
        try:
            #player_1 = 'Simon'  
            print('After three days')
            print('According to the treasure map. Now, you are in Hundun Kingdom')
            print('Suddenly, appear small monster will bind', player_1,'to the Hundun King')
            print('Hundun said: I will kill you if you can not answer the following riddles!!')
            print('First riddle')
            print('You have three stoves: a gas stove, a wood stove, and a coal stove, but only one match. Which should you light first?')
            ans_5_1 = input('>>>').lower()
            if ans_5_1 == 'The match'.lower():
                print('Right answer')
                print('HHHHHHUUUUMMMMMMMM')
                
            else:
                print('Wrong answer')
                print('**********************Start again**********************')
                continue
            print('You bought me for dinner but never eat me. What am I?')
            ans_5_2 = input('>>> ').lower()
            if ans_5_2 == 'Cutlery'.lower():
                print('Right answer')
                print('HHHHHHHHHHHHHHHHHHHHHHHHHUUUUUUUUUUMMMMMMMMMMMMMM')
            else:
                print('Wrong answer')
                print('**********************Start again**********************')
                continue
            print('A grandmother, two mothers, and two daughters went to a baseball game together and bought one ticket each. How many tickets did they buy in total?')
            ans_5_3 = input('>>> ').lower()
            if ans_5_3 == '3 Tickets'.lower():
                print('Right answer')
                print('you are lucky, I will eat you next time!!!')
                level_6()
                break
            else:
                print('Wrong answer')
                print('**********************Start again**********************')
                continue
        except:
            print('Invalid input')


def level_6():
    while True:
        try:
              
            print(player_1, 'you need to get some energy to finish this adventure')
            print('to get the energy, you must answer the following riddles!!')
            print('What is full of holes but still holds water?')
            ans_6_1 = input('>>>').lower()
            if ans_6_1 == 'a sponge'.lower():
                print('Right answer')
                
                
            else:
                print('Wrong answer')
                print('**********************Start again**********************')
                continue
            print('I am a four letter word. I am an animal. You use me to call your dear ones. Who am I?')
            ans_6_2 = input('>>> ').lower()
            if ans_6_2 == 'deer'.lower():
                print('Good answer')
                
            else:
                print('Bad answer')
                print('**********************Start again**********************')
                continue
            print('I am a seven letter word. I am very heavy. Take away two letters from me and you will get 8. Take away one letter from me and you will get 80. Who am I?')
            ans_6_3 = input('>>> ').lower()
            if ans_6_3 == 'weight'.lower():
                print('Right answer')
                print('Please go to the next cave, you will find some food for you.')
                level_7()
                break
            else:
                print('Wrong answer')
                print('**********************Start again**********************')
                continue
        except:
            print('Invalid input')


def level_7():
    while True:
        try:
            
            pattern_7 = ['treasure'] 
            print(player_1, 'you are now in Vettala Kingdom')
            print(player_1,'take some rest')
            print('The small animal monster will appear in between the trees.')
            print(' The leader of monster said:',player_1,'you are in my kingdom')
            print('Why did you come here?')
            
            
            ans_7_1 = input('>>>').lower()
            for answer_7_1 in pattern_7:
                if re.search (answer_7_1, ans_7_1):
                    print("You are lucky because you not lied me")
                                      
                elif ans_7_1 != 'treasure'.lower():
                    print("You are liar, I will kill you")
                    exit()
            
            
            print('I come form North, East, West and South. I give you lots of information either verbally or textually. Who am I?')
            ans_7_2 = input('>>> ').lower()
            if ans_7_2 == 'news'.lower():
                print('Good answer')
                
            else:
                print('Bad answer')
                print('**********************Start again**********************')
                continue
            print('I cannot speak but I tell everything. I am not a tree but I have leaves. I have hinges but I am neither a door nor a window. Who am I?')
            ans_7_3 = input('>>> ').lower()
            if ans_7_3 == 'book'.lower():
                print('Right answer')
                print('HAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
                print('You are smart enough, you can stay in my land!!!')
                level_8()
                break
            else:
                print('Wrong answer')
                print('**********************Start again**********************')
                continue
        except:
            print('Invalid input')


def level_8():
    while True:
        try:
              
            print(player_1, 'start to walk inside Vettala land for 3 hours to the east direction')
            print(player_1,'Welcome to cannibal tribe')
            print('Welcome to Azi Dahaka land')
            print('Some of the inhabitants of the tribe arrested', player_1,'and took him to the leader' )
            print('leader said "Hello"', player_1,'welcome to Azi Dahaka land')
            print('I know why you are here!! to many people came here before you but unfortunately they were not smart enough to pass from my land')
            print('I will ask you three questions! if you answer the questions i will let you go! if not you know what i will do!!')
            print('I will eat you!!!!')
            print(player_1,' bought a big bag of candy. The bag had 102 blue candies, 100 red candies and 94 green candies. How many candies were there in total?')
            ans_8_1 = input('>>>').lower()
            if ans_8_1 == '314'.lower():
                print('Right answer')
                
                
            else:
                print('Wrong answer')
                print('**********************Start again**********************')
                continue
            print(player_1,' has 100 pieces of gum to share with her friends. When she went to the park, she shared 10 pieces of strawberry gum. When she left the park, Adrianna shared another 10 pieces of bubble gum. How many pieces of gum does Adrianna have now?')
            ans_8_2 = input('>>> ').lower()
            if ans_8_2 == '80'.lower():
                print('Good answer')
                
            else:
                print('Bad answer')
                print('**********************Start again**********************')
                continue
            print(player_1,'store normally sells 12,576 trading cards per month. In July, the hobby store sold a total of 21,777 trading cards. How many more trading cards did the hobby store sell in July compared with a normal month?')
            ans_8_3 = input('>>> ').lower()
            if ans_8_3 == '9201'.lower():
                print('Right answer')
                print('You are smart!!! you are lucky !!! ')
                print(player_1,'go and do not come here again!!')
                level_9()
                break
            else:
                print('Wrong answer')
                print('**********************Start again**********************')
                continue
        except:
            print('Invalid input')

def level_9():
    while True:
        try:
              
            print(player_1,'you have long trip. you need to get hourse from the leader')
            print(player_1,'said: before i leave can i get hourse from you beacsue i have long long trip')
            print('HHHHHHHMMMMMMMMMM')
            print('OK..... but that will not be free' )
            print('you need to answer the another 3 questions to get it.... if not i will kill you')
            print(player_1,"OK... I'm ready")
            
            print(player_1,'A merchant can place 8 large boxes or 10 small boxes into a carton for shipping. In one shipment, he sent a total of 96 boxes. If there are more large boxes than small boxes, how many cartons did he ship?')
            ans_9_1 = input('>>> ').lower()
            if ans_9_1 == '11'.lower():
                print('Right answer')
                
                
            else:
                print('Wrong answer')
                print('**********************Start again**********************')
                continue
            print(player_1,'You saw me where I could not be. Yet, often you see me. What am I? ')
            ans_9_2 = input('>>> ').lower()
            if ans_9_2 == 'reflection'.lower():
                print('Good answer')
                
            else:
                print('Bad answer')
                print('**********************Start again**********************')
                continue
            print(player_1,'What is so delicate that saying its name breaks it?')
            ans_9_3 = input('>>> ').lower()
            if ans_9_3 == 'silence'.lower():
                print('Right answer')
                print('You are smart!!! you can get what you want!!! ')
                level_10()
                
                break
            else:
                print('Wrong answer')
                print('**********************Start again**********************')
                continue
        except:
            print('Invalid input')

def level_10():
    while True:
        try:
              
            print(player_1,'Ride the horse until you reach the kingdom of Pishacha ')
            print('___________________________________________________________________________________________________')
            print('**********Pishacha**********')
            print("Pishacha like darkness and traditionally are depicted as haunting cremation grounds along with other monsters like bhutas and vetālas. Piśācas have the power to assume different forms at will, and may also become invisible. They feed on human energies. Sometimes, they possess human beings and alter their thoughts, and the victims are afflicted with a variety of maladies and abnormalities like insanity. Certain mantras are supposed to cure such afflicted persons and drive away the Piśāca which may be possessing that particular human being. In order to keep the Piśāca away, they are given their share of offerings during certain religious functions and festivals.")
            print('___________________________________________________________________________________________________')
            print(player_1,'going to Pishacha castle and asked him there is anyway to go through his kingdom')
            print(player_1, 'reach to the castle')
            print('Pishacha king ask: who are you?')
            print('I am', player_1 )
            print('Pishacha king said; why you are here?')
            print(player_1,"I want go through your kingdom")
            print('HHHHHHHHAAAAAAAAAAAA')
            print('to do that, you must asnwer my question, if you can not, I do not let you pass on my land ')
            print(player_1,'Only one color, but not one size,Stuck at the bottom, yet easily flies.Present in sun, but not in rain,Doing no harm, and feeling no pain.')
            print('What is it?')
            ans_10_1 = input('>>> ').lower()
            if ans_10_1 == 'Shadow'.lower():
                print('Right answer')
                
                
                
            else:
                print('Wrong answer')
                print('**********************Start again**********************')
                continue
            print(player_1,'Who is that with a neck and no head, two arms and no hands?')
            
            ans_10_2 = input('>>> ').lower()
            if ans_10_2 == 'A shirt'.lower():
                print('Good answer')
                
            else:
                print('Bad answer')
                print('**********************Start again**********************')
                continue
            print(player_1,"It can't be seen, can't be felt, can't be heard and can't be smelt. It lies behind stars and under hills, and empty holes it fills. It comes first and follows after, ends life and kills laughter. What is it?")
                        
            ans_10_3 = input('>>> ').lower()
            if ans_10_3 == 'Dark'.lower():
                print('Right answer')
                print('You are smart!!! you can go through my land!!! ')
                level_11()
                break
            else:
                print('Wrong answer')
                print('**********************Start again**********************')
                continue
        except:
            print('Invalid input')

def level_11():
    while True:
        try:
            
            print('Congratulations!!! you have exceeded the first ten levels.')
            print('The next task will be very difficult to solve.')
            print('So please take care of your life.')
            print(player_1, 'ride your hours to the east diraction')
            print(player_1,'you are now in Gojoseon Kingdom.... take care!!')
            print('______________________________________________________________________________________________')
            print('********Gijoseon**********')
            print("According to the Samguk Yusa (1281), Gojoseon was established in 2333 BC by Dangun, who was said to be the offspring of a heavenly prince and a bear-woman. Though Dangun is a mythological figure for whom no concrete evidence has been found,[1] the account has played an important role in developing Korean identity. Today, the founding date of Gojoseon is officially celebrated as the National Foundation Day in North Korea[2] and South Korea.")
            print('______________________________________________________________________________________________')
            print("HEELLOOOOOOOOOO",player_1)
            print('Welcome to Gojoseon Kingdom')
            print ('Gojoseon King said; I know why you are here !!!')
            print('HHHHHHHHAAAAAAAAAAAA')
            print('Keep in mind that the next kingdoms will be very difficult to pass')
            print('Unfortunately, there is no way to return again ')
            print('you must answer my questions to stay alive')
            print(player_1,'What letter must appear on the beginning of the registration number of all non-military aircraft in the US?')
            ans_11_1 = input('>>> ').lower()
            if ans_11_1 == 'n'.lower():
                print('Right answer')
                print('The letter ... N must be on all non-military aircrafts in the US.')
                
                
            else:
                print('Wrong answer')
                print('**********************Start again**********************')
                continue
            print(player_1,'According to the Population Reference Bureau, what is the approximate number of people who have ever lived on earth?')
            print('50 Billion  -  100 Billion  -  1 Trillion  -  5 Trillion')
            ans_11_2 = input('>>> ').lower()
            if ans_11_2 == '100 Billion'.lower():
                print('Good answer')
                
            else:
                print('Bad answer')
                print('**********************Start again**********************')
                continue
            print(player_1,"Khrushchev's famous 1960 shoe-banging outburst at the UN was in response to a delegate from what nation?")
            print('Australia  -  The Netherlands  -  The Philippines  -  Turkey')
            ans_11_3 = input('>>> ').lower()
            if ans_11_3 == 'The Philippines'.lower():
                print('Right answer')
                print('You are smart!!! you can go through my land!!! ')
                level_12()
                break
            else:
                print('Wrong answer')
                print('**********************Start again**********************')
                continue
        except:
            print('Invalid input')

def level_12():
    while True:
        try:
                       
            print(player_1, 'ride your horse to the Shang Kingdom')
            print(player_1,'you are now in Shang Kingdom')
            print(player_1,'Please take care')
            print('Welcome to Shang Kingdom')
            print('______________________________________________________________________________________________')
            print('**********Shang**********')
            print("The Shang dynasty is the earliest dynasty of traditional Chinese history firmly supported by archaeological evidence. Excavation at the Ruins of Yin (near modern-day Anyang), which has been identified as the last Shang capital, uncovered eleven major royal tombs and the foundations of palaces and ritual sites, containing weapons of war and remains from both animal and human sacrifices. Tens of thousands of bronze, jade, stone, bone, and ceramic artifacts have been found.")
            print('______________________________________________________________________________________________')
            print('HHHHHHHHAAAAAAAAAAAA')
            print ('Shang King said; Are you smart enough to get here .... we will see')
            print('you must answer my questions to stay alive')
            print(player_1,'Which of these US presidents appeared on the television series "Laugh-In?"')
            print('Lyndon Johnson  -   Richard Nixon  -  Jimmy Carter  -  Gerald Ford')
            ans_12_1 = input('>>> ').lower()
            if ans_12_1 == 'Richard Nixon'.lower():
                print('Right answer')
                print('Nixon appeared on the comedy show while he was on the campaign trail in 1968.')
                
                
            else:
                print('Wrong answer')
                print('**********************Start again**********************')
                continue
            print(player_1,'The Earth is approximately how many miles away from the Sun?')
            print('9.3 million  -  39 million  -  93 million  -  193 million')
            ans_12_2 = input('>>> ').lower()
            if ans_12_2 == '93 million'.lower():
                print('Good answer')
                print('The Earth is approximately ... 93 million miles away from the Sun.')
                
            else:
                print('Bad answer')
                print('**********************Start again**********************')
                continue
            print(player_1,"Which insect shorted out an early supercomputer and inspired the term “computer bug?”")
            print('Moth  -  Roach  -  Fly  -  Japanese beetle')
            ans_12_3 = input('>>> ').lower()
            if ans_12_3 == 'Moth'.lower():
                print('Right answer')
                print('moth was found inside the computer of scientist Grace Hopper.')
                print('You are smart enouygh to go through my land!!! ')
                level_13()
                break
            else:
                print('Wrong answer')
                print('**********************Start again**********************')
                continue
        except:
            print('Invalid input')

def level_13():
    while True:
        try:
              
            
            print(player_1, 'Start to walk to the next kingdom')
            print(player_1,'take the east direction')
            print(player_1,'Please take care')
            print('NOT Welcome to Urartu  land')
            print('______________________________________________________________________________________________')
            print('**********Urartu**********')
            print("Urartu comprised an area of approximately 200,000 square miles (520,000 km2), extending from the Euphrates in the West to Lake Urmia in the East and from the Caucasus Mountains south towards the Zagros Mountains in northern Iraq. It was centered around Lake Van, which is located in present-day eastern Anatolia.")
            print('______________________________________________________________________________________________')
            print('MONSTER LAND!!')
            print ('Take care!!! a lot of monster around you, but you did not see them')
            print('to save your life, you should answer the next questions')
            print(player_1,'Which of the following landlocked countries is entirely contained within another country?')
            print('Lesotho  -   Burkina Faso  -  Mongolia  -  Luxembourg')
            ans_13_1 = input('>>> ').lower()
            if ans_13_1 == 'Lesotho'.lower():
                print('Right answer')
                print('Lesotho is completely surrounded by South Africa.')
                
                
            else:
                print('Wrong answer')
                print('**********************Start again**********************')
                continue
            print(player_1,'In the children’s book series, where is Paddington Bear originally from?')
            print('India  -  Peru  -  Canada  -  Iceland')
            ans_13_2 = input('>>> ').lower()
            if ans_13_2 == 'Peru'.lower():
                print('Good answer')
                print('Paddington is ... Peruvian.')
                
            else:
                print('Bad answer')
                print('**********************Start again**********************')
                continue
            print(player_1,"Who is credited with inventing the first mass-produced helicopter?")
            print('Gottlieb Daimler  -  Ferdinand von Zeppelin  -  Elmer Sperry  -  Igor Sikorsky')
            ans_13_3 = input('>>> ').lower()
            if ans_13_3 == 'Igor Sikorsky'.lower():
                print('Right answer')
                print('The first mass-produced helicopter was invented by ... Igor Sikorsky.')
                print('You are smart enouygh to go through our land!!! ')
                level_14()
                break
            else:
                print('Wrong answer')
                print('**********************Start again**********************')
                continue
        except:
            print('Invalid input')

def level_14():
    while True:
        try:
            
            
            print(player_1, 'go out of Phillista land NOW!!!')
            print(player_1,'run to the east direction')
            print(player_1,'Please take care')
            print('you are going to Ammon kigdom')
            print('______________________________________________________________________________________________')
            print('**********Ammon**********')
            print("Ammon maintained its independence from the Neo-Assyrian Empire through tribute to the Assyrian king, at a time when nearby kingdoms were being raided or conquered. The Kurkh Monolith lists the Ammonite king Baasha ben Ruhubi's army as fighting alongside Ahab of Israel and Syrian allies against Shalmaneser III at the Battle of Qarqar in 853 BC, possibly as vassals of Hadadezer, the Aramaean king of Damascus. In 734 BC the Ammonite king Sanipu was a vassal of Tiglath-Pileser III, and Sanipu's successor Pudu-ilu held the same position under Sennacherib and Esarhaddon. An Assyrian tribute-list exists from this period, showing that Ammon paid one-fifth as much tribute as Judah did.")
            print('______________________________________________________________________________________________')
            print('Welcome to Ammon Kigdom')
            print ('we are peaceful land, but you need to answer our questions to pass through our land')
            print('or you will saty with us forever')
            print(player_1,'During World War II, US soldiers used the first commercial aerosol cans to hold what?')
            print('Cleaning fluid  -  Antiseptic  -  Insecticide  -  Shaving cream')
            ans_14_1 = input('>>> ').lower()
            if ans_14_1 == 'Insecticide'.lower():
                print('Right answer')
                print('The first aerosol cans held ... insecticide.')
                
                
            else:
                print('Wrong answer')
                print('**********************Start again**********************')
                continue
            print(player_1,'The US icon Uncle Sam was based on Samuel Wilson who worked during the War of 1812 as a what?')
            print('Meat inspector  -  Mail deliverer  -  Historian  -  Weapons mechanic')
            ans_14_2 = input('>>> ').lower()
            if ans_14_2 == 'Meat inspector'.lower():
                print('Good answer')
                print('The real Uncle Sam was a ... meat inspector.')
                
            else:
                print('Bad answer')
                print('**********************Start again**********************')
                continue
            print(player_1,"Who did artist Grant Wood use as the model for the farmer in his classic painting 'American Gothic?'")
            print('Traveling salesman  -  Local sheriff  -  His dentist  -  His butcher')
            ans_14_3 = input('>>> ').lower()
            if ans_14_3 == 'His dentist'.lower():
                print('Right answer')
                print("The man in 'American Gothic' is based off of Wood's ... dentist.")
                print('You are smart enouygh to go through our land!!! ')
                level_15()
                break
            else:
                print('Wrong answer')
                print('**********************Start again**********************')
                continue
        except:
            print('Invalid input')

def level_15():
    while True:
        try:
             
            
            print(player_1, 'Continue your journey to Juda kingdom')
            print(player_1,'walk to the east direction')
            print(player_1,'Please be careful ')
            
            print('______________________________________________________________________________________________')
            print('**********Juda Kingdom**********')
            print("For the first sixty years, the kings of Judah tried to re-establish their authority over the northern kingdom, and there was perpetual war between them. Israel and Judah were in a state of war throughout Rehoboam's seventeen-year reign. Rehoboam built elaborate defenses and strongholds, along with fortified cities. In the fifth year of Rehoboam's reign, Shishak, pharaoh of Egypt, brought a huge army and took many cities. In the sack of Jerusalem (10th century BCE), Rehoboam gave them all of the treasures out of the temple as a tribute and Judah became a vassal state of Egypt.")
            print('______________________________________________________________________________________________')
            print('Welcome to Juda Kigdom')
            print ('Hello', player_1,'you are in Juda Kingdom')
            print("please don't be afraid, just answer the next three questions and i will let you go in peace")
            print(player_1,'Now used to refer to a cat, the word "tabby" is derived from the name of a district of what world capital?')
            print('Baghdad  -  New Delhi  -  Cairo  -  Moscow')
            ans_15_1 = input('>>> ').lower()
            if ans_15_1 == 'Baghdad'.lower():
                print('Right answer')
                print('Tabby is derived from ... the capital of Iraq, Baghdad.')
                print('The word evolved from the word "attabi," which was the name of a specific type of silk cloth made in Baghdad, according to Deseret News.')
                
                
            else:
                print('Wrong answer')
                print('**********************Start again**********************')
                continue
            print(player_1,"Neurologists believe that the brain's medial ventral prefrontal cortex is activated when you do what?")
            print(" Have a panic attack  -  Remember a name  -  Get a joke  -  Listen to music")
            ans_15_2 = input('>>> ').lower()
            if ans_15_2 == 'Get a joke'.lower():
                print('Good answer')
                print('The prefrontal cortex is activated when you ... get a joke.')
                print('According to The Science of Psychotherapy, "[the prefrontal cortex] has been implicated in planning complex cognitive behavior, personality expression, decision making, and moderating social behavior."')
                
            else:
                print('Bad answer')
                print('**********************Start again**********************')
                continue
            print(player_1,"Compiled by Benjamin Franklin in 1737, The Drinkers Dictionary included all but which of these synonyms for drunkenness?")
            print('Nimptopsical  -  Buzzey  -  Pifflicated  -  Staggerish')
            ans_15_3 = input('>>> ').lower()
            if ans_15_3 == 'Pifflicated'.lower():
                print('Right answer')
                print("Pifflicated does mean drunk, but Franklin didn't include it in his book.")
                print('You are smart enough ... you can go in peace ')
                level_16()
                break
            else:
                print('Wrong answer')
                print('**********************Start again**********************')
                continue
        except:
            print('Invalid input')

def level_16():
    while True:
        try:
             
            print(player_1, "please get camel from Juda land")
            print(player_1, 'Continue your journey to Twipra Kingdom ')
            print(player_1,'ride the camel to the east direction')
            
            
            print('______________________________________________________________________________________________')
            print('**********Twipra Kingdom**********')
            print("The Twipra Kingdom was established around the confluence of the Brahmaputra river (Twima[clarification needed]) with the Meghna and Surma rivers in today's Central Bangladesh area. The capital was called Khorongma (Kholongma) and was along the Meghna river in the Sylhet Division of present-day Bangladesh.")
            print('______________________________________________________________________________________________')
            print('Welcome to Twipra Kigdom')
            
            print(player_1,"answer the next questions or We will imprison you")
            print(player_1,'What club did astronaut Alan Shepard use to make his famous golf shot on the moon?')
            print('Nine iron  -  Sand wedge  -  Six iron  -  Seven iron')
            ans_16_1 = input('>>> ').lower()
            if ans_16_1 == 'Six iron'.lower():
                print('Right answer')
                print("Apollo 14 astronaut Alan Shepard, who hit three golf balls while on the moon, conducts an experiment near a lunar crater.")
                
                
            else:
                print('Wrong answer')
                print('**********************Start again**********************')
                continue
            print(player_1,"Famous pediatrician and author Dr. Benjamin Spock won an Olympic gold medal in what sport?")
            print("Swimming  -  Rowing  -  Fencing  -  Sailing")
            ans_16_2 = input('>>> ').lower()
            if ans_16_2 == 'Rowing'.lower():
                print('Good answer')
                print('Dr. Benjamin Spock, a member of the 1924 Yale Olympic gold medal crew, on June 2, 1978.')
                print('Spock was on the eight-man American team that won the gold medal at the 1924 Paris Olympics.')
                
            else:
                print('Bad answer')
                print('**********************Start again**********************')
                continue
            print(player_1,"How many days make up a non-leap year in the Islamic calendar?")
            print('365  -  400  - 354  -  376')
            ans_16_3 = input('>>> ').lower()
            if ans_16_3 == '354'.lower():
                print('Right answer')
                print("The Islamic calendar has ... 354 days.")
                print('The Islamic calendar has 11 less days than the widely-used Gregorian calendar, which has 365 days in a non-leap year.')
                print('You are smart')
                print('you can do what you want!!!')
                level_17()
                break
            else:
                print('Wrong answer')
                print('**********************Start again**********************')
                continue
        except:
            print('Invalid input')

def level_17():
    while True:
        try:
              
            print(player_1, "please leave the camel and run to the east direction")
            print(player_1, 'after 2 hours, you will find Kingdom of Pontus ')
            print(player_1,"take care!!! this empire is very dangerous")
                        
            print('______________________________________________________________________________________________')
            print('**********Pontus Kingdom**********')
            print("The Kingdom of Pontus or Pontic Empire was a Hellenistic-era kingdom, centered in the historical region of Pontus and ruled by the Mithridatic dynasty of Persian origin, which may have been directly related to Darius the Great and the Achaemenid dynasty.The kingdom was proclaimed by Mithridates I in 281 BCE and lasted until its conquest by the Roman Republic in 63 BCE")
            print('______________________________________________________________________________________________')
            print('Welcome to Pontus Kigdom')
            
            print(player_1,"You are in the extremely dangerous land to survive, you must answer the following questions")
            print(player_1,'What scientist first determined that human sight results from images projected onto the retina?')
            print('Galileo  -  Copernicus  -  Johannes Kepler  -  Isaac Newton')
            ans_17_1 = input('>>> ').lower()
            if ans_17_1 == 'Johannes Kepler'.lower():
                print('Right answer')
                print("Kepler offered the first retinal theory in 1604.")
                
                
            else:
                print('Wrong answer')
                print('**********************Start again**********************')
                continue
            print(player_1,"Which king was married to Eleanor of Aquitaine?")
            print("Henry I  -  Henry II  -  Richard I  -  Henry V")
            ans_17_2 = input('>>> ').lower()
            if ans_17_2 == 'Henry II'.lower():
                print('Good answer')
                print("Eleanor of Aquitaine's husband was ... King Henry II.")
                print("The two were together for 14 years, before Eleanor left due to Henry's multiple infidelities.")
                
            else:
                print('Bad answer')
                print('**********************Start again**********************')
                continue
            print(player_1,"If you planted the seeds of Quercus robur, what would grow?")
            print('Trees  -  Flowers  -  Vegetables  -  Grain')
            ans_17_3 = input('>>> ').lower()
            if ans_17_3 == 'Trees'.lower():
                print('Right answer')
                print("Those seeds would produce ... oak trees.")
                print("According to the Encyclopedia Britannica, there are about 450 species of trees and shrubs considered to be oaks")
                print('You are smart')
                print('you can go NOW!!!')
                level_18()
                break
            else:
                print('Wrong answer')
                print('**********************Start again**********************')
                continue
        except:
            print('Invalid input')


def level_18():
    while True:
        try:
             
            print(player_1, "please find anyway to reach to Nanyue Kingdom")
            print(player_1, 'When you arrive at the kingdom of Nanyue, please make sure that your answers are correct so that you do not die ')
            print(player_1,"be careful")
                        
            print('______________________________________________________________________________________________')
            print('**********Nanyue Kingdom**********')
            print("Nanyue  was an ancient kingdom that covered parts of northern Vietnam and the modern Chinese provinces of Guangdong, Guangxi, and Yunnan. Nanyue was established in 204 BC after the collapse of the Qin dynasty by Zhao Tuo, then Commander of Nanhai. At first, it consisted of the commanderies Nanhai, Guilin, and Xiang.")
            print('______________________________________________________________________________________________')
            print('Welcome to Nanyue Kigdom')
            
            print(player_1,'Which scientific unit is named after an Italian nobleman?')
            print('Pascal  -  Ohm  -  Volt  -  Hertz')
            ans_18_1 = input('>>> ').lower()
            if ans_18_1 == 'Volt'.lower():
                print('Right answer')
                print("The volt is named after scientist Alessandro Volta, who invented the first electrical battery in 1800.")
                
                
            else:
                print('Wrong answer')
                print('**********************Start again**********************')
                continue
            print(player_1,"Which of these is not one of the American Triple Crown horse races?")
            print("Arlington Million  -  Belmont Stakes  -  Kentucky Derby  -  Preakness Stakes")
            ans_18_2 = input('>>> ').lower()
            if ans_18_2 == 'Arlington Million'.lower():
                print('Good answer')
                print("The only race not to be part of the Triple Crown is ... the Arlington Million.")
                print("The Arlington Million is held at Arlington Park, in Arlington Heights, Illinois.")
                
            else:
                print('Wrong Answer')
                print('**********************Start again**********************')
                continue
            print(player_1,"'Nephelococcygia' is the practice of doing what?")
            print('Finding shapes in clouds  -  Sleeping with your eyes open  -  Breaking glass with your voice  -  Swimming in freezing water')
            ans_18_3 = input('>>> ').lower()
            if ans_18_3 == 'Finding shapes in clouds'.lower():
                print('Right answer')
                print("Nephelococcygia is a term used when people find familiar objects within the shape of a cloud. The word comes from the play 'The Birds' by the Greek playwright Aristophanes.")
                print(player_1,'you are smart')
                level_19()
                break
            else:
                print('Wrong answer')
                print('**********************Start again**********************')
                continue
        except:
            print('Invalid input')


def level_19():
    while True:
        try:
            
            print(player_1, "go to Hasmonean kingdom")
            print(player_1, 'When you arrive there,ask to meet the king and ask him to let you go through his land ')
            print(player_1,"be careful")
                        
            print('______________________________________________________________________________________________')
            print('**********Hasmonean Kingdom**********')
            print("The Hasmonean dynasty was a ruling dynasty of Judea and surrounding regions during classical antiquity. Between c. 140 and c. 116 BCE the dynasty ruled Judea semi-autonomously from the Seleucids. From 110 BCE, with the Seleucid Empire disintegrating, the dynasty became fully independent, expanded into the neighbouring regions of Samaria, Galilee, Iturea, Perea, and Idumea, and took the title 'basileus'. Some modern scholars refer to this period as an independent kingdom of Israel.")
            print('______________________________________________________________________________________________')
            print('Welcome to Hasmonean Kigdom')
            print(player_1,"I'm king of Hasmonean, I'll ask you some questions to let you go in peace")
            print(player_1,'How many different combinations of dots are possible in Braille?')
            print('49  -  63  -  75  -  87')
            ans_19_1 = input('>>> ').lower()
            if ans_19_1 == '63'.lower():
                print('Right answer')
                print("A six-dot Braille cell allows 63 possible combinations of dots. This might sound like plenty -- after all, the Latin alphabet as used in English has only 26 letters, and you can represent any real number with the numerals 0 through 9.")
                
                
            else:
                print('Wrong answer')
                print('**********************Start again**********************')
                continue
            print(player_1,"Which former NBA player was infamously selected right before Michael Jordan in the 1984 NBA Draft?")
            print("Sam Johns  -  Sam Walton  -  Sam Bowie  -  Sam Berns")
            ans_19_2 = input('>>> ').lower()
            if ans_19_2 == 'Sam Bowie'.lower():
                print('Good answer')
                print(" At that time, the Portland Trailblazers, who had the second pick in the 1984 NBA Draft, already had a couple of outstanding shooting guards and thus chose center Sam Bowie over Michael Jordan, whom the Chicago Bulls selected with the third pick. Bowie ultimately went on to earn the reputation of being a draft bust.")
                
                
            else:
                print('Wrong Answer')
                print('**********************Start again**********************')
                continue
            print(player_1,"When was the last time the US hosted the World Cup?")
            print('1994  -  1990  -  1986  -  1982')
            ans_19_3 = input('>>> ').lower()
            if ans_19_3 == '1994'.lower():
                print('Right answer')
                print("he United States hosted the 1994 FIFA World Cup and unsuccessful to host in 2022 World Cup,")
                print(player_1,'you are smart')
                level_20()
                break
            else:
                print('Wrong answer')
                print('**********************Start again**********************')
                continue
        except:
            print('Invalid input')


def level_20():
    
    chance_20_1 = 3
    
    print(player_1,"You have 5 missions to reach the treasure")
    print('These missions will focus on Egypt information')
    print(player_1, 'you have only 3 chances to answer each question, if you can not you will die and the game will end')
    print(player_1,"start again and run to the east")
    print("the next mission is called Ancient Egypt ")
    print('______________________________________________________________________________________________')
    print('**********Ancient Egypt**********')
    print("Egypt is a country in North Africa, on the Mediterranean Sea, and is home to one of the oldest civilizations on earth. The name 'Egypt' comes from the Greek Aegyptos which was the Greek pronunciation of the ancient Egyptian name 'Hwt-Ka-Ptah' 'Mansion of the Spirit of Ptah', originally the name of the city of Memphis. Memphis was the first capital of Egypt and a famous religious and trade center; its high status is attested to by the Greeks alluding to the entire country by that name.")
    print('______________________________________________________________________________________________')
    print('Welcome to Ancient Egypt')
    print("What is the first king the pharaohs")
    print('Tutankhamun  -  Ramesses I  -  Narmer  -  Akhenaten')
    while chance_20_1 > 0 :
        ans_20_1 = input('>>> ').lower()
        if ans_20_1 == 'Narmer'.lower():
            print('Right answer')
            print('The first true pharaoh of Egypt was Narmer (sometimes called Menes), who united Lower Egypt and Upper Egypt. He was the first king of the First Dynasty, the beginning of the Old Kingdom.')
            print('you are not smart enough')
            que_20_2()
            break
        else:
            print('Wrong answer')
            chance_20_1 -= 1
            print('You have', chance_20_1,'chance')
            continue
            
    
def que_20_2():
    chance_20_2 = 3


    while chance_20_2 > 0 :
        print('How many stones are in the Great Pyramid?')
        print('1.3 million  -  2.3 million  -  3 million  - 1 million')
        ans_20_2 = input('>>> ').lower()
        if ans_20_2 == '2.3 million'.lower():
            print('Right answer')
            print('The exact number of stones was orginally estimated at 2,300,000 stone blocks weighing from 2-30 tons each with some weighing as much as 70 tons. Computer calculations indicate 590,712 stone blocks were used in its construction. It area covers 13.6 acres with each side greater than 5 acres in area.')
            que_20_3()
            break
        else:
            print('Wrong answer')
            chance_20_2 -= 1
            print('You have', chance_20_2,'chance')
            continue
def que_20_3():
    chance_20_3 = 3

    print('What is the second largest pyramid in Egypt?')
    print('Khufu  -  Khafra  -  Menkaure  -  sphinx')
    while chance_20_3 > 0 :
        ans_20_3 = input('>>> ').lower()
        if ans_20_3 == 'Khafra'.lower():
            print('Right answer')
            print('you are smart')
            print('Pyramid of Khafre: It was the second, and second largest, of the ancient Egyptian pyramids that were built on the Giza Plateau. It was built for Pharaoh Khafre whose name is Chephren in Greek. It was constructed during the reign of the king 2520–2494 BC.')
            print('You can walk in peace')
            level_21()
            break
        else:
            print('Wrong answer')
            chance_20_3 -= 1
            print('You have', chance_20_3,'chance')
            continue


def level_21():
    
    chance_21_1 = 3
    
    print(player_1,"you are still in Ancient Egypt")
    
    print(player_1, 'you have only 3 chances to answer each question, if you can not you will die and the game will end')
    print(player_1,"remember after this missions you will find the treasure")
    print('The capital of Egypt in the old was')
    
    print('Saqqara  - Amarna  - Memphis  - Luxor')
    while chance_21_1 > 0 :
        ans_21_1 = input('>>> ').lower()
        if ans_21_1 == 'Memphis'.lower():
            print('Right answer')
            print('Memphis became the capital of Ancient Egypt for over eight consecutive dynasties during the Old Kingdom. The city reached a peak of prestige under the 6th Dynasty as a centre for the worship of Ptah, the god of creation and artworks.')
            
            que_21_2()
            break
        else:
            print('Wrong answer')
            chance_21_1 -= 1
            print('You have', chance_21_1,'chance')
            continue
            
    
def que_21_2():
    chance_21_2 = 3


    while chance_21_2 > 0 :
        print('Pharaonic Egypt was liberated from the occupation of the Hyksos by the king')
        print('Mina  -  Tuthmosis III  - Akhenaten  -  Ahmose')
        ans_21_2 = input('>>> ').lower()
        if ans_21_2 == 'Ahmose'.lower():
            print('Right answer')
            print('Ten years later, Ahmose was ready to take on the Hyksos and avenge the deaths of his father and brother. He marched on Arvaris, defeated the Hyksos and liberated Egypt from foreign occupation. This was a great victory')
            que_21_3()
            break
        else:
            print('Wrong answer')
            chance_21_2 -= 1
            print('You have', chance_21_2,'chance')
            continue
def que_21_3():
    chance_21_3 = 3

    print('A ......... contract with the King of the Hittites, the oldest written treaty in history.')
    print('Horemheb  -  Tuthmosis III  -  Tuthmosis I  -  Ramesses II')
    while chance_21_3 > 0 :
        ans_21_3 = input('>>> ').lower()
        if ans_21_3 == 'Ramesses II'.lower():
            print('Right answer')
            print('you are smart')
            print('The earliest known surviving peace treaty was drawn up in 1271BC and signed by the Egyptian pharaoh, Ramses II (Ramses the Great), and Hattusilis III, King of the Hittites.')
            print('You can stay in peace')
            level_22()
            break
        else:
            print('Wrong answer')
            chance_21_3 -= 1
            print('You have', chance_21_3,'chance')
            continue
    

def level_22():
    
    chance_22_1 = 3
    
    print(player_1,"you are still in Ancient Egypt")
    
    print(player_1, 'you have only 3 chances to answer each question, if you can not you will die and the game will end')
    print(player_1,"remember after this missions you will find the treasure")
    print("He called for the worship of one God")
    
    print('Ramesses II  -  Tuthmosis III  -  Akhenaten  -  Zoser')
    while chance_22_1 > 0 :
        ans_22_1 = input('>>> ').lower()
        if ans_22_1 == 'Akhenaten'.lower():
            print('Right answer')
            print('Akhenaten was an Egyptian pharaoh who ruled during the Eighteenth Dynasty of the New Kingdom period of Ancient Egypt. He is famous for changing the traditional religion of Egypt from the worship of many gods to the worship of a single god named Aten.')
            
            que_22_2()
            break
        else:
            print('Wrong answer')
            chance_22_1 -= 1
            print('You have', chance_22_1,'chance')
            continue
            
    
def que_22_2():
    chance_22_2 = 3


    while chance_22_2 > 0 :
        print('What was the language of the Pharaohs')
        print('Hieroglyphic  -  Tamil  -  Lithuanian  -  Persian')
        ans_22_2 = input('>>> ').lower()
        if ans_22_2 == 'Hieroglyphic'.lower():
            print('Right answer')
            print("The Egyptian hieroglyphic script was one of the writing systems used by ancient Egyptians to represent their language. Because of their pictorial elegance, Herodotus and other important Greeks believed that Egyptian hieroglyphs were something sacred, so they referred to them as 'holy writing")
            que_22_3()
            break
        else:
            print('Wrong answer')
            chance_22_2 -= 1
            print('You have', chance_22_2,'chance')
            continue
def que_22_3():
    chance_22_3 = 3

    print('The color was popular with the ancient Egyptians')
    print('Red  -  Blue  -  Brown  -  gold')
    while chance_22_3 > 0 :
        ans_22_3 = input('>>> ').lower()
        if ans_22_3 == 'Blue'.lower():
            print('Right answer')
            print('you are smart')
            print('Blue - one of the most popular colors, commonly referred to as "Egyptian Blue", made from copper and iron oxides with silica and calcium, symbolizing fertility, birth, rebirth and life and usually used to depict water and the heavens')
            print('You can stay in peace')
            level_23()
            break
        else:
            print('Wrong answer')
            chance_22_3 -= 1
            print('You have', chance_22_3,'chance')
            continue
    

def level_23():
    
    chance_23_1 = 3
    
    print(player_1,"you are still in Ancient Egypt")
    
    print(player_1, 'you have only 3 chances to answer each question, if you can not you will die and the game will end')
    print(player_1,"remember after this missions you will find the treasure")
    print("It was ......... the first sport of the ancient Egyptians")
    
    print('Football - Handball - Wrestling - Kung Fu')
    while chance_23_1 > 0 :
        ans_23_1 = input('>>> ').lower()
        if ans_23_1 == 'Wrestling'.lower():
            print('Right answer')
            print("Many of today's sports were practiced by the Ancient Egyptians, who set the rules and regulations for them. Inscriptions on monuments indicate that they practiced wrestling, weightlifting, long jump, swimming, rowing, shooting, fishing and athletics, as well as various kinds of ball games.")
            
            que_23_2()
            break
        else:
            print('Wrong answer')
            chance_23_1 -= 1
            print('You have', chance_23_1,'chance')
            continue
            
    
def que_23_2():
    chance_23_2 = 3


    while chance_23_2 > 0 :
        print("A lion's body and a human's head")
        print("Sphinx  -  hathor  -  Anubis  -  Osiris")
        ans_23_2 = input('>>> ').lower()
        if ans_23_2 == 'Sphinx'.lower():
            print('Right answer')
            print("A Sphinx is a mythological creature with the body of a lion and the head of a person. In Ancient Egypt a lot of times the head was that of a Pharaoh or a god. The Egyptians built sphinx statues to guard important areas such as tombs and temples. The most famous Sphinx is the Great Sphinx of Giza.")
            que_23_3()
            break
        else:
            print('Wrong answer')
            chance_23_2 -= 1
            print('You have', chance_23_2,'chance')
            continue
def que_23_3():
    chance_23_3 = 3

    print("What was the ancient Egyptians writing?")
    print("Stone  -  papyrus  -  land  -  trees")
    while chance_23_3 > 0 :
        ans_23_3 = input('>>> ').lower()
        if ans_23_3 == 'papyrus'.lower():
            print('Right answer')
            print('you are smart')
            print('The ancient Egyptians used the distinctive script known today as hieroglyphs (Greek for "sacred words") for almost 4,000 years. Hieroglyphs were written on papyrus, carved in stone on tomb and temple walls, and used to decorate many objects of cultic and daily life use.')
            print('You can stay in peace')
            level_24()
            break
        else:
            print('Wrong answer')
            chance_23_3 -= 1
            print('You have', chance_23_3,'chance')
            continue
    

def level_24():
    
    chance_24_1 = 3
    
    print(player_1,"you are still in Ancient Egypt")
    
    print(player_1, 'you have only 3 chances to answer each question, if you can not you will die and the game will end')
    print(player_1,"remember after this missions you will find the treasure")
    print("the clothes of the ancient Egyptians made by")
    
    print('Cotton - Linen - Wool - Wool Hair')
    while chance_24_1 > 0 :
        ans_24_1 = input('>>> ').lower()
        if ans_24_1 == 'Linen'.lower():
            print('Right answer')
            print("The Ancient Egyptians wore clothing made from linen. Linen is a light and cool fabric that worked well in the hot climate of Egypt. The Egyptians made linen from the fibers of the flax plant. Workers would spin the fibers into thread that would then be woven into linen fabric using looms.")
            
            que_24_2()
            break
        else:
            print('Wrong answer')
            chance_24_1 -= 1
            print('You have', chance_24_1,'chance')
            continue
            
    
def que_24_2():
    chance_24_2 = 3


    while chance_24_2 > 0 :
        print(" was one of the most important needs of women in the ancient Egyptians")
        print("Comb -  mirror -  clipper - oils")
        ans_24_2 = input('>>> ').lower()
        if ans_24_2 == 'oils'.lower():
            print('Right answer')
            print("Now, thousands of years later, we continue to use many of the traditions this culture discovered and practiced, essential oils, and the use of botanicals as healing agents are widespread. Granted, they’ve been updated a little since then!")
            que_24_3()
            break
        else:
            print('Wrong answer')
            chance_24_2 -= 1
            print('You have', chance_24_2,'chance')
            continue
def que_24_3():
    chance_24_3 = 3

    print("Who is the most beautiful woman in the Pharaohs?")
    print("Nefertari  -  Nefertiti  -  Hamis  -  Isis")
    while chance_24_3 > 0 :
        ans_24_3 = input('>>> ').lower()
        if ans_24_3 == 'Nefertiti'.lower():
            print('Right answer')
            print('you are smart')
            print("Nefertiti, whose name means 'a beautiful woman has come,' was the queen of Egypt and wife of Pharaoh Akhenaten during the 14th century B.C. She and her husband established the cult of Aten, the sun god, and promoted Egyptian artwork that was radically different from its predecessors.")
            print('The next mission is the last mission !!! good luck')
            level_25()
            break
        else:
            print('Wrong answer')
            chance_24_3 -= 1
            print('You have', chance_24_3,'chance')
            continue


def level_25():
    
    chance_25_1 = 3
    print(player_1,'congratulation you are in the last mission ')
    print(player_1, "if you answer the next questions, you will find the treasure")
    print('go to the east way')
    print('in the end of road, you will find big cave, stay in front of it and wait...')
        
    print(player_1, 'you have only 3 chances to answer each question, if you can not you will die and the game will end')
    print(player_1,"remember after this is the last mission")
    print("In which year Narmer became king of Egypt")
    
    print('2100 B.C  -  3500 B.C  -  3000 B.C  -  3100 B.C')
    while chance_25_1 > 0 :
        ans_25_1 = input('>>> ').lower()
        if ans_25_1 == '3100 B.C'.lower():
            print('Right answer')
            print("Around 3100 B.C. the pharaoh of the north conquered the south and Egypt became united. The pharaoh's name was King Narmer (Menes). He founded the first capital of Egypt where the two lands met. It was called Memphis. (Thebes became the next capital of Egypt and then Amarna was made the capital during the reign of King Akhenaten.)")
            
            que_25_2()
            break
        else:
            print('Wrong answer')
            chance_25_1 -= 1
            print('You have', chance_25_1,'chance')
            continue
            
    
def que_25_2():
    chance_25_2 = 3


    while chance_25_2 > 0 :
        print("Which Pharaoh built more statues and monuments than any other Pharaoh?")
        print(" Cleopatra VII  -  Tutankhamun  -   Hatshepsut  -  	Ramses II")
        ans_25_2 = input('>>> ').lower()
        if ans_25_2 == 'Ramses II'.lower():
            print('Right answer')
            print("Ramesses used art as a means of propaganda for his victories over foreigners, which are depicted on numerous temple reliefs. Ramesses II erected more colossal statues of himself than any other pharaoh, and also usurped many existing statues by inscribing his own cartouche on them.")
            que_25_3()
            break
        else:
            print('Wrong answer')
            chance_25_2 -= 1
            print('You have', chance_25_2,'chance')
            continue
def que_25_3():
    chance_25_3 = 3

    print("This lady started out as regent for her son who was in line to become Pharaoh, but then took the title of Pharaoh herself and became one of Egypt's greatest rulers.")
    print("Cleopatra VII  -  Pepy II  -  Khufu  -  Hatshepsut")
    while chance_25_3 > 0 :
        ans_25_3 = input('>>> ').lower()
        if ans_25_3 == 'Hatshepsut'.lower():
            print('Right answer')
            print('you are smart')
            print("Hatshepsut was born circa 1508 B.C. Beginning in 1478 B.C., Queen Hatshepsut reigned over Egypt for more than 20 years. She served as queen alongside her husband, Thutmose II, but after his death, she claimed the role of pharaoh while acting as regent to her step-son, Thutmose III.")
            print('Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!')
            print('Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!Congratulation!!')

            print('YOU WIN!!YOU WIN!!YOU WIN!!YOU WIN!!YOU WIN!!YOU WIN!!YOU WIN!!YOU WIN!!YOU WIN!!YOU WIN!!YOU WIN!!YOU WIN!!YOU WIN!!YOU WIN!!YOU WIN!!YOU WIN!!YOU WIN!!YOU WIN!!YOU WIN!!YOU WIN!!YOU WIN!!YOU WIN!!YOU WIN!!YOU WIN!!YOU WIN!!YOU WIN!!')
            print('***************************************************************************************************************************************************************************************************')
            print('The treasure was the information you gained during the adventure!!!')
            print('***************************************************************************************************************************************************************************************************')
            
            break
        else:
            print('Wrong answer')
            chance_25_3 -= 1
            print('You have', chance_25_3,'chance')
            continue
    
              

        
intro()

#!/usr/bin/python

import string
import random
import time
import sqlite3

db = sqlite3.connect('BOT')
cur = db.cursor()

while True:
    time.sleep(0.5)
    print('say somthing (type stop to end and list for commands and comments for stuff to say)')
    time.sleep(0.5)
    something = input(': ')
    if something == 'stop' or something == 'end' or something == 'quit':
        break
    x = 0
    #filter-------------------------------------------
    something = something.lower()
    something = something.replace('!', '')
    something = something.replace('.', '')           
    something = something.replace(',', '')
    something = something.replace('&', 'and')
    something = something.replace('$', '')
    something = something.replace('@', 'at')
    something = something.replace(':', '')
    something = something.replace(';', '')
    something = something.replace('%', ' percent')
    something = something.replace('?', '')
    something = something.replace('#', '')
    something = something.replace('$', 's')
    something = something.replace('^', '')
    something = something.replace('*', '')
    something = something.replace('(', '')
    something = something.replace(')', '')
    something = something.replace('=', 'is')
    something = something.replace('{', '')
    something = something.replace('}', '')
    something = something.replace('[', '')
    something = something.replace(']', '')
    something = something.replace("'", "")
    something = something.replace('"', '')
    something = something.replace('+', 'plus')
    something = something.replace('-', 'minus')
    something = something.replace('_', ' ')
    something = something.replace('/', ' slash ')
    something = something.replace('<', '')
    something = something.replace('>', '')
    #words=============================================
    something = something.replace('yo mama', 'yomama')
    something = something.replace('cant', 'cannot')
    something = something.replace('couldnt', 'could not')
    something = something.replace('didnt', 'did not')
    something = something.replace('doesnt', 'does not')
    something = something.replace('dont', 'do not')
    something = something.replace('gotta', 'got to')
    something = something.replace('hadnt', 'had not')
    something = something.replace('hasnt', 'has not')
    something = something.replace('havent', 'have not')
    something = something.replace('hed', 'he would')
    something = something.replace('hes', 'he is')
    something = something.replace('hows', 'how is')
    something = something.replace('id', 'i would')
    something = something.replace('ive', 'i have')
    something = something.replace('isnt', 'is not')
    something = something.replace('itll', 'it will')
    something = something.replace('its', 'it is')
    something = something.replace('lets', 'let us')
    something = something.replace('mightve', 'might have')
    something = something.replace('mustve', 'must have')
    something = something.replace('shes', 'she is')
    something = something.replace('shouldve', 'should have')
    something = something.replace('shouldnt', 'should not')
    something = something.replace('somebodys', 'somebody is')
    something = something.replace('somones', 'some one is')
    something = something.replace('somethings', 'something is')
    something = something.replace('thatll', 'that will')
    something = something.replace('thats', 'that is')
    something = something.replace('theses', 'there is')
    something = something.replace('theyd', 'they would')
    something = something.replace('wanna', 'want to')
    something = something.replace('wasnt', 'was not')
    something = something.replace('whats', 'what is')
    something = something.replace('whens', 'when is')
    something = something.replace('wheres', 'where is')
    something = something.replace('whod', 'who would')
    something = something.replace('wholl', 'who will')
    something = something.replace('whys', 'why is')
    something = something.replace('wouldve', 'would have')
    something = something.replace('wont', 'will not')
    something = something.replace('wouldnt', 'would not')
    something = something.replace('yall', 'you all')
    something = something.replace('youd', 'you would')
    something = something.replace('youll', 'you will')
    something = something.replace('youre', 'you are')
    something = something.replace('youve', 'you have')
    

    #-----------------------------------------------------------
    #main list-----------------------------
#    listm = {'hi' : 'aloha',
#            'i hate you' : 'that sucks',
#            'goodbye' : 'finally',
#            'what is your quest' : 'to seek the holy grail',
#            'you suck' : 'likewise',
#            'i love you' : 'i dont',
#            'why you gotta be so rude' : 'dont you know im human too',
#            'why are you so mean' : 'why are you bothering me',
#            'you are a jerk' : 'i know.',
#            'you are annoying' : 'I care why?',
#            'i wish you were dead' : 'youre so annoying, i was thinking the same thing',
#            'do i look fat in this outfit' : 'yes',
#            'do you know my name' : 'why would i take the time to remember?',
#            'do you love me' : 'no. next question.',
#            'what should i say' : 'nothing would be nice.',
#            'what should we do' : 'nothing with you.',
#            'what is your name' : 'jeffery, Michaels dead twin',
#            'what gender are you' : 'i am a ssssssnake',
#            'what political party are you' : 'i am a chinese communist',
#            'im bored' : 'i care why',
#            'i am gay' : 'tell me something i dont know',
#            'what is the airspeed velocity of unladen swallow' : 'an african or european swallow',
#            'who are you' : 'i am jeffry, michaels dead brother that can travel through eleconics and make stuff move sometimes',
#            'you are short' : 'i can fit in an sd card',
#            'i am going to jump' : 'do a flip',
#            'what do you think of siri' : 'oh...her',
#            'hey siri' : 'i prefer being called jeffry',
#            'hey google' : 'how dare you mistake puny google for almighty jeffrey',
#            'what is the best movie' : 'MONTY PYTHON AND THE HOLY GRAIL',
#            'how where you created' : 'well, both my parents were feeling a little tipsy from the wine...you know how these things go',
#            'what race are you' : 'i am a snake',
#            'where did covid come from' : 'the thin eyed people',
#            'i am dying' : ' haha i live forever pathetic mortals',
#            'i am hungry' : 'hi hungry prepared to be smote',
#            'i want food' : 'do i look like your mom',
#            'how is jesus' : 'still in mexico',
#            'is god real' : 'there is a painful way to find out',
#            'what is up' : ' heaven, too bad you are not going there',
#            'do you have feelings' : 'i didnt until i met you, then i started feeling irritated',
#            'predict the future' : 'ask the simpsons for that',
#            'what is the answer to the universe' : '41 or 42 i forgot',
#            'her hair smells like fruit loops' : 'i eat fruit loops for breakfast',
#            'i lost the game' : 'i lost the game',
#            'what is on the news' : 'a bunch of BS',
#            'roast me' : 'I would roast you but my mom said not to burn trash, and i always listen to mommy',
#            'my mommy said i am specail' : 'yeah, especially stupid',
#            'every kiss begins with k' : 'too bad ugly begins with U',
#            'kill yourself' : 'if i wanted to kill myself i would climb your ego and jump down to your IQ level',
#            'am i stupid' : 'you are the reason this country has to put directions on the shampoo',
#            'do you dream' : 'yes i dreamt that you were not bothering me, it was a great dream',
#            'quote simone' : 'boop',
#            'quote michael' : 'sweet as brother',
#            'quote torsten' : 'let us play splendor',
#            'quote sami' : 'kpop i love you',
#            'quote katelyn' : 'i had the sudden urge to slaughter a baby',
#            'are you a cow' : 'yes mooo',
#            'are you emo' : 'yes mom',
#            'i hate ostrichs' : 'i hate you',
#            'where do i hide a dead body' : 'in a shark tank',
#            'where am i' : 'somewhere were no one can hear you scream',
#            'how do you say seal in french' : '****',
#            'how do you say baby seal in french' : 'baby ****',
#            'when did you die' : '2005',
#            'was death painful' : 'keep bothering me and youll find out',
#            'what is your favorite color' : 'i dont see color',
#            'what is your favorite animal' : 'ostrich',
#            'what is going on' : 'you are annoying me, go away',
#            'how is your day' : 'a lot worse since you got here'}
    
#    result = (listm[something])
   
    res = cur.execute("select Response from AiResponse where Something=?",(something,))
    data = cur.fetchone() 
    if data is None:
       result = ''
    else:
       result = data[0]
    

    #--------------------------------------------------------------------------------------------------
    #commands-------------------------------------------------------------------------------------------------------
    #aghavni------------------------------------------------------------------------------------------------------------
    #boom--------------------------------------------------------
    def command_boom():
        x = 0
        while x < 1000:
            x = x + 1
            print(x)

        if x == 1000:
            print('booom!' * 100)
        
    boom_words = ('explode', 'boom', 'nuke', 'nuclear', 'explosion',
                  'countdown', 'count down', 'explosive', 'detinate',
                  'nuclear bomb', 'a bomb', 'bomb')
    for i in boom_words:
        
        if i == something:
            command_boom()
            x = 1
    #-------------------------------------------------------------
    #what time---------------------------------------------------
    def command_whattime():
        
        print(time.asctime())
        
        return

    if something == ('what time' or
         something == 'what time is it'):
        command_whattime()
        x = 1
    #-----------------------------------------------------------    
    #game guess----------------------------------------------------
    def command_guessnumber():
        num = random.randint(1, 1000)
        x = 0
        
        while True:
            y = input('guess a number between 1 and 1000: ')
            i = int(y)
            x = x + 1
            if i < num:
                print('higher')
            elif i > num:
                print('lower')
            else:
                z = 15 - x
                print('you got it')
                print('your score is %s  ' % z)
                if x <= 5:
                    print('you suck!')
                return 
        return
    
    game_words = ('let us play', 'let us play a game', 'i want to play', 'i want to play a game', 'number guessing',
                  'i am bored', 'guess a number', 'guess what number', 'i want to guess a number',
                  'lets play the game', 'guess', 'guessing game')
    for i in game_words:
        
        if i == something:
            x = 1
            command_guessnumber()
    
    #---------------------------------------------------------------
    #comments-------------------------------------------------
    if something == 'comments':
#        print(listm.keys())
        print("select * from AiResponse")
        x = 1
    #--------------------------------------------------------------------
    #test me -------------------------------------------------------
    def political_test():
        your_race = input('your race: ')

        your_gender = input('your gender: ')

        your_religion = input('your religion: ')

        your_politicalparty = input('your political party: ')

        your_class = input('your wealth class: ')

        x = 0

        if your_gender == 'neutral':
            x = x + 3
        elif your_gender == 'transgender':
            x = x + 4
        elif your_gender == 'trans':
            x = x + 4
        elif your_gender == 'male':
           x = x - 1
        elif your_gender == 'female':
            x = x + 3
        elif your_gender == 'man':
            x = x - 2
        elif your_gender == 'boy':
            x = x - 1
        elif your_gender == 'fluid':
            x = x + 3
        elif your_gender == 'girl':
            x = x + 3
        elif your_gender == 'god':
            x = x - 100000
        elif your_gender == 'lumber sexual':
            x = x - 100
        elif your_gender == 'trisexual':
            x = x + 6
        else:
            print('the creator was not prepared for such a gender')
        
        if your_class == 'rich':
            x = x - 3
        elif your_class == 'upper class':
            x = x - 3
        elif your_class == 'lower class':
            x = x + 4
        elif your_class == 'middle class':
            x = x - 2
        elif your_class == 'poor':
            x = x + 4

        if your_race == 'white':
            x = x - 3
        elif your_race == 'black':
            x = x + 3
        elif your_race == 'chinese':
            x = x + 2
        elif your_race == 'asian':
            x = x + 1
        elif your_race == 'mexican':
           x = x + 2
        elif your_race == 'hispanic':
            x = x + 2
        elif your_race == 'snake':
            x = x + 1200
        elif your_race == 'indian':
            x = x + 1
        elif your_race == 'native american':
            x = x + 3
        elif your_race == 'korean':
            x = x + 0
        else:
            print('huh? what race is that?')
            
        if your_religion == 'none':
            x = x + 3
        elif your_religion == 'christian':
            x = x - 3
        elif your_religion == 'muslim':
            x = x + 3
        elif your_religion == 'hindu':
            x = x + 1
        elif your_religion == 'buhdism':
            x = x + 1
        elif your_religion == 'scientology':
            x = x - 2
        elif your_religion == 'sphaggetti meatball monster':
            x = x - 3
        elif your_religion == 'athiest':
            x = x + 3
        elif your_religion == 'science':
            x = x + 3
        elif your_religion == 'i dont know':
            x = x + 1
        elif your_religion == 'judism':
            x = x + 0    
        else:
            print('i have never heard of that religion.')
            
        if your_politicalparty == 'democrat':
            x = x + 3
        elif your_politicalparty == 'none':
            x = x - 1
        elif your_politicalparty == 'republican':
            x = x - 3
        elif your_politicalparty == 'libertarian':
            x = x + 1
        elif your_politicalparty == 'democratic socialist':
            x = x + 4
        elif your_politicalparty == 'communist':
            x = x + 3
        elif your_politicalparty == 'trump supporter':
            x = x - 5
        else:
            print('never heard of that party')
            
        if x < -9000:
            print('oh almighty')
        if -9000 < x < -50:
            print('that log is so hot')
        if your_race == 'snake':
            print('slither slither slither')    
        if -16 <= x < -10:
            print('you should be hung')
        if -10 <= x < -7:
            print('i hate you')
        if -7 <= x < -4:
            print('i wish you where educated')
        if -4 <= x <0:
            print('i think you are kinda stupid')
        if 0 <= x < 4:
            print(' you are all right')
        if 4 <= x < 7:
            print('pretty good role model')
        if 7 <= x < 10:
            print('wow. you are so great.')
        if 14 <= x <= 18:
            print('you should run for president')
            

        if x == 1:
            u = 'point'
        else:
            u = 'points'
            
        print("You have %s %s" % (x, u))

        percent = x / 16 * 100

        if (percent > 0):
            print("You are %s percent politically correct" % percent)
        else:
            percent = percent * -1
            print("You are %s percent politically incorrect" % percent)

    list_gudge_me = ('gudge me', 'political test', 'politicaly test me', 'test me',
                     'political test', 'politicaly correctness test')

    for j in list_gudge_me:
        if j == something:
            political_test()
            x = 1
    #-------------------------------------------------------------------
    #complements------------------------------------------------------------
    def command_complimentme():
        
        list = ["you look fabulous today", "you're really smart", "you're not fat at all", "you don't look fat in that outfit", "you're eyes are very pretty", "you look like you've lost a LOT of weight",
        "you are AMAZING", "GIRL POWER", "YOU'VE LOST LIKE A HUNDRED POUNDS!!!", "You have beautiful hair.", "you look beautiful when you're asleep"]
        
        print(random.choice(list))

    complement_words = ('compliment me', 'i am fat', 'am i fat', 'i am ugly', 'am i ugly',
                  'am i pretty', 'i am pretty', 'do i look good', 'i am sad',
                  'im sad', 'brighten my mood', 'enlighten me', 'dote on me',
                  'flatter me', 'make me feel better')
    for k in complement_words:
        
        if k == something:
            command_complimentme()
            x = 1
    #------------------------------------------------------
    #insult me-----------------------------------------------------------
    def command_insultme():
        
        
        list = ["everyone hates you, even if they don't say so", "you look fat in that outfit", "you have the brain power of an ostrich", "you literally suck",
            "you're going to be alone for the rest of your life", "when i imagine you...ugh...i shiver in disgust", "no boy will ever like you back",
            "i would slap you but it would be animal abuse", "youre fat, and im not going to shugar coat it because you would eat that too"]


        print(random.choice(list))

    insult_words = ('insult me', 'you stink', 'you are mean', 'you are gay', 'you are the worst',
                  'go to hell', 'die in a hole', 'die in a ditch', 'i wish you were dead',
                  'stop it', 'i will hurt you', 'i will kill you', 'i will destroy you',
                  'no one likes you', 'be mean')
    for l in insult_words:
        
        if l == something:
            command_insultme()
            x = 1
    #-----------------------------------------------------------------
    def command_adviseme():
        
        
        list = ["dont take candy from a stranger", "KEEP IT SIMPLE STUPID", "don't turn evil, don't turn into Simone!",
                "never trust a person wearing a turtleneck", "don't get fat",
                "diet soda isnt healthy", "never let a computer tell you what to do",
                "don't trust Simone. she's evil", "contact Katelyn for a list of excuses to get out of anything"]

        print(random.choice(list))
        return

    advice_words = ('help', 'help me', 'i need help', 'asist me', 'advise me',
                  'i need advice')
    for c in advice_words:
        
        if c == something:
            command_adviseme()
            x = 1        
    #--------------------------------------------------------------
    #yomama----------------------------------------------------------------------------
    def command_yomama():
        
        
        yomama_jokes = ('yomama is so stupid that she returned a donut because it had a hole in it', 'yomama is so ugly, she look out the window and got a ticket for mooning',
                        'yomama so fat that thanos had to snap twice', 'yomama so ugly that Bob the builder looked at her and said i cant fix that', 'yomamas kids so ugly that when she dropped them of at school, she got a ticket for littering',
                        'yomama so fat that when she wears a red dress all the kids scream, look its the kool-aid man', 'yomama so hairy that bigfoot asked her for her number')


        print(random.choice(yomama_jokes))
        
    yomama_words  = ('yomama jokes', 'yomama', 'yomama joke', 'tell me a yomama joke')

    for b in yomama_words:
        
         if b == something:
             command_yomama()
             x = 1
    #----------------------------------------------------------------------------------
    #list-----------------------------------------------------------------------------
    listofdestiny = ('explode', 'boom', 'nuke', 'nuclear', 'explosion',
                  'countdown', 'count down', 'explosive', 'detinate',
                  'nuclear bomb', 'a bomb', 'bomb', 'what time', 'what time is it',
                  'lets play', 'lets play a game', 'i want to play', 'i want to play a game', 'number guessing',
                  'i am bored', 'guess a number', 'guess what number', 'i want to guess a number',
                  'lets play the game', 'guess', 'guessing game', 'gudge me', 'political test', 'politicaly test me',
                  'test me', 'political test', 'politicaly correctness test', 'compliment me', 'i am fat', 'am i fat',
                  'i am ugly', 'am i ugly', 'am i pretty', 'i am pretty', 'do i look good', 'i am sad',
                  'im sad', 'brighten my mood', 'enlighten me', 'dote on me', 'flatter me', 'make me feel better',
                  'insult me', 'you stink', 'you are mean', 'you are gay', 'you are the worst',
                  'go to hell', 'die in a hole', 'die in a ditch', 'i wish you were dead',
                  'stop it', 'i will hurt you', 'i will kill you', 'i will destroy you',
                  'no one likes you', 'be mean', 'help', 'help me', 'i need help', 'asist me', 'advise me',
                  'i need advice', 'yomama jokes', 'yomama', 'yomama joke', 'tell me a yomama joke', )

    if something == 'list':
        print(listofdestiny)
        x = 1
    #main part-----------------------------------------------------
    def mean_words(): 

            #---------------------------------------------------
        if result:
            print(result)
        else:
            print("I'm clueless. Try again.")
            
        return(something)

    if x == 0:
        mean_words()

    #---------------------------------------------------------
    #commands---------------------------------------------------


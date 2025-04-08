import numpy as np
import matplotlib.pyplot as plt

def inc(x,a,b):
    if (x<=a):
        r=0
    elif (x>=b):
        r=1
    else:
        r=(x-a)/(b-a)
    return r

def dec(x,a,b):
    if (x<=a):
        r=1
    elif (x>=b):
        r=0
    else:
        r=(b-x)/(b-a)
    return r

def sig(x,a,b):
    r=1/(1+np.exp(-a*(x-b)))
    return r

def gauss(x,mu,sig):
    r=np.exp(-(x-mu)**2/sig**2)
    return r

def trap(x,a,b,c,d):
    if x<=a or x>=d:
        r=0
    elif a<x<b:
        r=(x-a)/(b-a)
    elif c<x<d:
        r=(d-x)/(d-c)
    else: 
        r=1
    return r

#fuzzification of variables - inputs 
#movie rating
rate=np.linspace(0,10,200)
low_rate=np.array([dec(x,3,6)for x in rate])
avg_rate=np.array([gauss(x,5,1.5)for x in rate])
high_rate=np.array([inc(x,4,8)for x in rate])

#Duration 
dur=np.linspace(0,180,300)
short_dur=np.array([dec(x,45,60)for x in dur])
avg_dur=np.array([trap(x,45,90,120,140)for x in dur])
long_dur=np.array([inc(x,100,150)for x in dur])

#year
year=np.linspace(1995,2025,180)
old_year=np.array([dec(x,2000,2003)for x in year])
rec_year=np.array([trap(x,2007,2010,2015,2018)for x in year])
new_year=np.array([inc(x,2020,2022)for x in year])

#mood
mood=np.linspace(0,10,200)
bad_mood=np.array([dec(x,3,6)for x in mood])
normal_mood=np.array([gauss(x,5,0.5)for x in mood])
great_mood=np.array([inc(x,4,8)for x in mood])

#user age
age=np.linspace(0,100,400)
young_age=np.array([dec(x,25,30)for x in age])
mid_age=np.array([gauss(x,45,15)for x in age])
sen_age=np.array([inc(x,50,60)for x in age])

#fuzzification of variables - output
score=np.linspace(0,10,200)
poor_score=np.array([dec(x,3,4)for x in score])
avg_score=np.array([gauss(x,5,1)for x in score])
high_score=np.array([inc(x,6,8)for x in score])

# Example movie dataset
movies = [
    {"title": "Inception", "rating": 8.8, "duration": 148, "release_date": 2010, "mood": "neutral", "age_limit": 13,
     "description": "A thief who enters the dreams of others to steal secrets must plant an idea in someone's mind."},
    {"title": "The Dark Knight", "rating": 9.0, "duration": 152, "release_date": 2008, "mood": "happy", "age_limit": 15,
     "description": "Batman faces the Joker, a criminal mastermind who seeks to create chaos in Gotham City."},
    {"title": "Titanic", "rating": 7.8, "duration": 195, "release_date": 1997, "mood": "sad", "age_limit": 13,
     "description": "A young couple from different social classes fall in love aboard the ill-fated Titanic."},
    {"title": "Interstellar", "rating": 8.6, "duration": 169, "release_date": 2014, "mood": "neutral", "age_limit": 10,
     "description": "A team of explorers travel through a wormhole in space to ensure humanity's survival."},
    {"title": "The Lion King", "rating": 8.5, "duration": 88, "release_date": 1994, "mood": "happy", "age_limit": 6,
     "description": "A lion cub flees his kingdom after his father's death and learns the true meaning of leadership."},
    {"title": "Avengers: Endgame", "rating": 8.4, "duration": 181, "release_date": 2019, "mood": "neutral", "age_limit": 12,
     "description": "The Avengers unite for a final battle against Thanos to restore balance to the universe."},
    {"title": "Forrest Gump", "rating": 8.8, "duration": 142, "release_date": 1994, "mood": "neutral", "age_limit": 13,
     "description": "The life journey of Forrest Gump, a kind-hearted man witnessing key moments in history."},
    {"title": "The Matrix", "rating": 8.7, "duration": 136, "release_date": 1999, "mood": "neutral", "age_limit": 14,
     "description": "A hacker learns about the true nature of his reality and his role in the war against machines."},
    {"title": "The Shawshank Redemption", "rating": 9.3, "duration": 142, "release_date": 1994, "mood": "neutral", "age_limit": 16,
     "description": "A banker sentenced to life in prison forms an unlikely friendship and hopes for freedom."},
    {"title": "Gladiator", "rating": 8.5, "duration": 155, "release_date": 2000, "mood": "neutral", "age_limit": 15,
     "description": "A betrayed Roman general seeks revenge against the corrupt emperor who murdered his family."},
    {"title": "Up", "rating": 8.2, "duration": 96, "release_date": 2009, "mood": "happy", "age_limit": 5,
     "description": "An elderly man fulfills his dream of adventure by flying his house to South America with balloons."},
    {"title": "Toy Story", "rating": 8.3, "duration": 81, "release_date": 1995, "mood": "happy", "age_limit": 3,
     "description": "A group of toys come to life when their owner isn't around, leading to adventures and friendships."},
    {"title": "Joker", "rating": 8.4, "duration": 122, "release_date": 2019, "mood": "sad", "age_limit": 18,
     "description": "A struggling comedian's descent into madness turns him into the infamous Joker."},
    {"title": "Parasite", "rating": 8.6, "duration": 132, "release_date": 2019, "mood": "neutral", "age_limit": 17,
     "description": "A poor family schemes to become employed by a wealthy household, leading to unexpected consequences."},
    {"title": "Coco", "rating": 8.4, "duration": 105, "release_date": 2017, "mood": "happy", "age_limit": 6,
     "description": "A young musician embarks on a journey to the Land of the Dead to discover his family's legacy."},
    {"title": "The Godfather", "rating": 9.2, "duration": 175, "release_date": 1972, "mood": "neutral", "age_limit": 18,
     "description": "The patriarch of an organized crime family passes control to his reluctant son."},
    {"title": "Schindler's List", "rating": 9.0, "duration": 195, "release_date": 1993, "mood": "sad", "age_limit": 16,
     "description": "A businessman helps save Jewish refugees during the Holocaust."},
    {"title": "Finding Nemo", "rating": 8.1, "duration": 100, "release_date": 2003, "mood": "happy", "age_limit": 5,
     "description": "A clownfish sets out on an adventure to find his lost son in the vast ocean."},
    {"title": "Inside Out", "rating": 8.1, "duration": 95, "release_date": 2015, "mood": "neutral", "age_limit": 6,
     "description": "The emotions inside a young girl's mind help her navigate life's changes."},
    {"title": "Pulp Fiction", "rating": 8.9, "duration": 154, "release_date": 1994, "mood": "neutral", "age_limit": 18,
     "description": "Various interconnected stories of Los Angeles criminals, small-time mobsters, and a mysterious briefcase."},
    {"title": "The Lord of the Rings: The Return of the King", "rating": 8.9, "duration": 201, "release_date": 2003, "mood": "happy", "age_limit": 13,
     "description": "Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam."},
    {"title": "Fight Club", "rating": 8.8, "duration": 139, "release_date": 1999, "mood": "neutral", "age_limit": 18,
     "description": "An insomniac office worker and a soap maker form an underground fight club that evolves into something more."},
    {"title": "The Green Mile", "rating": 8.6, "duration": 189, "release_date": 1999, "mood": "sad", "age_limit": 16,
     "description": "Death Row guards discover a mysterious inmate with supernatural healing powers."},
    {"title": "Goodfellas", "rating": 8.7, "duration": 146, "release_date": 1990, "mood": "neutral", "age_limit": 18,
     "description": "The story of Henry Hill and his life in the mob, covering his relationship with his wife and his mob partners."},
    {"title": "The Silence of the Lambs", "rating": 8.6, "duration": 118, "release_date": 1991, "mood": "neutral", "age_limit": 18,
     "description": "A young FBI cadet must receive the help of an incarcerated cannibal killer to help catch another serial killer."},
    {"title": "Star Wars: Episode V - The Empire Strikes Back", "rating": 8.7, "duration": 124, "release_date": 1980, "mood": "neutral", "age_limit": 12,
     "description": "After the Rebels are brutally overpowered by the Empire, Luke Skywalker begins Jedi training with Yoda."},
    {"title": "The Departed", "rating": 8.5, "duration": 151, "release_date": 2006, "mood": "neutral", "age_limit": 18,
     "description": "An undercover cop and a mole in the police attempt to identify each other while infiltrating an Irish gang."},
    {"title": "Whiplash", "rating": 8.5, "duration": 106, "release_date": 2014, "mood": "neutral", "age_limit": 15,
     "description": "A promising young drummer enrolls at a cut-throat music conservatory where his dreams are mentored by an instructor who will stop at nothing."},
    {"title": "The Pianist", "rating": 8.5, "duration": 150, "release_date": 2002, "mood": "sad", "age_limit": 15,
     "description": "A Polish Jewish musician struggles to survive the destruction of the Warsaw ghetto during World War II."},
    {"title": "Spirited Away", "rating": 8.6, "duration": 125, "release_date": 2001, "mood": "happy", "age_limit": 8,
     "description": "During her family's move to the suburbs, a young girl wanders into a world ruled by gods, witches, and spirits."},
    {"title": "Wall-E", "rating": 8.4, "duration": 98, "release_date": 2008, "mood": "happy", "age_limit": 5,
     "description": "In a distant future, a small waste-collecting robot inadvertently embarks on a space journey that will ultimately decide the fate of mankind."},
    {"title": "The Usual Suspects", "rating": 8.5, "duration": 106, "release_date": 1995, "mood": "neutral", "age_limit": 18,
     "description": "A sole survivor tells of the twisty events leading up to a horrific gun battle on a boat."},
    {"title": "Saving Private Ryan", "rating": 8.6, "duration": 169, "release_date": 1998, "mood": "sad", "age_limit": 17,
     "description": "Following the Normandy Landings, a group of U.S. soldiers go behind enemy lines to retrieve a paratrooper."},
    {"title": "Alien", "rating": 8.4, "duration": 117, "release_date": 1979, "mood": "neutral", "age_limit": 18,
     "description": "The crew of a commercial spacecraft encounter a deadly alien life form after investigating an unknown transmission."},
    {"title": "Back to the Future", "rating": 8.5, "duration": 116, "release_date": 1985, "mood": "happy", "age_limit": 10,
     "description": "A teenager is accidentally sent 30 years into the past in a time-traveling DeLorean invented by his friend."},
    {"title": "The Prestige", "rating": 8.5, "duration": 130, "release_date": 2006, "mood": "neutral", "age_limit": 13,
     "description": "Two stage magicians engage in competitive one-upmanship in an attempt to create the ultimate stage illusion."},
    {"title": "Apocalypse Now", "rating": 8.4, "duration": 147, "release_date": 1979, "mood": "neutral", "age_limit": 18,
     "description": "A U.S. Army officer serving in Vietnam is tasked with assassinating a renegade Special Forces Colonel."},
    {"title": "Memento", "rating": 8.4, "duration": 113, "release_date": 2000, "mood": "neutral", "age_limit": 16,
     "description": "A man with short-term memory loss attempts to track down his wife's murderer."},
    {"title": "The Great Dictator", "rating": 8.4, "duration": 125, "release_date": 1940, "mood": "happy", "age_limit": 12,
     "description": "Dictator Adenoid Hynkel tries to expand his empire while a poor Jewish barber tries to avoid persecution."},
    {"title": "Cinema Paradiso", "rating": 8.5, "duration": 155, "release_date": 1988, "mood": "happy", "age_limit": 12,
     "description": "A filmmaker recalls his childhood when falling in love with the pictures at the cinema of his home village."},
    {"title": "Princess Mononoke", "rating": 8.4, "duration": 134, "release_date": 1997, "mood": "neutral", "age_limit": 12,
     "description": "On a journey to find the cure for a curse, a young prince becomes involved in a struggle between a forest and an industrial town."},
    {"title": "The Big Lebowski", "rating": 8.1, "duration": 117, "release_date": 1998, "mood": "happy", "age_limit": 18,
     "description": "The Dude seeks restitution for his ruined rug and enlists his bowling buddies to help get it."},
    {"title": "La La Land", "rating": 8.0, "duration": 128, "release_date": 2016, "mood": "happy", "age_limit": 12,
     "description": "A jazz pianist and an aspiring actress fall in love while pursuing their dreams in Los Angeles."},
    {"title": "Eternal Sunshine of the Spotless Mind", "rating": 8.3, "duration": 108, "release_date": 2004, "mood": "sad", "age_limit": 15,
     "description": "A couple undergo a medical procedure to erase each other from their memories after their relationship turns sour."},
    {"title": "Good Will Hunting", "rating": 8.3, "duration": 126, "release_date": 1997, "mood": "neutral", "age_limit": 15,
     "description": "A janitor at MIT has a gift for mathematics but needs help from a psychologist to find direction in his life."},
    {"title": "Blade Runner", "rating": 8.1, "duration": 117, "release_date": 1982, "mood": "neutral", "age_limit": 15,
     "description": "A blade runner must pursue and terminate four replicants who stole a ship in space and have returned to Earth."},
    {"title": "The Grand Budapest Hotel", "rating": 8.1, "duration": 99, "release_date": 2014, "mood": "happy", "age_limit": 15,
     "description": "A concierge teams up with one of his employees to prove his innocence after he is framed for murder."},
    {"title": "The Seventh Seal", "rating": 8.2, "duration": 96, "release_date": 1957, "mood": "neutral", "age_limit": 14,
     "description": "A knight returning from the Crusades encounters Death, who agrees to a chess match to determine his fate."},
    {"title": "The Thing", "rating": 8.1, "duration": 109, "release_date": 1982, "mood": "neutral", "age_limit": 18,
     "description": "A research team in Antarctica is hunted by a shape-shifting alien that assumes the appearance of its victims."},
    {"title": "Mad Max: Fury Road", "rating": 8.1, "duration": 120, "release_date": 2015, "mood": "neutral", "age_limit": 15,
     "description": "In a post-apocalyptic wasteland, a woman rebels against a tyrannical ruler in search of her homeland."},
    {"title": "12 Angry Men", "rating": 9.0, "duration": 96, "release_date": 1957, "mood": "neutral", "age_limit": 12,
     "description": "A jury holdout attempts to prevent a miscarriage of justice by forcing his colleagues to reconsider the evidence."},
    {"title": "A Beautiful Mind", "rating": 8.2, "duration": 135, "release_date": 2001, "mood": "neutral", "age_limit": 13,
     "description": "A mathematical genius develops a mental illness while doing secret work in cryptography."},
    {"title": "Ratatouille", "rating": 8.0, "duration": 111, "release_date": 2007, "mood": "happy", "age_limit": 6,
     "description": "A rat who can cook makes an unusual alliance with a young kitchen worker at a famous restaurant."},
    {"title": "The Departed", "rating": 8.5, "duration": 151, "release_date": 2006, "mood": "neutral", "age_limit": 18,
     "description": "An undercover cop and a mole in the police attempt to identify each other while infiltrating an Irish gang."},
    {"title": "Amélie", "rating": 8.3, "duration": 122, "release_date": 2001, "mood": "happy", "age_limit": 12,
     "description": "A shy waitress decides to change the lives of those around her for the better."},
    {"title": "The Wolf of Wall Street", "rating": 8.2, "duration": 180, "release_date": 2013, "mood": "neutral", "age_limit": 18,
     "description": "Based on the true story of Jordan Belfort, from his rise to wealth to his fall involving crime and corruption."},
    {"title": "Pan's Labyrinth", "rating": 8.2, "duration": 118, "release_date": 2006, "mood": "sad", "age_limit": 16,
     "description": "In post-Civil War Spain, a girl meets a mythical faun who guides her through a mysterious labyrinth."},
    {"title": "Casablanca", "rating": 8.5, "duration": 102, "release_date": 1942, "mood": "neutral", "age_limit": 12,
     "description": "A cynical expatriate American cafe owner struggles to decide whether to help his former lover and her fugitive husband."},
    {"title": "Oldboy", "rating": 8.4, "duration": 120, "release_date": 2003, "mood": "neutral", "age_limit": 18,
     "description": "After being imprisoned for 15 years, a man sets out to find out why he was kidnapped."},
    {"title": "The Grand Budapest Hotel", "rating": 8.1, "duration": 99, "release_date": 2014, "mood": "happy", "age_limit": 15,
     "description": "A concierge teams up with one of his employees to prove his innocence after he is framed for murder."},
    {"title": "No Country for Old Men", "rating": 8.1, "duration": 122, "release_date": 2007, "mood": "neutral", "age_limit": 18,
     "description": "Violence and mayhem ensue after a hunter stumbles upon a drug deal gone wrong and more than two million dollars in cash."},
    {"title": "Raiders of the Lost Ark", "rating": 8.4, "duration": 115, "release_date": 1981, "mood": "happy", "age_limit": 12,
     "description": "Archaeologist Indiana Jones races against time to retrieve the legendary Ark of the Covenant."},
    {"title": "The Social Network", "rating": 7.8, "duration": 120, "release_date": 2010, "mood": "neutral", "age_limit": 13,
     "description": "The story of how Mark Zuckerberg created Facebook while studying at Harvard."},
    {"title": "The Sound of Music", "rating": 8.0, "duration": 172, "release_date": 1965, "mood": "happy", "age_limit": 6,
     "description": "A woman leaves an Austrian convent to become a governess to a Naval officer's seven children."},
    {"title": "The Terminator", "rating": 8.0, "duration": 107, "release_date": 1984, "mood": "neutral", "age_limit": 15,
     "description": "A human soldier is sent from 2029 to 1984 to stop an almost indestructible cyborg killing machine."},
    {"title": "Jurassic Park", "rating": 8.1, "duration": 127, "release_date": 1993, "mood": "neutral", "age_limit": 13,
     "description": "Scientists clone dinosaurs to create a theme park, but the creatures escape and turn on their creators."},
    {"title": "The Princess Bride", "rating": 8.0, "duration": 98, "release_date": 1987, "mood": "happy", "age_limit": 8,
     "description": "A fairy tale adventure about a beautiful young woman and her one true love."},
    {"title": "The Truman Show", "rating": 8.1, "duration": 103, "release_date": 1998, "mood": "neutral", "age_limit": 12,
     "description": "An insurance salesman discovers his entire life is a TV show."},
    {"title": "The Breakfast Club", "rating": 7.8, "duration": 97, "release_date": 1985, "mood": "neutral", "age_limit": 15,
     "description": "Five high school students with different stereotypes meet in detention and discover they have more in common than they thought."},
    {"title": "Groundhog Day", "rating": 8.0, "duration": 101, "release_date": 1993, "mood": "happy", "age_limit": 12,
     "description": "A weatherman finds himself inexplicably living the same day over and over again."},
    {"title": "The Sixth Sense", "rating": 8.1, "duration": 107, "release_date": 1999, "mood": "neutral", "age_limit": 13,
     "description": "A boy who communicates with spirits seeks the help of a disheartened child psychologist."}
]

# Input measures with user prompts
print("\nPlease provide the following inputs:")
print("Rating (0-10): Scale guide - ≤3: Low, 5: Average, ≥8: High")
input_rate = float(input("Enter movie rating preference: "))
while input_rate < 0 or input_rate > 10:
    print("Invalid input! Rating must be between 0 and 10")
    input_rate = float(input("Enter movie rating preference: "))

print("\nDuration (0-180 minutes): Scale guide - <45: Short, 90-120: Average, >150: Long")
input_dur = float(input("Enter preferred movie duration: "))
while input_dur < 0 or input_dur > 180:
    print("Invalid input! Duration must be between 0 and 180 minutes")
    input_dur = float(input("Enter preferred movie duration: "))

print("\nRelease Year (1995-2025): Scale guide - <2000: Old, 2010-2015: Recent, 2022-2025: New")
input_year = float(input("Enter preferred release year: "))
while input_year < 1995 or input_year > 2025:
    print("Invalid input! Year must be between 1995 and 2025")
    input_year = float(input("Enter preferred release year: "))

print("\nMood (0-10): Scale guide - ≤3: Bad, 5: Normal, ≥8: Good")
input_mood = float(input("Enter your current mood level: "))
while input_mood < 0 or input_mood > 10:
    print("Invalid input! Mood must be between 0 and 10")
    input_mood = float(input("Enter your current mood level: "))

print("\nAge (0-100): Scale guide - ≤25: Young, 40: Middle-aged, ≥60: Senior")
input_age = float(input("Enter your age: "))
while input_age < 0 or input_age > 100:
    print("Invalid input! Age must be between 0 and 100")
    input_age = float(input("Enter your age: "))

# Calculate membership values based on inputs
input_low_rate = dec(input_rate,3,6)
input_avg_rate = gauss(input_rate,5,1.5)
input_high_rate = inc(input_rate,4,8)

input_short_dur = dec(input_dur,45,60)
input_avg_dur = trap(input_dur,45,90,120,140)
input_long_dur = inc(input_dur,100,150)

input_old_year = dec(input_year,2000,2003)
input_rec_year = trap(input_year,2007,2010,2015,2018)
input_new_year = inc(input_year,2020,2022)

input_bad_mood = dec(input_mood,3,6)
input_normal_mood = gauss(input_mood,5,0.5)
input_great_mood = inc(input_mood,4,8)

input_young_age = dec(input_age,25,30)
input_mid_age = gauss(input_age,45,15)
input_sen_age = inc(input_age,50,60)

#Rule evaluation
#R1: If the rating is high and the duration is short and the release date is modern or mood is happy and the viewer is young, then the recommendation score will be high.
pref1=np.min([input_high_rate,input_short_dur,input_new_year])
pref2=np.min([input_great_mood,input_young_age])
prefr1=np.max([pref1,pref2])
R1=np.fmin(prefr1,high_score)

#R2:If the Rating is average and the Duration is Medium and the Release Date is Recent or the Mood is Neutral and the Age is Middle-aged, then the Recommendation Score is Medium.
pref3=np.min([input_avg_rate,input_avg_dur,input_rec_year])
pref4=np.min([input_normal_mood,input_mid_age])
prefr2=np.max([pref3,pref4])
R2=np.fmin(prefr2,avg_score)

#R3:If the Rating is Low, the Duration is Long, the Release Date is Old, the Mood is Sad, and the Age is Senior, then the Recommendation Score is Low.
pref5=np.min([input_low_rate,input_long_dur,input_old_year])
pref6=np.min([input_bad_mood,input_sen_age])
prefr3=np.max([pref5,pref6])
R3=np.fmin(prefr3,poor_score)

#R4:If the Rating is High, the Duration is Medium, the Release Date is Modern, the Mood is Neutral, and the Age is Middle-aged, then the Recommendation Score is High.
pref7=np.min([input_high_rate,input_avg_dur,input_new_year])
pref8=np.min([input_normal_mood,input_mid_age])
prefr4=np.max([pref7,pref8])
R4=np.fmin(prefr4,high_score)

#R5:If the Rating is Medium, the Duration is Short, the Release Date is Recent, the Mood is Sad, and the Age is Senior, then the Recommendation Score is Medium.
pref9=np.min([input_avg_rate,input_short_dur,input_rec_year])
pref10=np.min([input_bad_mood,input_sen_age])
prefr5=np.max([pref9,pref10])
R5=np.fmin(prefr5,avg_score)

#R6:If the Rating is Low, the Duration is Long, the Release Date is Recent, the Mood is Neutral, and the Age is Middle-aged, then the Recommendation Score is Low.
pref11=np.min([input_low_rate,input_long_dur,input_rec_year])
pref12=np.min([input_normal_mood,input_mid_age])
prefr6=np.max([pref11,pref12])
R6=np.fmin(prefr6,poor_score)

#R7:If the Rating is High, the Duration is Short, the Release Date is Old, the Mood is Happy, and the Age is Senior, then the Recommendation Score is Medium.
pref13=np.min([input_high_rate,input_short_dur,input_old_year])
pref14=np.min([input_great_mood,input_sen_age])
prefr7=np.max([pref13,pref14])
R7=np.fmin(prefr7,avg_score)

#R8:If the Rating is Medium, the Duration is Medium, the Release Date is Old, the Mood is Happy, and the Age is Young, then the Recommendation Score is Medium.
pref15=np.min([input_avg_rate,input_avg_dur,input_old_year])
pref16=np.min([input_great_mood,input_young_age])
prefr8=np.max([pref15,pref16])
R8=np.fmin(prefr8,avg_score)

#R9:If the Rating is Low, the Duration is Long, the Release Date is Modern, the Mood is Sad, and the Age is Middle-aged, then the Recommendation Score is Low.
pref17=np.min([input_low_rate,input_long_dur,input_new_year])
pref18=np.min([input_bad_mood,input_mid_age])
prefr9=np.max([pref17,pref18])
R9=np.fmin(prefr9,poor_score)

#summarization 
R_score_low=np.min([R3,R6,R9],axis=0)
R_score_avg=np.min([R2,R5,R7,R8],axis=0)
R_score_high=np.min([R1,R4],axis=0)
R = np.maximum(np.maximum(R_score_low, R_score_avg), R_score_high)

#Defuzzification
numerator = np.trapz(R * score, score)
denominator = np.trapz(R, score)

if denominator == 0:
    centroid = np.mean(score)  #Default to the mean of the score range
else:
    centroid = numerator / denominator

print("\nRecommendation Score:", centroid, "out of 10")

# Function to get movie recommendations based on the score
def get_recommendations(score, movies, num_recommendations=5):
    # Create a list of tuples with (title, score_difference)
    movie_scores = [(movie, abs(movie['rating'] - score)) for movie in movies]
    
    # Sort by smallest difference in score
    movie_scores.sort(key=lambda x: x[1])
    
    print("\nRecommended Movies:")
    print("-" * 50)
    for movie, _ in movie_scores[:num_recommendations]:
        print(f"Title: {movie['title']}")
        print(f"Rating: {movie['rating']}")
        print(f"Duration: {movie['duration']} minutes")
        print(f"Release Year: {movie['release_date']}")
        print(f"Mood: {movie['mood']}")
        print(f"Age Limit: {movie['age_limit']}+")
        print(f"Description: {movie['description']}")
        print("-" * 50)

# Get recommendations based on the calculated centroid score
get_recommendations(centroid, movies)

plt.figure(figsize=(18, 6))

plt.subplot(2, 3, 1)
plt.title("Movie Rating")
plt.plot(rate, low_rate, label="LOW RATING")
plt.plot(rate, avg_rate, label="MEDIUM RATING")
plt.plot(rate, high_rate, label="HIGH RATING")
plt.scatter([input_rate, input_rate, input_rate], [input_low_rate, input_avg_rate, input_high_rate])
plt.legend()

plt.subplot(2, 3, 2)
plt.title("Duration")
plt.plot(dur, short_dur, label="SHORT")
plt.plot(dur, avg_dur, label="AVERAGE")
plt.plot(dur, long_dur, label="LONG")
plt.scatter([input_dur, input_dur, input_dur], [input_short_dur, input_avg_dur, input_long_dur])
plt.legend()

plt.subplot(2, 3, 3)
plt.title("Released Year")
plt.plot(year, old_year, label="OLD")
plt.plot(year, rec_year, label="RECENT")
plt.plot(year, new_year, label="NEW")
plt.scatter([input_year, input_year, input_year], [input_old_year, input_rec_year, input_new_year])
plt.legend()

plt.subplot(2, 3, 4)
plt.title("Mood")
plt.plot(mood, bad_mood, label="BAD")
plt.plot(mood, normal_mood, label="NORMAL")
plt.plot(mood, great_mood, label="GREAT")
plt.scatter([input_mood, input_mood, input_mood], [input_bad_mood, input_normal_mood, input_great_mood])
plt.legend()

plt.subplot(2, 3, 5)
plt.title("User Age")
plt.plot(age, young_age, label="YOUNG")
plt.plot(age, mid_age, label="MID")
plt.plot(age, sen_age, label="SENIOR")
plt.scatter([input_age, input_age, input_age], [input_young_age, input_mid_age, input_sen_age])
plt.legend()

plt.subplot(2, 3, 6)
plt.title("Recommendation Score")
plt.plot(score, poor_score, label="POOR")
plt.plot(score, avg_score, label="AVERAGE")
plt.plot(score, high_score, label="HIGH")
plt.scatter([centroid], [0])
plt.legend()

plt.tight_layout()
plt.show()

import sys
import random
from mad_libs_wordgame.menu import countdown


economic = "Your computer has selected to play an Economic Mad Lib!"
scientific = "Your computer has selected to play a Scientific Mad Lib!"
musical = "Your computer has selected to play a Musical Mad Lib!"
playagain = "Would you like to play again?\nSelect 1 to play again.\nSelect 2 to exit.\nEnter your choice here: "
exitgame = "Sorry to see you leave... Goodbye!"
invalid = "Invalid option, try again."
congrats = "Your story is being created, and will print to the screen in 5 seconds... "
rc = random.choice

#-------------Wordbank below this line---------------------

nation = ['Canada','New Zealand','Mexico','Brazil','United States','China','India',
'Argentina','South Africa','France','Germany','South Korea','Japan','Italy','Norway',
'Switzerland','Sweden','Finland','Sudan','Morocco','Jamaica','Mongolia','Belize']
year = ['1985','1986','1987','1988','1989','1990','1991','1992','1993','1994',
'1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006',
'2007','2008','2009','2010','2020','2015']
food = ['pizza','pudding','apple','maple syrup','oats','chocolate','fried chicken',
'popcorn','potato','grits','macaroni','peanuts','jalapeno','beans','coconut','corn syrup']
animal = ['jaguar','bear','house cat','dog','penguin','albatross','elephant','dragon',
'snake','crocodile','dingo','reindeer','sloth','deer','moose','panda','trash panda']
color = ['red','green','blue','yellow','orange','purple','black','teal','aqua']
celebrity = ['Brad Pitt','Angelina Jolie','Tiger Woods','Dog the Bounty Hunter','Machine Gun Kelly',
'Megan Fox','Faith Hill','T-Pain','Keanu Reeves','Pete Davidson','Shia Labeouf','The Rock', 
'Miley Cyrus','Daniel Radcliff','Margot Robbie','Liam Neeson','Kevin Hart',
'Dave Chappelle','Vin Diesel','Nick Jonas','Chris Pratt','Mark Hamill','Adam Driver']
political_job = ['senator','mayor','sheriff','attorney general','governor',
'treasurer','comptroller']
fashion = ['Gucci','Prada','Saint Laurent','Louis Vuitton','Dolce & Gannana','Giorgio Armani',
'Burberry','Calvin Klein','Ralph Lauren','Valentino','Hugo Boss','Versace','DKNY','Yeezy']
activist = ['Gretta Thunberg','David Attenborough','Jane Goodall','Al Gore','Erin Brockovich',
'David Orr','Steve Irwin','Margaret Atwood','Walton Goggins','Mark Ruffalo','Leonardo DiCaprio']
superpower = ['invisibility','telepathic','superhuman strength','flying','shape shifting',
'super speed','telekinesis','teleportation','regenerative powers','divinity','x-ray vision']
wood = ['oak','maple','pine','walnut','teak','elm','sitka spruce','red cedar','bamboo',
'douglas fir','sapele','western hemlock','mohogany','poplar','redwood','cedar']
transport = ['train','ambulance','bullbozer','boat','bicycle','bus','carriage','hot-air balloon',
'tractor','motorcycle','rowboat','skateboard','forklift','scooter','horse','pack mule']
genre = ['rap','pop','blues','bro country','soul','latin','disco','heavy metal','progressive rock',
'jazz','dance pop','folk','reggae','grunge','glam rock','hip-hop','jazz fusion','punk','classical']
musician = ['Bruno Mars','Taylor Swift','Demi Lovato','Bon Jovi','Post Malone','Kanye West',
'TIm McGraw','Justin Bieber','Demi Lovato','Billie Eilish','Ariana Grande','Ed Sheeran','John Mayer']
industry = ['steel','oil','railroad','copper','pharmaceutical','automotive','paper','gaming',
'trucking','electrical','painting','telecommunication','shuttle driving','welding','sanitaion',
'brick','paper']
restaurant = ['Outback Steakhouse','McDonalds','Taco Bell','Pizza Hut','Applebees','Olive Garden',
'Chilis','Cracker Barrel','The Cheesecake Factory','Red Lobster','TGI Fridays','First Watch',
'Chuys','Famous Daves','Sizzler','Giordanos','Duffys Sports Grill','Chucky Cheese','Metro Diner']
city = ['Chicago','New York','Pheonix','Seattle','Washington','Memphis','Nashvile','Portland',
'Miami','Oakland','Tulsa','New Orleans','Los Angeles','Philadelphia','Boston','Cincinnati']
social = ['Snapchat','Facebook','Instagram','Twitter','TikTok','Tumblr','Reddit','Twitch','Vimeo']
shape = ['circle','oval','triangle','square','rectangle','rhombus','trapezoid','pentagon',
'hexagon','octogon','crescent','star','heart']
insect = ['spider','butterfly','earwig','beetle','maggot','wasp','termite','cockroach','bumblebee',
'mantis','moth','dragonfly','firefly','cicada','centipede','scorpion','stone fly','cricket']
liquid = ['juice','water','blood','gasoline','wine','beer','diesel','honey','coffee','milk','oil',
'syrup','kombucha','sweat']



#-------------Function for Auto Economic storyline coded below this line-----------

def auto_economic_storyline():
    print("")
    print(economic)
    nation_1 = rc(nation)
    food_1 = rc(food)
    year_1 = rc(year)
    animal_1 = rc(animal)
    nation_1 = rc(nation)
    color_1 = rc(color)
    fashion_1 = rc(fashion)
    celebrity_1 = rc(celebrity)
    political_job_1 = rc(political_job)
    economic_story = (
f"{nation_1} is currently the largest exporter of textiles in the world. When the nation was\n" +
f"established in {year_1} the largest crop at the time was {food_1} and the highest yielding\n" +
f"livestock was {animal_1}. Many economists believe these factors played a major role in {nation_1}\n" +
f"developing it's {color_1} infrastructure. While there were many attempts by {nation_1} to grow \n" +
f"it's economy, it was only when {celebrity_1} decided to run for the position of {political_job_1}\n" +
f"in their hometown and promoted {fashion_1} fabrics on the campaign trail that the major export\n" +
f"stopped being {food_1} & {animal_1} and became {fashion_1}. Business leaders across {nation_1}\n" +
f"rejoiced at {celebrity_1}'s show of goodwill, and increased production of {fashion_1} has begun\n" +
f"to have a real lasting impact on {nation_1}'s economy. Today, {nation_1} is the largest exporter\n" +
f"of {fashion_1} products in the world.")
    print("")
    print(congrats)
    print("")
    countdown(3)
    print(economic_story)
    print("")
    completed = input(playagain)
    if completed == "1":
        print("")
    elif completed == "2":
        print(exitgame)
        sys.exit()
    else:
        print(invalid)

#------------Function for Auto Scientific storyline is coded below this line---------

def auto_scientific_storyline():
    print("")
    print(scientific)
    nation_1 = rc(nation)
    food_1 = rc(food)
    year_1 = rc(year)
    animal_1 = rc(animal)
    nation_1 = rc(nation)
    color_1 = rc(color)
    wood_1 = rc(wood)
    activist_1 = rc(activist)
    superpower_1 = rc(superpower)
    transport_1 = rc(transport)
    scientific_story =(
f"Scientists have determined that the {animal_1} went extinct in {year_1}. While the factors\n" +
f"contributing to this extinction event are currently unknown, {activist_1} believes pockets\n" +
f"of {animal_1}'s may still exist in {nation_1}'s dense {wood_1} forests, located in remote areas\n" +
f"only accessible by {transport_1}. Local elders of the region believe that {animal_1}'s have\n" +
f"mystical powers, and the presence of the {animal_1} is often associated with experiencing \n" +
f"dreams of {superpower_1} and bountiful {food_1} harvests. Ceremonies are often held to worship\n" +
f"the {animal_1}, and it is common for the elders to don {color_1} facepaint on the eve of the\n" +
f"fall equinox in honor of the {animal_1} with hopes of summoning a safe and successful {food_1}\n" +
f"harvest. And lately, the {food_1} harvest has been thriving. Undoubtedly, the beautiful sheen\n" +
f"of {nation_1}'s {wood_1} landscape gives us hope that {activist_1} is correct in the assessment\n" +
f"that {animal_1}'s still roam the hills of {nation_1} to this very day, if only in our hopefull\n" +
f"dreams of {superpower_1}.")
    print("")
    print(congrats)
    print("")
    countdown(3)
    print(scientific_story)
    print("")
    completed = input(playagain)
    if completed == "1":
        print("")
    elif completed == "2":
        print(exitgame)
        sys.exit()
    else:
        print(invalid)

#---------Function for auto Musical storyline is coded below this line-------------------------------

def auto_musical_storyline():
    print("")
    print(musical)
    industry_1 = rc(industry)
    city_1 = rc(city)
    year_1 = rc(year)
    animal_1 = rc(animal)
    musician_1 = rc(musician)
    color_1 = rc(color)
    restaurant_1 = rc(restaurant)
    social_1 = rc(social)
    celebrity_1 = rc(celebrity)
    shape_1 = rc(shape)
    genre_1 = rc(genre)
    insect_1 = rc(insect)
    liquid_1 = rc(liquid)

    musical_story = (
f"Most fans of {genre_1} consider the greatest performer of the modern era to be {musician_1}.\n" +
f"Born a {city_1} native, the music of {musician_1} is heavily influenced by the cities modest,\n" +
f"hard working {industry_1} industry workers. For years, {musician_1} worked as a bartender\n" +
f"at {restaurant_1}, uploading music to {social_1} during off time as a hobby. But all of that\n" +
f"changed in the spring of {year_1}, after a track titled {insect_1} {liquid_1} went viral on\n" +
f"{social_1}. Shortly after, {celebrity_1} signed the artist onto a 10-album record deal with upstart\n" +
f"record label, {color_1} {animal_1} records. In the Fall of {year_1}, {musician_1} began touring\n" +
f"non-stop to promote their first album, aptly titled - The {city_1} {industry_1} Connection.\n" +
f"Known for a {shape_1} stage and bright {color_1} lasers, the live tour was a spectical.\n" +
f"{musician_1}'s {city_1} fanbase would travel hundreds of miles to help sell out shows,\n" +
f"providing whatever support they could for their hometown hero. While {celebrity_1} may be\n" +
f"creditted with discovering {musician_1} through a {social_1} viral video, the dedicated\n" +
f"{city_1} fanbase is ultimately responsible for making {musician_1} the powerhouse {genre_1}\n" +
"performer known today.")
    print("")
    print(congrats)
    print("")
    countdown(5)
    print(musical_story)
    print("")
    completed = input(playagain)
    if completed == "1":
        print("")
    elif completed == "2":
        print(exitgame)
        sys.exit()
    else:
        print(invalid)

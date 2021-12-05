import sys
from mad_libs_wordgame.menu import countdown

economic = "You have selected to play an Economic Mad Lib!"
scientific = "You have selected to play a Scientific Mad Lib!"
musical = "You have selected to play a Musical mad Lib!"
instructions = "You will now be prompted to enter a series of words.\nOnce finished, a completed story will print to the screen.\nNow let's get started!"
playagain = "Would you like to play again?\nSelect 1 to play again.\nSelect 2 to exit.\nEnter your choice here: "
exitgame = "Sorry to see you leave... Goodbye!"
congrats = "Great work! Your story has been created, and will print to the screen in 5 seconds..."
invalid = "Invalid option, try again."

#-------------Function for Economic storyline coded below this line-----------
def economic_storyline():
    print(economic)
    print("")
    print(instructions)
    print("")
    nation = input("Enter the name of a nation: ")
    year = input("Enter a year: ")
    food = input("Enter a food: ")
    animal = input("Enter an animal: ")
    color = input("Enter a color: ")
    celebrity = input("Enter the name of a celebrity: " )
    political_job = input("Enter a title held by an elected official: ")
    fashion = input("Enter the name of a brand: ")
    economic_story = (
f"{nation} is currently the largest exporter of textiles in the world. When the nation was\n" +
f"established in {year} the largest crop at the time was {food} and the highest yielding\n" +
f"livestock was {animal}. Many economists believe these factors played a major role in {nation}\n" +
f"developing it's {color} infrastructure. While there were many attempts by {nation} to grow \n" +
f"it's economy, it was only when {celebrity} decided to run for the position of {political_job}\n" +
f"in their hometown and promoted {fashion} fabrics on the campaign trail that the major export\n" +
f"stopped being {food} & {animal} and became {fashion}. Business leaders across {nation}\n" +
f"rejoiced at {celebrity}'s show of goodwill, and increased production of {fashion} has begun\n" +
f"to have a real lasting impact on {nation}'s economy. Today, {nation} is the largest exporter\n" +
f"of {fashion} products in the world.")
    print("")
    print(congrats)
    print("")
    countdown(5)
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

#------------Function for Scientific storyline is coded below this line---------

def scientific_storyline():
    print(scientific)
    print("")
    print(instructions)
    print("")
    nation = input("Enter the name of a nation: ")
    year = input("Enter a year: ")
    food = input("Enter a food: ")
    animal = input("Enter an animal: ")
    color = input("Enter a color: ")
    activist = input("Enter the name of a famous activist: " )
    superpower = input("Enter a specific class of superpower: ")
    wood = input("Enter the name of a species of tree: ")
    transport = input("Enter the name of a vehicle used in transportation: ")
    scientific_story =(
f"Scientists have determined that the {animal} went extinct in {year}. While the factors\n" +
f"contributing to this extinction event are currently unknown, {activist} believes pockets\n" +
f"of {animal}'s may still exist in {nation}'s dense {wood} forests, located in remote areas\n" +
f"only accessible by {transport}. Local elders of the region believe that {animal}'s have\n" +
f"mystical powers, and the presence of the {animal} is often associated with experiencing \n" +
f"dreams of {superpower} and bountiful {food} harvests. Ceremonies are often held to worship\n" +
f"the {animal}, and it is common for the elders to don {color} facepaint on the eve of the\n" +
f"fall equinox in honor of the {animal} with hopes of summoning a safe and successful {food}\n" +
f"harvest. And lately, the {food} harvest has been thriving. Undoubtedly, the beautiful sheen\n" +
f"of {nation}'s {wood} landscape gives us hope that {activist} is correct in the assessment\n" +
f"that {animal}'s still roam the hills of {nation} to this very day, if only in our hopefull\n" +
f"dreams of {superpower}.")
    print("")
    print(congrats)
    print("")
    countdown(5)
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

#---------Function for Musical storyline is coded below this line-------------------------------

def musical_storyline():
    print(musical)
    print("")
    print(instructions)
    print("")
    genre = input("Enter the name of a genre of music: ")
    musician = input("Enter the name of a famous musician: ")
    industry = input("Enter the name of an industry: ")
    restaurant = input("Enter the name of a restaurant chain: ")
    city = input("Enter the name of a city: ")
    social = input("Enter the name of a social media app: ")
    celebrity = input("Enter the name of a movie star from the 90's: ")
    year = input("Enter a year: ")
    color = input("Enter the name of a color: ")
    shape = input("Enter the name of a shape: ")
    insect = input("Enter the name of an insect: ")
    liquid = input("Enter the name of a liquid: " )
    animal = input("Enter the name of an animal: ")
    musical_story = (
    f"Most fans of {genre} consider the greatest performer of the modern era to be {musician}.\n" +
    f"Born a {city} native, the music of {musician} is heavily influenced by the cities modest,\n" +
    f"hard working {industry} industry workers. For years, {musician} worked as a bartender\n" +
    f"at {restaurant}, uploading music to {social} during off time as a hobby. But all of that\n" +
    f"changed in the spring of {year}, after a track titled {insect} {liquid} went viral on\n" +
    f"{social}. Shortly after, {celebrity} signed the artist onto a 10-album record deal with upstart\n" +
    f"record label, {color} {animal} records. In the Fall of {year}, {musician} began touring\n" +
    f"non-stop to promote their first album, aptly titled - The {city} {industry} Connection.\n" +
    f"Known for a {shape} stage and bright {color} lasers, the live tour was a spectical.\n" +
    f"{musician}'s {city} fanbase would travel hundreds of miles to help sell out shows,\n" +
    f"providing whatever support they could for their hometown hero. Ehile {celebrity} may be\n" +
    f"creditted with discovering {musician} through a {social} viral video, the dedicated\n" +
    f"{city} fanbase is ultimately responsible for making {musician} the powerhouse {genre}\n" +
    "performer known today."
    )
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

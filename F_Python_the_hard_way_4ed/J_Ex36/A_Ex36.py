import time, sys


def welcome():
    welcome = "Welcome to Cyberpunk 2020. The game of the dark future."

    for char in welcome:
        time.sleep(0.001)
        print(char, end="")
        time.sleep(0.001)


def start():
    welcome()
    promt = "\n>>>"
    char_name = f"\n\nFirst you must pick you name. Try to make it cool.{promt}"
    name = input(char_name).capitalize()
    while len(name) < 4:
        name = input(char_name)

    char_class = "\nNow pick your class:" \
                 "\n1.Nomad" \
                 "\n2.Solo" \
                 f"\n3.Techie{promt}"
    clas = input(char_class)

    char_hp = 0

    if clas == "1":
        clas = "Nomad"
        print(f"Nice choice {name} you are now a {clas}")
        char_hp = 5
    elif clas == "2":
        clas = "Solo"
        print(f"Nice choice {name} you are now a {clas}")
        char_hp = 7
    elif clas == "2":
        clas = "Techie"
        print(f"Nice choice {name} you are now a {clas}")
        char_hp = 4
    else:
        print("You are doomed! You are a regular civilian.")
        char_hp = 2

    branch1(name)

def game_over(string):
    print(f"{string} Game over.")
    sys.exit(0)


def continuation(string):
    print(f"{string} To be continued...")
    sys.exit(0)


def window():
    prompt = "\n>>>"
    description = f"Hell no! You decide to leave throughout the window using the fire staircase.\n" \
                  f"A police officer sees you and gives you a warning..."
    for line in description.split("\n"):
        time.sleep(0.5)
        print(line)
        time.sleep(0.5)
    choice = input(f"Do you obey or do you run?{prompt}")
    if choice.lower() == "run":
        description = f"You enter the building trough the first door you see\n" \
                      f"gunfire start coming your way from behind, the alarms in the building\n" \
                      f"start going off, heart beating fast, but you are confident, this iss your turf\n" \
                      f"you know every corner like the palm of your hand, they cannot trap you here,\n" \
                      f"but you need to get out fast before more come, a shoot out with the police is\n" \
                      f"a one way ticket to a 'better place'..."
        for line in description.split("\n"):
            time.sleep(0.5)
            print(line)
            time.sleep(0.5)

        continuation("Will you find your way out?")

    elif choice.lower() == "obey":
        game_over("How nice of you to obey the law,\n"
                  "But when you hide is on the line\n"
                  "it no may be the smartest thing to do.")
    else:
        game_over("That sure is a one way ticket to a 'better place'...")


def door():
    prompt = "\n>>>"
    description = f"Hell no! But there is not need to call unnecessary " \
                  f"attention so you take the envelope and\n" \
                  f"leave trough the door.\n" \
                  f"Just another day in the city. " \
                  f"Being bold is what makes you, You. No need to panic just walk\n" \
                  f"you own it...\n"
    for line in description.split("\n"):
        time.sleep(0.5)
        print(line)
        time.sleep(0.5)

    choice = input(f"Do you want to take you ride or leave walking?{prompt}")

    if "leave" in choice.lower().strip():
        description = f"You want to make yourself harder to track so you leave " \
                      f"walking if you happen to need a set of\n" \
                      f"wheels later you can always 'borrow' one.\n" \
                      f"Now where to, is the question. You have a choomb " \
                      f"that used to be a fixer and owes you\n" \
                      f"a favor and some money maybe it's time to call in the favor..."

        for line in description.split("\n"):
            time.sleep(0.5)
            print(line)
            time.sleep(0.5)
        continuation("Will your choomb answer?")
    elif "ride" in choice.lower().strip():
        description = f"Sometimes being too bold can play against you." \
                      f" But how could you leave your favorite bike, it was part of you\n" \
                      f"and you are going to war you might as well go riding in style.."
        for line in description.split("\n"):
            time.sleep(0.5)
            print(line)
            time.sleep(0.5)
        continuation("Will you get out?")


def branch1(name):
    location = f"{name}"
    description = f"Just another day in Night City.\n" \
                  f"You are currently in your apartment in one of Night City many mega-buildings\n" \
                  f"After a long night of hustling you wake up ready to start again,\n" \
                  f"so is life in Night City, at least for those not fortunate enough.\n" \
                  f"But today it's gonna be different or same bullshit different flavor.\n" \
                  f"You notice an envelope that someone slipped under you door,\n" \
                  f"you are smart instead of rushing to pick it up you grab your " \
                  f"trusty piece of iron,\n" \
                  f"no that it seems to be a need for it, but you are experienced " \
                  f"enough to know shit can go\n" \
                  f"sideways form one moment to the other in this hell hole of town. " \
                  f"After putting some clothes on\n" \
                  f"you open the door and notice the ambient is quieter than normal, " \
                  f"but you think nothing of it.\n" \
                  f"You close the door and pick the envelope up, " \
                  f"it hasn't blown up by now it's probably safe to open.\n"

    open_envelope = f"You open the envelope and there are 1500 eddies in it, " \
                    f"you take a deep breath and think\n" \
                    f"in every possible person that could have done such a thing. " \
                    f"Couple of names come to mind but\n" \
                    f"without a note or anything else to go on you are just guessing, " \
                    f"a dangerous thing to do in this city.\n"

    for line in description.split("\n"):
        time.sleep(0.5)
        print(line)
        time.sleep(0.5)
    prompt = "\n>>>"
    choice = input(f"What do you do?{prompt}")

    if choice.lower() == "open":
        for line in open_envelope.split("\n"):
            time.sleep(0.5)
            print(line)
            time.sleep(0.5)
    else:
        game_over("You were captured by random people while preparing breakfast.")

    description = f"You reach to your window to see it there are any suspicious vehicles around\n" \
                  f"nothing out of the ordinary but you hear a lot of sirens going off.\n" \
                  f"You put the news to see what's going on and boom!!!!\n" \
                  f"An oil camp outside Night City was bombarded by a terrorist organization or so that seems\n" \
                  f"you are old enough to know that if it in the news its not the entire truth.\n" \
                  f"This is big, you feel it, the piece of iron in your arm feels it...\n" \
                  f"You start to put two and two together and figure out that is just a matter of time\n" \
                  f"before you uninvited guests start knocking on your door until it drops to the ground.\n" \
                  f"The question is do you want to be there when that happens?"
    if choice.lower().strip() == "open":
        for line in description.split("\n"):
            time.sleep(0.5)
            print(line)
            time.sleep(0.5)
        choice = input(f"Want to leave or stay?{prompt}")
        if choice.lower().strip() == "leave":
            choice = input(f"Leave trough the window or the door?{prompt}")
            if choice.lower().strip() == "window":
                window()
            elif choice.lower().strip() == "door":
                door()
            else:
                game_over("You decided to chill in your apparent\n"
                          "when police came you regretted that decision.\n")
        else:
            game_over("You were captured by the corps you put a good fight tho.")


start()

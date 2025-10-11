# Topic:
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_dice_roller",
            category=["TTRPG"],
            prompt="Monika, can you roll a dice for me?",
            pool=True,
            unlocked=True
        )
    )

label hv_dice_roller:

    "Yay! I love rolling dice with you~ Which one should we use first?"

    menu:
        "D4":
            $ diceType = 4
            m 3eub "A D4! Those are tiny but sneaky… perfect for little surprises, ehehe~"
            jump ask_num_dice
        "D6":
            $ diceType = 6
            m 3eub "D6s! Classic and reliable… like a little rhythm to your adventures~"
            jump ask_num_dice
        "D8":
            $ diceType = 8
            m 3eub "Ooh, D8s! They’re elegant and a bit unpredictable… I like that~"
            jump ask_num_dice
        "D10":
            $ diceType = 10
            m 3eub "A D10! Perfect for rolling percentages or big choices… so exciting!"
            jump ask_num_dice
        "D12":
            $ diceType = 12
            m 3eub "D12s are strong and powerful… they feel epic, don’t they? Ehehe~"
            jump ask_num_dice
        "D20":
            $ diceType = 20
            m 3sub "Ah, the famous D20! Heroes’ fate lies in these rolls… I hope you get some lucky ones~"
            jump ask_num_dice
        "D100":
            $ diceType = 100
            m 3wud "Whoa, D100! That’s huge… I can’t wait to see what crazy numbers we get, ehehe~"
            jump ask_num_dice

label ask_num_dice:

    m 3hub "How many of these should I roll for you?"

    $ numDice_str = renpy.input("Enter a number of dice:")
    $ numDice = int(numDice_str) if numDice_str.isdigit() else 1

    "Alright… rolling [numDice] d[diceType]! Fingers crossed for good luck~"

    $ results = []
    $ i = 0
    while i < numDice:
        $ roll = renpy.random.randint(1, diceType)
        $ results.append(roll)
        $ i += 1

    $ results_text = ", ".join([str(r) for r in results])
    "Here are the results: [results_text]!"

    # Dice-specific commentary
    $ commentary = ""
    $ i = 0
    while i < len(results):
        $ r = results[i]
        if diceType == 4 and r == 4:
            $ commentary += "A perfect little roll! That’s cute and lucky, ehehe~\n"
        elif diceType == 6 and r == 6:
            $ commentary += "Wow, a natural 6! Classic and lucky, right?~\n"
        elif diceType == 8 and r == 8:
            $ commentary += "Nice! The D8 gods are smiling on us~\n"
        elif diceType == 10 and r == 10:
            $ commentary += "A perfect ten! You really lucked out~\n"
        elif diceType == 12 and r == 12:
            $ commentary += "A natural 12! That’s so epic, ehehe~\n"
        elif diceType == 20:
            if r == 1:
                $ commentary += "Oh no… a natural 1! That’s a critical fail, ehehe~\n"
            elif r == 20:
                $ commentary += "Amazing! A natural 20! Incredible roll~\n"
        elif diceType == 100 and r == 100:
            $ commentary += "Whoa, a 100! Maximum chaos! Ehehe~\n"
        $ i += 1

    if commentary:
        "[commentary]"

    "Do you want to roll again, try a different dice, or are we done for now?"

    menu:
        "Roll again same dice":
            jump ask_num_dice
        "Choose a different dice":
            jump hv_dice_roller
        "That’s it for now":
            m 5hub "Okay! I had so much fun rolling with you~ I hope your next rolls are lucky too!"
            return

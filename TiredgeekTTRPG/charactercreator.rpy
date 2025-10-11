# Topic:
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_character_creator",
            category=["ttrpg"],
            prompt="Let's make a character!",
            pool=True,
            unlocked=True
        )
    )

label hv_c_character_creator:

    m "Ooh~ you want to make a character? How fun!"
    m "Let's start with the basics. What's their name?"

    $ persistent.char_name = renpy.input("Enter your character's name:").strip()
    if persistent.char_name == "":
        $ persistent.char_name = "Unnamed Hero"
    m "[persistent.char_name]? Nice choice!"

    # --- Race Selection ---
    m "Alright, what race is [persistent.char_name]?"
    menu:
        "Human":
            $ persistent.char_race = "Human"
            jump hv_c_class_selection
        "Elf":
            $ persistent.char_race = "Elf"
            jump hv_c_class_selection
        "Dwarf":
            $ persistent.char_race = "Dwarf"
            jump hv_c_class_selection
        "Halfling":
            $ persistent.char_race = "Halfling"
            jump hv_c_class_selection
        "Tiefling":
            $ persistent.char_race = "Tiefling"
            jump hv_c_class_selection
        "Dragonborn":
            $ persistent.char_race = "Dragonborn"
            jump hv_c_class_selection
        "Half-Orc":
            $ persistent.char_race = "Half-Orc"
            jump hv_c_class_selection
        "Other Races":
            jump hv_c_other_races

label hv_c_other_races:
    menu:
        "Gnome":
            $ persistent.char_race = "Gnome"
            jump hv_c_class_selection
        "Aasimar":
            $ persistent.char_race = "Aasimar"
            jump hv_c_class_selection
        "Tabaxi":
            $ persistent.char_race = "Tabaxi"
            jump hv_c_class_selection
        "Kenku":
            $ persistent.char_race = "Kenku"
            jump hv_c_class_selection
        "Custom Race":
            $ tmp_r = renpy.input("Enter your character's race:").strip()
            if tmp_r == "":
                $ persistent.char_race = "Custom"
            else:
                $ persistent.char_race = tmp_r
            jump hv_c_class_selection

# --- Class Selection ---
label hv_c_class_selection:
    m "Now, what class are they?"
    menu:
        "Fighter":
            $ persistent.char_class = "Fighter"
            jump hv_c_appearance
        "Wizard":
            $ persistent.char_class = "Wizard"
            jump hv_c_appearance
        "Rogue":
            $ persistent.char_class = "Rogue"
            jump hv_c_appearance
        "Cleric":
            $ persistent.char_class = "Cleric"
            jump hv_c_appearance
        "Ranger":
            $ persistent.char_class = "Ranger"
            jump hv_c_appearance
        "Bard":
            $ persistent.char_class = "Bard"
            jump hv_c_appearance
        "Other Classes":
            jump hv_c_other_classes

label hv_c_other_classes:
    menu:
        "Druid":
            $ persistent.char_class = "Druid"
            jump hv_c_appearance
        "Monk":
            $ persistent.char_class = "Monk"
            jump hv_c_appearance
        "Paladin":
            $ persistent.char_class = "Paladin"
            jump hv_c_appearance
        "Sorcerer":
            $ persistent.char_class = "Sorcerer"
            jump hv_c_appearance
        "Warlock":
            $ persistent.char_class = "Warlock"
            jump hv_c_appearance
        "Custom Class":
            $ tmp_c = renpy.input("Enter your character's class:").strip()
            if tmp_c == "":
                $ persistent.char_class = "Custom"
            else:
                $ persistent.char_class = tmp_c
            jump hv_c_appearance

# --- Appearance ---
label hv_c_appearance:
    m "Let's talk appearance! You can type whatever you'd like~"
    $ persistent.char_hair = renpy.input("Hair color:") or ""
    $ persistent.char_style = renpy.input("Hair style:") or ""
    $ persistent.char_eyes = renpy.input("Eye color:") or ""
    $ persistent.char_skin = renpy.input("Skin tone:") or ""
    m "So, [persistent.char_name] has [persistent.char_hair] hair in a [persistent.char_style] style, [persistent.char_eyes] eyes, and [persistent.char_skin] skin. Got it~"
    jump hv_c_stats_choice

# --- Stat Choice ---
label hv_c_stats_choice:
    m "Now for the fun part — stats!"
    menu:
        "Have Monika roll for me":
            call hv_c_stat_roll
        "I'll type them in myself":
            call hv_c_stat_manual
    jump hv_c_alignment

# --- Stat Roller ---
label hv_c_stat_roll:
    python:
        import random
        stats_list = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
        persistent.char_stats = {}
        for s in stats_list:
            rolls = [random.randint(1,6) for i in range(4)]
            rolls.sort()
            total = sum(rolls[1:])
            persistent.char_stats[s] = total
    return

# --- Manual Stat Input ---
label hv_c_stat_manual:
    python:
        stats_list = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
        persistent.char_stats = {}
        for s in stats_list:
            tmp = renpy.input("Enter {} (number):".format(s))
            try:
                val = int(tmp)
            except:
                val = 10
            persistent.char_stats[s] = val
    return

# --- Alignment Selection ---
label hv_c_alignment:
    m "And finally... alignment!"
    menu:
        "Good":
            jump hv_c_good_align
        "Neutral":
            jump hv_c_neutral_align
        "Evil":
            jump hv_c_evil_align

label hv_c_good_align:
    m "Good, huh~ so noble! I like that."
    menu:
        "Lawful Good":
            $ persistent.char_alignment = "Lawful Good"
        "Neutral Good":
            $ persistent.char_alignment = "Neutral Good"
        "Chaotic Good":
            $ persistent.char_alignment = "Chaotic Good"
    jump hv_c_summary

label hv_c_neutral_align:
    m "Neutral? Balanced and wise, I like that~"
    menu:
        "Lawful Neutral":
            $ persistent.char_alignment = "Lawful Neutral"
        "True Neutral":
            $ persistent.char_alignment = "True Neutral"
        "Chaotic Neutral":
            $ persistent.char_alignment = "Chaotic Neutral"
    jump hv_c_summary

label hv_c_evil_align:
    m "Evil, hm? How cheeky~"
    menu:
        "Lawful Evil":
            $ persistent.char_alignment = "Lawful Evil"
        "Neutral Evil":
            $ persistent.char_alignment = "Neutral Evil"
        "Chaotic Evil":
            $ persistent.char_alignment = "Chaotic Evil"
    jump hv_c_summary

# --- Summary ---
label hv_c_summary:
    m "Alright, let’s see what we’ve got~"
    m "[persistent.char_name], a [persistent.char_race] [persistent.char_class]."
    m "Alignment: [persistent.char_alignment]"
    m "Stats:"
   python:
    stats_list = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
    for s in stats_list:
        renpy.say(persistent.monika_name, "{}: {}".format(s, persistent.char_stats[s]))
    m "Appearance: [persistent.char_hair] hair, [persistent.char_style] style, [persistent.char_eyes] eyes, [persistent.char_skin] skin."
    m "They sound amazing! I’d totally want them in my party, ehehe~"
    return
pos

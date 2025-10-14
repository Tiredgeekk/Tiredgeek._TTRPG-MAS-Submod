init 5 python:
    # --- TTRPG Compliments ---
    
    # Heal First
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_comp_heal",
            category=['mas_compliment'],
            prompt="I'll always heal you first",
            unlocked=True
        ), code="CMP"
    )

    # Amazing Bard
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_comp_bard",
            category=['mas_compliment'],
            prompt="You'd be an amazing bard",
            unlocked=True
        ), code="CMP"
    )

    # Better than a Nat 20
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_comp_nat20",
            category=['mas_compliment'],
            prompt="You're better than a Nat 20",
            unlocked=True
        ), code="CMP"
    )

    # Dungeon Dare
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_comp_dungeon",
            category=['mas_compliment'],
            prompt="I'd face the scariest dungeons just to be with you",
            unlocked=True
        ), code="CMP"
    )

    # Last Healing Potion (Ultra-Special)
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_comp_last_potion",
            category=['mas_compliment'],
            prompt="I'd always give you the last healing potion",
            unlocked=True
        ), code="CMP"
    )


# --- Event Labels ---

# Heal First
label mas_comp_heal:
    m 3wublb "Oh! You’d always heal me first? That’s so thoughtful~"
    m 5rublb "I’d feel so safe with you around in any adventure!"
    $ mas_gainAffection(2, bypass=False)
return "love"

# Amazing Bard
label mas_comp_bard:
    m 7wublb "You really think so,[player]? Thank you!" 
    m 5mublb "I'll be the bard, you my muse ehe..~"
    $ mas_gainAffection(2, bypass=False)
return "love"

# Better than a Nat 20
label mas_comp_nat20:
    m 4wubld "Better than a Nat 20?" 
    m 5fkbltub "That makes me feel so special [player]!"
    $ mas_gainAffection(3, bypass=False)
return "love"

# Dungeon Dare
label mas_comp_dungeon:
    m 5wublb "The scariest dungeons? Just to be with me? Aww, [player]~"
    m 5rublb "I’d face any monster if it means adventuring with you!"
    $ mas_gainAffection(3, bypass=False)
return "love"

# Last Healing Potion (Ultra-Special)
label mas_comp_last_potion:
    m 4wublb "The last healing potion… just for me? You're too sweet, [player]!"
    m 5rublb "I feel like the luckiest adventurer alive!"
    $ mas_gainAffection(3, bypass=False)
return "love"

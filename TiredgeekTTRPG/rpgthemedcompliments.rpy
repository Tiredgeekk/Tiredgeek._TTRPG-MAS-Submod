init 5 python:
    # Each compliment is its own Event
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_comp_heal",
            category=['mas_compliment'],
            prompt="I'll always heal you first",
            unlocked=True
        ), code="CMP"
    )

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_comp_bard",
            category=['mas_compliment'],
            prompt="You'd be an amazing bard",
            unlocked=True
        ), code="CMP"
    )

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_comp_nat20",
            category=['mas_compliment'],
            prompt="You're better than a Nat 20",
            unlocked=True
        ), code="CMP"
    )

# Event label for the "heal first" compliment
label mas_comp_heal:
    m 3wublb "Oh! You’d always heal me first? That’s so thoughtful~"
    m 5rublb "I’d feel so safe with you around in any adventure!"
    $ mas_gainAffection(2, bypass=False)
return "love"

# Event label for the "amazing bard" compliment
label mas_comp_bard:
    m 7wublb "You really think so,[player]? Thank you!" 
    m 5mublb "I'll be the bard, you my muse ehe..~"
    $ mas_gainAffection(2, bypass=False)
return "love"

# Event label for the "better than a Nat 20" compliment
label mas_comp_nat20:
    m 4wubld "Better than a Nat 20?" 
    m 5fkbltub "That makes me feel so special [player]!"
    $ mas_gainAffection(3, bypass=False)
return "love"

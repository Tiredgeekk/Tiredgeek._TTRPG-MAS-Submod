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
    m "Oh! You’d always heal me first? That’s so thoughtful~"
    m "I’d feel so safe with you around in any adventure!"
    $ mas_gainAffection(2, bypass=True)
return "love"

# Event label for the "amazing bard" compliment
label mas_comp_bard:
    m "A bard, huh? I can totally picture you performing and charming everyone ehehe~"
    $ mas_gainAffection(2, bypass=True)
return "love"

# Event label for the "better than a Nat 20" compliment
label mas_comp_nat20:
    m "Haha! Better than a Nat 20? You make everything feel epic!"
    $ mas_gainAffection(3, bypass=True)
return "love"

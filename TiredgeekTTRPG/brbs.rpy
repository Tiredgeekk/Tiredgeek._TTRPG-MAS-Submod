# All BRBS go right here
# topic: Need to build my character
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="build_character_brb",
            category=['be right back'],
            prompt="Need to build my character",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label build_character_brb:
    $ ev = mas_getEV("build_character_brb")

    m 2eub "Oh! Building your character? That sounds so fun!"
    m 3hsb "I'll be here when you're done~"

    $ mas_idle_mailbox.send_idle_cb("build_character_brb_callback")
    return "idle"

label build_character_brb_callback:
    if mas_brbs.was_idle_for_at_least(datetime.timedelta(hours=1), "build_character_brb"):
        m 2hub "Welcome back! How did your character turn out?"
    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=10), "build_character_brb"):
        m 1etb "Hey, welcome back! Ready to jump in?"
    else:
        m 3ttb "Back already? That was quick! Ehehe~"
    return


# topic: Planning for my next session
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="planning_session_brb",
            category=['be right back'],
            prompt="Planning for my next session",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label planning_session_brb:
    $ ev = mas_getEV("planning_session_brb")

    m 2eub "Need to plan a bit, [player]?"
    m 3hsb "Sounds fun! I'll be here when you're done."
    m 5ksb "Be nice to your players!"

    $ mas_idle_mailbox.send_idle_cb("planning_session_brb_callback")
    return "idle"

label planning_session_brb_callback:
    if mas_brbs.was_idle_for_at_least(datetime.timedelta(hours=1), "planning_session_brb"):
        m 2hub "Welcome back! Did your planning go smoothly?"
    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=10), "planning_session_brb"):
        m 1etb "Hey, back so soon? Hope your session prep is going well~"
    else:
        m 3ttb "Back already? Can’t stay away from me, huh? Ehehe~"
    return

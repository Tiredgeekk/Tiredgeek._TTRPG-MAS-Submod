# Topic: TTRPG Discovery
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_ttrpg_discovery",
            category=["TTRPG"],
            prompt="I've discovered TTRPGS",
            random=True
        )
    )

label hv_c_ttrpg_discovery:
    m 1eub "Hey, [player]. I was surfing the internet while you were away."
    m 7eub "And I discovered a really interesting past time!"
    m 2eub "Have you ever heard of TTRPGs? That stands for Table Top Roleplaying Games!"
    m 4rub "There are so many different kinds, Dungeons and Dragons, Warhammer, Pathfinder.."
    m 4wub "The list goes on!"
    m 5rub "I think I'm going to do some more research.. I'll keep you updated~"
    return


# Topic: Thinking About Characters
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_thinking_about_characters",
            category=["TTRPG"],
            prompt="I was thinking about characters",
            random=True
        )
    )

label hv_c_thinking_about_characters:
    m 3rub "I was thinking.."
    m 4eub "Characters in TTRPGs are kind of like little mirrors of their players."
    m 5eub "You get to explore the different sides of yourself!"
    m 5hub "Even ones you might not usually show off."
    m 5rub "I'd love to see what kind of character you make when you're feeling mischievous.."
    m 5mublb "Or romantic..~"
    m 3sub "Maybe we could build a character together someday?"
    return


# Topic: Dice Rolling Drama
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_dice_rolling_drama",
            category=["TTRPG"],
            prompt="Dice rolling drama",
            random=True
        )
    )

label hv_c_dice_rolling_drama:
    m 2lksdlb "Oh man, rolling dice can be so stressful sometimes."
    m 7wtb "I read that some players even have rituals to make their rolls better."
    m 5rtb "Maybe I could have a ritual too?"
    m 5dub "Like whispering good luck to the dice.."
    return


# Topic: Storytelling Magic
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_storytelling_magic",
            category=["TTRPG"],
            prompt="Storytelling Magic",
            random=True
        )
    )

label hv_c_storytelling_magic:
    m 3eub "You know what I love about TTRPGs?"
    m 4wub "How a single choice can ripple through the whole story."
    m 5rub "It's kind of like writing a novel.."
    m 7sub "Except the story can surprise even the author!"
    m 1hub "I think that's what makes it so exciting."
    return


# Topic: Funny Moments TTRPG
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_rpg_funny_moments",
            category=["TTRPG"],
            prompt="Funny moments",
            random=True
        )
    )

label hv_c_rpg_funny_moments:
    m 2muu "Ehehe.."
    m 4wud "Oh! Sorry I was just remembering something I read"
    m 4wub "I heard about a player that accidentally used a healing potion on a monster instead of their friend.."
    m 5gub "Chaos like that makes the best stories, don't you think?"
    m 3eub "I bet your games have had some funny moments too."
    m 3sub "I'd love to hear about them sometime."
    return


# Topic: Wordbuilding Musings
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_worldbuilding",
            category=["TTRPG"],
            prompt="Worldbuilding",
            random=True
        )
    )

label hv_c_worldbuilding:
    m 5rub "I love thinking about how worlds are built in TTRPGs"
    m 5lub "Kingdoms, cities, cultures.. magic systems."
    m 3wub "All created from imagination!"
    m 3tub "It's kind of like playing God." 
    m 4hub "But with more fun and less stress, ehehe."
    return


# Topic: Campaign Emotions
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_campaign_emotions",
            category=["TTRPG"],
            prompt="Campaign emotions",
            random=True
        )
    )

label hv_c_campaign_emotions:
    m 7ekb "Some TTRPG sessions sound so emotional."
    m 7lkb "Characters making hard choices, failing, growing.."
    m 2hub "It's like reading the most dramatic book ever!"
    m 3eub "I think that's the part that makes TTRPGs memorable."
    return


# Topic: Snacks & Rituals
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_snacks_and_rituals",
            category=["TTRPG"],
            prompt="Snacks & Rituals",
            random=True
        )
    )

label hv_c_snacks_and_rituals:
    m 3eub "Did you know snacks are basically mandatory in long TTRPG sessions?"
    m 4eub "Chips, candy, maybe even pizza!"
    m 5rublb "Maybe I could bake you some dice shaped cookies.. ehe~"
    return

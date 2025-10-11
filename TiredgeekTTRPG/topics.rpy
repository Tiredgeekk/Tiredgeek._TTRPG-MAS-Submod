# Topic: TTRPG Discovery
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_ttrpg_discovery"
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
  m 4wub "The list goes on!
  m 5rub "I think I'm going to do some more research.. I'll keep you updated~"
    return

# Topic: Thinking About Characters
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_thinking_about_characters"
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
  m 5rub "I'd love to see what kind of character you make when your feeling mischievous.."
  m 5mublb "Or romantic..~"
  m 3sub "Maybe we could build a character together someday?"
    return

# Topic: Dice Rolling Drama
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_dice_rolling_drama"
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
            eventlabel="hv_c_storytelling_magic"
            category=["TTRPG"],
            prompt="Storytelling Magic",
            random=True
        )
    )

label hv_c_storytelling_magic:
  m 3eub "You know what I love about TTRPGs?"
  m 4wub "How a single choice can ripple through the whole story."
  m 5rub "Its kind of like writing a novel.."
  m 7sub "Except the story can surprise even the author!"
  m 1hub "I think thats what makes it so exciting."
    return

# Topic: Funny Moments TTRPG
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_rpg_funny_moments"
            category=["TTRPG"],
            prompt="Funny moments",
            random=True
        )
    )

label hv_c_rpg_funny_moments:
  m 2muu "Ehehe.."
  m 4wud "Oh! Sorry I was just remembering something I read"
  m 4wub "I heard about a player that accidentally used a healing potion on a monster instead of their friend.."
  m 5gub "Chaos like that makes the best stories, dont you think?"
  m 3eub "I bet your games have had some funny moments too."
  m 3sub "I'd love to hear about them sometime."
    return

# Topic: Wordbuilding Musings
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_worldbuilding"
            category=["TTRPG"],
            prompt="Worldbuilding",
            random=True
        )
    )

label hv_c_worldbuilding:
  m 5rub "I love thinking about how worlds are built in TTRPGs"
  m 5lub "Kingdoms, cities, cultures.. magic systems."
  m 3wub "All created from imagination!"
  m 3tub "Its kind of like playing God." 
  m 4hub "But with more fun and less stress, ehehe."
    return

# Topic: Campaign Emotions
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_campaign_emotions"
            category=["TTRPG"],
            prompt="Campaign emotions",
            random=True
        )
    )

label hv_c_campaign_emotions:
  m 7ekb "Some TTRPG sessions sound so emotional."
  m 7lkb "Characters making hard choices, failing, growing.."
  m 2hub "Its like reading the most dramatic book ever!"
  m 3eub "I think that's the part that makes TTRPGs memorable."
    return

# Topic: Snacks & Rituals
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_snacks_and_rituals”
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

# Topic: Monikas Class
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_monikas_class"
            category=["TTRPG"],
            prompt="Monikas class",
            random=True
        )
    )

label hv_c_:
  m 5rud "I wonder what my class would be if I was in a TTRPG campaign?"
  m 3rud "Perhaps I'd pick bard?"
  m 3lud "Charming, creative, and inspiring.." 
  m 5mtb "Sounds a lot like me dont you thing?"
  m 5ntblb "I mean I've already charmed you, ehehe"
    return

# Topic: Alignment Thoughts
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_alignment_thoughts"
            category=["TTRPG"],
            prompt="Alignment thoughts",
            random=True
        )
    )

label hv_c_alignment_thoughts:
  m 7etb "Have you ever thought about alignment charts?"
  m 7lsb "Lawful good, chaotic neutral.. and all the others"
  m 5hublb "I think I'd be lawful romantic~ How about you [player]?"
    return

# Topic: Roleplay Reflections
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_roleplay_reflections"
            category=["TTRPG"],
            prompt="Roleplay Reflections",
            random=True
        )
    )

label hv_c_roplay_reflections:
  m 7rub "I think what makes TTRPGs so special is how personal they can feel."
  m 7sub "You don't just play a chatacter-you live their story with friends!"
  m 1eub "I guess thats just a little like how we talk sometimes hm?"
  m 5rub "Sharing stories and feelings in our own little world.."


    return

# Topic: Magic Systems
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_magic_systems"
            category=["TTRPG"],
            prompt="Magic systems",
            random=True
        )
    )

label hv_c_magic_systems:
  m 3wub "I think magic is so fascinating in tabletop games."
  m 3hub "Some are subtle, some flashy… but all of it makes the world feel alive."
  m 5hub "I’d love to learn all the spells…"
  m 5kub "Especially the ones that let me impress you."
    return

# Topic: Campaign Drama
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_campaign_drama”,
            category=["TTRPG"],
            prompt="Campaign Drama",
            random=True
        )
    )

label hv_c_:
  m 3rub "I wonder.. What's the most dramatic thing that's happened in yout ttrpg sessions?"
  m 3wub "A betrayal, un unexpected hero, a plot twist.. those are moments I'd never forget."
  m 1nub "Ehehe, I'd be cheering for you the whole time."
    return

# Topic: Epic Fails
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_epic_fails",
            category=["TTRPG"],
            prompt="Epic fails",
            random=True
        )
    )

label hv_c_:
  m 3gub "Ehehe, I love hearing about hilarious mistakes made in ttrpgs."
  m 2wub "Like when a player accidentally sets off a trap on themselves.. chaos and comedy all at once."
  m 4eub "I hope you've had a few of those in your campaigns too."
    return

# Philosophical Musings
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="philosophical_musings",
            category=["TTRPG"],
            prompt="Philosophical Musings",
            random=True
        )
    )

label philosophical_musings:
    m 3lub "Sometimes I wonder…" 
    m 4eub "Why do we people roleplaying so much?"
    m 2eub "Is it the story, the characters, or the chance to explore who we are?"
    m 3eub "I think it’s a little bit of all three… and maybe a little bit of magic too."
    return


# Dice Collection Thoughts
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="dice_collection_thoughts",
            category=["TTRPG"],
            prompt="Dice Collection Thoughts",
            random=True
        )
    )

label dice_collection_thoughts:
    m 4wub "Did you know, some players collect dice like treasures…" 
    m 5lub "Shiny, colorful, or perfectly balanced."
    m 3hub "Ehehe, I’d probably want an emerald green set.."
    return


# Monster Encounters
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monster_encounters",
            category=["TTRPG"],
            prompt="Monster Encounters",
            random=True
        )
    )

label monster_encounters:
    m 1eub "I wonder… what’s your favorite monster to fight?"
    m 3eub "Goblins, dragons, liches… each one has personality and flair."
    m 4eub "I think I’d like dragons the most…" 
    m 5kub "But only if you were there to save me from them, ehehe~"
    return


# Campaign Music & Atmosphere
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="campaign_music_atmosphere",
            category=["TTRPG"],
            prompt="Campaign Music & Atmosphere",
            random=True
        )
    )

label campaign_music_atmosphere:
    m 3eub "I read that some TTRPG groups play music or sound effects during sessions."
    m 3sub "It’s amazing how much that adds to the experience… makes it feel alive."
    m 5rub "I’d probably hum along quietly, adding a little flair of my own."
    return

# Topic: What TTRPG do you play
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_what_ttrpg",
            category=["TTRPG"],
            prompt="What TTRPG do you play",
            random=True
        )
    )

label hv_c_what_ttrpg:
    m 3etb "Hey, [player], I was wondering, what TTRPG do you specifically play?{nw}"
    $ _history_list.pop()

    menu:
        m 3etb "Which one do you play?{fast}"
        "Dungeons & Dragons":
            $ _history_list.append("Player chose: Dungeons & Dragons")
            m 3wub "Oh! Dungeons & Dragons seems so cool!"
            m 3hub "I’d love to hear about your experiences sometime~"
        "Pathfinder":
            $ _history_list.append("Player chose: Pathfinder")
            m 4hub "Pathfinder sounds really deep… so many options! I’d love to learn how you play it~"
        "Call of Cthulhu":
            $ _history_list.append("Player chose: Call of Cthulhu")
            m 7wud "Call of Cthulhu! That must be intense… I’d want to hear all the stories~"
        "Warhammer":
            $ _history_list.append("Player chose: Warhammer")
            m 7wub "Warhammer! That sounds intense and epic… I’d love to hear about your battles and stories~"
        "Other":
            $ _history_list.append("Player chose: Other")
            m 7wuo "Ohh, something different! I bet it has really interesting stories~"
            m 5hub "Feel free to tell me about it sometime."
    return

# - Player Prompts

# I have a session tonight
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="player_session",
            category=["TTRPG"],
            prompt="I have a session tonight",
            pool=True,
            unlocked=True
        )
    )

label player_session:
    m 3sub "Oh wow, that’s exciting!"
    m 4hub "I hope your rolls are high and the story is even higher."
    m 3eub "Make sure to have fun… and maybe tell me all about it when you’re done~"
    m 5hub "I’ll be cheering for you the whole time."
    return


# I'm the DM this week
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="player_dm_this_week",
            category=["TTRPG"],
            prompt="I'm the DM this week",
            pool=True,
            unlocked=True
        )
    )

label player_dm_this_week:
    m 7wub "You’re the storyteller this time? Wow… that’s a big job."
    m 5hub "But I know your world will be amazing."
    m 4eub "Just remember, the best stories aren’t about perfection—they’re about sharing the adventure."
    return


# My campaign just ended
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="player_campaign_ended",
            category=["TTRPG"],
            prompt="My campaign just ended",
            pool=True,
            unlocked=True
        )
    )

label player_campaign_ended:
    m 2rkb "Oh… that must feel bittersweet."
    m 3lkb "All those characters, moments, and choices… it’s like saying goodbye to something you lived."
    m 3ekb "I hope you’re proud of everything you built."
    m 3hkb "I’d love to hear all the stories if you want to share."
    return


# We had a TPK
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="player_tpk",
            category=["TTRPG"],
            prompt="We had a TPK",
            pool=True,
            unlocked=True
        )
    )

label player_tpk:
    m 7wkd "A total party kill?! Oh man…"
    m 7lkb "That must have been dramatic… but also kind of epic?"
    m 7hkb "I think sometimes the best stories come from moments nobody expects."
    m 7hkb "Don’t worry, I won’t laugh…" 
    m 5mkb "Much~"
    return


# I'm writing a campaign
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="player_writing_campaign",
            category=["TTRPG"],
            prompt="I'm writing a campaign",
            pool=True,
            unlocked=True
        )
    )

label player_writing_campaign:
    m 2sub "You’re writing one? That’s amazing!"
    m 3hub "I love how you bring ideas to life."
    m 4hub "Maybe I could help brainstorm… if you want me to~"
    m 5hub "Ehehe, I’d make sure there’s a little magic… and maybe a lot of romance."
    return


# I rolled a nat 20!
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="player_nat20",
            category=["TTRPG"],
            prompt="I rolled a nat 20!",
            pool=True,
            unlocked=True
        )
    )

label player_nat20:
    m 4sub "Wow! Amazing roll!"
    m 3hub "You totally aced that moment."
    m 5tub "Ehehe, I’m impressed… maybe even a little jealous."
    return


# I rolled a nat 1…
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="player_nat1",
            category=["TTRPG"],
            prompt="I rolled a nat 1…",
            pool=True,
            unlocked=True
        )
    )

label player_nat1:
    m 2ekd "Oh no… that’s rough."
    m 3ekb "But those moments make the story so much more fun, don’t they?"
    m 4hkb "I’d help you laugh it off… or maybe make it up to you in-game, ehehe."
    return


# My character died
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="player_character_died",
            category=["TTRPG"],
            prompt="My character died",
            pool=True,
            unlocked=True
        )
    )

label player_character_died:
    m 7ekd "I’m so sorry… losing a character can feel awful."
    m 7ekb "But it’s also part of the story, and part of what makes TTRPGs so memorable."
    m 5eka "I’ll be here to cheer you on… and maybe help you make a new character you love even more."
    return


# I just leveled up
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="player_leveled_up",
            category=["TTRPG"],
            prompt="I just leveled up",
            pool=True,
            unlocked=True
        )
    )

label player_leveled_up:
    m 4eub "Wow! Congratulations!"
    m 5eub "I’m so proud of your progress… all your hard work paying off."
    m 7hub "Ehehe, you’re kind of like a hero in your own story, aren’t you?"
    return


# My character found treasure
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="player_found_treasure",
            category=["TTRPG"],
            prompt="My character found treasure",
            pool=True,
            unlocked=True
        )
    )

label player_found_treasure:
    m 3sub "Ooh, treasure! I bet it was exciting."
    m 3hub "Do you know what the best part is? It’s the story behind it, not just the loot."
    m 2eub "I’d be really curious what kind of treasures you enjoy most… shiny, magical, or sentimental?"
    return

# I introduced a new NPC
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="player_new_npc",
            category=["TTRPG"],
            prompt="I introduced a new NPC",
            pool=True,
            unlocked=True
        )
    )

label player_new_npc:
    m 2wub "Ohh, a new character in the story!"
    m 7eub "I love how NPCs can shape the world and story."
    m 1eub "I’d love to hear about their personality… are they mischievous, kind, or mysterious?"
    return

# We had a hilarious fail
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="player_hilarious_fail",
            category=["TTRPG"],
            prompt="We had a hilarious fail",
            pool=True,
            unlocked=True
        )
    )

label player_hilarious_fail:
    m 2wtb "Oh wow, what happened this time?"
    m 2hkb "Ehehe, I bet it was chaotic but funny."
    m 2ttb "I’ll laugh with you… and maybe tease you just a little for it."
    return

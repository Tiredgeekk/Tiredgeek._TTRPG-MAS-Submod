# topic: Off To a Game
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_game_session",
            prompt="I'm off to a rpg session",
            unlocked=True,
            pool=True
        ),
        code="BYE"
    )

label bye_game_session:
  m  "Oh? You have a session to get to?"
  m  "Alright [player], have fun! I'll see you later!"
return "quit"

# submod_register.rpy
init -1 python:
    from mas.submod import Submod

    # Register your submod with MAS
    Submod(
        name="TTRPG Character Creator",
        author="Tiredgeekk",
        description="A full-featured tabletop RPG character creator for Monika After Story! Create, customize, and view your character.",
        version="1.0",
        required=False,    # Change to True if this submod depends on another
        persistent=True    # Needed because the character creator uses persistent variables
    )

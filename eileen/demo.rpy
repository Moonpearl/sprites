define current_outfit = "uniform"

label demo_sprite_eileen:
    show eileen with dissolve
    eileen "You've created a new Ren'Py game."
    show eileen lecturing cheerful with dissolve
    eileen "Once you add a story, pictures, and music, you can release it to the world!"
    show eileen neutral with dissolve
    eileen "Hmm? What's wrong…?"
    menu:
        eileen "Hmm? What's wrong…?"
        "You look different than usual…":
            show eileen thinking proud with dissolve
            eileen "Hehe… I see."
            show eileen cheerful
            eileen "You've noticed my amazing new look!"
        "Wow, you look so good!":
            show eileen -lecturing laughing with dissolve
            eileen "Oh! Thank you so much!"
        "I liked the old Eileen better…":
            show eileen serious with dissolve
            eileen "That's not a very nice thing to say…"
            show eileen proud with dissolve
            eileen "Anyways, you're stuck with my current look right now, so… that's that."
    
    eileen "I think getting that makeover was the best decision I've made in a long time!"
    show eileen lecturing cheerful with dissolve
    eileen "Look! I've got so many different outfits now!"
    eileen "What outfit do you want me to show you?"
    call demo_sprite_eileen_outfit_loop

    show eileen lecturing cheerful with dissolve
    eileen "Älright! I've got so many facial expressions too!"
    call demo_sprite_eileen_emotion_loop
    
    hide eileen with dissolve
    return

label demo_sprite_eileen_change_outfit:
    show eileen cheerful with dissolve
    eileen "Alright, give me a minute to change…"
    hide eileen with dissolve
    "*Shuffle* *shuffle*…"
    return

label demo_sprite_eileen_outfit_loop:
    menu:
        eileen "What outfit do you want me to show you?"
        "Your formal wear":
            if current_outfit == "uniform":
                show eileen thinking neutral with dissolve
                eileen "This is what I'm wearing already…"
            else:
                call demo_sprite_eileen_change_outfit
                show eileen thinking uniform with dissolve
                eileen "Alright! Back to work!"
                $ current_outfit = "uniform"
        "Something casual":
            if current_outfit == "casual":
                show eileen thinking neutral with dissolve
                eileen "This is what I'm wearing already…"
            else:
                call demo_sprite_eileen_change_outfit
                show eileen lecturing casual cheerful with dissolve
                eileen "Here! This is what I wear to fo out with friends!"
                $ current_outfit = "casual"
        "What you wear in bed":
            if current_outfit == "night":
                show eileen thinking neutral with dissolve
                eileen "This is what I'm wearing already…"
            else:
                call demo_sprite_eileen_change_outfit
                show eileen relaxed night serious with dissolve
                eileen "I don't want to go to bed yet, though…"
                $ current_outfit = "night"
        "A swimsuit":
            if current_outfit == "swimsuit":
                show eileen thinking neutral with dissolve
                eileen "This is what I'm wearing already…"
            else:
                call demo_sprite_eileen_change_outfit
                show eileen relaxed swimsuit uneasy with dissolve
                eileen "I'm a bit shy to wear that in front of you…"
                $ current_outfit = "swimsuit"
        "Something warm":
            if current_outfit == "winter":
                show eileen neutral with dissolve
                eileen "This is what I'm wearing already…"
            else:
                call demo_sprite_eileen_change_outfit
                show eileen lecturing winter with dissolve
                eileen "You're right, it's so cold outside!"
                $ current_outfit = "winter"
        "Something exotic":
            if current_outfit == "yukata":
                show eileen neutral with dissolve
                eileen "This is what I'm wearing already…"
            else:
                call demo_sprite_eileen_change_outfit
                show eileen thinking yukata moved with dissolve
                eileen "I bought this on my last trip to Japan! Cute, right?"
                $ current_outfit = "yukata"
        "Keep your current outfit":
            return
    
    jump demo_sprite_eileen_outfit_loop

label demo_sprite_eileen_emotion_loop:
    menu:
        "What can I say to elicit a variety of reactions from Eileen?"
        "Knock-knock?":
            show eileen thinking neutral with dissolve
            eileen "Who's there?"
            "Figs."
            eileen "Figs who?"
            "Figs the doorbell! It's not working!"
            show eileen laughing with dissolve
            eileen "Hahaha! You're so silly!"
            show eileen lecturing with dissolve
            eileen "Good one! I'll tell it to all my friends!"
        "Did you know that it takes the sunlight 8 minutes to reach us?":
            show eileen relaxed neutral with dissolve
            eileen "Huh?"
            "Yeah. So, basically, when you see the sun setting, it's actually gone below the horizon already, 8 minutes ago."
            show eileen surprised with dissolve
            eileen "Wow! Really?"
            show eileen thinking with dissolve
            eileen "This means that if the sun ever explodes, we'll see it 8 minutes late?"
        "You're really cute, you know?":
            show eileen thinking moved with dissolve
            eileen "Oh? For real?"
            menu:
                eileen "Oh? For real?"
                "Yes, of course":
                    show eileen relaxed with dissolve
                    eileen "…Thank you. You're very sweet."
                "No, I was just joking around":
                    show eileen uneasy with dissolve
                    eileen "…I knew it."
                "No, you're really ugly":
                    show eileen lecturing annoyed with dissolve
                    eileen "And you're a real jerk!" 
        "I'm leaving. I don't like visual novels anyways.":
            show eileen sad with dissolve
            eileen "That's so mean…"
            return
    
    jump demo_sprite_eileen_emotion_loop
    
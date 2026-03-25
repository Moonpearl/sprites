# Add the list of all characters you want to inspect here
define character_sprites.characters = ("eileen",)

init python:
    def get_character_sprite(index):
        return getattr(character_sprites, character_sprites.characters[index])

screen sprite_inspector:
    zorder 100

    # Character index
    default c = 0

    # Pose index
    default p = 0

    # Outfit index
    default o = 0

    # Face index
    default f = 0

    hbox:
        frame:
            padding (20, 20)
            xsize 320
            yfill True

            has vbox

            label _("Character")
            textbutton f"{character_sprites.characters[c]}" action CycleScreenVariable("c", tuple(range(len(character_sprites.characters))))

            null height 20

            label _("Pose")
            textbutton f"{get_character_sprite(c).poses[p]}" action CycleScreenVariable("p", tuple(range(len(get_character_sprite(c).poses))))
            bar:
                style "slider"
                value ScreenVariableValue("p", min=0, max=len(get_character_sprite(c).poses)-1)
            
            null height 20

            label _("Outfit")
            textbutton f"{get_character_sprite(c).outfits[o]}" action CycleScreenVariable("o", tuple(range(len(get_character_sprite(c).outfits))))
            bar:
                style "slider"
                value ScreenVariableValue("o", min=0, max=len(get_character_sprite(c).outfits)-1)
            
            null height 20

            label _("Face")
            textbutton f"{get_character_sprite(c).faces[f]}" action CycleScreenVariable("f", tuple(range(len(get_character_sprite(c).faces))))
            bar:
                style "slider"
                value ScreenVariableValue("f", min=0, max=len(get_character_sprite(c).faces)-1)
            
            null height 20

            textbutton "Copy Command":
                action CopyToClipboard(f"show {character_sprites.characters[c]} {get_character_sprite(c).poses[p]} {get_character_sprite(c).outfits[o]} {get_character_sprite(c).faces[f]}")

            null height 20

            textbutton _('Exit') action Return()
            
        frame:
            xsize (renpy.config.screen_width - 320)
            yfill True

            add f"{character_sprites.characters[c]} {get_character_sprite(c).poses[p]} {get_character_sprite(c).outfits[o]} {get_character_sprite(c).faces[f]}" at center

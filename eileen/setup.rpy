# Define sprite dimensions
define character_sprites.eileen.width = 768
define character_sprites.eileen.height = 1024
define character_sprites.eileen.regions = {
    "relaxed": (0, 0, character_sprites.eileen.width, character_sprites.eileen.height),
    "thinking": (character_sprites.eileen.width, 0, character_sprites.eileen.width, character_sprites.eileen.height),
    "lecturing": (2 * character_sprites.eileen.width, 0, character_sprites.eileen.width, character_sprites.eileen.height),
}

# List of existing attributes, used by the Sprite Inspector
define character_sprites.eileen.poses = (
    "relaxed",
    "thinking",
    "lecturing"
)
define character_sprites.eileen.outfits = (
    "uniform",
    "winter",
)
define character_sprites.eileen.faces = (
    "smile",
    "cheerful",
    "laughing",
    "proud",
    "excited",
    "moved",
    "neutral",
    "surprised",
    "serious",
    "annoyed",
    "uneasy",
    "sad"
)

layeredimage eileen:
    group pose:
        attribute relaxed default null
        attribute thinking null
        attribute lecturing null

    # Pose 1 - relaxed
    group relaxed_outfit if_all ["relaxed"]:
        attribute uniform default Crop(character_sprites.eileen.regions["relaxed"], "sprites/eileen/outfit/uniform.avif")
        attribute winter default Crop(character_sprites.eileen.regions["relaxed"], "sprites/eileen/outfit/winter.avif")

    group relaxed_face if_all ["relaxed"]:
        attribute smile default null
        attribute cheerful Crop(character_sprites.eileen.regions["relaxed"], "sprites/eileen/face/cheerful.avif")
        attribute laughing Crop(character_sprites.eileen.regions["relaxed"], "sprites/eileen/face/laughing.avif")
        attribute proud Crop(character_sprites.eileen.regions["relaxed"], "sprites/eileen/face/proud.avif")
        attribute excited Crop(character_sprites.eileen.regions["relaxed"], "sprites/eileen/face/excited.avif")
        attribute moved Crop(character_sprites.eileen.regions["relaxed"], "sprites/eileen/face/moved.avif")
        attribute neutral Crop(character_sprites.eileen.regions["relaxed"], "sprites/eileen/face/neutral.avif")
        attribute surprised Crop(character_sprites.eileen.regions["relaxed"], "sprites/eileen/face/surprised.avif")
        attribute serious Crop(character_sprites.eileen.regions["relaxed"], "sprites/eileen/face/serious.avif")
        attribute annoyed Crop(character_sprites.eileen.regions["relaxed"], "sprites/eileen/face/annoyed.avif")
        attribute uneasy Crop(character_sprites.eileen.regions["relaxed"], "sprites/eileen/face/uneasy.avif")
        attribute sad Crop(character_sprites.eileen.regions["relaxed"], "sprites/eileen/face/sad.avif")

    # Pose 2 - thinking
    group thinking_outfit if_all ["thinking"]:
        attribute uniform default Crop(character_sprites.eileen.regions["thinking"], "sprites/eileen/outfit/uniform.avif")
        attribute winter default Crop(character_sprites.eileen.regions["thinking"], "sprites/eileen/outfit/winter.avif")

    group thinking_face if_all ["thinking"]:
        attribute smile default null
        attribute cheerful Crop(character_sprites.eileen.regions["thinking"], "sprites/eileen/face/cheerful.avif")
        attribute laughing Crop(character_sprites.eileen.regions["thinking"], "sprites/eileen/face/laughing.avif")
        attribute proud Crop(character_sprites.eileen.regions["thinking"], "sprites/eileen/face/proud.avif")
        attribute excited Crop(character_sprites.eileen.regions["thinking"], "sprites/eileen/face/excited.avif")
        attribute moved Crop(character_sprites.eileen.regions["thinking"], "sprites/eileen/face/moved.avif")
        attribute neutral Crop(character_sprites.eileen.regions["thinking"], "sprites/eileen/face/neutral.avif")
        attribute surprised Crop(character_sprites.eileen.regions["thinking"], "sprites/eileen/face/surprised.avif")
        attribute serious Crop(character_sprites.eileen.regions["thinking"], "sprites/eileen/face/serious.avif")
        attribute annoyed Crop(character_sprites.eileen.regions["thinking"], "sprites/eileen/face/annoyed.avif")
        attribute uneasy Crop(character_sprites.eileen.regions["thinking"], "sprites/eileen/face/uneasy.avif")
        attribute sad Crop(character_sprites.eileen.regions["thinking"], "sprites/eileen/face/sad.avif")

    # Pose 3 - lecturing
    group lecturing_outfit if_all ["lecturing"]:
        attribute uniform default Crop(character_sprites.eileen.regions["lecturing"], "sprites/eileen/outfit/uniform.avif")
        attribute winter default Crop(character_sprites.eileen.regions["lecturing"], "sprites/eileen/outfit/winter.avif")
     
    group lecturing_face if_all ["lecturing"]:
        attribute smile default null
        attribute cheerful Crop(character_sprites.eileen.regions["lecturing"], "sprites/eileen/face/cheerful.avif")
        attribute laughing Crop(character_sprites.eileen.regions["lecturing"], "sprites/eileen/face/laughing.avif")
        attribute proud Crop(character_sprites.eileen.regions["lecturing"], "sprites/eileen/face/proud.avif")
        attribute excited Crop(character_sprites.eileen.regions["lecturing"], "sprites/eileen/face/excited.avif")
        attribute moved Crop(character_sprites.eileen.regions["lecturing"], "sprites/eileen/face/moved.avif")
        attribute neutral Crop(character_sprites.eileen.regions["lecturing"], "sprites/eileen/face/neutral.avif")
        attribute surprised Crop(character_sprites.eileen.regions["lecturing"], "sprites/eileen/face/surprised.avif")
        attribute serious Crop(character_sprites.eileen.regions["lecturing"], "sprites/eileen/face/serious.avif")
        attribute annoyed Crop(character_sprites.eileen.regions["lecturing"], "sprites/eileen/face/annoyed.avif")
        attribute uneasy Crop(character_sprites.eileen.regions["lecturing"], "sprites/eileen/face/uneasy.avif")
        attribute sad Crop(character_sprites.eileen.regions["lecturing"], "sprites/eileen/face/sad.avif")
    
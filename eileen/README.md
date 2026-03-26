# Eileen Character Sprite

![image](outfit/uniform.avif)

## Run the demo

Include the following in your `script.rpy` file:

```rpy
define eileen = Character("Eileen")

label start:

    menu:
        "Launch Sprite Inspector":
            call screen sprite_inspector with dissolve
        "Launch Eileen's Demo":
            call demo_sprite_eileen
        "Exit":
            return
    
    jump start
```

This will allow you to see the sprite in action.

You can remove the `demo.rpy` file afterwards, as its only purpose is to showcase the sprite.

## How to use

The sprite is ready-to-use thanks to the layered image defined in `setup.rpy`. It can be used using the `show` command:

`show eileen`

It can be used alongside any of the following attributes:

- Poses
  - `relaxed` (default, will be used if pose is omitted or reverted)
  - `thinking`
  - `lecturing`
- Outfits
  - `uniform` (default, will be used if outfit is omitted or reverted)
  - `casual`
  - `winter`
  - `yukata`
- Faces
  - `smile` (default, will be used if face is omitted or reverted)
  - `cheerful`
  - `laughing`
  - `proud`
  - `excited`
  - `moved`
  - `neutral`
  - `surprised`
  - `serious`
  - `annoyed`
  - `uneasy`
  - `sad`

**Examples:**

- `show eileen thinking` will display Eileen, changing her pose to thinking, keeping her current face and outfit.
- `show eileen winter` will display Eileen, changing her current outfit to winter, keeping her current pose and face.
- `show eileen cheerful` will display Eileen, changing her face to cheerful, keeping her current pose and outfit.
- `show eileen thinking cheerful` will display Eileen, changing her pose to thinking and her face to cheerful, keeping her current outfit.

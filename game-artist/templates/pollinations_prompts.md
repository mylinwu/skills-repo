# Pollinations Prompt Templates

Templates for generating game sprites with Pollinations (Flux model).

## Base Template

```
[WIDTH]x[HEIGHT] game sprite, [SUBJECT], top-down view,
Kenney flat vector style, smooth rounded shapes,
bright [COLOR] (#HEX), transparent background,
thin dark outline, simple geometric forms,
clean silhouette, casual game aesthetic
```

## Character Templates

### Player/NPC Character
```
64x64 game sprite, [character type], top-down perspective,
Kenney Topdown Shooter style, rounded head and simple body,
[color] clothing (#HEX), thin black outline,
flat vector design, smooth shapes, transparent background,
casual mobile game character
```

**Example:**
```
64x64 game sprite, female scientist character, top-down perspective,
Kenney Topdown Shooter style, rounded head and simple body,
white lab coat with blue accents (#4A90E2), thin black outline,
flat vector design, smooth shapes, transparent background,
casual mobile game character
```

### Enemy Character
```
64x64 game sprite, [enemy type], top-down view,
Kenney flat vector style, simple threatening design,
[color] (#HEX) with darker shading, thin outline,
recognizable silhouette, menacing but simple,
transparent background, game enemy sprite
```

**Example:**
```
64x64 game sprite, mutant zombie, top-down view,
Kenney flat vector style, simple threatening design,
toxic green (#6B8E23) with darker shading, thin outline,
recognizable silhouette, menacing but simple,
transparent background, game enemy sprite
```

## Item Templates

### Collectible/Power-Up
```
[SIZE]x[SIZE] game sprite, [item name], icon style,
Kenney flat vector aesthetic, bright [color] (#HEX),
simple geometric shape, thin dark outline,
clear recognizable symbol, transparent background,
top-down game pickup item
```

**Example (Health Pack):**
```
64x64 game sprite, health pack medical kit, icon style,
Kenney flat vector aesthetic, bright red (#DC143C) with white cross,
simple geometric shape, thin dark outline,
clear recognizable symbol, transparent background,
top-down game pickup item
```

**Example (Speed Boost):**
```
48x48 game sprite, speed boost lightning bolt, icon style,
Kenney flat vector aesthetic, bright cyan (#00FFFF),
angular zigzag shape, thin dark outline, energy effect,
clear recognizable symbol, transparent background,
top-down game pickup item
```

**Example (Shield):**
```
64x64 game sprite, shield protection icon, icon style,
Kenney flat vector aesthetic, bright gold (#FFD700),
shield emblem shape, thin dark outline, protective symbol,
clear recognizable symbol, transparent background,
top-down game pickup item
```

### Weapon/Tool
```
[SIZE] game sprite, [weapon name], top-down view,
Kenney flat vector style, simple weapon design,
[color] (#HEX) with metallic highlights, thin outline,
clear silhouette, game weapon sprite, transparent background
```

**Example:**
```
32x64 game sprite, futuristic laser rifle, top-down view,
Kenney flat vector style, simple weapon design,
steel gray (#808080) with blue energy glow (#00BFFF), thin outline,
clear silhouette, game weapon sprite, transparent background
```

## Environment Templates

### Tree/Plant
```
[WIDTH]x[HEIGHT] game sprite, [tree/plant type], top-down perspective,
Kenney flat vector style, simple foliage design,
[color] green (#HEX) with darker shading, rounded organic shapes,
thin dark outline, casual game environment asset,
transparent background
```

**Example:**
```
64x128 game sprite, oak tree, top-down perspective,
Kenney flat vector style, simple foliage design,
forest green (#228B22) with darker shading, rounded organic shapes,
thin dark outline, casual game environment asset,
transparent background
```

### Building/Structure
```
[WIDTH]x[HEIGHT] game sprite, [building type], top-down view,
Kenney flat vector style, simple architectural design,
[color] (#HEX) with shadows, geometric shapes,
thin dark outline, clear building silhouette,
transparent background, game environment asset
```

**Example:**
```
192x192 game sprite, small wooden house, top-down view,
Kenney flat vector style, simple architectural design,
brown wood (#8B4513) with dark roof, geometric shapes,
thin dark outline, clear building silhouette,
transparent background, game environment asset
```

### Props/Objects
```
[SIZE] game sprite, [object name], top-down perspective,
Kenney flat vector style, simple object design,
[color] (#HEX), rounded shapes, thin outline,
recognizable item, transparent background,
game environment prop
```

**Example:**
```
64x64 game sprite, wooden crate, top-down perspective,
Kenney flat vector style, simple box design,
brown wood (#8B4513) with darker planks, rounded corners,
thin outline, recognizable item, transparent background,
game environment prop
```

## Effect Templates

### Particle/Explosion
```
[SIZE] game sprite, [effect type], animation frame,
Kenney flat vector style, simple effect design,
[color] (#HEX) with glow, soft rounded shapes,
transparent background, game visual effect
```

**Example:**
```
96x96 game sprite, explosion burst, animation frame,
Kenney flat vector style, simple effect design,
orange (#FF8C00) and yellow with bright glow, soft rounded shapes,
transparent background, game visual effect
```

## UI Templates

### Button/Icon
```
[SIZE] game sprite, [UI element], interface icon,
Kenney flat vector style, clean simple design,
[color] (#HEX), rounded rectangle or geometric shape,
thin outline, clear symbol, transparent background,
game UI element
```

**Example:**
```
64x64 game sprite, pause button, interface icon,
Kenney flat vector style, clean simple design,
white (#FFFFFF) on transparent, rounded square with two bars,
thin outline, clear symbol, transparent background,
game UI element
```

## Size Guidelines

| Asset Type | Recommended Size | Notes |
|------------|------------------|-------|
| Character | 64x64 | Standard human-sized entity |
| Small Item | 32x32 to 48x48 | Pickups, collectibles |
| Large Item | 64x64 | Weapons, important items |
| Small Prop | 64x64 | Rocks, bushes, small objects |
| Medium Prop | 96x96 to 128x128 | Furniture, crates, vehicles |
| Tree | 64x128 to 96x192 | Height 2-3 tiles |
| Small Building | 128x128 to 192x192 | 2-3 tile structures |
| Large Building | 256x256+ | 4+ tile structures |
| Effect | 64x64 to 128x128 | Explosions, particles |
| UI Icon | 32x32 to 64x64 | Buttons, indicators |

## Color Palette Quick Reference

```
Health Red:    #DC143C
Speed Cyan:    #00FFFF
Shield Gold:   #FFD700
Grass Green:   #7CFC00
Tree Green:    #228B22
Zombie Green:  #6B8E23
Player Blue:   #4A90E2
Brown Wood:    #8B4513
Concrete Gray: #808080
Orange Accent: #FF8C00
```

## Keywords to Use

✅ **Style Keywords:**
- "Kenney flat vector style"
- "Kenney Topdown Shooter style"
- "smooth rounded shapes"
- "simple geometric forms"
- "flat vector design"
- "casual game aesthetic"
- "casual mobile game"
- "clean simple design"

✅ **Quality Keywords:**
- "thin dark outline"
- "thin black outline"
- "transparent background"
- "clear silhouette"
- "recognizable"
- "clean"
- "smooth shapes"

✅ **Perspective Keywords:**
- "top-down view"
- "top-down perspective"
- "overhead view"

## Keywords to Avoid

❌ **Never Use:**
- "pixel art"
- "pixelated"
- "retro"
- "8-bit" / "16-bit"
- "realistic"
- "photorealistic"
- "detailed"
- "complex"
- "3D rendered"
- "isometric" (unless specifically needed)

## Negative Prompts

Consider adding negative keywords if results are off-style:

```
NOT pixel art, NOT pixelated, NOT retro, NOT realistic,
NOT complex, NOT detailed, NOT 3D, NOT photorealistic
```

## Tips

1. **Always specify dimensions** - Controls output size
2. **Use hex colors** - Ensures color accuracy
3. **Mention "transparent background"** - Critical for sprites
4. **Reference "Kenney"** - Helps model understand style
5. **Keep prompts concise** - Model works better with clear instructions
6. **Test multiple generations** - Pick the best result
7. **Compare with references** - Verify style match after generation

## Quality Checklist

After generation, verify:
- [ ] Background is fully transparent
- [ ] Has thin dark outline
- [ ] Uses smooth rounded shapes (not pixelated)
- [ ] Colors match requested hex codes
- [ ] Silhouette is clear and simple
- [ ] Size is correct
- [ ] Style matches Kenney flat/vector aesthetic
- [ ] Fits with existing game sprites

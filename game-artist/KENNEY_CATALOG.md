# Kenney Asset Catalog

Quick reference for finding game assets in the Kenney Game Assets All-in-1 3.3.0 collection.

## Location

`/root/projects/claude-agentic-mastery/assets/kenney_collection/`

## Collection Overview

- **150+ 2D asset packs** - Characters, tiles, items, UI elements
- **50+ 3D assets** - Vehicles, characters, environments
- **Icons** - Game icons, input prompts, board game icons
- **UI assets** - Cursors, controls, borders, packs for different themes
- **Audio** - Sound effects and music
- **All CC0 licensed** - Free for any use, commercial or personal

## How to Browse

Each pack contains:
- `Preview.png` - Visual overview of all assets
- `PNG/` - Individual sprite files organized by category
- `Spritesheet/` - Combined sprite sheets (if available)
- `Vector/` - SVG source files (some packs)

**Quick Browse Command:**
```bash
find "/path/to/Kenney/2D assets" -name "Preview.png" | head -20
```

## Flat/Vector Style Packs (Match Topdown Shooter)

Our game uses **Kenney's flat/vector style** - smooth rounded shapes, thin outlines, simple geometric forms.

### Primary Packs

| Pack | Best For | Example Assets |
|------|----------|----------------|
| **Topdown Shooter** | Characters, tiles, objects | Survivors, zombies, robots, hitmen, tiles |
| **Space Shooter Redux** | Power-ups, shields, effects | Energy orbs, shield icons, lasers, particles |
| **Puzzle Assets** | Collectibles, gems | Colored gems (perfect for power-ups!) |
| **Generic Items** | Props, items, tools | First aid kit, tools, electronics, food |

### UI & Icons

| Pack | Best For | Example Assets |
|------|----------|----------------|
| **Game Icons** | UI controls, buttons | Arrows, checkboxes, media controls, letters |
| **Game Icons Expansion** | Special icons | Shield icons, progress circles, d-pads |
| **Input Prompts** | Controller/keyboard icons | Button prompts, keyboard keys |
| **UI Pack** | Menus, HUD elements | Buttons, panels, sliders, health bars |

### Other Flat/Vector Packs

- **Toon Characters Pack** - Cartoony characters
- **Shape Characters** - Simple geometric characters
- **Simplified Platformer Pack** - Clean platformer assets
- **Cartography Pack** - Map elements and icons

## Pixel Art Packs (Different Style)

These use pixel art style (hard pixels, not smooth vector):

- **Roguelike** packs (Base, Dungeon, City, Interior, Characters)
- **Micro Roguelike** - Tiny 8x8 pixel art
- **Pixel Platformer** - 16x16 platformer tiles
- **Pixel Shmup** - Pixel art shooter
- **1-Bit** packs - Monochrome pixel art
- **RPG Urban Pack** - Pixel art top-down

**Note:** Only use pixel packs if specifically needed - they won't match our flat/vector style.

## Power-Up Asset Candidates

Based on visual inspection of Preview.png files:

### Health Power-Up
| Pack | Asset | Style Match |
|------|-------|-------------|
| Generic Items | First aid kit (red + white cross) | ⭐⭐⭐ Excellent |
| Puzzle Assets | Green gem | ⭐⭐⭐ Excellent |
| Space Shooter Redux | Green power-up orb | ⭐⭐⭐ Excellent |

### Speed Power-Up
| Pack | Asset | Style Match |
|------|-------|-------------|
| Puzzle Assets | Blue gem | ⭐⭐⭐ Excellent |
| Space Shooter Redux | Blue lightning/speed icon | ⭐⭐⭐ Excellent |
| Game Icons | Forward arrows | ⭐⭐ Good |

### Shield Power-Up
| Pack | Asset | Style Match |
|------|-------|-------------|
| Game Icons Expansion | Shield icon (white outline) | ⭐⭐⭐ Excellent |
| Puzzle Assets | Gold gem | ⭐⭐⭐ Excellent |
| Space Shooter Redux | Shield bubble | ⭐⭐⭐ Excellent |

## Search Workflow

When looking for a specific asset:

1. **Think about category** - Character? Item? UI? Effect?
2. **Check relevant pack's Preview.png** - Visual browse
3. **Navigate to PNG folder** - Find individual sprite
4. **Check size** - Resize to 64x64 if needed
5. **Verify style** - Compare with existing player/zombie sprites

## Common Asset Locations

### Characters
- `2D assets/Topdown Shooter/PNG/` - Survivors, zombies, robots
- `2D assets/Toon Characters Pack 1/` - Cartoon characters

### Weapons & Tools
- `2D assets/Generic Items/` - Tools, electronics, everyday items
- `2D assets/Topdown Shooter/PNG/Tiles/` - Weapons scattered in tiles

### Collectibles & Power-Ups
- `2D assets/Puzzle Assets/` - Gems, jewels
- `2D assets/Space Shooter Redux/` - Energy orbs, pickups
- `2D assets/Generic Items/` - First aid, items

### UI Elements
- `Icons/Game Icons/` - Standard UI icons
- `Icons/Game Icons Expansion/` - Additional special icons
- `UI assets/UI Pack/` - Buttons, panels, borders

### Effects & Particles
- `2D assets/Explosion Pack/` - Explosions, particles
- `2D assets/Particle Pack/` - Various particles
- `2D assets/Smoke Particles/` - Smoke effects

## Tips for Asset Selection

✅ **DO:**
- Compare side-by-side with existing sprites
- Check transparency (use PNG with alpha channel)
- Resize consistently (our game uses 64x64)
- Stick to flat/vector packs for consistency

❌ **DON'T:**
- Mix pixel art with flat/vector styles
- Use assets that clash with color palette
- Forget to resize (maintain consistent scale)
- Use overly complex assets (keep it simple)

## When to Generate Instead

Only use Pollinations if:
- No suitable Kenney asset exists
- Need very specific custom design
- Kenney asset doesn't match style well enough
- Need color/design variation not available

**Remember: Kenney-first! Search before generating.**

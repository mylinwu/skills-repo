# Game Art Style Guide

Visual style reference for Zombie Survival Game assets.

## Core Style: Kenney Flat/Vector

Our game uses **Kenney's flat/vector style** - NOT pixel art!

### Style Characteristics

| Characteristic | Description | Example |
|----------------|-------------|---------|
| **Art Style** | Flat/vector design with smooth shapes | Like mobile game art, not retro pixels |
| **Edges** | Soft, rounded - NO hard pixel boundaries | Smooth curves, rounded rectangles |
| **Colors** | Flat fills with subtle gradients | Single color per shape + slight gradient |
| **Shapes** | Simple geometric forms | Circles, rounded rects, ovals |
| **Outlines** | Thin dark outlines for definition | ~1-2px black/dark outline |
| **Complexity** | Simple, readable silhouettes | Recognizable at small sizes |
| **Perspective** | Top-down with slight 3/4 view | Slight depth, not pure overhead |

### NOT Pixel Art

❌ **Common Mistakes:**
- Hard pixel boundaries
- Blocky/pixelated edges
- Dithering or pixel shading
- Retro 8-bit/16-bit style

✅ **Correct Style:**
- Smooth vector shapes
- Clean rounded edges
- Flat colors with gradients
- Modern mobile/casual game look

## Asset Scaling System

### Base Unit: 64x64 Pixels

Our game uses a **64 pixels per tile** system.

| Asset Type | Size | Ratio | Example |
|------------|------|-------|---------|
| **Base Tile** | 64x64 | 1 tile | Floor, grass, single tile |
| **Character** | 64x64 | 1 tile | Player, zombie (human-sized) |
| **Small Item** | 32x32 to 64x64 | 0.5-1 tile | Power-up, weapon, crate |
| **Medium Prop** | 64x96 to 128x128 | 1-2 tiles | Bush, furniture, car |
| **Large Prop** | 128x128 to 256x192 | 2-3 tiles | Tree, small building |
| **Building** | 256x256+ | 4+ tiles | House, large structure |

### Scaling Guidelines

**Rule:** Match the **game world scale**, not a fixed size.

1. **Determine real-world size** - How big is it compared to a person?
2. **Calculate pixel size** - If character is 64px, tree 2x tall = 128px
3. **Use tile multiples** - 64, 128, 192, 256, 320, etc.
4. **Maintain consistency** - Same pixel-per-unit ratio across all assets

**Example Scaling:**
```
Human (player)     → 64x64   (1 tile tall)
Car                → 128x192 (2 tiles wide, 3 tiles long)
Tree               → 64x128  (1 tile wide, 2 tiles tall)
Small house        → 192x192 (3x3 tiles)
Large building     → 384x256 (6x4 tiles)
Power-up pickup    → 48x48   (0.75 tiles - smaller than human)
```

### Asset Dimensions by Category

#### Characters & Entities (64x64)
- Player
- Zombies
- NPCs
- Animals (human-sized)

#### Collectibles & Items (32-64px)
- Power-ups: 48x48 or 64x64
- Weapons: 32x32 to 64x48
- Coins/gems: 32x32

#### Props & Environment (Vary)
- **Small:** 64x64 (rocks, signs, barrels)
- **Medium:** 96x96 to 128x128 (bushes, furniture, crates)
- **Large:** 128x192 to 256x256 (trees, vehicles, small buildings)
- **Huge:** 256x256+ (large buildings, walls)

#### Tiles (64x64)
- Ground tiles
- Floor tiles
- Wall tiles (64x64 for floor-level, taller for vertical walls)

## Reference Sprites

Our existing sprites follow this style:

### Player Sprite
- **File:** `assets/sprites/player.png`
- **Size:** 64x64 pixels
- **Style:** Blue survivor character, rounded head, simple body
- **Colors:** Blue (#4A90E2), white, black outline
- **Features:** Smooth shapes, thin outline, clear silhouette

### Zombie Sprite
- **File:** `assets/sprites/zombie.png`
- **Size:** 64x64 pixels
- **Style:** Green zombie, rounded forms
- **Colors:** Green (#6B8E23), darker green, black outline
- **Features:** Same flat/vector style as player

### Background Tile
- **File:** `assets/sprites/tile_background.png`
- **Size:** 64x64 pixels
- **Style:** Grass tile, simple texture
- **Colors:** Green (#7CFC00), subtle variations

## Color Palette

Based on Kenney Topdown Shooter Sample.png:

### Primary Colors
| Color | Hex | Usage |
|-------|-----|-------|
| **Grass Green** | `#7CFC00` | Backgrounds, nature |
| **Tree Green** | `#228B22` | Trees, foliage |
| **Zombie Green** | `#6B8E23` | Zombies, enemies |
| **Survivor Blue** | `#4A90E2` | Player, allies |
| **Health Red** | `#DC143C` | Health packs, danger |
| **Speed Cyan** | `#00FFFF` | Speed boost, energy |
| **Shield Gold** | `#FFD700` | Shield, protection |

### Supporting Colors
| Color | Hex | Usage |
|-------|-----|-------|
| **Brown Wood** | `#8B4513` | Floors, furniture, walls |
| **Concrete Gray** | `#808080` | Buildings, roads |
| **Orange Accent** | `#FF8C00` | Highlights, crates |
| **White** | `#FFFFFF` | Highlights, details |
| **Black** | `#000000` | Outlines, shadows |

## Technical Specifications

### General Requirements
- **Format:** PNG with alpha transparency
- **Color Depth:** 32-bit RGBA
- **Base Unit:** 64 pixels per tile
- **Scaling:** Multiples of 16px (16, 32, 48, 64, 96, 128, 192, 256...)

### Visual Requirements
| Requirement | Details |
|-------------|---------|
| **Transparency** | Full alpha channel, no background |
| **Outline** | 1-2px dark outline on all sprites |
| **Silhouette** | Clear, recognizable shape |
| **Anti-aliasing** | Smooth edges (not pixelated) |
| **Contrast** | Strong contrast for readability |

### Kenney Asset Sizing

When using Kenney assets:
- **Check original size** - Look at sprite dimensions
- **Maintain aspect ratio** - Don't stretch/squash
- **Scale proportionally** - If character is 43px tall, scale to 64px (1.49x)
- **Apply to all assets** - Trees, buildings, props scale by same ratio

Example:
```
Kenney zombie: 43px tall → Scale to 64px (1.49x)
Kenney tree: 86px tall → Scale to 128px (1.49x) - maintains proportion
```

### Style Consistency Checklist

When evaluating a new asset:

- [ ] Does it have smooth, rounded shapes?
- [ ] Are edges anti-aliased (not pixelated)?
- [ ] Does it use flat colors with subtle gradients?
- [ ] Does it have a thin dark outline?
- [ ] Is the silhouette simple and clear?
- [ ] Does it use colors from our palette?
- [ ] Is it readable at the displayed size?
- [ ] Does it match player/zombie sprite style?
- [ ] Is the perspective top-down with slight depth?
- [ ] Does it have proper transparency?
- [ ] Is the scale appropriate for game world?
- [ ] Does it use tile-based dimensions (64px multiples)?

## Generation Guidelines

### For Pollinations (Flux Model)

**Good Prompts:**
```
[WIDTHxHEIGHT] game sprite, [subject], top-down view,
Kenney flat vector style, smooth rounded shapes,
bright [color] (#HEX), transparent background,
thin dark outline, simple geometric forms,
clean silhouette, casual game aesthetic
```

**Example Sizes:**
- Character: `64x64 game sprite, zombie...`
- Tree: `64x128 game sprite, oak tree, top-down...`
- House: `256x192 game sprite, small house, top-down...`
- Power-up: `48x48 game sprite, health pack...`

**Keywords to Use:**
- "flat vector style"
- "smooth rounded shapes"
- "Kenney style" or "Kenney Topdown Shooter"
- "casual game"
- "simple geometric"
- "thin outline"
- "transparent background"
- "top-down view"

**Keywords to Avoid:**
- "pixel art"
- "retro"
- "8-bit" / "16-bit"
- "realistic"
- "detailed"
- "complex"
- "3D rendered"

### For Midjourney (Reference Only)

Use for moodboards and style references:
```
flat vector game asset, [subject],
Kenney topdown shooter style,
smooth rounded shapes, simple forms,
casual mobile game aesthetic,
clean background --v 6 --style raw
```

## Common Pitfalls

### ❌ Scaling Issues
- Assets not using tile-based dimensions
- Inconsistent scale (tiny tree next to huge player)
- Stretched or squashed sprites (lost aspect ratio)
- Forgetting to scale related assets together

### ❌ Style Mismatches
- Using pixel art sprites with vector sprites
- Mixing realistic renders with flat graphics
- Complex detailed art with simple art
- Inconsistent outline thickness

### ❌ Technical Issues
- No transparency (white/colored background)
- Inconsistent sizes (random dimensions, not multiples of 16)
- Jaggy edges (aliasing artifacts)
- Wrong file format (JPEG instead of PNG)

### ❌ Design Problems
- Silhouette too complex to read
- Colors clash with palette
- Too much detail for size
- Inconsistent perspective

## Quality Verification

Use Claude Vision to verify:

1. **Compare to reference** - Side-by-side with player/zombie sprite
2. **Check transparency** - Alpha channel present?
3. **Verify scale** - Appropriate size relative to characters?
4. **Verify colors** - Within palette?
5. **Inspect edges** - Smooth and clean?
6. **Style match** - Flat/vector, not pixel art?
7. **Check dimensions** - Multiples of 16px?

## References

- **Kenney Topdown Shooter:** `/assets/kenney_collection/2D assets/Topdown Shooter/`
- **Preview:** `Sample.png` and `Preview.png` in pack folder
- **Existing Sprites:** `assets/sprites/player.png`, `zombie.png`, `tile_background.png`
- **Kenney Website:** https://kenney.nl/assets/top-down-shooter

## Example Workflow

When creating/selecting a new asset:

1. **Define Requirements** - What is it? What size in-game? What colors?
2. **Calculate Dimensions** - How many tiles tall/wide? (e.g., tree = 2 tiles = 128px)
3. **Search Kenney First** - Check KENNEY_CATALOG.md for candidates
4. **Visual Compare** - Open Preview.png files in relevant packs
5. **Extract Asset** - Copy from PNG/ folder
6. **Resize Proportionally** - Maintain aspect ratio, scale to tile multiples
7. **Verify Style** - Use checklist above
8. **Test In-Game** - See it alongside existing sprites, check scale
9. **Generate If Needed** - Only if no Kenney match found

**Remember:** Kenney first, generate second!

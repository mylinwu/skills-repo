---
name: threejs-assets
description: "Finding and downloading 3D models, HDRIs and textures with licenses recorded: Poly Haven, Sketchfab, Kenney, Quaternius, Mixamo. Use when a project needs a model, environment map or material it lacks. Hands off to `threejs-model-inspect`."
---

# Source 3D assets

Every downloaded asset carries a license, and the license decides whether it can ship, whether it can be modified
(optimizing counts), and what credit is owed. Record it at download time; reconstructing it later is guesswork.

Paths: `<this-skill-dir>` is the directory containing this SKILL.md; replace it with that absolute path. The script
needs Node 22+ and network access (behind a proxy, set `NODE_USE_ENV_PROXY=1`).

## Where to look

| Source | What | License | Access |
| --- | --- | --- | --- |
| Poly Haven | Photoscanned models, HDRIs, PBR textures | CC0 | Script, no key |
| Sketchfab | Huge model library, many animated | Per model (CC0, CC-BY, NC, ND...) | Search free; download needs `SKETCHFAB_TOKEN` |
| Kenney (kenney.nl) | Stylized low-poly kits, game assets | CC0 | Manual zip download |
| Quaternius (quaternius.com) | Low-poly kits, rigged animated characters | CC0 | Manual zip download |
| Mixamo | Rigs and animations for humanoids | Free for projects; no redistribution of raw files | Adobe account, manual |
| Khronos glTF Sample Assets | Test models for every glTF feature | Per model, mostly CC-BY or CC0 | GitHub |
| Generated | Text or image to 3D | Provider terms | `threejs-model-generate` |

## Process

1. Search, preferring CC0 so nothing is owed and anything is allowed:

   ```bash
   node "<this-skill-dir>/scripts/fetch.mjs" search polyhaven chair
   node "<this-skill-dir>/scripts/fetch.mjs" search polyhaven studio --type hdris
   node "<this-skill-dir>/scripts/fetch.mjs" search sketchfab "office chair" --license cc0 --max-faces 50000
   ```

2. Download into the project's asset folder; the script writes `CREDITS.json` and `CREDITS.md` there:

   ```bash
   node "<this-skill-dir>/scripts/fetch.mjs" download polyhaven ArmChair_01 --res 1k --out public/models
   node "<this-skill-dir>/scripts/fetch.mjs" download polyhaven studio_small_03 --type hdris --res 2k --out public/hdr
   node "<this-skill-dir>/scripts/fetch.mjs" download sketchfab <uid> --out public/models
   ```

   For manual sources (Kenney, Quaternius, Mixamo), add an entry to `CREDITS.json` by hand with the same fields.
3. Check the license against the use: `NonCommercial` cannot ship in a commercial product; `NoDerivs` forbids
   modification, which includes optimizing and recoloring; `CC-BY` needs visible credit (an about page or footer).
   Stop and ask the user when the license does not fit.
4. Pick resolution for the target: 1k textures for props, 2k for hero objects, 1k-2k HDRIs for lighting only (use
   a larger one only when it is also the visible background).
5. Hand every model to `threejs-model-inspect`: downloaded models often arrive in centimeters, off-center, or with
   8k textures.

## Anti-patterns

- Downloading from Sketchfab without checking the license label, or from sites that rehost paid models.
- Shipping CC-BY assets with no credit anywhere in the product.
- 4k HDRIs used only for lighting; the PMREM blurs them anyway.
- Committing manual downloads with no `CREDITS.json` entry.

## Done when

- Every asset in the project has a credit entry with source, author and license.
- Licenses fit the intended use, and required attribution is shown in the product.
- Downloaded models passed through `threejs-model-inspect`.

Next: `threejs-model-inspect` on each downloaded model.

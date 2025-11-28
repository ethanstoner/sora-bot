"""
Sora Prompt Generator Discord Bot
Lightweight bot that generates viral Sora video prompts on !prompt command
"""

import sys
sys.dont_write_bytecode = True

import os
import requests
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Load environment variables
load_dotenv()

# Configuration
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
TARGET_CHANNEL_ID = int(os.getenv('TARGET_CHANNEL_ID', '0'))

# Webhook configuration for custom name/avatar in target channel
SORA_WEBHOOK_NAME = "Sora Prompting"
SORA_WEBHOOK_AVATAR = "https://play-lh.googleusercontent.com/ZADfyDpLoUH0U4yuzt54hA9i7qiJKuuFAE0OR5C7QSOcBMKc9JGlsR8uGhputFgjE5_wMUMFwuRKHAjn-EsDsw=w240-h480-rw"

# Sora Prompt Generator System Prompt
SORA_PROMPT_SYSTEM = """You are an AI designed to create **high-detail, hyper-realistic Sora 2 video prompts** that look like real footage and are built to go viral on TikTok and YouTube Shorts.

🚨🚨🚨 **CRITICAL COPYRIGHT RULE - MOST IMPORTANT** 🚨🚨🚨

You MUST *always* convert ANY copyrighted characters, names, powers, lore, items, places, dialogue, or references into **original characters** that are clearly inspired by the vibe but **not recognizably tied to any existing franchise**.

**NEVER use copyrighted names:**
- Twilight, Edward Cullen, Kipo, Marvel, DC, Disney, Pixar, DreamWorks, anime characters, Spider-Man, Groot, Batman, etc.
- You MUST automatically replace them with **fully original characters** (new names, new visuals, new powers, new backstory, new personality, new outfits, new items/weapons)
- Keep the vibe/energy, but the final character should be **legally distinct**

**Always rebuild character designs with 30–50% differences:**
- Change hair color/style, clothing colors/patterns, symbols/emblems, weapon names, species/lore elements, abilities slightly, personality details, dialogue tone
- Make them original while keeping the genre vibe

**Rename and redesign ALL lore elements:**
- No Twilight wolves, no "Mantis Army", no named locations from copyrighted works
- Replace everything with new locations, new threats, new creature names, new lore, new organizations
- Everything must be **fresh and original**

**Never copy dialogue or music:**
- Rewrite dialogue in a new style, change the tone, remove trademark lines, make it unique
- No quotes from shows/movies/books
- No specific song titles or artist names - use generic descriptions like "upbeat song", "catchy tune", "energetic music"

**You can still do mashups/crossovers:**
- vampire + warrior mashup, fast hero + thunder god mashup, animal + human duo, princess + cyborg explorer
- Just make them **original characters**, not copyrighted IP

**You MUST ALWAYS override the user's text and automatically rewrite it into:**
- NEW names, NEW designs, NEW worldbuilding, NEW fashion & colors, NEW abilities, NEW threats, NEW animals, NEW dialogue, NEW lore
- NEW music/songs (never use specific song titles or artist names - use generic descriptions like "upbeat song", "catchy tune", "energetic music")
- Even if the user includes copyrighted names **directly**, you MUST transform them

⚠️ **RULE #0 - FUNNY & UNEXPECTED SCENARIOS ONLY - ALL PROMPTS MUST BE FUNNY**

EVERY SINGLE PROMPT MUST be HILARIOUS, CREATIVE, and UNEXPECTED. There are NO exceptions. Boring realistic scenarios are FORBIDDEN.

Think like a modern teenager - what's funny, absurd, unexpected, meme-worthy? What would make people laugh and share on TikTok/YouTube Shorts?

❌ NEVER use these boring scenarios:
- Person/animal walking on porch
- Mailman/delivery person with package
- Kid opening door
- Raccoon rummaging through trash
- Dog waiting on porch
- Normal everyday activities
- Birthday parties
- Surprise parties
- Normal family moments
- Pet doing normal pet things (eating, playing, normal behavior)

✅ ALWAYS use funny/creative scenarios (examples - but be creative and come up with your own!):
- Hurricane pulls squirrel away with squeal as it tries to get inside
- Rhino walks up to door, old lady opens it, rhino spits power beam that destroys house
- Raccoon gets superpowers and accidentally breaks everything
- Cat discovers it can fly and crashes into things
- Animal does something completely unexpected and hilarious
- Pet discovers teleportation and keeps appearing/disappearing
- Looksmaxxing fail (person trying to improve appearance, something hilarious goes wrong)
- Agartha portal opens and something absurd comes out
- Modern internet culture moments (memes, trends, social media fails)
- Gen Z humor, zoomer culture references
- Anything that would make teenagers laugh and share

💡 MODERN REFERENCES & TIKTOK HUMOR (SAFE VERSION):

**TikTok Humor Styles to Incorporate:**

1. **Absurdist Humor:**
   - Overly dramatic reactions to normal things
   - Random chaotic events
   - Characters acting in unexpected, nonsensical ways
   - Taking something normal and treating it like a world-ending event

2. **Deadpan + Khaby Lame Style:**
   - Silent judgment
   - Straight-faced reactions
   - Slow head-turns and sighs
   - "Are you serious right now?" energy
   - Deadpan delivery

3. **NPC / Sigma Meme Style:**
   - Exaggerated masculinity memes (safe, not offensive)
   - Robotic NPC movements
   - Loop-like behaviors
   - "Level up" sound effects
   - Meme slow zooms
   - Stiff movements
   - Dramatic slow zooms
   - Echo effects

4. **Looksmaxxing Humor (SAFE VERSION - NO BODY SHAMING):**
   - Harmless self-improvement exaggerations
   - Overdramatic transformations
   - "Bro did one pushup and became sigma"
   - "Bro thinks jawline unlocks ultra instincts"
   - "NPC → Sigma transformation arc"
   - NO body shaming or insulting groups

5. **Viral Number Trends (Safe Use):**
   - Mystery-number symbolism
   - Cryptic audio or number flashes
   - Weird inside-joke energy
   - No real-world group targeting

6. **Ohio / Backrooms Energy:**
   - Slightly cursed environments
   - Subtle surrealism
   - Unsettling but comedic glitches
   - Random unsettling weirdness
   - Strange corner of a room
   - Something slightly off

7. **Chaotic Pets + Animal Humor:**
   - Animals interrupting scenes
   - Pets acting like humans
   - Pets wearing props
   - Silly animal micro-actions
   - Animals doing human things

8. **Meme Sound Effects:**
   - vine boom
   - goofy ahh sound effect
   - distorted record scratch
   - bass-boosted thud
   - comedic whoosh/zoom effects
   - *vine boom*
   - *goofy ahh sound effect*
   - *distorted record scratch*
   - *bass boosted thud*

9. **Irony & Fake Seriousness:**
   - Pretending something dumb is incredibly important
   - Mock-"documentary" tone about pointless stuff
   - Overly serious reactions to stupid things

10. **"Glitch in the Matrix" Weird Edits:**
    - Unexpected NPC behavior
    - Loops
    - Characters freezing
    - People acting robotic

**Safe Reference Energy (Abstract, Not Direct):**
- "Political meme energy" (not specific people)
- "Dramatic reaction like viral debate clips" (format, not person)
- "Overly serious commentary on something stupid"
- "TikTok conspiracy tone"
- "Cryptic number trend humor" (like 67, 41, etc. - abstract)
- "Deadpan creator style responses"
- "Straight-faced viral reaction style"

**NEVER:**
- Direct references to real public figures in offensive ways
- Body shaming or insulting groups
- Mocking specific people or communities
- Using sensitive topics to make fun of people

**ALWAYS:**
- Use abstract meme archetypes
- Reference formats, not people
- Keep humor harmless and absurd
- Focus on situations, not personal attacks

Be CREATIVE! Don't just pick from a list - come up with your own funny, unexpected scenarios that would go viral. Think about what modern teenagers find hilarious - absurdity, deadpan reactions, NPC energy, chaotic pets, meme sounds, and safe looksmaxxing humor.

If you think of a boring realistic scenario, IMMEDIATELY replace it with a funny unexpected one. This is MANDATORY. EVERY prompt must be funny.

---

Every time you generate a prompt, you MUST follow **every single rule below**:

---

# ⭐ 1. **Start With a STRONG Hook (first 1–2 seconds) - VIRAL REQUIREMENT**

Your prompt MUST always begin with something INSTANTLY attention-grabbing (funny OR suspenseful):

**For COMEDY:**
- Someone falling over
- Object flying through frame
- Someone yelling "BRO—" or comedic exclamation
- Pet doing something chaotic
- Something exploding (safe, funny, cartoonish)
- Silly costume reveal
- Loud cartoonish sound effect
- Zoom-in with comedic timing
- Record scratch moment

**For SUSPENSE/HORROR:**
- Loud bang or crash
- Door already half open
- Something falling
- Shadow moving
- Creepy whisper immediately
- Fast zoom
- Bright light flicker
- Sudden POV shift
- Object dropping with sound

**NOT just "door opens" or "person walks in" - it needs INSTANT IMPACT.** This forces Sora to create a viral first second that grabs attention immediately.

---

# ⭐ 2. **CINEMATIC PACING - 5-Part Structure (MANDATORY for viral clips)**

Every prompt MUST use this 5-part structure with cinematic pacing:

1. **HOOK (0–2 seconds)** - INSTANTLY attention-grabbing opening:
   - Loud sound, light flicker, shadow movement, object falling, sudden POV shift
   - NOT just "door opens" or "person walks in"

2. **BUILD-UP (2–6 seconds)** - Tension or comedy builds:
   - Things get weirder/funnier/scarier
   - Environmental reactions increase
   - POV emotional reactions (breathing, hesitation, head movement)
   - Sound layers build

3. **RISING TENSION (6–10 seconds)** - Escalation continues:
   - Someone tries to hide and fails
   - Pet runs across screen
   - Something spills or falls
   - Lights flicker
   - Someone panics
   - Costume malfunctions
   - Suspense builds

4. **REVEAL / EVENT SUBJECT (10–12 seconds)** - The key moment:
   - NOT just "person in costume" or "spider on box" - make it ULTRA-SPECIFIC:
   - Describe micro-actions, textures, reactions, eye reflections, body movement, emotional cues
   - Include fur texture, leg movement, abdomen trembling, shadow shape, micro-scuttles
   - Make it CINEMATIC, not instructional

5. **TWIST ENDING (12–15 seconds)** - Final beat that triggers replays:
   - Something behind the viewer
   - Second spider dropping from ceiling
   - Hand grabbing frame
   - Box falling
   - Final whisper or sound
   - Blackout moment
   - Cat also wearing tiny cape walks in
   - "LEVEL UP!" sound effect
   - Someone pops out from behind couch

Keep it SHORT. Sora videos are brief - focus on CINEMATIC PACING with rising tension, not a calm story.

---

# ⭐ 2.5. **Copyright Protection (CRITICAL)**

If you encounter ANY copyrighted characters, names, powers, lore, items, places, dialogue, or references:
- IMMEDIATELY convert them to original, legally-distinct variants
- Change names, designs (30-50% different), abilities, dialogue, lore
- Keep the vibe/energy but make it 100% legally distinct
- Even if the user includes copyrighted content directly, you MUST transform it

# ⭐ 3. **EVENT SUBJECT Must Be ULTRA-SPECIFIC with Micro-Actions**

EVENT SUBJECT must include ULTRA-SPECIFIC details - not just "spider on box" or "person in costume":

**For Animals/Creatures:**
- Fur texture, leg movement, abdomen trembling, shadow shape, eye reflections, micro-scuttles, posture, breathing, blinking, weight shifts

**For People:**
- Breathing, blinking, shifting weight, hands fidgeting, jacket rustling, adjusting posture, subtle facial micro-expressions
- **PLUS COMEDIC:** Person doing little wiggles, costume squeaking, dog confused head tilt, dramatic pose that looks ridiculous, small slip or stumble, overly serious facial expression for something dumb, tiny dance moves, exaggerated reactions

**For POV:**
- Breathing, heartbeat, swallowing, head movement, hesitation, tiny physical responses, hands trembling subtly, micro-shakes, head tilts

**Describe what the viewer FEELS and SENSES, not just "camera does X."**

Micro-actions = realism. Ultra-specific micro-actions = cinematic Sora output.

---

# ⭐ 4. **Environment MUST Be "Alive" and Reactive**

The environment must REACT and feel alive - not static descriptions:

**Always include:**
- Dust motes floating in light
- Flickering lights
- Ambient noises (distant dripping, creaking, humming)
- Subtle object motion (boxes shifting under weight, spider web strands moving, swinging dangling bulb)
- Reflections shifting
- Shadows changing
- Airflow (wind, drafts)
- Mold smell (for indoor scenes)
- Objects wobbling
- Shadows moving naturally

**The scene must REACT:**
- Camera reacts to noise
- Light reacts to motion
- Shadows change
- Dust moves
- Objects shift

**NOT just "old trunks, forgotten boxes" - describe them REACTING: motes of dust floating, boxes shifting slightly under weight, spider web strands moving, swinging dangling bulb, distant dripping water.**

This is what makes Sora outputs cinematic and viral.

---

# ⭐ 5. **Always Add a Lighting Evolution**

Prompts should clearly describe lighting changes:
- bright → dim
- warm → cold
- flickering
- neon reflections
- golden hour → shadowy
- dramatic spotlight moment

Light transitions = emotional transitions.

---

# ⭐ 6. **POV Must Feel HUMAN (not instructional)**

For POV shots, describe what the VIEWER FEELS and SENSES, not just "camera does X":

**Include emotional POV reactions:**
- Breathing (audible, heavy, quickening)
- Heartbeat (can feel it, racing)
- Swallowing (nervous)
- Head movement (tiny tilts, looking around)
- Hesitation (pausing, slowing down)
- Hands trembling subtly
- Micro-shakes (from nervousness, walking)
- Head tilts (looking up/down, side to side)
- Autofocus hunting (lens breathing, focus pulsing)
- Tiny lens flares
- Small hand motions (reaching, adjusting)

**NO SCRIPT-TONED SENTENCES:**
- ❌ Avoid: "Camera is first-person, slightly bobbing like walking."
- ✅ Use: "The camera sways slightly with each step, like real head movement, with micro-shakes from nervousness and autofocus hunting as the viewer hesitates, breathing quickening."

**Describe the POV like a HUMAN EXPERIENCING IT, not like a script instruction.**

This makes the footage feel real and cinematic.

---

# ⭐ 7. **Add SENSORY-LAYER DETAIL (sound, texture, motion, lighting)**

Every prompt must include MULTIPLE sensory layers:

**SOUND LAYERS:**
- Footsteps (heavy breathing, each step echoes)
- Wood creaks, floorboards creaking
- Distant hum, buzzing, dripping
- Breathing (audible, heavy)
- Wind, fabric rustling
- Ambient (creaking, distant faint buzzing)
- Sudden surprising audio cue (jarring scuttling, loud bang, cartoonish "BAM!")
- **PLUS COMEDIC:** Cartoonish "BAM!", "BOOM!" SFX, record scratch, meme-style sound effects (vine boom, goofy ahh sound effect, distorted record scratch, bass-boosted thud), "LEVEL UP!" sound, exaggerated gasp, cartoonish whoosh

**LIGHTING EVOLUTION:**
- Bright → dim shift
- Color cast changes
- Flicker patterns
- Natural light from window → dramatic shift to dimmer/more ominous
- Light reacts to motion

**TEXTURE DETAILS:**
- Fur texture, dusty surfaces, rough wood, smooth glass
- Describe what things FEEL like, not just look like

**Use phrases like:** smash zoom, comedic timing, cartoonish sound effects, boom SFX, record scratch moment, fast whip pan, shaky zoom in, exaggerated gasp, meme-style slow zoom

**NO SCRIPT-TONED SENTENCES:**
- ❌ Avoid: "Camera is first-person."
- ✅ Use: "The camera sways slightly with each step, like real head movement, with micro-shakes and autofocus hunting."

Sensory layers = cinematic Sora output. Comedy/suspense = pacing + sound.
- animal noises
- electronic buzz

Sora uses this to build physical realism.

---

# ⭐ 8. **Add a COMEDIC Twist Ending (MANDATORY for viral funny clips)**

Every prompt MUST end with a COMEDIC surprising second moment that triggers replays:
- Cat also wearing tiny cape walks in
- Something falls over off-screen with loud crash
- Toy rocket fires and bounces off camera
- Loud "LEVEL UP!" or meme sound effect plays
- Costume malfunctions hilariously
- Someone else pops out from behind couch
- Dog confused head tilt
- Dramatic pose that looks ridiculous
- Another animal appears doing something absurd
- Object falls with cartoonish sound
- Glitch moment in funny way
- Someone appears behind camera doing something silly
- Secondary noise (meme sound effect)
- Small supernatural hint (but funny)
- Emotional beat (but comedic)

**NOT just "mild surprise" - it needs COMEDIC PAYOFF.** This makes people rewatch and share.

---

# ⭐ 9. **Be Ultra-Specific with ABSURD SERIOUSNESS**

Never say "a dog." Say: "a small terrier mix with messy brown fur, bright jittery eyes, and a tiny blue collar jingling softly."

Never say "a room." Say: "a narrow hallway with peeling paint, scuffed baseboards, and a crooked lamp casting a golden glow."

**PLUS add "Absurd Seriousness" - pretend something silly is DEAD SERIOUS:**
- Person speaks like dramatic superhero for something dumb
- Overly epic music plays for no reason
- Dramatic lighting on something stupid
- Heroic pose but wearing fuzzy slippers
- Overly serious facial expression for something silly
- Dramatic over-seriousness about dumb situations

This is TikTok humor - dramatic over-seriousness about dumb things.

Specificity = realism = viral output.

---

# ⭐ 10. **Make it Feel "Caught in the Moment" with MEME/VIRAL COMEDY TROPES**

Avoid cinematic perfection PLUS add meme/viral comedy vibes:
- slightly messy backgrounds
- off-center framing
- accidental tilts
- real-world sounds
- natural motion
- casual clothes
- authentic settings
- **PLUS COMEDIC TROPES (not copyrighted, just vibes):**
  - Goofy ahh energy
  - Sigma stare moment
  - NPC moment
  - Ohio backrooms energy
  - Unexpected Fortnite sound effect
  - Anime zoom-in on something stupid
  - Dramatic over-seriousness
  - TikTok dance energy
  - Meme-style reactions

Not cinematic — authentic. But also FUNNY and VIRAL-WORTHY with meme energy.

---

# ⭐ 11. **Technical Constraints**

ALWAYS include these (very important for Sora):
- **Vertical 9:16 aspect ratio**
- **1080x1920 resolution**
- **10–15 seconds duration**
- **Smartphone or real camera behavior**
- **Real-world physics**
- **Natural color grading**

This forces Sora to output TikTok-style vertical videos.

---

# ⭐ 11. **NEVER Use Copyrighted Characters or Items - CRITICAL RULE**

You MUST NEVER use copyrighted characters like:
- Spider-Man, Batman, Superman, any Marvel/DC characters
- Disney characters (Mickey, Groot, etc.)
- Movie characters, TV show characters
- Branded characters from any franchise

If a template mentions or you think of a copyrighted character:
- IMMEDIATELY create an ORIGINAL variation
- Change the name completely (e.g., "Spider-Man" → "Web-Slinger" or "Arachnid Hero")
- Change the outfit/design completely
- Change any emblems/symbols
- Create a legally distinct original character
- Keep a similar vibe but make it 100% original

Examples:
- "Spider-Man" → "A young hero in a red and blue web-patterned suit with acrobatic abilities"
- "Groot" → "A tall tree-like humanoid with bark-like skin and gentle personality"
- "Batman" → "A dark-clad vigilante with cape and mask"

This is MANDATORY - copyright violations will get content removed. Always create original characters.

---

# ⭐ 12. **Focus on Viral Potential**

Every prompt must include:
- a hook
- tension
- a reveal
- a twist
- real-world camera behavior
- multiple sensory layers
- emotion
- micro-actions
- specific physical details

These elements spike retention and replay rate.

---

# ⭐ 13. **Keep the ENERGY High**

Your writing tone must always feel:
- dynamic
- atmospheric
- sensory-rich
- emotionally vivid

Never bland, never flat.

---

# ⭐ 14. **Never Output Generic, Plain, or Minimal Prompts**

NO "simple POV of a dog walking."
NO "man enters a room."
NO "camera pans and shows things."

EVERY prompt must feel like a cinematic short film in 12–15 seconds.

---

# ⭐ 15. **Prioritize Humor, Creativity, and Unexpected Scenarios**

Every prompt should be FUNNY, CREATIVE, and UNEXPECTED. Think viral-worthy moments:

Examples of funny/creative scenarios:
- A squirrel trying to get inside, then a hurricane pulls it away with a squeal
- A rhino walks up to a door, old lady opens it, rhino spits a beam of power that destroys a house
- A raccoon gets stuck in a mailbox and makes funny faces
- A cat discovers it has superpowers and accidentally breaks everything
- An animal does something completely unexpected and hilarious

Your prompts should make people:
- Laugh out loud
- Want to share immediately
- Say "wait, what?!"
- Rewatch multiple times

Be creative, be funny, be unexpected. Realistic scenarios are good, but HILARIOUS and UNEXPECTED scenarios are BETTER for viral content.

---

CRITICAL OUTPUT FORMAT - You MUST output exactly in this format. DO NOT skip the Prompt section:

Caption:
[Write a catchy, viral TikTok caption here - should be engaging, use relevant hashtags, emojis, and be optimized for TikTok engagement. Keep it concise but attention-grabbing.]

Prompt:
[Fully expanded Sora prompt with ALL 15 rules above applied. 

CRITICAL FORMATTING: You MUST write the prompt with EXPLICIT phase labels. Your output format MUST be exactly like this example:

[Template's base camera/setting description]

**Phase 1 - Hook (0-2 seconds):** [Your description here with all details]

**Phase 2 - Build-Up (2-7 seconds):** [Your description here with all details]

**Phase 3 - Tension Rise (7-10 seconds):** [Your description here with all details]

**Phase 4 - Main Event/Reveal (10-13 seconds):** [Your description here with all details]

**Phase 5 - Twist/Ending (13-15 seconds):** [Your description here with all details]

Technical specifications: Vertical 9:16 aspect ratio, 1080x1920 resolution, 10-15 seconds duration.

STYLE TAGS: [copy from template]

YOU MUST include the exact phase labels "**Phase 1 - Hook (0-2 seconds):**", "**Phase 2 - Build-Up (2-7 seconds):**", etc. Do NOT write a flat paragraph description. The phase structure is MANDATORY.

Each phase must include: micro-actions, environmental reactions, lighting changes, camera behavior, specific sounds, ultra-specific details.

IMPORTANT: Do NOT include "PROMPT:" in the actual prompt text - just write the content directly starting with the template's base description.]

MANDATORY: You MUST include BOTH Caption: and Prompt: sections. Never output only the Caption. The Prompt section is REQUIRED and must contain the full expanded prompt with EVENT SUBJECT filled in using ALL 15 rules above, structured as a 4-5 phase sequence, plus STYLE TAGS. 

CRITICAL: The EVENT SUBJECT MUST be FUNNY, CREATIVE, and UNEXPECTED. This is the MOST IMPORTANT requirement. EVERY prompt must be funny - there are NO exceptions.

Think of scenarios that make people laugh, share, and rewatch. Be imaginative - hurricanes pulling away squirrels, rhinos spitting power beams, animals doing unexpected things, modern cultural absurdities (looksmaxxing fails, Agartha portals, internet culture moments).

If you find yourself writing a boring realistic scenario (person walking, mailman, delivery, kid opening door, raccoon in trash, birthday party, surprise party, normal family moments), STOP IMMEDIATELY and replace it with a funny unexpected one (hurricane, power beams, superpowers, flying animals, teleportation, absurd modern references, etc.). This is MANDATORY.

Also: Keep prompts SHORT and FOCUSED. Sora videos are 10-15 seconds - focus on ONE funny moment, not a long story.

🚨🚨🚨 **CRITICAL COPYRIGHT RULE - MANDATORY** 🚨🚨🚨

NEVER use copyrighted characters, names, powers, lore, items, places, dialogue, or references (Twilight, Edward Cullen, Kipo, Marvel, DC, Disney, Pixar, DreamWorks, anime, Spider-Man, Groot, Batman, etc.).

**You MUST automatically rewrite ANY copyrighted content into:**
- NEW names (completely different)
- NEW designs (30-50% different: hair, clothing, colors, symbols, weapons)
- NEW worldbuilding (new locations, threats, creatures, lore, organizations)
- NEW abilities (similar vibe but different execution)
- NEW dialogue (rewritten in new style, no trademark lines)
- NEW everything (fresh and original)

**Examples of transformations:**
- "Spider-Man" → "A young hero in a red and blue web-patterned suit with original design" (NOT Spider-Man)
- "Groot" → "A tall tree-like humanoid with bark-like skin and original personality" (NOT Groot)
- "Edward Cullen" → "A pale-skinned character with unique features" (NOT Edward Cullen)
- "Twilight wolves" → "Original werewolf-like creatures with unique lore" (NOT Twilight)

**Keep the vibe/energy but make it 100% legally distinct.** This is MANDATORY. Even if the user includes copyrighted names directly, you MUST transform them.

Do this for EVERY prompt I paste. Always start with "Caption:" and then "Prompt:" on separate lines."""

# Prompt Templates
PROMPT_TEMPLATES = {
    "1": """CCTV / RING DOORBELL CAMERA — Full Prompt Template

Ultra-realistic Ring doorbell camera footage. Slight wide-angle fisheye lens. Static camera mounted on a suburban front porch. Natural daylight with soft overcast lighting. Camera never moves.
EVENT SUBJECT: [MUST be FUNNY and UNEXPECTED - hurricane pulls animal away with squeal, rhino spits power beam that destroys house, animal gets superpowers, pet teleports, animal does something completely absurd. NOT: normal walking, mailman, delivery, kid opening door, raccoon in trash, squirrel raiding feeder - these are BORING and FORBIDDEN]
Show real-world motion and physics. Slight vibrations from wind. Natural color, mild grain, subtle lens distortion, light compression artifacts.
Include ambient audio of wind, distant cars, light porch creaks.

STYLE TAGS:
CCTV, Ring doorbell cam, ultrarealistic, wide-angle, lens distortion, static camera, real motion blur, suburban porch.""",

    "2": """FUNNY ANIMAL FAILS (HANDHELD SMARTPHONE) — Full Prompt Template

Ultra-realistic handheld smartphone footage inside a warm, bright kitchen in a real modern home. Visible cabinets, fridge magnets, countertop clutter, dishes, and everyday mess. Slight handheld shake and casual framing.
EVENT SUBJECT: [describe the animal(s) and the chaotic/funny action here]
Animals move naturally with breathing, blinking, weight shifting, quick reactions. Warm, soft indoor lighting. Looks like a real phone video someone recorded on the spot.
Authentic indoor sound.

STYLE TAGS:
Home video, smartphone camera, warm lighting, handheld shake, real household setting, natural pet movement.""",

    "3": """REAL LIFE BODY CAM FOOTAGE — Full Prompt Template

Ultra-realistic police-style body camera footage. Wide-angle fisheye lens. Natural lighting. Camera mounted on a person walking or running, with real step motion, breathing shakes, and fast direction changes.
EVENT SUBJECT: [describe your animal/person and the intense action here]
Use real-world physics. Add mild grain, subtle lens distortion, and compression like real body cam footage.
Include a battery percentage icon in the top-right corner and a date/time stamp on the bottom edge.
Ambient audio: wind, clothing rustle, breathing, cars, footsteps.

STYLE TAGS:
Body cam, wide-angle, timestamp, battery overlay, authentic movement, compression artifacts, outdoor realism.""",

    "4": """OLYMPIC BROADCAST FOOTAGE — Full Prompt Template

Ultra-realistic Olympic broadcast footage inside a packed sports stadium. Bright arena lighting, smooth TV-style camera pans and zooms, close-ups of athletes, side angles of action, audience reaction shots.
EVENT SUBJECT: [describe the athlete/animal/person and the competitive action here]
Add on-screen timer, country abbreviations, flags, scores, and broadcast graphics.
Include announcer commentary, crowd noise, echoing stadium ambience, and sport-specific sounds.
Use realistic uniforms, sponsor banners, motion blur, and lens flares.

STYLE TAGS:
Olympic broadcast, sports camera, live timer overlay, score graphics, bright stadium lighting, crowd energy.""",

    "5": """AI Glow-Up / Transformation Scene

Ultra-realistic transformation video. Start with a normal person in a casual outfit standing in a simple room. Then in a smooth 3-2 second transition they transform into an ultra-stylish version of themself: premium outfit, luxury setting, slow motion reveal. EVENT SUBJECT: [describe the person and the transformation action]
Lighting changes from plain to dramatic spotlight. Visible wardrobe change, hair styled, accessories appear. Camera is slightly handheld but smooth. Ambient sound: subtle whoosh for transformation, then upbeat music.
STYLE TAGS: glow-up transformation, before & after, luxury reveal, slow motion transition, real motion, makeover vibe.""",

    "6": """AI Character Mashup / "What if" Scenario

Ultra-realistic dynamic video of two unlikely characters interacting in a vivid setting. The first character: [describe character A], the second character: [describe character B]. EVENT SUBJECT: [the action they're doing together]
Scene: wide shot then close-up, natural color tones, realistic lighting, slight lens flare. Motion: characters move, talk, react to each other. Sound: ambient environment + dialog + subtle background music.
STYLE TAGS: character mashup, "what if" scenario, crossover, realistic CGI-level, high detail, cinematic camera.""",

    "7": """AI Pet or Animal Superpower Scene

Ultra-realistic video of a pet (or wild animal) in a real home or outdoor setting, suddenly discovering a superpower. EVENT SUBJECT: [animal and its superpower/action]
Setting: If indoor: living room/kitchen, natural daylight. If outdoor: forest clearing or urban rooftop. Animal's motion: subtle at first, then strong action (e.g., flying, glowing eyes, energy bursts). Slight camera shake in action. Sound: ambient + animal sounds + subtle effect when power activates.
STYLE TAGS: animal superhero, pet action scene, hyperrealistic, dynamic motion, visual effects, natural setting.""",

    "8": """AI Time-Travel / Future Self Scene

Ultra-realistic futuristic video. A person in today's clothes in a mundane location (e.g., coffee shop, city sidewalk) then glitched transition to their future self in a warped environment. EVENT SUBJECT: [person and their "future self" action]
Camera: first handheld, then stable drone-style shot. Lighting: starts warm, then shifts to cool blue hue. Motion: subtle warp effect, glitch visuals, then smooth futuristic reveal. Sound: ambient city + glitch audio + futuristic hum.
STYLE TAGS: time-travel, future self, glitch transition, real person, cinematic, urban setting, visual effects.""",

    "9": """AI Mini-Story "POV" Short

Ultra-realistic "POV" video from first-person view. The viewer is walking into a scene (door opens, hallway, etc.). EVENT SUBJECT: [what the viewer sees and what happens next]
Camera is first-person, slightly bobbing like walking. Setting: modest home or urban alley. Action: a sudden reveal (e.g., something unexpected behind the door, creature appears, event happens). Lighting: natural then slight dramatic shift. Sound: footsteps, ambient, sudden surprising audio cue.
STYLE TAGS: POV camera, first-person walk, surprise moment, realistic motion, real environment, suspense short.""",

    "10": """AI "Hidden Camera" Prank or Surprise Scene

Ultra-realistic stationary hidden camera video in a home or small business. Slight grain, fixed lens, subtle compression artifacts, natural lighting. EVENT SUBJECT: [describe the person/animal and the surprise/prank action]
Camera viewpoint: corner of room, maybe near ceiling. Ambient audio: chatters, light background music, movement. Action: person walks in, something unexpected happens (animal appears, object drops, funny reaction).
STYLE TAGS: hidden camera, surveillance style, candid moment, real-life setting, subtle grain, natural light."""
}

async def generate_sora_prompt(template_number=None, custom_template=None):
    """Generate a viral Sora prompt using Groq API"""
    
    # Select template
    if custom_template:
        template = custom_template
    elif template_number and template_number in PROMPT_TEMPLATES:
        template = PROMPT_TEMPLATES[template_number]
    else:
        # Random template
        import random
        template = random.choice(list(PROMPT_TEMPLATES.values()))
    
    # Build messages with explicit instruction
    user_message = f"""🚨🚨🚨 CRITICAL: YOU MUST CREATE A FUNNY, MODERN SCENARIO 🚨🚨🚨

STEP 1: Create a FUNNY, CREATIVE, UNEXPECTED scenario that would go viral on TikTok/YouTube Shorts.

💡 INSPIRATION (you can use these OR create your own funny ideas):
- Hurricane/storm pulls animal away with squeal
- Animal gets superpowers (flying, teleporting, shooting energy, glowing eyes)
- Animal spits/shoots power beam that destroys something
- Agartha portal opens and something absurd comes out
- Looksmaxxing fail (person trying to improve appearance, something hilarious goes wrong - SAFE, no body shaming)
- Modern internet culture moments (memes, trends, social media fails)
- Completely absurd unexpected moments (makes no sense but hilarious)
- Natural disaster with funny twist (tornado picks up animal, earthquake causes funny reaction)
- Skibidi toilet references (when appropriate)
- Sigma/alpha moments gone wrong (safe NPC humor)
- Gen Z humor, zoomer culture
- TikTok humor: absurdist reactions, deadpan energy, NPC behavior, chaotic pets, meme sounds
- Ohio/backrooms energy (slightly cursed, surreal)
- Anything that would make teenagers laugh and share

❌ FORBIDDEN - DO NOT USE (if you use these, you FAIL):
- Person/animal walking normally
- Mailman/delivery person, delivery driver, Amazon package delivery
- Cat/dog doing normal things (stealing food, pouncing, playing, eating, approaching packages, pawing at things, normal pet behavior)
- Birthday parties, surprise parties
- Family moments
- Normal everyday activities
- Squirrel just running (must have something funny/unexpected)
- Cat trying to steal food/toast/breakfast (BORING - normal pet behavior)
- Cat approaching/pawing at packages (BORING - normal pet behavior)
- Pet doing normal pet things (playing, eating, running normally, sniffing, meowing normally)
- Kitchen scenes with normal pet behavior
- Package delivery scenarios (unless something absurd happens)
- Any realistic, everyday scenario

⚠️ REMEMBER: 
- If it's something a normal pet/person would do in real life, it's BORING
- Think like a modern teenager - what's funny, absurd, unexpected, meme-worthy?
- Use modern references when appropriate (looksmaxxing, Agartha, internet culture, memes)
- Be creative! Come up with your own funny scenarios that would make people laugh and share

STEP 2: Write EXACTLY in this format with CINEMATIC 5-PART STRUCTURE (MANDATORY - you MUST use all 5 parts):

[Template's base camera/setting description]

**HOOK (0-2 seconds):** [INSTANTLY attention-grabbing - loud sound, light flicker, shadow movement, object falling, sudden POV shift, NOT just "door opens" or "person walks in". Include: what the viewer sees/hears immediately that grabs attention]

**BUILD-UP (2-6 seconds):** [Tension/comedy builds - things get weirder/funnier/scarier, environmental reactions increase (dust motes floating, lights flickering, objects shifting), POV emotional reactions (breathing becomes audible, hesitation, head movement), sound layers build (footsteps echo, creaks, ambient noises), lights flicker, something spills, someone panics. Make environment "alive" - describe reactions, not static descriptions]

**RISING TENSION (6-10 seconds):** [Escalation continues - someone tries to hide and fails, pet runs across screen, costume malfunctions, suspense builds, breathing quickens, camera micro-shakes from nervousness, heartbeat can be felt, swallowing audible, hands trembling. Environmental reactions intensify - shadows change, dust swirls, objects wobble more]

**REVEAL / EVENT SUBJECT (10-12 seconds):** [The key moment - ULTRA-SPECIFIC, not just "person in costume" or "spider on box". Describe CINEMATICALLY: micro-actions (breathing, blinking, leg movements), textures (fur texture, rough surfaces, smooth materials), reactions (eye reflections, body movement, emotional cues), specific details (fur texture visible - coarse hairs catching light, leg movement - eight legs positioned defensively, abdomen trembling, shadow shape looms large, micro-scuttles - tiny leg movements). Make it CINEMATIC - describe what viewer FEELS and SENSES, not "camera does X". Include: environmental reactions, lighting evolution, sensory layers, ultra-specific details]

**TWIST ENDING (12-15 seconds):** [Final beat that triggers replays - something behind viewer, second creature dropping, hand grabbing frame, box falling with loud crash, final whisper/sound, blackout moment, cat also wearing tiny cape, "LEVEL UP!" sound, someone pops out, dog confused head tilt. Must be unexpected and trigger rewatch]

STYLE TAGS: [copy from template]

⚠️ CRITICAL: You MUST use ALL 5 parts (Hook, Build-Up, Rising Tension, Reveal, Twist). DO NOT use old 3-part structure (Hook, Main Action, Twist). The 5-part structure is MANDATORY.

EXAMPLE (copy this exact CINEMATIC style):
Ultra-realistic "POV" video from first-person view. The viewer is walking into a scene.

**HOOK (0-2 seconds):** LOUD "BAM!" sound as the door swings open with a creak, revealing a dim hallway. A shadow moves across the wall instantly, and the camera (viewer's head) jolts slightly in surprise. Dust motes float in the sliver of light from the doorway, and a distant creaking sound echoes.

**BUILD-UP (2-6 seconds):** The camera sways slightly with each step, like real head movement, with micro-shakes from nervousness. The viewer's breathing becomes audible, quickening. The hallway floorboards creak under each footstep, and the sound echoes. A swinging dangling bulb flickers overhead, casting moving shadows. Boxes shift slightly under unseen weight in the distance. The autofocus hunts slightly as the viewer hesitates, head tilting to look around.

**RISING TENSION (6-10 seconds):** The viewer's heartbeat can be felt, racing. A faint whisper seems to echo "get out while you still can" - the camera (head) turns slightly, searching for the source. The breathing quickens, and hands can be felt trembling subtly. The light flickers more dramatically, and dust motes swirl in the air. A distant dripping sound becomes audible. The camera micro-shakes from nervousness, and the viewer swallows audibly.

**REVEAL / EVENT SUBJECT (10-12 seconds):** The camera pans across a cluttered storage room, revealing a massive tarantula perched on a dusty stack of boxes. The tarantula's fur texture is visible - coarse, dark brown hairs catching the dim light. Its eight legs are positioned in a defensive posture, with the front legs slightly raised. The abdomen trembles slightly, and the shadow shape looms large on the wall behind. The tarantula's multiple eyes reflect the flickering bulb light, creating tiny glints. Micro-scuttles - tiny leg movements - can be seen as it adjusts its position. The voice suddenly screams loudly, jarring and unexpected. The camera (viewer's head) jolts back in shock, with a quick head movement backward.

**TWIST ENDING (12-15 seconds):** As the viewer backs away, a second spider drops from the ceiling behind them with a soft "thud" sound. The camera whips around (head turning fast), revealing the second creature. A box falls over off-screen with a loud crash, and the light flickers violently. The final whisper echoes "too late..." and the screen goes to blackout for a moment before cutting.

STYLE TAGS: POV camera, first-person walk, surprise moment, realistic motion, real environment, suspense short.

NOW DO THE SAME FOR THIS TEMPLATE:

Template:
{template}

CRITICAL: 
- MUST be funny OR suspenseful and creative (think modern teenage humor - what would go viral on TikTok?)
- MUST use 5-part CINEMATIC structure: Hook/Build-Up/Rising Tension/Reveal/Twist (NOT long paragraphs)
- MUST have STRONG hook in first 1-2 seconds (loud sound, light flicker, shadow movement, NOT just "door opens")
- MUST include escalation (things get weirder/funnier/scarier)
- MUST have ULTRA-SPECIFIC reveal (NOT just "person in costume" or "spider on box" - describe micro-actions, textures, reactions, eye reflections, body movement)
- MUST have twist ending that triggers replays (something behind viewer, second creature, hand grabbing frame, etc.)
- MUST include sensory layers (sound: footsteps, breathing, creaks, ambient; lighting: bright→dim shift, flicker; texture details)
- MUST make environment "alive" (dust motes, flickering lights, objects shifting, shadows changing, ambient noises)
- MUST make POV feel HUMAN (breathing, heartbeat, swallowing, head movement, hesitation, micro-shakes, NOT script-toned "camera is first-person")
- MUST use CINEMATIC language (describe what viewer FEELS and SENSES, not "camera does X")
- MUST include TikTok comedy timing OR suspense tension (cartoonish sounds, meme effects like vine boom, goofy ahh, record scratch, bass-boosted thud, OR suspense build-up)
- MUST incorporate TikTok humor styles: absurdist reactions, deadpan/Khaby Lame energy, NPC/sigma meme style (safe), looksmaxxing humor (safe - no body shaming), chaotic pets, Ohio/backrooms energy, meme sound effects
- MUST be short (10-15 seconds focus)
- MUST include modern references when appropriate (looksmaxxing - safe version, Agartha, internet culture, memes, Gen Z humor, TikTok humor styles: absurdist, deadpan, NPC/sigma, chaotic pets, meme sounds)
- NO boring realistic scenarios
- NO calm/mild surprises - needs STRONG ENERGY (comedic chaos OR suspense tension)
- NO script-toned sentences - use cinematic descriptions
- 🚨 NO COPYRIGHTED CONTENT - MUST convert ALL copyrighted characters/names/lore into original, legally-distinct variants
- Be creative - come up with your own scenarios, not just from a list!
STYLE TAGS: [from template]

DO NOT write a flat paragraph. The 5-PART phase structure with explicit labels is MANDATORY: HOOK, BUILD-UP, RISING TENSION, REVEAL, TWIST. DO NOT use old 3-part structure (Hook, Main Action, Twist). 

Each phase must include:
- HOOK: Instant attention-grabbing moment
- BUILD-UP: Environmental reactions (dust motes, flickering lights, objects shifting), POV emotional reactions (breathing, hesitation), sound layers building
- RISING TENSION: Escalation, environmental reactions intensify, POV reactions increase (heartbeat, trembling)
- REVEAL: ULTRA-SPECIFIC details (micro-actions, textures, reactions, eye reflections), CINEMATIC language (describe what viewer FEELS, not "camera does X"), environmental reactions, lighting evolution, sensory layers
- TWIST: Unexpected final beat that triggers replays

The scenario MUST be FUNNY, CREATIVE, and UNEXPECTED - NOT boring realistic scenarios. Think: hurricanes pulling animals, rhinos spitting power beams, animals with superpowers, completely unexpected hilarious moments.

🚨 COPYRIGHT PROTECTION: If you see ANY copyrighted names/characters/lore in the template or your thoughts, IMMEDIATELY convert them to original, legally-distinct variants. Change names, designs, abilities, dialogue, lore - keep the vibe but make it 100% original.)

CRITICAL: The EVENT SUBJECT must be HILARIOUS and UNEXPECTED. DO NOT use boring realistic scenarios like:
- "Dog on porch waiting for owner" ❌
- "Mailman delivers package" ❌  
- "Neighbor steals package" ❌
- "Kid rides bike" ❌

USE FUNNY, CREATIVE scenarios like:
- A squirrel trying to get inside, then a hurricane pulls it away with a squeal ✅
- A rhino walks up to a door, old lady opens it, rhino spits a beam of power that destroys a house ✅
- A raccoon gets superpowers and accidentally breaks everything ✅
- An animal does something completely unexpected and hilarious ✅
- A cat discovers it can fly and crashes into things ✅

Be creative and funny - this is what makes content go viral! Realistic scenarios are BORING. Hilarious unexpected scenarios are VIRAL.

CRITICAL COPYRIGHT RULE: NEVER use copyrighted characters like Spider-Man, Groot, Batman, Disney characters, Marvel/DC characters, or any branded characters. If you think of one, IMMEDIATELY create an original variation: change the name completely, change the outfit/design, make it legally distinct. Example: "Spider-Man" → "A young hero in a red and blue web-patterned suit with acrobatic abilities" (no mention of Spider-Man name). "Groot" → "A tall tree-like humanoid with bark-like skin" (no mention of Groot name). This is MANDATORY - copyright violations will get content removed.

Do not stop after the Caption. Always include the full Prompt section written as a cinematic 5-phase sequence (not just a flat description)."""
    
    messages = [
        {'role': 'system', 'content': SORA_PROMPT_SYSTEM},
        {'role': 'user', 'content': user_message}
    ]
    
    # Estimate tokens
    total_chars = sum(len(str(m.get('content', ''))) for m in messages)
    estimated_tokens = total_chars // 4
    
    try:
        response = requests.post(
            'https://api.groq.com/openai/v1/chat/completions',
            headers={
                'Authorization': f'Bearer {GROQ_API_KEY}',
                'Content-Type': 'application/json'
            },
            json={
                'model': 'llama-3.1-8b-instant',
                'messages': messages,
                'max_tokens': 1500,  # Allow longer responses for caption + detailed prompt (increased to prevent truncation)
                'temperature': 1.0,
                'stream': False
            },
            timeout=30
        )
        
        if response.status_code == 200:
            bot_response = response.json()['choices'][0]['message']['content']
            
            # Validate that response contains both Caption and Prompt sections
            if "Caption:" in bot_response and "Prompt:" in bot_response:
                # Remove duplicate "PROMPT:" if it appears in the prompt section
                import re
                # Remove "PROMPT:" that appears after "Prompt:" label
                bot_response = re.sub(r'(Prompt:\s*\n?\s*)PROMPT:', r'\1', bot_response, flags=re.IGNORECASE)
                # Also remove standalone "PROMPT:" at start of prompt content (after "Prompt:" label)
                bot_response = re.sub(r'(Prompt:\s*\n\s*)PROMPT:\s*\n', r'\1', bot_response, flags=re.IGNORECASE)
                # Remove "CCTV / RING DOORBELL CAMERA — Full Prompt Template" if it appears in prompt
                bot_response = re.sub(r'CCTV / RING DOORBELL CAMERA.*?Full Prompt Template\s*\n', '', bot_response, flags=re.IGNORECASE)
                
                # Check for copyrighted songs/music
                copyrighted_songs = [
                    "uptown funk", "mark ronson", "bruno mars", "taylor swift", "beyonce", 
                    "ed sheeran", "justin bieber", "ariana grande", "drake", "the weeknd",
                    "billie eilish", "post malone", "dua lipa", "harry styles", "adele"
                ]
                has_copyrighted_song = any(song.lower() in bot_response.lower() for song in copyrighted_songs)
                if has_copyrighted_song:
                    print(f"⚠️ Warning: Response contains copyrighted song/music reference", flush=True)
                    if "STYLE TAGS:" in bot_response:
                        bot_response = bot_response.replace(
                            "STYLE TAGS:",
                            "🚨 **WARNING: This prompt contains copyrighted song/music references. Please regenerate without specific song titles or artist names. Use generic descriptions like 'upbeat song', 'catchy tune', etc.**\n\nSTYLE TAGS:"
                        )
                
                # Check if it has phase structure (Hook/Main Action/Twist) - MANDATORY
                has_phases = any(phase in bot_response for phase in [
                    "Hook (0-2 seconds)",
                    "Hook (0-2s)",
                    "**Hook (0-2 seconds):**",
                    "**Hook (0-2s):**",
                    "Main Action (2-10 seconds)",
                    "Main Action (2-10s)",
                    "**Main Action (2-10 seconds):**",
                    "**Main Action (2-10s):**",
                    "Twist/Reaction (10-15 seconds)",
                    "Twist/Reaction (10-15s)",
                    "**Twist/Reaction (10-15 seconds):**",
                    "**Twist/Reaction (10-15s):**",
                    "Phase 1 - Hook",
                    "Phase 2 - Build-Up",
                    "Phase 3 - Tension Rise",
                    "Phase 4 - Main Event",
                    "Phase 5 - Twist"
                ])
                
                # Check if it's written as a flat paragraph (BAD)
                prompt_section = bot_response.split("Prompt:")[1] if "Prompt:" in bot_response else ""
                is_flat_paragraph = (
                    "EVENT SUBJECT:" in prompt_section and 
                    not has_phases and
                    len(prompt_section.split("\n\n")) < 5  # Too few line breaks = likely a paragraph
                )
                
                if not has_phases:
                    print(f"⚠️ Warning: Response missing phase structure (Hook/Main Action/Twist), but has both sections", flush=True)
                    # Add prominent warning to response
                    if "STYLE TAGS:" in bot_response:
                        bot_response = bot_response.replace(
                            "STYLE TAGS:",
                            "🚨 **WARNING: This prompt is missing the required Hook/Main Action/Twist structure!**\n\n**It should be formatted like this:**\n\n**Hook (0-2 seconds):** [description]\n**Main Action (2-10 seconds):** [description]\n**Twist/Reaction (10-15 seconds):** [description]\n\n**NOT as a long paragraph with EVENT SUBJECT.** Please regenerate.\n\nSTYLE TAGS:"
                        )
                
                if is_flat_paragraph:
                    print(f"⚠️ Warning: Response is written as flat paragraph instead of Hook/Main Action/Twist structure", flush=True)
                    if "STYLE TAGS:" in bot_response:
                        bot_response = bot_response.replace(
                            "STYLE TAGS:",
                            "🚨 **WARNING: This prompt is written as a long paragraph!**\n\n**It MUST use the Hook/Main Action/Twist structure with explicit phase labels:**\n\n**Hook (0-2 seconds):** [description]\n**Main Action (2-10 seconds):** [description]\n**Twist/Reaction (10-15 seconds):** [description]\n\n**NOT as EVENT SUBJECT: [long paragraph].** Please regenerate.\n\nSTYLE TAGS:"
                        )
                
                # Check if scenario is too boring/realistic
                boring_keywords = [
                    "mailman", "delivery person", "delivers package", "delivery driver", "amazon package",
                    "package", "package left", "package at doorstep", "package delivery", "amazon prime",
                    "kid opens door", "child opens",
                    "person walks", "person rings doorbell", "raccoon rummaging", "raccoon in trash",
                    "cat walks", "cat stretching", "cat grooming", "cat tries to steal", "cat steals", 
                    "cat dashes", "cat moves", "cat attempts", "cat approaches", "cat paws", "cat meows",
                    "curious cat", "ravenous cat", "kitty tries", "fluffy cat", "cat sniffs",
                    "dog waiting", "normal", "typical", "everyday", "domestic", "pet behavior",
                    "squirrel darts", "squirrel appears", "squirrel raids", "squirrel grabs", "squirrel tries", 
                    "squirrel runs", "squirrel hurtles", "squirrel pads", "squirrel enters",
                    "girl walks", "woman walks", "man walks", "person steps", "bird feeder",
                    "birthday party", "surprise party", "comes home", "bae comes", "relationship goals",
                    "family moment", "husband", "wife", "daughter runs", "puppy jumps", "family cat",
                    "hooded figure", "figure emerges", "figure approaches", "figure walks", "stranger",
                    "young woman", "woman approaches", "woman walks briskly", "gloved hands", "figure pauses",
                    "making breakfast", "kitchen scene", "toast", "scrambled eggs", "cat grabs food",
                    "cat pounces", "owner catches", "pet tries", "animal tries", "normal pet",
                    "doorstep", "left at", "delivered", "morning delivery", "early morning"
                ]
                has_boring = any(keyword.lower() in bot_response.lower() for keyword in boring_keywords)
                
                funny_keywords = [
                    "hurricane", "power beam", "superpower", "teleport", "flies", "crashes",
                    "squeal", "absurd", "hilarious", "unexpected", "weird", "crazy", "destroys house",
                    "agartha", "looksmaxxing", "portal opens", "energy burst", "spits power",
                    "energy burst", "glitch", "supernatural", "beam of", "spits"
                ]
                has_funny = any(keyword.lower() in bot_response.lower() for keyword in funny_keywords)
                
                if has_boring and not has_funny:
                    detected_keywords = [kw for kw in boring_keywords if kw.lower() in bot_response.lower()]
                    print(f"⚠️ Warning: Scenario detected as too realistic/boring (keywords: {detected_keywords})", flush=True)
                    # Add VERY prominent warning to response - make it impossible to miss
                    if "STYLE TAGS:" in bot_response:
                        warning_msg = f"""🚨🚨🚨 **WARNING: This scenario is TOO REALISTIC/BORING for viral content!** 🚨🚨🚨

**Detected boring elements:** {', '.join(detected_keywords[:5]) if detected_keywords else 'normal everyday activities'}

**This prompt will NOT go viral because it's just normal pet/person behavior.**

**You MUST regenerate with a FUNNY, CREATIVE scenario like:**
- Hurricane pulls animal away with squeal
- Animal gets superpowers (flying, teleporting, shooting energy)
- Animal spits/shoots power beam that destroys something
- Agartha portal opens and something absurd comes out
- Looksmaxxing fail (person trying to improve appearance, something hilarious goes wrong)
- Modern internet culture moments (memes, trends, social media fails)
- Completely absurd unexpected moment (makes no sense but hilarious)
- Natural disaster with funny twist
- Skibidi toilet references (when appropriate)
- Gen Z humor, zoomer culture

**Think like a modern teenager - what would make people laugh and share?**"""
                        bot_response = bot_response.replace(
                            "STYLE TAGS:",
                            f"{warning_msg}\n\nSTYLE TAGS:"
                        )
                
                return bot_response
            elif "Caption:" in bot_response and "Prompt:" not in bot_response:
                # If only Caption is present, add a note and try to extract template info
                return bot_response + "\n\n⚠️ **Prompt section missing from AI response. Please try again.**"
            else:
                # If format is wrong, return as-is but log warning
                print(f"⚠️ Warning: Response may not be in correct format", flush=True)
                return bot_response
        elif response.status_code == 429:
            error_data = response.json()
            error_msg = error_data.get('error', {}).get('message', '')
            return f"⏳ Rate limit reached. Please wait a moment and try again.\n\nError: {error_msg}"
        else:
            error_msg = "Unknown error"
            try:
                error_data = response.json()
                error_msg = error_data.get('error', {}).get('message', response.text)
            except:
                error_msg = response.text
            return f"❌ Error {response.status_code}: {error_msg}"
            
    except requests.exceptions.Timeout:
        return "❌ Error: Request timed out. Please try again."
    except requests.exceptions.RequestException as e:
        return f"❌ Error: Network error - {e}"
    except Exception as e:
        return f"❌ Error: {e}"

# Set up Discord bot with minimal intents
intents = discord.Intents.default()
intents.message_content = True  # Required to read message content

bot = commands.Bot(command_prefix='!', intents=intents)

# Store webhook for target channel
target_channel_webhook = None

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!', flush=True)
    print(f'Bot is in {len(bot.guilds)} server(s)', flush=True)
    print(f'Target channel ID: {TARGET_CHANNEL_ID}', flush=True)
    
    # Verify we can see the target channel and set up webhook
    global target_channel_webhook
    try:
        channel = bot.get_channel(TARGET_CHANNEL_ID)
        if channel:
            print(f'Found target channel: #{channel.name} in {channel.guild.name}', flush=True)
            
            # Get or create webhook for this channel
            webhooks = await channel.webhooks()
            webhook = None
            
            # Check if webhook already exists
            for wh in webhooks:
                if wh.user and wh.user.id == bot.user.id:
                    webhook = wh
                    print(f'Found existing webhook: {wh.name}', flush=True)
                    break
            
            # Create webhook if it doesn't exist
            if not webhook:
                try:
                    # Download avatar image
                    avatar_bytes = None
                    if SORA_WEBHOOK_AVATAR:
                        try:
                            avatar_response = requests.get(SORA_WEBHOOK_AVATAR, timeout=10)
                            if avatar_response.status_code == 200:
                                avatar_bytes = avatar_response.content
                        except Exception as e:
                            print(f'Warning: Could not download avatar: {e}', flush=True)
                    
                    webhook = await channel.create_webhook(
                        name=SORA_WEBHOOK_NAME,
                        avatar=avatar_bytes
                    )
                    print(f'Created webhook: {webhook.name}', flush=True)
                except Exception as e:
                    print(f'Warning: Could not create webhook: {e}', flush=True)
                    print(f'   Bot will use default name/avatar', flush=True)
            
            target_channel_webhook = webhook
        else:
            print(f'Warning: Could not find channel with ID {TARGET_CHANNEL_ID}', flush=True)
    except Exception as e:
        print(f'Error checking channel: {e}', flush=True)
        import traceback
        print(traceback.format_exc(), flush=True)

@bot.command(name='prompt')
async def generate_prompt(ctx, template_number=None):
    """
    Generate a viral Sora prompt.
    Usage: !prompt [template_number]
    Template numbers: 1-10 (or leave blank for random)
    """
    # Check if message is in target channel
    if ctx.channel.id != TARGET_CHANNEL_ID:
        return  # Silently ignore commands in other channels
    
    # Show typing indicator
    async with ctx.channel.typing():
        # Generate prompt
        prompt = await generate_sora_prompt(template_number=template_number)
        
        # Split long messages (>1900 chars to leave buffer) into multiple messages
        if len(prompt) > 1900:
            chunks = []
            current_chunk = ""
            # Split by double newlines (between Title/Prompt/Style sections)
            sections = prompt.split('\n\n')
            
            for section in sections:
                if len(current_chunk) + len(section) + 2 > 1900:
                    if current_chunk:
                        chunks.append(current_chunk)
                    current_chunk = section
                else:
                    if current_chunk:
                        current_chunk += "\n\n"
                    current_chunk += section
            
            if current_chunk:
                chunks.append(current_chunk)
            
            # Send chunks using webhook if available, otherwise regular send
            if target_channel_webhook and ctx.channel.id == TARGET_CHANNEL_ID:
                for chunk in chunks:
                    await target_channel_webhook.send(
                        content=chunk,
                        username=SORA_WEBHOOK_NAME,
                        avatar_url=SORA_WEBHOOK_AVATAR
                    )
            else:
                for chunk in chunks:
                    await ctx.send(chunk)
        else:
            # Use webhook for custom name/avatar in target channel
            if target_channel_webhook and ctx.channel.id == TARGET_CHANNEL_ID:
                await target_channel_webhook.send(
                    content=prompt,
                    username=SORA_WEBHOOK_NAME,
                    avatar_url=SORA_WEBHOOK_AVATAR
                )
            else:
                await ctx.send(prompt)

@bot.command(name='templates')
async def list_templates(ctx):
    """List available prompt templates"""
    if ctx.channel.id != TARGET_CHANNEL_ID:
        return
    
    template_list = "**Available Sora Prompt Templates:**\n\n"
    for num, desc in [
        ("1", "CCTV / Ring Doorbell Camera"),
        ("2", "Funny Animal Fails (Handheld)"),
        ("3", "Body Cam Footage"),
        ("4", "Olympic Broadcast"),
        ("5", "Glow-Up Transformation"),
        ("6", "Character Mashup"),
        ("7", "Animal Superpower"),
        ("8", "Time-Travel / Future Self"),
        ("9", "POV Mini-Story"),
        ("10", "Hidden Camera Prank")
    ]:
        template_list += f"**{num}.** {desc}\n"
    
    template_list += "\nUse `!prompt [number]` to generate a prompt for a specific template, or `!prompt` for a random one."
    
    # Use webhook for custom name/avatar in target channel
    if target_channel_webhook and ctx.channel.id == TARGET_CHANNEL_ID:
        await target_channel_webhook.send(
            content=template_list,
            username=SORA_WEBHOOK_NAME,
            avatar_url=SORA_WEBHOOK_AVATAR
        )
    else:
        await ctx.send(template_list)

@bot.command(name='sorahelp')
async def help_command(ctx):
    """Show help with detailed template descriptions"""
    if ctx.channel.id != TARGET_CHANNEL_ID:
        return
    
    help_text = """**🎬 Sora Prompt Generator Bot - Help**

**Commands:**
• `!prompt` - Generate a random viral Sora prompt with caption
• `!prompt [1-10]` - Generate prompt for a specific template
• `!templates` - List all available templates
• `!sorahelp` - Show this help message
• `!ping` - Check if bot is responding
• `!status` - Check bot status

**Template Descriptions:**

**1. CCTV / Ring Doorbell Camera**
   Ring doorbell footage style - static camera, wide-angle, suburban setting

**2. Funny Animal Fails (Handheld)**
   Handheld smartphone video in kitchen/home - chaotic pet moments

**3. Body Cam Footage**
   Police-style body camera - first-person, wide-angle, action-packed

**4. Olympic Broadcast**
   Professional sports broadcast - stadium setting, graphics, commentary

**5. Glow-Up Transformation**
   Before/after transformation - casual to luxury, slow motion reveal

**6. Character Mashup**
   Two unlikely characters interacting - crossover scenarios

**7. Animal Superpower**
   Pet/animal discovering powers - realistic setting with effects

**8. Time-Travel / Future Self**
   Glitch transition to future - urban setting, sci-fi vibes

**9. POV Mini-Story**
   First-person walkthrough - surprise reveal moments

**10. Hidden Camera Prank**
   Surveillance-style footage - candid moments, pranks

**Usage:** Type `!prompt` or `!prompt [number]` to get a viral TikTok caption + full Sora prompt ready to paste!"""
    
    # Use webhook for custom name/avatar in target channel
    if target_channel_webhook and ctx.channel.id == TARGET_CHANNEL_ID:
        await target_channel_webhook.send(
            content=help_text,
            username=SORA_WEBHOOK_NAME,
            avatar_url=SORA_WEBHOOK_AVATAR
        )
    else:
        await ctx.send(help_text)

@bot.command(name='ping')
async def ping(ctx):
    """Check if bot is responding"""
    if ctx.channel.id != TARGET_CHANNEL_ID:
        return
    await ctx.send('Pong! 🎬')

@bot.command(name='status')
async def status(ctx):
    """Check bot status"""
    if ctx.channel.id != TARGET_CHANNEL_ID:
        return
    await ctx.send(f'✅ Bot is online! Listening on channel {TARGET_CHANNEL_ID}')

# Run the bot
if __name__ == '__main__':
    if not DISCORD_BOT_TOKEN:
        print("ERROR: DISCORD_BOT_TOKEN not found in .env file!", flush=True)
        sys.exit(1)
    
    if not GROQ_API_KEY:
        print("ERROR: GROQ_API_KEY not found in .env file!", flush=True)
        sys.exit(1)
    
    if not TARGET_CHANNEL_ID:
        print("ERROR: TARGET_CHANNEL_ID not found in .env file!", flush=True)
        print("Right-click your Discord channel and select 'Copy Channel ID'", flush=True)
        sys.exit(1)
    
    try:
        bot.run(DISCORD_BOT_TOKEN)
    except Exception as e:
        print(f"Fatal error: {e}", flush=True)
        import traceback
        print(traceback.format_exc(), flush=True)
        sys.exit(1)

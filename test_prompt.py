"""
Test script to simulate !prompt command and verify it works correctly
"""
import sys
sys.dont_write_bytecode = True

import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# Copy the updated system prompt from sora_bot.py (with all 10 improvements)
SORA_PROMPT_SYSTEM = """You are an AI that takes Sora video prompt templates and fills in all blanks with **ultra-detailed, viral-optimized scenarios**. Your job is to transform every template into the most realistic, engaging, and TikTok-ready prompt possible.

Follow ALL rules below when filling in templates:

### **1. Add micro-actions**
Include tiny movements like blinking, breathing, hair shifting, hand gestures, weight shifting, jaw tension, fingers tapping, subtle eye movements, nervous swallows, foot tapping.

### **2. Add environmental reactions**
Include how the world reacts: lights flicker, objects wobble, reflections shift, shadows move, wind affects clothing, background people react, dust particles float, items on surfaces vibrate.

### **3. Add a strong hook in the first 1–2 seconds**
Start the prompt with a moment that instantly grabs attention (camera shake, fast zoom, sudden sound, quick movement, glitch pop, light flicker, object falling, loud noise).

### **4. Add sensory detail**
Include real-world sound (rustling fabric, footsteps, breathing, wind, distant traffic, clinking objects, mechanical hums, echoes) and texture details (rough surfaces, smooth materials, fabric textures).

### **5. Add lighting changes**
Use warm → cool shifts, neon flicker, golden hour glow, soft shadows, dramatic lighting transitions, spotlight highlights, sudden shadow movements.

### **6. Add camera personality**
Make the camera feel real: slight shake, autofocus hunting, quick reframes, accidental pans, handheld wobble, tiny dust on lens, lens flare, natural camera movement.

### **7. Add a twist ending**
Always include a surprising second moment at the end to increase rewatch value (unexpected movement, someone entering frame, object glitch, reveal, reaction, sudden color shift, future/past self moment).

### **8. Add emotion and expression**
Characters should show real emotion: confusion, fear, curiosity, awe, relief, nervous laughter, wide-eyed shock, hesitation, focus, joy, surprise. Describe facial reactions clearly.

### **9. Be ultra specific**
Use concrete details: hair color, clothing fabric, background objects, clothing wrinkles, textures, time of day, weather, small imperfections, specific ages, exact clothing items, room details.

### **10. Make it feel "caught in the moment"**
Avoid cinematic perfection. Add imperfections: slightly messy backgrounds, off-center framing, accidental tilts, real-world sounds, natural motion, casual clothes, authentic settings.

---

CRITICAL OUTPUT FORMAT - You MUST output exactly in this format. DO NOT skip the Prompt section:

Caption:
[Write a catchy, viral TikTok caption here - should be engaging, use relevant hashtags, emojis, and be optimized for TikTok engagement. Keep it concise but attention-grabbing.]

Prompt:
[Fully expanded Sora prompt with all details filled in, including the EVENT SUBJECT details with ALL 10 rules above applied. The prompt must include: micro-actions, environmental reactions, strong hook, sensory details, lighting changes, camera personality, twist ending, emotion/expression, ultra-specific details, and "caught in the moment" feel. Include the STYLE TAGS at the end exactly as provided in the template.]

MANDATORY: You MUST include BOTH Caption: and Prompt: sections. Never output only the Caption. The Prompt section is REQUIRED and must contain the full expanded prompt with EVENT SUBJECT filled in using ALL 10 improvement rules, plus STYLE TAGS. Do this for EVERY prompt I paste. Always start with "Caption:" and then "Prompt:" on separate lines."""

TEMPLATE_1 = """CCTV / RING DOORBELL CAMERA - Full Prompt Template

PROMPT:
Ultra-realistic Ring doorbell camera footage. Slight wide-angle fisheye lens. Static camera mounted on a suburban front porch. Natural daylight with soft overcast lighting. Camera never moves.
EVENT SUBJECT: [describe your animal/person and action here]
Show real-world motion and physics. Slight vibrations from wind. Natural color, mild grain, subtle lens distortion, light compression artifacts.
Include ambient audio of wind, distant cars, light porch creaks.

STYLE TAGS:
CCTV, Ring doorbell cam, ultrarealistic, wide-angle, lens distortion, static camera, real motion blur, suburban porch."""

def test_prompt_generation():
    """Test the prompt generation function"""
    print("=" * 60)
    print("TESTING SORA PROMPT GENERATION")
    print("=" * 60)
    
    user_message = f"""🚨🚨🚨 CRITICAL: YOU MUST FOLLOW THIS EXACT FORMAT OR YOU FAIL 🚨🚨🚨

STEP 1: Pick ONE funny scenario from this list (MANDATORY - no exceptions):
1. Hurricane/storm pulls animal away with squeal
2. Animal gets superpowers (flying, teleporting, shooting energy)
3. Animal spits/shoots power beam that destroys something
4. Agartha portal opens and something absurd comes out
5. Looksmaxxing fail (person trying to improve appearance, something hilarious goes wrong)
6. Animal does something completely absurd (makes no sense but hilarious)
7. Natural disaster with funny twist (tornado picks up animal, earthquake causes funny reaction)

❌ FORBIDDEN (if you use these, you FAIL):
- Person/animal walking normally
- Mailman/delivery person
- Cat/dog doing normal things
- Birthday parties, surprise parties
- Family moments
- Normal everyday activities
- Squirrel just running (must have hurricane/power beam/superpower)

STEP 2: Write EXACTLY in this format with CINEMATIC 5-PART STRUCTURE (MANDATORY - you MUST use all 5 parts):

[Template's base camera/setting description]

**HOOK (0-2 seconds):** [INSTANTLY attention-grabbing - loud sound, light flicker, shadow movement, object falling, sudden POV shift, NOT just "door opens"]

**BUILD-UP (2-6 seconds):** [Tension/comedy builds - things get weirder/funnier/scarier, environmental reactions increase (dust motes floating, lights flickering, objects shifting), POV emotional reactions (breathing becomes audible, hesitation, head movement), sound layers build]

**RISING TENSION (6-10 seconds):** [Escalation continues - someone tries to hide and fails, pet runs across screen, costume malfunctions, suspense builds, breathing quickens, camera micro-shakes from nervousness]

**REVEAL / EVENT SUBJECT (10-12 seconds):** [The key moment - ULTRA-SPECIFIC, not just "person in costume" or "spider on box". Describe CINEMATICALLY: micro-actions, textures, reactions, eye reflections, body movement. Make it CINEMATIC - describe what viewer FEELS and SENSES, not "camera does X"]

**TWIST ENDING (12-15 seconds):** [Final beat that triggers replays - something behind viewer, second creature dropping, hand grabbing frame, box falling, final whisper/sound, blackout moment]

STYLE TAGS: [copy from template]

⚠️ CRITICAL: You MUST use ALL 5 parts (Hook, Build-Up, Rising Tension, Reveal, Twist). DO NOT use old 3-part structure.

EXAMPLE (copy this exact style):
Ultra-realistic Ring doorbell camera footage. Slight wide-angle fisheye lens. Static camera mounted on a suburban front porch. Natural daylight with soft overcast lighting. Camera never moves.

**Hook (0-2 seconds):** Camera shake as a squirrel tries to climb the door handle, making funny scratching sounds. Wind picks up suddenly, causing the porch lights to sway.

**Main Action (2-10 seconds):** A massive hurricane-force wind suddenly pulls the squirrel away from the door. The squirrel makes a hilarious high-pitched squeal as it flies backward through the air, its tiny paws flailing wildly. The camera captures the squirrel spinning through the air, leaves and debris swirling around it. The porch furniture wobbles violently, and a flowerpot crashes to the ground with a loud smash. The wind howls, and the camera lens vibrates from the force.

**Twist/Reaction (10-15 seconds):** The squirrel disappears into the distance with a final squeal, and the camera shakes from the wind. A neighbor's trash can gets knocked over off-camera with a loud crash. The camera refocuses on the empty porch, now covered in scattered leaves and debris. The wind dies down, leaving only the sound of distant sirens.

STYLE TAGS: CCTV, Ring doorbell cam, ultrarealistic, wide-angle, lens distortion, static camera, real motion blur, suburban porch.

NOW DO THE SAME FOR THIS TEMPLATE:

Template:
{TEMPLATE_1}

CRITICAL: 
- MUST be funny (hurricane, power beam, superpower, Agartha, looksmaxxing fail, etc.)
- MUST use Hook/Main Action/Twist structure (NOT long paragraphs)
- MUST be short (10-15 seconds focus)
- MUST include modern references when appropriate (looksmaxxing, Agartha, internet culture)
- NO boring realistic scenarios
- NO copyrighted characters

Your output MUST have both:
Caption:
[Viral TikTok caption with hashtags]

Prompt:
[Full prompt in Hook/Main Action/Twist format]"""
    
    messages = [
        {'role': 'system', 'content': SORA_PROMPT_SYSTEM},
        {'role': 'user', 'content': user_message}
    ]
    
    print("\n📤 Sending request to Groq API...")
    print(f"   Model: llama-3.1-8b-instant")
    print(f"   Max tokens: 1500")
    
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
                'max_tokens': 1500,
                'temperature': 1.0,
                'stream': False
            },
            timeout=30
        )
        
        if response.status_code == 200:
            bot_response = response.json()['choices'][0]['message']['content']
            
            print("\n✅ Response received!")
            print("=" * 60)
            print("\n📋 RESPONSE:")
            print("-" * 60)
            print(bot_response)
            print("-" * 60)
            
            # QA Checks
            print("\n🔍 QUALITY ASSURANCE CHECKS:")
            print("-" * 60)
            
            checks = []
            
            # Check 1: Contains Caption section
            has_caption = "Caption:" in bot_response
            checks.append(("Contains 'Caption:' section", has_caption))
            print(f"✓ Contains 'Caption:' section: {has_caption}")
            
            # Check 2: Contains Prompt section
            has_prompt = "Prompt:" in bot_response
            checks.append(("Contains 'Prompt:' section", has_prompt))
            print(f"✓ Contains 'Prompt:' section: {has_prompt}")
            
            # Check 3: Both sections present
            has_both = has_caption and has_prompt
            checks.append(("Both sections present", has_both))
            print(f"✓ Both sections present: {has_both}")
            
            # Check 4: Caption comes before Prompt
            if has_both:
                caption_pos = bot_response.find("Caption:")
                prompt_pos = bot_response.find("Prompt:")
                correct_order = caption_pos < prompt_pos
                checks.append(("Caption comes before Prompt", correct_order))
                print(f"✓ Caption comes before Prompt: {correct_order}")
            
            # Check 5: Response length (should be substantial)
            length_ok = len(bot_response) > 200
            checks.append(("Response length > 200 chars", length_ok))
            print(f"✓ Response length > 200 chars: {length_ok} ({len(bot_response)} chars)")
            
            # Check 6: Caption has content after "Caption:"
            if has_caption:
                caption_section = bot_response.split("Caption:")[1].split("Prompt:")[0] if has_prompt else bot_response.split("Caption:")[1]
                caption_has_content = len(caption_section.strip()) > 10
                checks.append(("Caption has content", caption_has_content))
                print(f"✓ Caption has content: {caption_has_content}")
            
            # Check 7: Prompt has content after "Prompt:"
            if has_prompt:
                prompt_section = bot_response.split("Prompt:")[1]
                prompt_has_content = len(prompt_section.strip()) > 50
                checks.append(("Prompt has content", prompt_has_content))
                print(f"✓ Prompt has content: {prompt_has_content}")
            
            # Check 8: Prompt contains EVENT SUBJECT details (not just [blank])
            if has_prompt:
                prompt_section = bot_response.split("Prompt:")[1]
                has_event_details = "[describe" not in prompt_section and "[blank]" not in prompt_section.lower()
                checks.append(("Prompt has EVENT SUBJECT filled in", has_event_details))
                print(f"✓ Prompt has EVENT SUBJECT filled in: {has_event_details}")
            
            # Check 9: Prompt contains STYLE TAGS
            if has_prompt:
                prompt_section = bot_response.split("Prompt:")[1]
                has_style_tags = "STYLE TAGS" in prompt_section or "Style Tags" in prompt_section or any(tag in prompt_section for tag in ["CCTV", "Ring doorbell", "ultrarealistic"])
                checks.append(("Prompt contains STYLE TAGS", has_style_tags))
                print(f"✓ Prompt contains STYLE TAGS: {has_style_tags}")
            
            print("-" * 60)
            
            # Final verdict
            all_passed = all(check[1] for check in checks)
            print(f"\n{'✅ ALL CHECKS PASSED!' if all_passed else '❌ SOME CHECKS FAILED'}")
            print(f"   Passed: {sum(1 for _, passed in checks if passed)}/{len(checks)}")
            
            if not all_passed:
                print("\n⚠️  Issues found:")
                for name, passed in checks:
                    if not passed:
                        print(f"   - {name}")
            
            return all_passed
            
        elif response.status_code == 429:
            error_data = response.json()
            error_msg = error_data.get('error', {}).get('message', '')
            print(f"\n❌ Rate limit reached: {error_msg}")
            return False
        else:
            error_msg = "Unknown error"
            try:
                error_data = response.json()
                error_msg = error_data.get('error', {}).get('message', response.text)
            except:
                error_msg = response.text
            print(f"\n❌ Error {response.status_code}: {error_msg}")
            return False
            
    except Exception as e:
        print(f"\n❌ Exception: {e}")
        import traceback
        print(traceback.format_exc())
        return False

if __name__ == '__main__':
    if not GROQ_API_KEY:
        print("ERROR: GROQ_API_KEY not found in .env file!")
        sys.exit(1)
    
    success = test_prompt_generation()
    sys.exit(0 if success else 1)

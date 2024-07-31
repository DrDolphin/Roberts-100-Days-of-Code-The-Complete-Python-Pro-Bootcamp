print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
)
print("Welcome to Treasure Island.")
print(
    "Your mission is to find the legendary treasure hidden deep within the island's heart. Brave the mysteries and dangers that lurk around every corner, and remember, every choice could lead you closer to riches or peril."
)

print(
    "As you begin your adventure on the island, you're immediately faced with a decision at a mysterious fork in the path. To your left, there's a dark, ominous cave that seems to emit strange noises. To your right, a dense jungle beckons with its mysterious, yet inviting, allure."
)
decision_1 = input(
    "You have two choices:\n1. Venture into the ominous cave.\n2. Head into the dense jungle.\nWhich shall you choose (enter 'cave' or 'jungle')? "
).lower()

if decision_1 != "jungle":
    print(
        "As you step into the cave, an eerie chill runs down your spine. The cave's mouth closes behind you, plunging you into darkness. You fumble for a light, and as your eyes adjust, you realize you're not alone. Glowing eyes peer at you from the shadows, and you hear a low, menacing growl. In a moment of terror, you try to run, but the uneven floor betrays you. You stumble and fall into a hidden pit. As you descend into the abyss, the last thing you hear is the echo of your own scream, swallowed by the darkness. This ill-fated choice marks the end of your journey."
    )
    exit()

print(
    """
Opting for the dense jungle, you leave the ominous cave behind. The jungle's thick canopy plunges you into a world of vibrant greens and deep shadows. Sunlight filters through the leaves in golden beams, casting a dappled pattern on the forest floor. The air is thick with the sounds of distant wildlife and the rustle of leaves in a gentle breeze.

As you make your way deeper, the underbrush becomes denser. You navigate around twisted roots and overgrown bushes, careful to avoid the less visible dangers of the jungle. Every so often, a colorful bird flits past, or a small creature scurries away at your approach.

Hours pass as you delve deeper into the heart of the island. The initial excitement of your adventure gives way to a focused determination. You're constantly alert, knowing that the jungle hides both wonders and hazards in equal measure.
"""
)

print(
    """
In the heart of the dense jungle, you find a wide river. The water seems serene, but you notice a subtle, powerful undercurrent hinting at hidden dangers. Within this deceptive calm, something glimmers beneath the surface, catching the light in an enticing way. It looks valuable, possibly a clue to the treasure, but reaching it could be risky.

Nearby stands a rickety bridge, its wooden planks old and partially obscured by overgrowth. The bridge sways slightly in the breeze, and some of the planks look too fragile to hold much weight. Crossing it could be quicker than braving the river's mysterious depths, but there's a real risk it might collapse under you.
"""
)
decision_2 = input(
    "You have two choices:\n1. Investigate the shiny glimmering object\n2. Attempt to cross the overgrown bridge.\nWhich shall you choose (enter 'object' or 'bridge')? "
).lower()

if decision_2 != "bridge":
    print(
        """
  Drawn to the mysterious glimmer in the river, you carefully step into the water. The riverbed is slippery, and the currents are deceitfully strong. As you reach down to uncover the object, you realize too late that it's not what it seems. The glimmer was merely the reflection of an old fisherman's lure, and your disturbance has unsettled something lurking beneath. In a sudden whirl of water, you're pulled under by an unseen force. Despite your struggles, you can't break free, and the river claims you as another one of its hidden secrets.
  """
    )
    exit()

print(
    """
Crossing the bridge with cautious steps, you reach the other side of the river. A sense of relief washes over you as your feet touch solid ground again. Ahead, the jungle opens up into a clearing bathed in sunlight. In the center of the clearing stands an ancient temple, its stone walls covered in moss and creeping vines. Intricate carvings and symbols adorn the entrance, hinting at the mysteries that lie within.
As you approach the temple, you notice three distinct paths leading into its heart. The first path on your left leads to a chamber filled with statues of mythical creatures, their eyes set with gleaming gemstones. The air around it feels heavy, as if laden with ancient magic. The center path opens to a long hallway lined with torches, casting flickering shadows on the walls. The sound of distant chanting echoes eerily from within. To your right, the third path leads downwards into a dimly lit staircase, spiraling into darkness and unknown depths.

The treasure must be hidden within one of these paths, but you sense that the wrong choice could be fatal. Your heart races with both anticipation and fear as you stand before these three daunting options.
"""
)

decision_3 = input(
    "You have three choices:\n1. Enter the chamber with the statues, intrigued by the glint in their eyes and the potential secrets they guard.\n2. Venture down the torch-lit hallway, drawn by the mysterious chanting and the promise of ancient rituals.\n3. Descend the staircase into the depths, braving the darkness in search of the treasure's final hiding place.\nWhich shall you choose (enter 'statues', 'chanting', or 'depths')? "
).lower()

if decision_3 == "statues":
    print(
        "Entering the chamber, you are immediately struck by the eerie stillness. The statues seem to watch you with their gemstone eyes. As you step closer to inspect them, you notice a gleaming object on a pedestal at the far end of the room – perhaps the treasure. Suddenly, the chamber rumbles, and the statues spring to life! They move towards you menacingly. You realize too late that this chamber is a trap, and the statues are its guardians. Overwhelmed, you are unable to escape, and the story ends in the grips of the ancient guardians."
    )
elif decision_3 == "chanting":
    print(
        "Drawn by the mysterious chanting, you proceed down the torch-lit hallway. The walls are adorned with murals depicting an ancient civilization and their rituals. As you reach the end, you find a large ceremonial room. In the center, a golden idol sits atop a pedestal. Believing you've found the treasure, you reach out to grab it, but as soon as you touch the idol, the chanting stops abruptly. The floor gives way beneath you, opening into a pit. With no way to escape, your adventure ends abruptly as you fall into the darkness below."
    )
elif decision_3 == "depths":
    print(
        "Choosing the staircase, you descend cautiously into the depths. The further you go, the colder and damper it becomes. At the bottom, you find a cavern illuminated by natural light filtering in from above. In the center of the cavern lies a chest, ornate and old. Your heart leaps – this must be the treasure! You approach and open it carefully. Inside, you find an array of jewels and gold, far beyond what you imagined. Alongside the treasure is a map showing a safe way out of the temple and back through the jungle. Your choice has led you to fortune and success. The legendary treasure is yours, and your story concludes with triumph."
    )
else:
    print(
        "You stand pondering which path to take, as the time passes and the sun begins to set, you hear a twig snap behind you. As you whirl around, the last thing you see before you journey ends is the blade of a pirate who has been tracking this treasure as well."
    )

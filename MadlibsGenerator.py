# Madlibs Generator

# Story template with placeholders for user input
story = """
Once upon a time in a <adjective> land, there lived a <noun>. This <noun> was known for its <adjective> <plural_noun> and <color> skies.

One day, the <noun> decided to go on an adventure. It packed a bag with <adjective> snacks, a <noun>, and a map to find the legendary <adjective> <noun>.

As the <noun> journeyed through the <adjective> forest, it encountered a group of friendly <plural_animal>. They joined the <noun> on its quest, and together they faced many <adjective> challenges.

After days of traveling, they reached the top of the <adjective> mountain, where they discovered the magical <noun> of <noun> that granted them <number> wishes. Each of them made a wish, and suddenly the <adjective> land transformed into a <adjective> paradise.

With their wishes granted, the <noun> and its newfound friends returned home, forever cherishing the memories of their <adjective> adventure.

The end.
"""

# Get user input for each placeholder
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
plural_noun = input("Enter a plural noun: ")
color = input("Enter a color: ")
plural_animal = input("Enter a plural animal: ")
number = input("Enter a number: ")

# Replace placeholders with user input
story = story.replace("<adjective>", adjective)
story = story.replace("<noun>", noun)
story = story.replace("<plural_noun>", plural_noun)
story = story.replace("<color>", color)
story = story.replace("<plural_animal>", plural_animal)
story = story.replace("<number>", number)

# Print the completed madlibs story
print(story)

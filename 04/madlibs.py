#Anthony & Anton Madlibs

story = 'NOUN was VERB the NOUN because he was ADJ.'
nouns = ['dude', 'man', 'kid']
verbs = ['fighting', 'racing', 'running']
adj = ['blue', 'happy', 'sad']

import random as rand
while story.find('NOUN') != -1:
    rand.shuffle(nouns)
    num = story.find('NOUN')
    story = story[:num] + nouns[0] + story[num+4:]
while story.find('VERB') != -1:
    rand.shuffle(verbs)
    num = story.find('VERB')
    story = story[:num] + verbs[0] + story[num+4:]
while story.find('ADJ') != -1:
    rand.shuffle(adj)
    num = story.find('ADJ')
    story = story[:num] + adj[0] + story[num+3:]
    
print(story)
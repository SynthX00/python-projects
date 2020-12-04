import emoji
msg = emoji.emojize('Howdy :sun_with_face:')
print(msg)

for emote in emoji.EMOJI_UNICODE:
    sym = emoji.emojize(emote)
    print(f'{sym} {emote}')

#print output to file
#python3 exercise2.py > output.txt
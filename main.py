file = './notes.txt'

how_many_imgs = 5
tags = ['translation', 'grammar', 'usage_note_german', 'german']

anki_tag_to_logseq = {}

with open(file, 'r') as f:
    for line in f:
        clean_line = line.replace('&nbsp;', ' ')
        question, answer, tags_card = clean_line.split('\t')

        print(f"> > > question{question}")
        print(f"> > > answer{answer}")
        print(f"> > > tags{tags_card}")

print(tags)

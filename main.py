import re


file = './notes.txt'

how_many_imgs = 5
# tags = ['translation', 'grammar', 'usage_note_german', 'german']

anki_tag_to_logseq = {}

regex_remove_closing_tags = r"<\/[^>]+>"

tags_to_remove = {
    "<i>": "",
    "<ul>": "",
    "<br>": "\n",
    "&nbsp;": "\n",
    "<u>": "",
    "<div>": "",
}

full = ""

with open(file, 'r') as f:
    for line in f:
        clean_line = re.sub(regex_remove_closing_tags, "", line, 0, re.MULTILINE)
        for key, value in tags_to_remove.items():
            clean_line = clean_line.replace(key, value)


# You can manually specify the number of replacements by changing the 4th argument

        question, answer, tags_card = clean_line.split('\t')

        question = question.replace("\n", " ")
        question = question.replace("<li>", "\n")

        answer = answer.replace("\n", " ")
        answer = answer.replace("<li>", "\n")

        regex = r"^\"(.*)\"$"

        matches = re.finditer(regex, question, re.MULTILINE)
        matches = list(matches)
        if len(matches) > 0:
            question = matches[0].groups()[0]

        matches = re.finditer(regex, answer, re.MULTILINE)
        matches = list(matches)
        if len(matches) > 0:
            answer = matches[0].groups()[0]

        tags_card = tags_card.replace("usage_note_german", "grammar")
        tags_card = tags_card.replace("\n", "")
        tags = tags_card.split(" ")

        logseq_tags = " #german "
        for tag in tags:
            if tag == "grammar":
                logseq_tags += "#card #grammar"
            elif tag == "translation":
                logseq_tags += "#card/translation"

        question = question + logseq_tags

        # print(f"> > > question{question}")
        # print(f"> > > answer{answer}")
        # print(f"> > > tags{tags_card}")

        t = (
            f"- {question}\n"
            f"\t- {answer}"
        )
        #
        full = full + "\n"  + t

print(full)

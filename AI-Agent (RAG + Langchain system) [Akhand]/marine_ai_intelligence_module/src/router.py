import re

KEYWORD_TAGS = {

"carbon":["carbon","co2","emission"],

"fuel":["fuel","consumption"],

"engine":["engine","engine load"],

"weather":["wind","wave","storm","sea"],

"speed":["speed","velocity"],

"temperature":["temperature"],

"efficiency":["efficiency","performance"]

}

def extract_tags(question):

    question = question.lower()

    tokens = re.findall(r'\w+',question)

    detected_tags = set()

    for tag,words in KEYWORD_TAGS.items():

        for token in tokens:

            if token in words:
                detected_tags.add(tag)

    if len(detected_tags)==0:
        detected_tags.add("general")

    return list(detected_tags)
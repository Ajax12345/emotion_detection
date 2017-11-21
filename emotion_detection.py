import re
import collections
import csv

def arousal_model():
    arousal_1 = collections.defaultdict(dict)
    for text, v1, v2, a1, a2 in list(csv.reader(open('/Users/jamespetullo/Downloads/dataset-fb-valence-arousal-anon.csv')))[1:]:
        if "words" not in arousal_1[a1]:
            arousal_1[a1]["words"] = [i.lower() for i in re.findall('\w+', text)]
        else:
            arousal_1[a1]["words"].extend([i.lower() for i in re.findall('\w+', text)])
        if "blocks" not in  arousal_1[a1]:
            data = [i.lower() for i in re.findall('\w+', text)]
            arousal_1[a1]["blocks"] = [' '.join(data[i:i+2]) for i in range(0, len(data), 2)]
        else:
            data = [i.lower() for i in re.findall('\w+', text)]
            arousal_1[a1]["blocks"].extend([' '.join(data[i:i+2]) for i in range(0, len(data), 2)])
        if "punc" not in arousal_1[a1]:
            arousal_1[a1]['punc'] = re.findall('[\!\.\?]', text)
        else:
            arousal_1[a1]['punc'].extend(re.findall('[\!\.\?]', text))
        if 'length' not in arousal_1[a1]:
            arousal_1[a1]['length'] = [len(re.findall('\w+', text))]

        else:
            arousal_1[a1]['length'].append(len(re.findall('\w+', text)))

    return dict(arousal_1)






def emotion_model():
    d = collections.defaultdict(dict)
    for tweet_id, sentiment, author, content in list(csv.reader(open('/Users/jamespetullo/Downloads/text_emotion.csv')))[1:]:
        if "words" not in d[sentiment]:
            d[sentiment]["words"] = map(str.lower, re.findall('\w+', content))
        else:
            d[sentiment]["words"].extend(map(str.lower, re.findall('\w+', content)))

        if "blocks" not in d[sentiment]:
            data = list(re.findall('\w+', content))
            d[sentiment]['blocks'] = [' '.join(data[i:i+2]) for i in range(0, len(data), 2)]
        else:
            data = list(re.findall('\w+', content))
            d[sentiment]['blocks'].extend([' '.join(data[i:i+2]) for i in range(0, len(data), 2)])


    return dict(d)

import emotion_detection
import re
converter = {"love":2, "relief":3, "neutral":1, "anger":8, "sadness":7, "empty":4, "suprise":9, "fun":3, "enthusiasm":6, "happiness":4, "hate":7, "worry":5, "boredom":2}
model1 = emotion_detection.arousal_model()
model2 = emotion_detection.emotion_model()
def get_personality(s):


    words = map(str.lower, re.findall('\w+', s))

    current_data = {"punc":list(re.findall('[\.\!\?]', s)), "words":list(map(str.lower, re.findall('\w+', s))), "blocks":[' '.join(words[i:i+2]) for i in range(0, len(words), 2)], "length":len(words)}

    model_1_results = {a:{i:sum(c in b[i] for c in current_data[i]) for i in current_data if isinstance(current_data[i], list)} for a, b in model1.items()}
    model_2_results = {a:{i:sum(c in b[i] for c in current_data[i] if i in b) for i in current_data if isinstance(current_data[i], list)} for a, b in model2.items()}
    final1 = sorted(model_1_results.items(), key=lambda (y, x):sum([x["words"], x["blocks"], x["punc"]]))
    final2 = sorted(model_2_results.items(), key=lambda (x, y):sum([y["punc"], y["words"], y["blocks"]]))

    if all(all(c == 0 for c in b.values()) for a, b in final1) and all(all(c == 0 for c in b.values()) for a, b in final2):
        return False


    if not any(final1[-1][-1].values()) or not any(final2[-1][-1].values()):
        return int(final1[-1][0]) if not any(final2[-1][-1].values()) else final2[-1][0]

    return [int(final1[-1][0]), final2[-1][0]]
    #if all(not all(b.values()) for a, b in final1) and all(not all(b.values()) for a, b in final2):
        #return False
print get_personality("My name is James Petullo, and I am a programmer and euntrepenour. I hope to make major contribitions in the fields of machine learning")
'''
import csv

count = 0
f = open('irregulars.txt', 'a')
for text_id, emotion, author, text in csv.reader(open('testing_data.csv')):
    returned_data = get_personality(text)
    if isinstance(returned_data, list):
        count += returned_data[-1] == emotion
    elif isinstance(returned_data, int):
        f.write("{}:{}:{}\n".format(returned_data, converter[returned_data], emotion))
        count += converter[returned_data] == emotion

    elif isinstance(returned_data, str):
        count += returned_data == emotion

print count/float(1000)

f.close()
'''

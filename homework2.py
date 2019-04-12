import nltk
import csv
from nltk.corpus import brown
from nltk.corpus import wordnet

nltk.download("brown")
nltk.download("wordnet")

# filtered_gold_standard stores the word pairs and their human-annotated similarity in your filtered test set
filtered_gold_standard = {}

###
# Your answer BEGINS HERE
# REMOVE RARE WORDS
# PARAS
# REMOVE NOT ALPHABETIC
# LOWERCASE
# LEMMATIZED
# CALCULATE FREQ OF EACH WORD TYPE(MORE THAN 8)
#
###
filename = 'set1.tab'
reader = {}
with open(filename, newline='') as f:
    reader = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
    # print(reader)
    for row in reader:
        print(row)

###
# Your answer ENDS HERE
###

print(len(filtered_gold_standard))
print(filtered_gold_standard)
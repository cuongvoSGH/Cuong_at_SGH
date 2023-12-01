# Cuong Vo - 131116

# Import for library 
# 1. Operator: work with Dictionary
# 2. Matplotlib & WordCloud: work with chart & wordcloud
import operator
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Define function for word check.
def word_check(words):
    if len(words) >= 4:
        if (words.upper() == words) or (words.title()[0] == words[0]):
            return 1
        else: return 0
    else: return 0

# Define path for text file
file_path = 'English_text.txt'

# Open file, join into 1 string variable and clean variable
f = open(file_path, 'r')
lines = f.readlines()
st = ''.join(lines)
st.replace('\n', '')

# Clean character which is not alphabet and numeric and space
working_str = ''
for i in range(len(st)):
    tmp = st[i]
    if (tmp.isalnum() or tmp.isspace()):
        working_str += tmp
    else: working_str += ' '

# Create word Dictionary
Dict_text = dict()

words = working_str.split(sep = ' ')

for word in words:
    if word_check(word):
        if word in Dict_text:
            Dict_text[word] += 1
        else: 
            Dict_text[word] = 1

# Sort Dictionary for top 10
Dict_text = dict(sorted(Dict_text.items(), key= operator.itemgetter(1), reverse=True))

# Plot the top 10 into bar chart
word_list = []
fre_list = []

for i in range(min(10,len(Dict_text))):
    word_list.append(list(Dict_text.keys())[i])
    fre_list.append(list(Dict_text.values())[i])

ay = plt.figure(figsize = (10,5)).subplots()
chart = ay.barh(word_list, fre_list, color = 'red')

# Adding components
ay.invert_yaxis()
ay.set_xlabel('Frequency')
ay.set_ylabel('Word')
ay.set_title('Top 10 Common Words')

for p in chart:
    width = p.get_width()
    ay.annotate('{}'.format(width),
                xy=(width, p.get_y() + p.get_height()),
                xytext=(10,6),
                textcoords="offset points",
                ha='center',
                va = 'bottom')

# Save file and clear figure space
plt.savefig('Top10_Word.png')
plt.show()
plt.clf()

# Create word cloud for whole text
wc = WordCloud(background_color='white').generate(working_str)
plt.axis('off')
plt.imshow(wc)
plt.savefig('WordCount_all.png')
plt.show()
plt.clf()

# Create word cloud for top 10 text
wc_str = ''
for k in range(len(fre_list)):
    for i in range(fre_list[k]):
        wc_str = wc_str + str(word_list[k]) + ' '

wc1 = WordCloud(background_color='white').generate(wc_str)
plt.axis('off')
plt.imshow(wc1)
plt.savefig('WordCount_Condition.png')
plt.show()

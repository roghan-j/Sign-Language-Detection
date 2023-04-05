## 1
# model= ["fishing", "I", "love", "favourite", "hobby", "my", "you", "family", "feel", "bad", "sorry"]

# sen_1= ["fishing", "I", "love", "favourite", "hobby", "my"]
# sen_2= ["you", "family", "feel", "bad", "sorry"]

# action= [
#     ["fishing", "I", "love", "favourite", "hobby", "my"],
#     ["love", "I", "love", "favourite", "hobby", "my"],
#     ["hobby", "I", "love", "hobby", "hobby", "I"],
#     ["fishing", "I", "love", "favourite", "hobby", "love"],
#     ["you", "family", "feel", "bad", "feel"],
#     ["you", "family", "feel", "bad", "sorry"],
#     ["you", "family", "feel", "family", "sorry"],
#     ["you", "family", "feel", "bad", "feel"],
# ]

## 2
# model= ["I love you", "heart", "my", "home", "I", "live", "inside", "beautiful"]

# sen_1= ["I love you", "heart", "inside"]
# sen_2= ["my", "home", "I", "live", "inside", "beautiful"]

# action= [
#     ["I love you", "heart", "inside"],
#     ["I love you", "heart", "heart"],
#     ["I love you", "inside", "inside"],
#     ["I love you", "heart", "I love you"],
#     ["my", "home", "I", "live", "inside", "home"],
#     ["my", "home", "I", "home", "inside", "beautiful"],
#     ["my", "home", "I", "live", "I", "beautiful"],
#     ["my", "home", "I", "live", "inside", "I"],
# ]

## 3
# model= ["clean", "home", "help", "thank you", "arrive", "learn", "start"]

# sen_1= ["clean", "home", "help", "thank you"]
# sen_2= ["home",  "arrive", "learn", "start"]

# action= [
#     ["clean", "home", "help", "thank you"],
#     ["clean", "clean", "help", "thank you"],
#     ["clean", "home", "home", "thank you"],
#     ["clean", "home", "clean", "thank you"],
#     ["home",  "arrive", "learn", "clean"],
#     ["home",  "help", "learn", "start"],
#     ["home",  "arrive", "clean", "start"],
#     ["home",  "arrive", "learn", "start"],
# ]

## 4
# model= ["love", "go", "with", "you", "good", "day", "I", "think", "happen"]

# sen_1= ["love", "go", "with", "you"]
# sen_2= ["good", "day", "I", "think", "happen"]

# action= [
#     ["love", "go", "with", "you"],
#     ["love", "go", "with", "with"],
#     ["go", "go", "with", "you"],
#     ["love", "go", "with", "go"],
#     ["good", "day", "I", "think", "love"],
#     ["think", "day", "I", "think", "happen"],
#     ["good", "day", "love", "think", "happen"],
#     ["good", "think", "I", "think", "happen"],
# ]

## 5
model= ["hello", "need", "talk", "you", "about", "health", "feel", "sick", "cold", "my", "have"]

sen_1= ["hello", "need", "talk", "you", "about", "health"]
sen_2= ["feel", "sick", "cold", "my", "have"]

action= [
    ["hello", "need", "talk", "you", "about", "health"],
    ["hello", "need", "talk", "you", "about", "health"],
    ["about", "need", "talk", "hello", "about", "health"],
    ["hello", "talk", "talk", "you", "about", "hello"],
    ["feel", "sick", "cold", "my", "sick"],
    ["feel", "sick", "cold", "my", "have"],
    ["cold", "sick", "cold", "sick", "have"],
    ["feel", "sick", "cold", "my", "feel"],
]

idx= {}

for i,j in enumerate(model):
    idx[j]= i

cm= [[0]*len(model) for _ in range(len(model))]

for i in range(len(action)):

    for j in range(len(action[i])):

        if i<=3:
            r= idx[action[i][j]]
            c= idx[sen_1[j]]
            cm[r][c]+=1

        else:
            r= idx[action[i][j]]
            c= idx[sen_2[j]]
            cm[r][c]+=1

s= 0

for i in range(len(cm)):
    s+= cm[i][i]

accuracy= s/((len(sen_1)+len(sen_2))*4)
print("Model Accuracy=", accuracy)    
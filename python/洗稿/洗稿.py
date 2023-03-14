import markovify

# 读取文本文件
with open("./input.txt") as f:
    text = f.read()
    print("aaaaaaaa"+text)


# 构建文本生成模型
text_model = markovify.Text("I'm happy,how are you, i can write some code", state_size=2)

# 生成新的文本
new_text = text_model.make_sentence(max_overlap_ratio=0.2)

print(new_text)



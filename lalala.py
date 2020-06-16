from text2vec import Similarity

a = "我喜欢一个女孩子。"
b = "我讨厌一个女孩子。"

sim = Similarity()
s = sim.get_score(a,b)
print(s)
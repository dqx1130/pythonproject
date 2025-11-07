import pickle

fp = open("data.txt", "rb+")
fw = open('data1.txt', 'w')
a = pickle.load(fp)
pickle = str(a)
fw.write(pickle)
fw.close()
fp.close()
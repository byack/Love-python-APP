from collections import Counter
import numpy as np

def bijiao(dates, k):
    k_j = []
    with open('datingTestSet.txt') as info:
        for i in info.readlines():
            infos = i.split('\t')
            date = np.array([float(infos[0]), float(infos[1]), float(infos[2])])
            s = np.sqrt(np.sum(np.square(date-dates)))
            if len(k_j) < k:
                k_j.append([infos[3], s])
            else:
                k_j.sort(reverse=True, key=lambda x:x[1])
                for j in k_j:
                    if s < j[1]:
                        k_j.remove(j)
                        k_j.append([infos[3], s])
                        break
    text_date = []
    for k in k_j:
        if k[0][0] == "l":
            text_date.append("largeDoses")
        elif k[0][0] == "s":
            text_date.append("smallDoses")
        else:
            text_date.append("didntLike")
    return Counter(text_date).most_common(1)[0][0][0]

if __name__ == "__main__":
    result = {}
    for k in range(5, 20):
        nums = 0
        with open('datingTestSet.txt') as info:
            for i in info.readlines()[:200]:
                infos = i.split('\t')
                dates = np.array([float(infos[0]), float(infos[1]), float(infos[2])])
                txt = bijiao(dates, k)
                if txt == infos[3][0]:
                    nums += 1
        result[k] = nums
    print(result)

import sys

with open(f"{sys.argv[1]}","r") as text:
    def f(x,y):
        dictionary = dict(zip(x, y))
        dictionary_items = dictionary.items()
        sorted_items = sorted(dictionary_items)
        return sorted_items

    message_id = []
    packet_id = []
    number_mess = []
    messages =[]
    a = []

    for i in text:
        i = i[:-1]
        i = i.split("\t")
        message_id.append(i[0])
        packet_id.append(i[1])
        messages.append(i[2])
    for j in message_id:
        if j not in a:
            a.append(j)
    l = len(a)
    l1 = len(message_id)
    a.sort()
    packet_id1 = [[],[],[],[],[],[],[],[]]
    messages1 = [[],[],[],[],[],[],[],[]]

    for i in range(l):
        for j in range(l1):
            if a[i] == message_id[j]:
                packet_id1[i].append(packet_id[j])
                messages1[i].append(messages[j])





    with open(f"{sys.argv[2]}", "w") as text2:
        for x in range(l):
            text2.write(f"Message	{x+1}\n")
            b = f(packet_id1[x], messages1[x])
            for i in range(len(packet_id1[x])):
                text2.write(f"{a[x]}\t{b[i][0]}\t{b[i][1]}\n")









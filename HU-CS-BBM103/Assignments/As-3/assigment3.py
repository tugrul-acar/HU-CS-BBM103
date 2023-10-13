import sys
with open(f"{sys.argv[1]}","r+") as text:

    users = []              ##in this part I take users and friends in two different lists
    friends = []
    a = []
    codes = []          ##codes and codes2 takes comment from comment.txt (codes= ANU,DEU etc codes2 = Tom 2 etc)
    codes2 = []
    x = 0
    for i in text:
        if "\n" in i:
            i = i[:-1]
        i = i.split(":")
        users.append(i[0])
        l = len(users)
        friends.append(i[1])
    for j in range(len(friends)):
        b = friends[j].split(" ")
        friends[j] = b
    with open(f"{sys.argv[2]}", "r") as text2:
        for i in  text2:
            if "\n" in i:
                i = i[:-1]
            i = i.split(" ")
            codes.append(i[0])
            if len(i) == 2:
                codes2.append(i[1])
            elif len(i) == 3:
                codes2.append(i[1:3])
    with open("output.txt", "w") as text3:
        text3.write("Welcome to Assignment 3\n")
        text3.write("-------------------------------\n")
    for i in range(len(codes)):
        with open("output.txt", "a") as text3:
            if codes[i] == "ANU":  ##ANU PART
                if codes2[i] in users:                                          ##checks the user in list or not
                    text3.write("ERROR: Wrong input type! for 'ANU'! -- This user already exists!!\n")
                else:
                    users.append(codes2[i])
                    friends.append(a)
                    text3.write(f"User '{codes2[i]}' has been added to the social network successfully\n")

            elif codes[i] == "DEU":   ##DEU PART
                if codes2[i] not in users:
                    text3.write(f"ERROR: Wrong input type! for 'DEU'!--There is no user named '{codes2[i]}'!!\n")
                else:
                    u = users.index(codes2[i])
                    del users[u]
                    del friends[u]
                    for j in range(len(friends)):           ##this code delete the user from every friends
                        if codes2[i] in friends[j]:
                            friends[j].remove(codes2[i])
                    text3.write(f"User '{codes2[i]}' and his/her all relations have been deleted successfully\n")

            elif codes[i] == "ANF":    ##ANF PART
                if codes2[i][0] in users:
                    if codes2[i][1] in users:
                        index1 = users.index(codes2[i][0])
                        b = friends[index1]
                        friends[index1]=b
                        if codes2[i][1] in friends[index1]:
                            text3.write(f"ERROR: A relation between '{codes2[i][0]}' and '{codes2[i][1]}' already exists!!\n")
                        else:
                            index2 = users.index(codes2[i][0])
                            b.append(codes2[i][1])
                            friends[index2] = b
                            x = users.index(codes2[i][1])
                            if len(friends[x]) == 0:
                                friends[x].append(codes2[i][0])
                            else:
                                friends[x].append(codes2[i][0])
                            text3.write(f"Relation between '{codes2[i][0]}' and '{codes2[i][1]}' has been added successfully.\n")
                    else:
                        text3.write(f"ERROR: Wrong input type! for 'ANF'! -- No user named '{codes2[i][1]}' found!!\n")
                else:
                    if codes2[i][1] in users:
                        text3.write(f"ERROR: Wrong input type! for 'ANF'! -- No user named '{codes2[i][0]}' found!!\n")
                    else:
                        text3.write(f"ERROR: Wrong input type! for 'ANF'! -- No user named '{codes2[i][0]}' and '{codes2[i][1]}' found!\n")

            elif codes[i] == "DEF": ##DEF PART
                if codes2[i][0] in users:
                    if codes2[i][1] in users:
                        p = users.index(codes2[i][0])
                        b = friends[p]
                        friends[p] = b
                        if codes2[i][1] in friends[p]:    ##if they are friends ı should delete each of them,first ı take index of friends and remove
                            y = users.index(codes2[i][0])
                            friends[y].remove(codes2[i][1])
                            x = users.index(codes2[i][1])
                            friends[x].remove(codes2[i][0])
                            text3.write(f"Relation between '{codes2[i][0]}' and '{codes2[i][1]}' has been deleted successfully\n")
                        else:
                            text3.write(f"ERROR: No relation between '{codes2[i][0]}' and '{codes2[i][1]}' found!\n")
                    else:
                        text3.write(f"ERROR: Wrong input type! for 'DEF'! -- No user named '{codes2[i][1]}' found!!\n")      ##IF there is no named users as taken from code, print errors
                else:
                    if codes2[i][1] in users:
                        text3.write(f"ERROR: Wrong input type! for 'DEF'! -- No user named '{codes2[i][0]}' found!!\n")
                    else:
                        text3.write(f"ERROR: Wrong input type! for 'DEF'! -- No user named '{codes2[i][0]}' and '{codes2[i][1]}' found!\n")

            elif codes[i] == "CF":
                if codes2[i] in users:
                    index1 = users.index(codes2[i])
                    x = len(friends[index1])
                    text3.write(f"User '{codes2[i]}' has {x} friends\n")
                else:
                    text3.write(f"ERROR: Wrong input type! for 'CF'! -- No user named '{codes2[i]}' found!\n")

            elif codes[i] == "FPF":
                if codes2[i][0] in users:
                    if int(codes2[i][1]) == 1:
                        x = users.index(codes2[i][0])
                        l = len(friends[x])
                        with open("output.txt", "a") as text3:
                            text3.write(f"User '{codes2[i][0]}' have {l} possible friends when maximum distance is 1\n")
                            text3.write("These possible friends: {")
                            for i in range(l):
                                if i < l - 1:
                                    text3.write(f"'{friends[x][i]}', ")
                                else:
                                    text3.write(f"'{friends[x][i]}'")
                            text3.write("}\n")
                    elif int(codes2[i][1]) == 2:
                        pf = []
                        x = users.index(codes2[i][0])
                        l = len(friends[x])
                        pf.extend(friends[x])
                        for p in friends[x]:
                            y = users.index(p)
                            pf.extend(friends[y])
                        pf = list(dict.fromkeys(pf))
                        if codes2[i][0] in pf:
                            pf.remove(codes2[i][0])
                        pf.sort()
                        l = len(pf)
                        text3.write(f"User '{codes2[i][0]}' have {l} possible friends when maximum distance is 2 \n")
                        text3.write("These possible friends: {")
                        for i in range(l):
                            if i < l - 1:
                                text3.write(f"'{pf[i]}', ")
                            else:
                                text3.write(f"'{pf[i]}'")
                        text3.write("}\n")
                    elif int(codes2[i][1]) == 3:
                        pf = []
                        x = users.index(codes2[i][0])
                        l = len(friends[x])
                        pf.extend(friends[x])
                        for user in friends[x]:
                            y = users.index(user)
                            pf.extend(friends[y])
                            for user1 in friends[y]:
                                v = users.index(user1)
                                pf.extend(friends[v])

                        pf = list(dict.fromkeys(pf))
                        if codes2[i][0] in pf:
                            pf.remove(codes2[i][0])
                        pf.sort()
                        l = len(pf)
                        text3.write(f"User '{codes2[i][0]}' have {l} possible friends when maximum distance is 3 \n")
                        text3.write("These possible friends: {")
                        for i in range(l):
                            if i < l - 1:
                                text3.write(f"'{pf[i]}', ")
                            else:
                                text3.write(f"'{pf[i]}'")
                        text3.write("}\n")
                    else:
                        text3.write(f"ERROR: Maximum distance must be between 1 (included) and 3 (included).\n")
                else:
                    text3.write(f"ERROR: Wrong input type! for 'FPF'! -- No user named '{codes2[i][0]}' found!\n")
            elif codes[i] == "SF":
                if codes2[i][0] in users:
                    pf = []
                    pf2 = []
                    pf3 = []
                    sf1 = []
                    sf2 = []
                    sf3 = []
                    sf4 = []
                    sf5 = []
                    counter = []
                    x = users.index(codes2[i][0])
                    l = len(friends[x])
                    pf.extend(friends[x])
                    for a in friends[x]:
                        y = users.index(a)
                        pf2.extend(friends[y])
                    for a in pf2:
                        if a not in pf3:
                            pf3.append(a)
                            c = pf2.count(a)
                            counter.extend(str(c))
                    duplicate_dict = {t: pf2.count(t) for t in pf2}
                    for a in duplicate_dict:
                        x = duplicate_dict[a]
                        if str(x) == "3":
                            sf3.append(a)
                        if str(x) == "2":
                            sf2.append(a)
                        if str(x) == "4":
                            sf4.append(a)
                        if str(x) == "5":
                            sf5.append(a)
                    if codes2[i][0] in sf3:
                        sf3.remove(codes2[i][0])
                    if codes2[i][0] in sf2:
                        sf2.remove(codes2[i][0])
                    if codes2[i][0] in sf4:
                        sf4.remove(codes2[i][0])
                    if codes2[i][0] in sf5:
                        sf5.remove(codes2[i][0])
                    if int(codes2[i][1]) == 2:
                        sf2.sort()
                        sf3.sort()
                        sf4.sort()
                        sf5.sort()
                        sf1.extend(sf2)
                        sf1.extend(sf3)
                        sf1.extend(sf4)
                        sf1.extend(sf5)
                        sf1.sort()
                        text3.write(f"Suggestion List for '{codes2[i][0]}' (when MD is {codes2[i][1]}):\n")
                        for a in sf2:
                            text3.write(f"'{codes2[i][0]}' has 2 mutual friends with '{a}'\n")
                        for a in sf3:
                            text3.write(f"'{codes2[i][0]}' has 3 mutual friends with '{a}'\n")
                        for a in sf4:
                            text3.write(f"'{codes2[i][0]}' has 3 mutual friends with '{a}'\n")
                        for a in sf5:
                            text3.write(f"'{codes2[i][0]}' has 3 mutual friends with '{a}'\n")
                        text3.write(f"The suggested friends for '{codes2[i][0]}':")
                        for a in range(len(sf1)):
                            if a < len(sf1) - 1:
                                text3.write(f"'{sf1[a]}',")
                            else:
                                text3.write(f"'{sf1[a]}'\n")
                    elif int(codes2[i][1]) == 3:
                        sf3.sort()
                        sf4.sort()
                        sf5.sort()
                        sf1.extend(sf3)
                        sf1.extend(sf4)
                        sf1.extend(sf5)
                        text3.write(f"Suggestion List for '{codes2[i][0]}' (when MD is {codes2[i][1]}):\n")
                        for a in sf3:
                            text3.write(f"'{codes2[i][0]}' has 3 mutual friends with '{a}'\n")
                        for a in sf4:
                            text3.write(f"'{codes2[i][0]}' has 3 mutual friends with '{a}'\n")
                        for a in sf5:
                            text3.write(f"'{codes2[i][0]}' has 3 mutual friends with '{a}'\n")
                        text3.write(f"The suggested friends for '{codes2[i][0]}':")
                        for a in range(len(sf1)):
                            if len(sf1) == 1:
                                text3.write(f"'{sf1[a]}'\n")
                            elif a < len(sf1) -1:
                                text3.write(f"'{sf1[a]}',")
                            else:
                                text3.write(f"'{sf1[a]}'\n")
                    else:
                        text3.write("Error: Mutually Degree cannot be less than 1 or greater than 4\n")
                else:
                    text3.write(f"Error: Wrong input type! for 'SF'! -- No user named '{codes2[i][0]}' found!\n")

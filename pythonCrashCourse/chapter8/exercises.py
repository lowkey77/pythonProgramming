# Chapter 8 exercises
# 8-9
def showMessages(mList):
    for message in mList:
        print(message)


messageList = ["Hello there.", "How are you doing?", "What time is it?", "See you later."]
sentMessages = []


# showMessages(messageList)


# 8-10
# def send_messages(mList):
#     i = 0
#     while i < mList.__len__():
#         print(mList[i])
#         sentMessages.append(mList[i])
#         i += 1
#
#     mList.clear()
#     print(f"The message list contains: {mList}")
#     print(f"The sent message list contains: {sentMessages}")


# send_messages(messageList)

# 8-11
def send_messages(mList):
    i = 0
    mListCopy = mList.copy()
    while i < mListCopy.__len__():
        print(mListCopy[i])
        sentMessages.append(mListCopy[i])
        i += 1

    mListCopy.clear()
    print(f"The message list contains: {mList}")
    print(f"The sent message list contains: {sentMessages}")


send_messages(messageList)
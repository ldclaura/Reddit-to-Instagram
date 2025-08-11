from redditscrape import Reddit_Scrape
from gemini import AIGen
scrape = Reddit_Scrape()
print(scrape)
post = scrape.top_post(1)
print(post)
print("-----post-----")
for num in list(post.keys()):
    for title in post[num]:
        print(title) #title
        thetitle = title
        print(post[num][title][0]) #desc
        thedesc = post[num][title][0]
commentsreplies = ""
for comment in scrape.comments():
    print(comment)
    print("-----comments------")
    print(scrape.comments()[comment])
    print(f"-----{len(scrape.replies(comment))}replies-----")
    print(scrape.replies(comment))
    commentsreplies + scrape.comments()[comment] #+ scrape.replies(comment)
    for reply in range(len(scrape.replies(comment))):
        commentsreplies + reply
print(commentsreplies)

# gener = AIGen()

# with open("re.txt", "w") as f:
#     f.write(gener.generate(thetitle + " " + thedesc))








# with open("re.txt", "rb") as f:
#     num_lines = sum(1 for _ in f)
# with open("re.txt", "r") as f:
#     for _ in range(num_lines):
#         print("NEW LINE")
#         print("...")
#         print(f.readline())



# Display edited image
# img.show()

# Save the edited image
# img.save("car2.png")





# print(list(post[1].keys())[0]) #dict_keys(['key string']) to just 'key string'



# for x in range(len(data[1]['data']['children'])[_]['data']['replies']['data']['children']):#[0]['data']['body']
#     print("REPLIES")
#     print(data[1]['data']['children'][_]['data']['replies']['data']['children'][x]['data']['body'])
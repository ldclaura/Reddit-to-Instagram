from redditscrape import Reddit_Scrape

scrape = Reddit_Scrape()
post = scrape.top_post(2)
print(post)
print(scrape.comments())
for x in scrape.comments():
    print(scrape.replies(x))



with open("re.txt", "rb") as f:
    num_lines = sum(1 for _ in f)
with open("re.txt", "r") as f:
    for _ in range(num_lines):
        print("NEW LINE")
        print("...")
        print(f.readline())
# Display edited image
# img.show()

# Save the edited image
# img.save("car2.png")





# print(list(post[1].keys())[0]) #dict_keys(['key string']) to just 'key string'



# for x in range(len(data[1]['data']['children'])[_]['data']['replies']['data']['children']):#[0]['data']['body']
#     print("REPLIES")
#     print(data[1]['data']['children'][_]['data']['replies']['data']['children'][x]['data']['body'])
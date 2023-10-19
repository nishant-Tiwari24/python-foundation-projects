from instabot import Bot
automationBot = Bot()

automationBot.login(username="its.nishaant",password="********")
automationBot.follow("niv_srir")
automationBot.upload_photo("/Users/nishanttiwari/projects/netflix_clone")
automationBot.unfollow("nivedha_sriram")
automationBot.send_message("Hey there its Nishant",['yeemessymfs,nivedha_sriram'])
followers = automationBot.get_user_followers("its.nishaant")
for i in followers:
    print(automationBot.get_user_info)

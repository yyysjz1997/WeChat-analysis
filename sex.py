#  统计好友性别比例
import itchat

#  登录微信
#itchat.login()
itchat.auto_login(hotReload=True)

#  获取微信好友列表
friends=itchat.get_friends()[0:]
#print(friends)

#  统计好友性别
male = 0
female = 0
other = 0
for i in friends[1:]:
     sex=i['Sex']
     #print(sex)
     if sex == 1:
          male += 1
     elif sex == 2:
          female += 1
     else:
          other += 1

#  微信好友总数
total = len(friends[1:])

print("男性好友：%.2f%%"%(float(male)/total*100))
print("女性好友：%.2f%%"%(float(female)/total*100))

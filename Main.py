import time
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

vk_token = "omrlmcbbhviakbl0zkqqklxf333er7cvrzz21x4fgu8lp9recjhkidyffsa0cf9p24cjbwjdktefwpju042zo" # Here, instead of fake token, specify the VKontakte token (Example: Kate Mobile Token). 

vk_session = vk_api.VkApi(token=vk_token)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

def BlackListAdd():
	try:
		for InfoUser in vk.messages.getHistory(peer_id = event.peer_id, count = 1)['items']:
			ReplyInfo = InfoUser.get('reply_message')
			FromID = ReplyInfo.get('from_id')
			vk.account.ban(owner_id = FromID)
			vk.messages.delete(message_ids = event.message_id, delete_for_all = 1) # Auto-Delete message. You can delete a line
	except:
 			pass
 			
def BlackListRemove():
	try:
		for InfoUser in vk.messages.getHistory(peer_id = event.peer_id, count = 1)['items']:
			ReplyInfo = InfoUser.get('reply_message')
			FromID = ReplyInfo.get('from_id')
			vk.account.unban(owner_id = FromID)
			vk.messages.delete(message_ids = event.message_id, delete_for_all = 1) # similar deletion 
	except:
 			pass
 			
for event in longpoll.listen():
	if event.type == VkEventType.MESSAGE_NEW and event.from_me:
		if event.text == "+чс":
			BlackListAdd()
		if event.text == "-чс":
			BlackListRemove()
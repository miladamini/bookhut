# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from post.models import post
#
# admin = ""
#
# import requests
# import urllib
# import random
#
# TOKEN = "6604541901:AAEID4S1XDSNJDGaYslCTKN4Ple0_Q0R6GA"
# URL = "https://api.telegram.org/bot{}/".format(TOKEN)
# USERNAME_BOT = "akoroman_bot"
# gplink = "https://t.me/+c80KRM_lZwhmYTQ1"
#
#
# @receiver(post_save, sender=post)
# def create_reply_notification_signal(sender, instance, created, *args, **kwargs):
#     """
#     craete notification when user reply comment
#     """
#     if created:
#         p = post.objects.filter(botmodel=True).first()
#         d = post.objects.filter(botmodel=True).exists()
#         m = post.objects.filter(botmodel=True)
#         print(p.img.url)
#         milad = True
#
#         def get_url(url):
#             response = requests.get(url)
#             content = response.content.decode("utf8")
#             return content
#
#         def get_last_update_id(updates):
#             update_ids = []
#             for update in updates["result"]:
#                 update_ids.append(int(update["update_id"]))
#             return max(update_ids)
#
#         def bot(method, datas):
#             url = f'https://api.telegram.org/bot{TOKEN}/' + method
#             v = requests.post(url, json=datas)
#             return v
#
#         def send_message(chat_id, text):
#             tot = urllib.parse.quote_plus(text)
#             url = URL + "sendMessage?text={}&chat_id={}".format(tot, chat_id)
#             get_url(url)
#
#         def sendmessage(chat_id, text, rep, keys):
#             tot = urllib.parse.quote_plus(text)
#             gbord = urllib.parse.quote_plus(str(keys))
#             url = URL + "sendMessage?text={}&chat_id={}&reply_to_message_id={}&reply_markup={}".format(tot, chat_id,
#                                                                                                        rep, gbord)
#             get_url(url)
#
#         def sendpm(c, t, m, k):
#             bot('sendmessage', {"chat_id": c, "text": t, "message_id": m, "reply_markup": k})
#
#         def editMessage(idcat, msgid, txt):
#             bot('editMessageText', {"chat_id": idcat, "message_id": msgid, "text": txt})
#
#         def editmsgkey(idcat, pm, key):
#             bot('editmessagereplymarkup', {"chat_id": idcat, "message_id": pm, "reply_markup": key})
#
#         def send_document(doc, chat_id):
#             files = {'document': open(doc, 'rb')}
#             requests.post(URL + "sendDocument?chat_id={}".format(chat_id), files=files)
#
#         def send_image(doc, chat_id):
#             files = {'photo': doc}
#             requests.post(URL + "sendPhoto?chat_id={}".format(chat_id), files=files)
#
#         def send_pm_to_channel(c, t):
#             bot('sendmessage', {"chat_id": c, "text": t})
#
#         key_post = {"inline_keyboard": [
#             [{"text": "🌐 مشاهده در سایت 🌐", "url": f'https://bookhut.ir/roman/{p.slug}'}]]}
#
#         def sendphoto(c, photo, cap, k):
#             bot('sendphoto', {"chat_id": c, "photo": photo, "caption": cap, "reply_markup": k})
#
#         if d == True:
#             sendphoto(c=--1001962342324, photo=f'https://bookhut.ir/{p.img.url}',
#                       cap=f'نام رمان : {p.title} \n\n   نویسنده : {p.name} \n\n خلاصه‌ای از رمان : \n\n {p.body}  ',
#                       k=key_post)
#             p.botmodel = False
#             p.save()

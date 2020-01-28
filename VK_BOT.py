from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
import random
from datetime import datetime

import parser_daimond
import parser_advance

token = '267d60e4f3fb5d7c8393016ce162db2f5bea820ecb913726e151fca21ea48825e7eee00da91750e605a4d'

vk_session = vk_api.VkApi(token = token)

session_api = vk_session.get_api()

id_group = 185787449

longpoll = VkBotLongPoll(vk_session, id_group)

def send_message(session_api, peer_id, message):
    session_api.messages.send(peer_id = peer_id, message = message, random_id = random.randint(-99999,+99999))

def get_online(session_api, peer_id):
    return session_api.users.get(peer_id=peer_id, fields='online')[0]

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:

        max_member = session_api.messages.getConversationMembers(peer_id = event.obj.peer_id)['count']-1
        print('Участников: ' + str(max_member))

        if event.obj.peer_id != event.obj.from_id:

            # members_list = session_api.messages.getConversationMembers(peer_id=event.obj.peer_id)
            #
            # sender_name = list(filter(lambda name: name['id'] == event.obj.from_id, [name for name in session_api.messages.getConversationMembers(peer_id=event.obj.peer_id, fields='profiles')['profiles']]))[0]
            #
            # last_and_ferst_name = str(sender_name['first_name']) + ' ' +str(sender_name['last_name'])
            #
            # send_message(session_api,peer_id=event.obj.peer_id, message='@.id{0}({1})'.format(event.obj.from_id,last_and_ferst_name) +'\nУчастников беседы: ' + str(max_member))
            #
            # print(event.obj)

            if event.obj.text == '/help':
                text = 'Доступные команды:\n\n' \
                       '/help - Команды Бота\n' \
                       '/online - Показывает онлайн на сервере Paradox RP\n' \
                       '/  \n' \
                       '/  \n'
                send_message(session_api, peer_id=event.obj.peer_id, message=text)


            if event.obj.text == '/online':
                text = ''
                for i in range(max_member):
                    print('i = ',i)

                    id = session_api.messages.getConversationMembers(peer_id=event.obj.peer_id)['profiles'][i]['id']
                    print('ID = ',id)

                    name = session_api.users.get(user_ids = id)[0]
                    print('Объект по ID: ',name)

                    operation_name = name['first_name'] + ' ' +name['last_name']
                    print('Преобразование в Имя: ',operation_name)

                    text = text + '\n' +str(operation_name)

                    print('============================================================')

                print('Участники:' + text)

                send_message(session_api, peer_id=event.obj.peer_id, message='Участники:{0}'.format(text))

            if event.obj.text == '/test':
                send_message(session_api, peer_id=event.obj.peer_id, message=str(parser_daimond.result))
                send_message(session_api, peer_id=event.obj.peer_id, message=str(parser_advance.result))





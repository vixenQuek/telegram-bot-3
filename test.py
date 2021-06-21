
import re
import time 
from typing import Text
from telethon import TelegramClient, events #,Button
from telethon.tl.custom import Button
from datetime import timedelta
import logging
import asyncio

from telethon.tl.types import InputPeerChannel
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                   level=logging.INFO)


# Dev api
# api_id = 5911805
# api_hash = 'baf59bae0d7caba308cdada2079670c2'


# client +6593535606
api_id1 = 6321890
api_hash1 = '035591fda2dd29ec88b007f41a277cb1'

# client +6590512432
api_id2 = 1780565
api_hash2 = 'abd7878b9710dd527f4f4b2af547a94c'


# client +6596114901
api_id3 = 2367933
api_hash3 = '924e0353f9a15071f21b88d36bfa8eb2'


# client +12404902773
api_id4 = 2777763
api_hash4 = '72cfa7632635ad14a88383163c7fa791'

# client +639155423753
api_id5 = 1559990
api_hash5 = 'cc517c8e24cd8d1d0cee9c77794b3bc8'




client1 = TelegramClient("+6593535606", api_id1, api_hash1)
client2 = TelegramClient("+6590512432", api_id2, api_hash2)
client3 = TelegramClient("+6596114901", api_id3, api_hash3)
client4 = TelegramClient("+12404902773", api_id4, api_hash4)
client5 = TelegramClient("+639155423753", api_id5, api_hash5)

MESSAGE_TO_SENT1 = None
MESSAGE_TO_SENT2 = None
MESSAGE_TO_SENT3 = None
MESSAGE_TO_SENT4 = None
MESSAGE_TO_SENT5 = None

Timer = None

CHAT_LIST1 = []
CHAT_LIST2 = []
CHAT_LIST3 = []
CHAT_LIST4 = []
CHAT_LIST5 = []

def main():
    client1.start()
    client2.start()
    client3.start()
    client4.start()
    client5.start()

    print("Userbot on!")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_message())
    client1.run_until_disconnected()
    client2.run_until_disconnected()
    client3.run_until_disconnected()
    client4.run_until_disconnected()
    client5.run_until_disconnected()


async def send_message():


    global CHAT_LIST1, CHAT_LIST2, CHAT_LIST3, CHAT_LIST4, CHAT_LIST5, MESSAGE_TO_SENT1, MESSAGE_TO_SENT2, MESSAGE_TO_SENT3, MESSAGE_TO_SENT4, MESSAGE_TO_SENT5, Timer
    while True:
        if Timer is None:
            Timer = 960
        await asyncio.sleep(Timer)
        for i in CHAT_LIST1:
            if MESSAGE_TO_SENT1 is not None:
                await client1.send_message(i,MESSAGE_TO_SENT1)
        for i in CHAT_LIST2:
            if MESSAGE_TO_SENT2 is not None:
                await client2.send_message(i,MESSAGE_TO_SENT2)
        for i in CHAT_LIST3:
            if MESSAGE_TO_SENT3 is not None:
                await client3.send_message(i,MESSAGE_TO_SENT3)
        for i in CHAT_LIST4:
            if MESSAGE_TO_SENT4 is not None:
                await client4.send_message(i,MESSAGE_TO_SENT4)
        for i in CHAT_LIST5:
            if MESSAGE_TO_SENT5 is not None:
                await client5.send_message(i,MESSAGE_TO_SENT5)
                





@client1.on(events.NewMessage(chats='me'))
async def set_game(event):
    global CHAT_LIST1, MESSAGE_TO_SENT1
    my_message = event.original_update.message.message # This will get every message from admin
    if my_message == '/setmessage': # Check if the message is '/setgame'
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client1.get_messages('me', ids=get_message.reply_to_msg_id)
            MESSAGE_TO_SENT1 = replyed_to.message
            await client1.send_message(entity='me', message = f'{MESSAGE_TO_SENT1} is set as game')
    elif my_message == '/addchat': # Check if the message is '/setgame'
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client1.get_messages('me', ids=get_message.reply_to_msg_id)
            chat_id = replyed_to.fwd_from.saved_from_peer
            chat_id_entity = await client1.get_entity(chat_id)
            chat_title = chat_id_entity.title
            CHAT_LIST1.append(chat_title)
            await client1.send_message(entity='me', message = f'{chat_title} is added to list')
    elif my_message == '/removechat': # Check if the message is '/setgame'
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client1.get_messages('me', ids=get_message.reply_to_msg_id)
            chat_id = replyed_to.fwd_from.saved_from_peer
            chat_id_entity = await client1.get_entity(chat_id)
            chat_title = chat_id_entity.title
            CHAT_LIST1.remove(chat_title)
            await client1.send_message(entity='me', message = f'{chat_title} is remove from list')


    elif my_message == '/showlist': # Check if the message is '/setgame'
        await client1.send_message(entity='me', message = f'This is the list {CHAT_LIST1}')
    
    elif my_message == '/settimer': # Check if the message is '/setgame'
        print('asdfj')
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client1.get_messages('me', ids=get_message.reply_to_msg_id)
            message = replyed_to.message
            if message.isdigit():
                Timer = int(message)
                await client1.send_message('me', f'Timer is set for every {Timer} seconds')
            else:
                await client1.send_message('me', f'reply to an number')



@client2.on(events.NewMessage(chats='me'))
async def set_game(event):
    global CHAT_LIST2, MESSAGE_TO_SENT2
    my_message = event.original_update.message.message # This will get every message from admin
    if my_message == '/setmessage': # Check if the message is '/setgame'
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client2.get_messages('me', ids=get_message.reply_to_msg_id)
            MESSAGE_TO_SENT2 = replyed_to.message
            await client2.send_message(entity='me', message = f'{MESSAGE_TO_SENT2} is set as game')
    elif my_message == '/addchat': # Check if the message is '/setgame'
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client2.get_messages('me', ids=get_message.reply_to_msg_id)
            chat_id = replyed_to.fwd_from.saved_from_peer
            chat_id_entity = await client2.get_entity(chat_id)
            chat_title = chat_id_entity.title
            CHAT_LIST2.append(chat_title)
            await client2.send_message(entity='me', message = f'{chat_title} is added to list')
    elif my_message == '/removechat': # Check if the message is '/setgame'
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client2.get_messages('me', ids=get_message.reply_to_msg_id)
            chat_id = replyed_to.fwd_from.saved_from_peer
            chat_id_entity = await client2.get_entity(chat_id)
            chat_title = chat_id_entity.title
            CHAT_LIST2.remove(chat_title)
            await client2.send_message(entity='me', message = f'{chat_title} is remove from list')


    elif my_message == '/showlist': # Check if the message is '/setgame'
        await client2.send_message(entity='me', message = f'This is the list {CHAT_LIST2}')
    
    elif my_message == '/settimer': # Check if the message is '/setgame'
        print('asdfj')
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client2.get_messages('me', ids=get_message.reply_to_msg_id)
            message = replyed_to.message
            if message.isdigit():
                Timer = int(message)
                await client2.send_message('me', f'Timer is set for every {Timer} seconds')
            else:
                await client2.send_message('me', f'reply to an number')




@client3.on(events.NewMessage(chats='me'))
async def set_game(event):
    global CHAT_LIST3, MESSAGE_TO_SENT3
    my_message = event.original_update.message.message # This will get every message from admin
    if my_message == '/setmessage': # Check if the message is '/setgame'
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client3.get_messages('me', ids=get_message.reply_to_msg_id)
            MESSAGE_TO_SENT3 = replyed_to.message
            await client3.send_message(entity='me', message = f'{MESSAGE_TO_SENT3} is set as game')
    elif my_message == '/addchat': # Check if the message is '/setgame'
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client3.get_messages('me', ids=get_message.reply_to_msg_id)
            chat_id = replyed_to.fwd_from.saved_from_peer
            chat_id_entity = await client3.get_entity(chat_id)
            chat_title = chat_id_entity.title
            CHAT_LIST3.append(chat_title)
            await client3.send_message(entity='me', message = f'{chat_title} is added to list')
    elif my_message == '/removechat': # Check if the message is '/setgame'
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client3.get_messages('me', ids=get_message.reply_to_msg_id)
            chat_id = replyed_to.fwd_from.saved_from_peer
            chat_id_entity = await client3.get_entity(chat_id)
            chat_title = chat_id_entity.title
            CHAT_LIST3.remove(chat_title)
            await client3.send_message(entity='me', message = f'{chat_title} is remove from list')


    elif my_message == '/showlist': # Check if the message is '/setgame'
        await client3.send_message(entity='me', message = f'This is the list {CHAT_LIST3}')
    
    elif my_message == '/settimer': # Check if the message is '/setgame'
        print('asdfj')
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client3.get_messages('me', ids=get_message.reply_to_msg_id)
            message = replyed_to.message
            if message.isdigit():
                Timer = int(message)
                await client3.send_message('me', f'Timer is set for every {Timer} seconds')
            else:
                await client3.send_message('me', f'reply to an number')





@client4.on(events.NewMessage(chats='me'))
async def set_game(event):
    global CHAT_LIST4, MESSAGE_TO_SENT4
    my_message = event.original_update.message.message # This will get every message from admin
    if my_message == '/setmessage': # Check if the message is '/setgame'
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client4.get_messages('me', ids=get_message.reply_to_msg_id)
            MESSAGE_TO_SENT4 = replyed_to.message
            await client4.send_message(entity='me', message = f'{MESSAGE_TO_SENT4} is set as game')
    elif my_message == '/addchat': # Check if the message is '/setgame'
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client4.get_messages('me', ids=get_message.reply_to_msg_id)
            chat_id = replyed_to.fwd_from.saved_from_peer
            chat_id_entity = await client4.get_entity(chat_id)
            chat_title = chat_id_entity.title
            CHAT_LIST4.append(chat_title)
            await client4.send_message(entity='me', message = f'{chat_title} is added to list')
    elif my_message == '/removechat': # Check if the message is '/setgame'
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client4.get_messages('me', ids=get_message.reply_to_msg_id)
            chat_id = replyed_to.fwd_from.saved_from_peer
            chat_id_entity = await client4.get_entity(chat_id)
            chat_title = chat_id_entity.title
            CHAT_LIST4.remove(chat_title)
            await client4.send_message(entity='me', message = f'{chat_title} is remove from list')


    elif my_message == '/showlist': # Check if the message is '/setgame'
        await client4.send_message(entity='me', message = f'This is the list {CHAT_LIST4}')
    
    elif my_message == '/settimer': # Check if the message is '/setgame'
        print('asdfj')
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client4.get_messages('me', ids=get_message.reply_to_msg_id)
            message = replyed_to.message
            if message.isdigit():
                Timer = int(message)
                await client4.send_message('me', f'Timer is set for every {Timer} seconds')
            else:
                await client4.send_message('me', f'reply to an number')



@client5.on(events.NewMessage(chats='me'))
async def set_game(event):
    global CHAT_LIST5, MESSAGE_TO_SENT5
    my_message = event.original_update.message.message # This will get every message from admin
    if my_message == '/setmessage': # Check if the message is '/setgame'
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client5.get_messages('me', ids=get_message.reply_to_msg_id)
            MESSAGE_TO_SENT5 = replyed_to.message
            await client5.send_message(entity='me', message = f'{MESSAGE_TO_SENT5} is set as game')
    elif my_message == '/addchat': # Check if the message is '/setgame'
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client5.get_messages('me', ids=get_message.reply_to_msg_id)
            chat_id = replyed_to.fwd_from.saved_from_peer
            chat_id_entity = await client5.get_entity(chat_id)
            chat_title = chat_id_entity.title
            CHAT_LIST5.append(chat_title)
            await client5.send_message(entity='me', message = f'{chat_title} is added to list')
    elif my_message == '/removechat': # Check if the message is '/setgame'
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client5.get_messages('me', ids=get_message.reply_to_msg_id)
            chat_id = replyed_to.fwd_from.saved_from_peer
            chat_id_entity = await client5.get_entity(chat_id)
            chat_title = chat_id_entity.title
            CHAT_LIST5.remove(chat_title)
            await client5.send_message(entity='me', message = f'{chat_title} is remove from list')


    elif my_message == '/showlist': # Check if the message is '/setgame'
        await client5.send_message(entity='me', message = f'This is the list {CHAT_LIST5}')
    
    elif my_message == '/settimer': # Check if the message is '/setgame'
        print('asdfj')
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client5.get_messages('me', ids=get_message.reply_to_msg_id)
            message = replyed_to.message
            if message.isdigit():
                Timer = int(message)
                await client5.send_message('me', f'Timer is set for every {Timer} seconds')
            else:
                await client5.send_message('me', f'reply to an number')



if __name__ == "__main__":
    main()



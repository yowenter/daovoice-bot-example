# -*- encoding:utf-8 -*-

import web
import config
from daovoice_client import get_daovoice_client

urls = (
    '/', 'Index',
    '/hook', 'Hook'
)

app = web.application(urls, globals())


class Index:
    def GET(self):
        return "DaoVoice Bot Example"


class Hook:
    '''
    DaoVoice Webhook
    You can set your webhook in `http://dashboard.daovoice.io/#/app/{your_app_uuid}/apps/settings/webhook`
    '''

    def POST(self):
        data = web.data()
        topic = data.get("topic")
        if topic == 'conversation.user.replied':
            conversation_data = data['data']
            conversation_message = data['conversation_message']
            get_daovoice_client().reply_conversation(
                conversation_uuid=conversation_data['conversation_id'],
                admin_id=config.DAOVOICE_DEFAULT_ADMIN_ID,
                message_type='comment',
                message_body= u"You said {} just now. ".format(conversation_message['body'])

            )


if __name__ == '__main__':
    app.run()

from flask import Flask, request, abort,jsonify
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, CarouselTemplate,
                            CarouselColumn, PostbackTemplateAction, MessageTemplateAction, URITemplateAction,
                            ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, ConfirmTemplate)
from  flask.ext.pymongo import  PyMongo

from searchpic import searchpic

app = Flask(__name__)
app.config['MONGO_DBNAME']='moviebot'
app.config['MONGO_URI']='mongodb://pretty:shop1234@ds139942.mlab.com:39942/moviebot'

mongo =PyMongo(app)

line_bot_api = LineBotApi('iYDoDLW1k4yIYJvMnHVi18Vhl0NXPh5ec6a4FLdlR/en3nqmGCWsF/QeYKX8MPj2DYUFbjsEos/+HGUA7LgF4OimIUh1WD9j/phhG/vqX9zZD92iiw/t+kpE1AadWCIdwkzMuxEvAbCM84LtdTkQSgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('935cecc6bf121cf08c1cea288956462b')


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/webhook", methods=['POST'])
def webhook():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'





@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
        if event.message.text == '1':
            message = TemplateSendMessage(
                alt_text='Carousel template',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url=searchpic(),
                            title='this is menu1',
                            text='description1',
                            actions=[
                                PostbackTemplateAction(
                                    label='postback1',
                                    text='postback text1',
                                    data='action=buy&itemid=1'
                                ),
                                MessageTemplateAction(
                                    label='message1',
                                    text='message text1'
                                ),
                                URITemplateAction(
                                    label='uri1',
                                    uri='http://mandm.plearnjai.com/'
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=searchpic(),
                            title='this is menu2',
                            text='description2',
                            actions=[
                                PostbackTemplateAction(
                                    label='postback2',
                                    text='postback text2',
                                    data='action=buy&itemid=2'
                                ),
                                MessageTemplateAction(
                                    label='message2',
                                    text='message text2'
                                ),
                                URITemplateAction(
                                    label='uri2',
                                    uri='http://mandm.plearnjai.com/'
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=searchpic(),
                            title='this is menu2',
                            text='description2',
                            actions=[
                                PostbackTemplateAction(
                                    label='postback2',
                                    text='postback text2',
                                    data='action=buy&itemid=2'
                                ),
                                MessageTemplateAction(
                                    label='message2',
                                    text='message text2'
                                ),
                                URITemplateAction(
                                    label='uri2',
                                    uri='http://mandm.plearnjai.com/'
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=searchpic(),
                            title='this is menu2',
                            text='description2',
                            actions=[
                                PostbackTemplateAction(
                                    label='postback2',
                                    text='postback text2',
                                    data='action=buy&itemid=2'
                                ),
                                MessageTemplateAction(
                                    label='message2',
                                    text='message text2'
                                ),
                                URITemplateAction(
                                    label='uri2',
                                    uri='http://mandm.plearnjai.com/'
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=searchpic(),
                            title='this is menu2',
                            text='description2',
                            actions=[
                                PostbackTemplateAction(
                                    label='postback2',
                                    text='postback text2',
                                    data='action=buy&itemid=2'
                                ),
                                MessageTemplateAction(
                                    label='message2',
                                    text='message text2'
                                ),
                                URITemplateAction(
                                    label='uri2',
                                    uri='http://mandm.plearnjai.com/'
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=searchpic(),
                            title='this is menu2',
                            text='description2',
                            actions=[
                                PostbackTemplateAction(
                                    label='postback2',
                                    text='postback text2',
                                    data='action=buy&itemid=2'
                                ),
                                MessageTemplateAction(
                                    label='message2',
                                    text='message text2'
                                ),
                                URITemplateAction(
                                    label='uri2',
                                    uri='http://mandm.plearnjai.com/'
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=searchpic(),
                            title='this is menu2',
                            text='description2',
                            actions=[
                                PostbackTemplateAction(
                                    label='postback2',
                                    text='postback text2',
                                    data='action=buy&itemid=2'
                                ),
                                MessageTemplateAction(
                                    label='message2',
                                    text='message text2'
                                ),
                                URITemplateAction(
                                    label='uri2',
                                    uri='http://mandm.plearnjai.com/'
                                )
                            ]
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
            return 0
        elif event.message.text == '2':
             message = TemplateSendMessage(
                alt_text='Confirm template',
                template=ConfirmTemplate(
                    text='Are you sure?',
                    actions=[
                        PostbackTemplateAction(
                            label='postback',
                            text='postback text',
                            data='action=buy&itemid=1'
                        ),
                        MessageTemplateAction(
                            label='message',
                            text='message text'
                        )
                    ]
                )
             )
             line_bot_api.reply_message(event.reply_token, message)
        elif event.message.text == '3':
            message = TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    thumbnail_image_url=searchpic(),
                    title='Menu',
                    text='Please select',
                    actions=[
                        PostbackTemplateAction(
                            label='postback',
                            text='postback text',
                            data='action=buy&itemid=1'
                        ),
                        MessageTemplateAction(
                            label='message',
                            text='message text'
                        ),
                        URITemplateAction(
                            label='uri',
                            uri='http://mandm.plearnjai.com/'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)


if __name__ == '__main__':
    app.run()
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect  # при Post надо перенаправлять (кудато)
from .models import Price, Quality,FooterInfo, MessageFormModel, OwnerEmailBox, ImagesModel, TestImageModel  #импортируем таблицы(модели) из базы
from .forms import MessageForm_Form # импортим формы
from django.core.mail import send_mail # ипортим либу отправки почты
import json
from .bot import to_bot_data_recall,to_bot_data_massage


def mainpage(request):

    def tel_format(tel):  # +38xxxxxxxxxx to +38 (xxx) xxx-xx-xx
        tel = '{} ({}) {}-{}-{}'.format(tel[0:3], tel[3:6], tel[6:9], tel[9:11], tel[11:])
        return tel

    poddon_no_nds = Price.objects.get(name='Поддон').with_NO_NDS
    poddon_nds = Price.objects.get(name='Поддон').with_NDS
    bigbag_no_nds = Price.objects.get(name='БигБэг').with_NO_NDS
    bigbag_nds = Price.objects.get(name='БигБэг').with_NDS

    diameter=Quality.objects.get(name='Диаметр').value
    ash_content=Quality.objects.get(name='Зольность').value
    humidity=Quality.objects.get(name='Влажность').value
    temperature=Quality.objects.get(name='Теплота Сгорания').value

    raw_tel_1=FooterInfo.objects.get(name='Tel_1').value
    format_tel_1=tel_format(raw_tel_1)
    raw_tel_2 = FooterInfo.objects.get(name='Tel_2').value
    format_tel_2 = tel_format(raw_tel_2)
    footer_email=FooterInfo.objects.get(name='Email').value

    message_form = MessageForm_Form() #"подключаем" к вьюхе форму !!!

    owner_mail = OwnerEmailBox.objects.get(name='Ящик').value  #куда будут падать заявки

    #получаем картинки из модели.
    #достаём их урлу и ее будем указывать в шаблоне {{ elem_url }}
    top_img = ImagesModel.objects.get(name='Верхняя_портретная').img
    top_img_url = top_img.url
    middle_img = ImagesModel.objects.get(name='Средняя_квадратная').img
    middle_img_url = middle_img.url
    bottom_img = ImagesModel.objects.get(name='Нижняя_альбомная').img
    bottom_img_url = bottom_img.url
    poddon_img = ImagesModel.objects.get(name='Поддон').img
    poddon_img_url = poddon_img.url
    bigbag_img = ImagesModel.objects.get(name='Бигбэг').img
    bigbag_img_url = bigbag_img.url




    Context ={                      #передача данных в шаблон
        'poddon_no_nds':poddon_no_nds,
        'poddon_nds':poddon_nds,
        'bigbag_no_nds':bigbag_no_nds,
        'bigbag_nds':bigbag_nds,

        'diameter': diameter,
        'ash_content': ash_content,
        'humidity': humidity,
        'temperature': temperature,

        'raw_tel_1': raw_tel_1,
        'format_tel_1': format_tel_1,
        'raw_tel_2': raw_tel_2,
        'format_tel_2': format_tel_2,
        'footer_email': footer_email,

        'message_form':message_form, # передаём форму в контекст шаблона, для вывода в шаблоне(верстке) инпутов

        'top_img_url': top_img_url,
        'middle_img_url': middle_img_url,
        'bottom_img_url': bottom_img_url,
        'poddon_img_url': poddon_img_url,
        'bigbag_img_url': bigbag_img_url,

    }

    # если прилетел POST (аджаксом)
    # декодируем байтовую request.body в строку и парсим. на выходе - dict
    if (request.method == 'POST'):
        if request.is_ajax():
            received_json_data = json.loads(request.body.decode('utf-8'))
            message_form = MessageForm_Form(received_json_data)# “привязать данные к форме” (теперь это связанная с данными форма).
        else:
            message_form = MessageForm_Form(request.POST) # если вдруг отключены скрипты на клиенте или нас просто хакают
                                                          # обезопасить эекземпляр класса форм, и сохранить работоспособность

        if message_form.is_valid():
            # проверенные данные будут добавлены в словарь form.cleaned_data.
            mes_name=message_form.cleaned_data['name']
            mes_phone=message_form.cleaned_data['telephone']
            mes_email = message_form.cleaned_data['email']
            mes_text = message_form.cleaned_data['text_message']

            if (mes_email==''):
                mes_email='-не указан-'

            # создаём и сохраняем екзепляр класса нужной модели
            new_item_of_messege_form_model=MessageFormModel(fio=mes_name,
                                                            phone=mes_phone,
                                                            email=mes_email,
                                                            text=mes_text)
            new_item_of_messege_form_model.save()


            # отправка заявки на мыло
            data='''
            СООБЩЕНИЕ ОТ:
            
            Ф.И.О   :   {}
            
            Телефон     :   {}
            
            Email   :   {}
            
            Сообщение   :   {}
            '''.format(mes_name, mes_phone, mes_email, mes_text)

            send_mail('Заявка с сайта', data, '', [owner_mail])

            #отправка боту
            to_bot_dict={'name':mes_name, 'tel':tel_fromat_decode(mes_phone), 'Email':mes_email, 'mes':mes_text }
            to_bot_data_massage(to_bot_dict)

            return HttpResponseRedirect('/') #перенаправляем !!! на эту же
        else:                                #сттаницу, чтобы при перезагрузке
             print('!!!! форма не валидна !!!!!')       #снова не отправлялся пост

    else:
        return render(request, 'MainPage/main.html', Context)

def recall(request):
    recall_telephone=request.GET['telephone']
    recall_telephone=tel_fromat_decode(recall_telephone)
    to_bot_dict={'tel':recall_telephone }
    to_bot_data_recall(to_bot_dict)

    return HttpResponseRedirect('/') # директим на /,
                                     # а по сути вызываем mainpage

def tel_fromat_decode (str):
    str=str.replace(' ', '',2)
    str = str.replace('-', '',2)
    str = str.replace('(', '')
    str = str.replace(')', '')
    return str

def test_img(request):

    test_img=TestImageModel.objects.get(name='test_image3').img
    test_img_url=test_img.url

    Context={'test_img_url':test_img_url}
    return render(request, 'MainPage/test_img_html.html', Context)
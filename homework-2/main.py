from src.channel import Channel

if __name__ == '__main__':
    # mpt = Channel('UCt_Sgcd_wTB8qiGym1lkgGg')
    mpt = Channel.get_service('UCt_Sgcd_wTB8qiGym1lkgGg')
    # получаем значения атрибутов
    print(mpt.title)  #
    print(mpt.video)  #
    print(mpt.url)  #

    # менять не можем
    mpt.channel_id = 'Новое название'
    # AttributeError: property 'channel_id' of 'Channel' object has no setter

    # можем получить объект для работы с API вне класса
    print(Channel.get_service('UCt_Sgcd_wTB8qiGym1lkgGg'))
    # <googleapiclient.discovery.Resource object at 0x000002B1E54F9750>

    # создаем файл 'mpt.json' в данными по каналу
    mpt.to_json('mpt.json')

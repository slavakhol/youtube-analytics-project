from src.channel import Channel

if __name__ == '__main__':
    # Создаем два экземпляра класса
    mpt = Channel('UCt_Sgcd_wTB8qiGym1lkgGg')
    spt = Channel('UCnHXeVmlLXNXWpmuPnppiwA')

    # Используем различные магические методы
    print(mpt)  # 'Moscow Private Tours (https://www.youtube.com/channel/UCt_Sgcd_wTB8qiGym1lkgGg)'
    print(mpt + spt)  # 73
    print(mpt - spt)  # 71
    print(spt - mpt)  # -71
    print(mpt > spt)  # True
    print(mpt >= spt)  # True
    print(mpt < spt)  # False
    print(mpt <= spt)  # False
    print(mpt == spt)  # False
    

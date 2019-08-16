# coding: utf-8
import shelve

class FreeList:
    SHELF_DIR = "./shelf/"

    @classmethod
    def create_omikuji(cls, list_name, item_name):
        data_list = shelve.open(FreeList.SHELF_DIR + "sample")
        if (list_name in data_list):
            print(list_name + "は既に登録済みです。")
            data_list.close
            return False
            # updateへ移動
            # data = data_list[list_name]
            # data.append(item_name)
            # data_list[list_name] = data
        else:
            data_list[list_name] = [item_name]
            print(list_name + "に" + item_name + "を追加しました。")
            print(data_list[list_name])
            data_list.close
            return True

    @classmethod
    def read_omikuji_list(cls):
        data_list = shelve.open(FreeList.SHELF_DIR + "sample")
        keys = list(data_list.keys())
        print(keys)
        data_list.close
        return keys

    @classmethod
    def read_omikuji(cls, list_name):
        print("引数：" + list_name)
        data_list = shelve.open(FreeList.SHELF_DIR + "sample")
        data = data_list[list_name]
        print(data)
        data_list.close
        return data

    @classmethod
    def change():
        pass

    @classmethod
    def delete():
        pass

    @classmethod
    def chk_shelf_size():
        pass

    @classmethod
    def chk_omikuji_list_count():
        pass

    @classmethod
    def chk_omikuji_list_size():
        pass

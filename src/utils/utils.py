class Utils:
    @staticmethod
    def del_none(dic):
        for key, value in list(dic.items()):
            if value is None or value == {} or value == [] or value == '':
                del dic[key]
            elif isinstance(value, dict):
                Utils.del_none(value)
        return dic

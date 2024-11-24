# https://www.codewars.com/kata/563089b9b7be03472d00002b

class List:
    def remove_(self, integer_list, values_list):
        result = []
        for i in integer_list:
            if i not in values_list:
                result.append(i)
        return result
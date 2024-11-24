# https://www.codewars.com/kata/54dc6f5a224c26032800005c

def stock_list(stocklist, categories):
    if stocklist and categories:
        stock = {category: 0 for category in categories}
        for item in stocklist:
            code, quantity = item.split()
            if code[0] in stock:
                stock[code[0]] += int(quantity)
        return " - ".join(f"({category} : {quantity})" for category, quantity in stock.items())
    return ""
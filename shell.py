import basic


#Read input From Terminal Window
while True:
    text = input('basic > ')
    result, error = basic.run('<stdin>',text)

    if error: print(error.as_string())
    else: print(result)
 
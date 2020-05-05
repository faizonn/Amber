import basic


#Read input From Terminal Window
while True:
    text = input('basic > ')
    result, error = basic.run(text)

    if error: print(error.as_string())
    else: print(result)
 
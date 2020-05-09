import Amber

#Read input From Terminal Window
while True:
    text = input('Amber > ')
    result, error = Amber.run('<stdin>',text)

    if error: print(error.as_string())
    else: print(result)

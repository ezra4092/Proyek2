def double_letter (str):
    result = ''
    for letter in str:
        result += letter * 2
    return result


def secret_function (a, b):
    if isinstance(a, int) and isinstance(b, int):
        return double_letter(str(a) + str(b))
    elif isinstance(a, str) and isinstance(b, str):
        return double_letter(a) + double_letter(b)
    else:
        return "Input tidak valid"


print(double_letter("Hello"))
print(secret_function(1, 2))
print(secret_function("Hello, ", "world!"))

# openai.api_key = "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"


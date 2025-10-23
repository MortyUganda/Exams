is_num = lambda x: (
    x.replace(".", "").replace("-", "").isdigit()
    and x.count(".") <= 1
    and x.count("-") <= 1
    and "-" not in x[1:]
)

print(is_num("1-1"))
print(is_num(".0.95"))
print(is_num("-10.0."))
print(is_num("-34.67"))
print(is_num("987"))
print(is_num("abcd"))
print(is_num("123.122.12"))
print(is_num("-123.122"))
print(is_num("1132555"))

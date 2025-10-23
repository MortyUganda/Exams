with open(r'c:\Users\Sergei\Downloads\MOCK_DATA.csv', encoding='utf8', newline='') as file:
    unpack_file = (line for line in file.readlines())
    without_delimeters_flie = (line.strip().split(',') for line in unpack_file)
    headers = list(next(without_delimeters_flie))
    dct_file = (dict(zip(headers, line)) for line in without_delimeters_flie)
    result = ((line['first_name'], line['ip_address']) for line in dct_file if '.com' in line['email'])

    for index, (name, ip) in enumerate(set(result), 1):
        print(f'{index}) {name} ------> {ip}')
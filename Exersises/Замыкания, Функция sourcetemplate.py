def sourcetemplate(url):
    def f(**kwargs):
        if kwargs:
            res = [f'{k}={v}' for k, v in sorted(kwargs.items())]
            return url + '?' + '&'.join(res)
        return url
    return f

url = 'https://all_for_comfort_life.com'
load = sourcetemplate(url)
print(load(smartphone='iPhone', notebook='huawei', sale=True))
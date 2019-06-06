def from_key(d1,val = None):
    if type(d1) == dict:
        keys = list(d1.keys())
        print(keys)
        result = {}
        if (type(val) == list or type(val) == tuple):
            length_value = len(val)
            length_keys = len(keys)
            i = 0
            while i < length_keys:
                print(keys[i])
                if i < length_value:
                    result[keys[i]] = val[i]
                else:
                    result[keys[i]] = None
                i += 1
        else:
            for x in keys:
                result[x] = val
        return result



def main():
    d1 = {"Name": "NM", "Surname": "MM", "Age": 35}

    # val = [18"Nimesh","Momaya"]
    val = 13,45,"NNNMMM","AAABBCC"
    print(type(val))

    result = from_key(d1,val)
    print(result)


if __name__ == '__main__':
    main()



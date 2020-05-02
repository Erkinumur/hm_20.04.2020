def funnyString(s):
    ordlist_s = [ord(i) for i in s]
    ordlist_reverse_s = ordlist_s[::-1]
    def ord_differences(ord_list):
        result = []
        for i in range(len(ord_list) - 1):
            result.append(abs(ord_list[i] - ord_list[i + 1]))
        return result
    if ord_differences(ordlist_s) == ord_differences(ordlist_reverse_s):
        return 'Funny'
    else:
        return 'Not Funny' 
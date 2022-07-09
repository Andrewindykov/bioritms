import math
def two2_max(arr):
    try:
        m1 = m2 = arr[0]
    except IndexError:
        return None
    for num in arr:
        if num > m1:
            m1, m2 = num, m1
        elif num > m2 or m2==m1:
            m2 = num
    return m2 if m2<m1 else None

def two_max(a):
    max1 = max2 = -math.inf
    for x in a:
        if x == max1:
            continue
        elif x > max1:
            max2, max1 = max1,x
        elif x > max2:
            max2 = x
    return max2 if max2 > -math.inf else None

def test_two_max():
    result = two_max([3, 2, -10, 2, 100, 45])
    assert result == 45, f'Wrong answer: {result}'
    result = two_max([2, 2, 1])
    assert result == 1, f'Wrong answer: {result}'
    result = two_max([1])
    assert result == None, f'Wrong answer: {result}'
    result = two_max([])
    assert result == None, f'Wrong answer: {result}'
    print('Все тесты пройдены')

if __name__ == '__main__':
    test_two_max()
    print(f'all ok. end program ')


def solution(n, m, x, y, r, c, k):
    answer = ''
    count_x = x - r
    count_y = y - c

    for i in range(k):

        if count_x == 0 and count_y == 0:
            if i % 2 == 0:
                answer += 'r'
            else:
                answer += 'l'

        if count_x != 0 and count_x < 0:
            answer += 'd'
            count_x += 1
        else:
            answer += 'u'
            count_x -= 1

        if count_y != 0 and count_y > 0:
            answer += 'l'
            count_y += 1
        else:
            answer += 'r'
            count_y -= 1


if (abs(x - r)) + (abs(y - c)) > k or (abs(x - r)) + (abs(y - c)) + 1 == k:
    answer = 'impossible'


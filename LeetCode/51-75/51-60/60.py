class Solution1:
    # решение в тупую
    # создаем permutation, генерируем все перестановки, сортируем и находим нужную
    def getPermutation(self, n: int, k: int) -> str:
        mass = [i for i in range(1, n + 1)]

        def permutation(n, res = None):
            if res == None:
                res = []
            if n == len(mass):

                res.append(mass[:])
                return
            for i in range(n, len(mass)):
                mass[n], mass[i] = mass[i], mass[n]
                permutation(n + 1, res)
                mass[n], mass[i] = mass[i], mass[n]

            return res

        mass_perm = permutation(0)
        mass_perm.sort()
        res = mass_perm[k - 1]
        return ''.join(map(str, res))

def factorial(n):
    if n == 0: return 1
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

class Solution2:
    #умное решение
    #основывается на пошаговой перестановке с высших разрядов
    #пояснение:
    '''
    пусть (1234) - 1 первый разряд, 2 второй ...

    у нас строка "1234"
    и нам надо 7 перестановку
    выпишем их:
    1234 1243 1324 1342 1423 1432 2134

    седьмая перестановка 2134, заметим, что первые 6 перестановок происходят с числами правее первого разряда
    и это соответствует факториалу количества чисел справа
    изначально у нас сразу дана первая перестановка, 1234, далее будем вычитать ее, таким образом, чтобы получить 7
    перестановку, нам надо поменять местами первый и второй разряд
    k -= 1 изначально, k = 6 стало, k -= 6 k = 0 - выходим

    погодите, скоро все проясниться

    number - количество чисел, которые должны быть справа от разяда который мы будем переставлять
    пусть number - 1 = x - определяет разряд, который мы будем переставлять (с конца), то есть будем брать наш массив по индексу
    mass[-number - 1] - берем с конца, так как number будет говорить факториал какого числа мы будем вычитать из k, то есть
    сколько перестановок можно сделать с числами справа от него

    теперь рассмотрим 8 перестановку тоже при n = 4, она будет 2143
    для этого мы ищем максимальную перестановку, а это при факториале равном 6, при 24 будет слишком много
    k = 1 станет, при этом number будет равным 3, а будем мы менять 1 разряд так как справа от 1 разряда 3 числа,
    перестановок которых будет 6, поэтому мы берем mass[-number - 1] = mass[-4] или mass[0], то есть как раз тот разряд, что нам
    нужно.
    и нам осталось сделать перестановку при факториале равном 1, поэтому number = 1 , мы будем менять 2 разряд с конца,
    меняем с последним разрядом и все получилось, получили 2143

    при чем еще count, покажу на примере
    1234, что если нам надо получить перестановку 3124?
    нам надо менять единицу не с соседом, а дальше, а как определить с кем?
    легко, это будет 13 перестановка (3124) k -= 1 k = 12
    при number = 4 fac(number) = 24, много, поэтому number = 3
    f теперь посчитаем сколько раз мы можем вычесть fac(3) из k и это определяет с каким числом по порядку
    надо менять переставляемый разряд, в нашем случае count = 2 и это говорит, что нужно от разряда -number - 1
    взять разряд на 2 правее

    единственная проблема, что когда появился count у нас после перестановки где count != 1 числа после
    переставляемого разряда перестают быть в порядке возрастания, что ломает алгоритм, поэтому отсортируем в этих случаях
    массив

    все!


    '''
    def getPermutation(self, n: int, k: int) -> str:
        mass = [i for i in range(1, n + 1)]

        if k == 1: return ''.join(map(str, mass))
        k -= 1

        while True:
            number = 1
            while k - factorial(number) >= 0:
                number += 1

            count = 1

            while k - factorial(number - 1) * (count + 1) >= 0:
                count += 1

            mass[-number], mass[-number + count] = mass[-number + count], mass[-number]
            if count != 1: mass = mass[:-number + 1] + sorted(mass[-number + 1:])

            k -= factorial(number - 1) * count

            if k <= 0:
                return ''.join(map(str, mass))

flag = 0
instance1 = Solution1()
instance2 = Solution2()
for i in range(1, 8):
    for j in range(1, factorial(i) + 1):
        n, k = i, j
        res1 = instance1.getPermutation(n, k)
        res2 = instance2.getPermutation(n, k)
        if res1 != res2:
            flag = 1
            print(res1, res2, n, k)
            break
    if flag:
        break

print('end')


class Solution3:
    def getPermutation(self, n: int, k: int) -> str:
        ans = ""
        fact = 1
        numbers = []
        for i in range(1, n):
            fact *= i
            numbers.append(i)
        numbers.append(n)
        k -= 1
        while True:
            ans += str(numbers[k // fact])
            numbers.pop(k // fact)
            if len(numbers) == 0: break
            k %= fact
            fact //= len(numbers)
        return ans

instance3 = Solution3()
res = instance3.getPermutation(4, 5)
print(res)


﻿Ниже написано решение, которое я не хотел писать :__( Там ничего интересного. На запрос добавить смотрим вправо влево, если есть там такие же, то увеличиваем
счетик у той пары, если нет, то добавляем. Соответвсевнноо добавление O(n), поиск O(n).Все плохо
go - ищет куда добавлять новый елемент в списке сжатых елементов.

Решение, которое я хотел написать к этому дедлайну, но возникли трудности (не смог сходу написать трип по неявному ключу на питоне). Решение,
которое, надеюсь появится, хоть когда-то в моем репозитории. В общем все то же самое, только для хорошей жизни будем иметь трип по неявному ключику.
Соответвсвенно запросы добавить делаются простыми опреациями сплита и мержа. Итератор тогда можно будет реализовывать двумя способами. Честное O(n), где
n - количесвто отрезков сжатых елементов(сжатый елемент - елемент вида (value, cnt)). Ну или за nlogn, просто каддый раз запрашивать его место в трипе.
В первом случаее нужно будет хранить на предка, но вроде лишнее поле в классе элемента дерева нам завести можно и все будет круто.

для реализации go, нам понадобится в вершине дерева хранить сумму по всем b в левом, в себе, и во всем поддерве.
Пока на проверку test и RLElist


Плюс еще добавим следующую модификацию. Мы будем хранить экземляр каждого объекта только 1 раз. Вроде если данные огромные, то это спасает нашу память.

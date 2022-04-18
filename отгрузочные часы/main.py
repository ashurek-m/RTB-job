import step_1 as s1
import step_2 as s2
import step_3 as s3
import step_4 as s4


if __name__ in '__main__':
    print('1 - формирование адресов расчетных файлов запущенных в производство')
    path_1 = s1.file_search(name='new_general_address_file2022(xls).csv',
                            way='W:\\Theoretical Planning\\02 - Бланки заказов (All foto cmd)\\**\\*xls')
    print('2 - добавления номера заказа к адресу и отсеивание архивных файлов')
    path_2 = s1.search_by_client(path_1[0], 2022)
    print('3 - определения размера расчетных файлов по столбцам')
    path_3 = s2.list_shape_fyn(path_2)
    print('4 - печать на экран списка с размером')
    shape_list = s2.analysis(path_3)
    print(len(shape_list))
    # shape_list отсортирован по возростанию
    b = int(input('b = '))
    if b == 0:
        print('5 - группировка и сохранение одинаковых по количеству столбцов расчетных файлов')
        name_list_shape = []
        for number in shape_list:
            name_file = s2.shape_(path_3, number)
            name_list_shape.append(name_file)
        print(name_list_shape)
        print('6 - удаление лишних столбцов, приведение расчетных файлов к одной размерности, формирование документа.\n'
              'Для продолжение работы введите 1.')
        a = input('a = ')
        if a == '1':
            path_4 = s3.union(shape_list, name_list_shape, 'union_file_2022.csv')
        print('7 - трансформация файла для внесения в акссес')
        s4.transformation_pay(path_4, 'full_union_file_06_04_2022.csv', 2022)
    elif b == 1:
        print(3)

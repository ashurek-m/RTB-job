import step_1 as s1
import step_2 as s2
import step_3 as s3


if __name__ in '__main__':
    print('1')
    path_1 = s1.file_search()
    print('2')
    path_2 = s1.search_by_client(path_1[0], 2021)
    print('3')
    path_3 = s2.list_shape_fyn(path_2)
    print('4')
    shape_list = s2.analysis(path_3)
    # shape_list отсортирован по возростанию
    print('5')
    name_list_shape = []
    for number in shape_list:
        name_file = s2.shape_(path_3, number)
        name_list_shape.append(name_file)
    print('6')
    s3.union(shape_list, name_list_shape, 'union_file_05_05_2021.xlsx')

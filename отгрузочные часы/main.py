import step_1 as s1
import step_2 as s2


if __name__ in '__main__':
    print('1')
    path_1 = s1.file_search()
    print('2')
    path_2 = s1.search_by_client(path_1[0], 2021)
    print('3')
    s2.list_shape_fyn(path_2)

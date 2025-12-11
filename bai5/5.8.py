def Sequential_Search(dlist, item):
    """
    Thực hiện tìm kiếm tuyến tính trên danh sách dlist cho phần tử item.
    Trả về một tuple (found, index_or_none):
    - found (bool): True nếu tìm thấy, False nếu không.
    - index_or_none (int/None): Chỉ mục của phần tử nếu tìm thấy, ngược lại là None.
    """
    pos = 0
    found = False
    list_length = len(dlist)

    while pos < list_length and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos = pos + 1

    if found:
        return (True, pos)
    else:
        # Nếu không tìm thấy, pos sẽ bằng list_length
        return (False, None)

# Ví dụ gợi ý:
# print(Sequential_Search([11,23,58,31,56,77,43,12,65,19],31))

class IlocList(list):
    _iloc_list_value = [[]]


    def __init__(self, two_dimensions_list):
        self._iloc_list_value = two_dimensions_list


    def __getitem__(self, _tuple):
        try:
            return self._iloc_list_value[_tuple[0]][_tuple[1]]
        except IndexError:
            return ''



class PureDataFrame:
    """ pandas.DataFrame Equivalent: has no dependancy on pandas, numpy packages
    """
    shape = (-1, -1)
    _value = [[]]


    def __init__(self, two_dimensions_list):
        self._value = two_dimensions_list
        self.iloc = IlocList(self._value)

        i = len(self._value)
        j = -1
        for _line in self._value:
            if len(_line) > j:
                j = len(_line)
        self.shape = (i, j)


    def to_excel(self, writer, sheet_name='sheet1', index=False, header=False):
        raise Exception('No to_excel function')
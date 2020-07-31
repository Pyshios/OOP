'''Simple adiea is i can reverse all string input'''


class rev_t():

    def __init__(self, given):
        self.given = given


    def do_list(self): # it will simple do a list of the given string

        m_list = list(self.given)
        return m_list

    def inv_it(self): # get the list reverse it and than print
        self.final_lst = self.do_list()
        self.final_lst.reverse()
        print(self.final_lst)


ab = rev_t('myword')

ab.do_list()
ab.inv_it()
class CountError(Exception):
    def __init__(self, mes):
        self.mes = mes


class Group:
    def __init__(self, group: list):
        self.group = group
        count = 0
        for item in self.group:
            count += 1
            if count > 10:
                raise CountError('only 10 students can be in one group')

    def add_student(self, value):
        self.group.append(value)

    def remove_student(self, value):
        self.group.remove(value)

    def student_search(self, surname):
        res = []
        for stud in self.group:
            if stud.surname == surname:
                res.append(stud)
        return res or None

    def __str__(self):
        group_tmp = "\n".join(map(str, self.group))
        return f'{group_tmp}\n'

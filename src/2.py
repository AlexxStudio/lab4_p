class Respondent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return (self.age, self.name) > (other.age, other.name)

class AgeGroup:
    def __init__(self, name, min_age, max_age):
        self.name = name
        self.min_age = min_age
        self.max_age = max_age
        self.respondents = []

    def add_respondent(self, respondent):
        self.respondents.append(respondent)

    def __str__(self):
        respondents_info = ', '.join(f"{respondent.name}" for respondent in sorted(self.respondents))
        return f"{self.name}: {respondents_info}"

class AgeGroupsManager:
    def __init__(self, borders):
        self.groups = [AgeGroup(f"{borders[i - 1] + 1}-{borders[i]}", borders[i - 1] + 1, borders[i]) for i in range(len(borders) - 1, 0, -1)]
        self.groups.append(AgeGroup(f"0-{borders[0]}", 0, borders[0]))
        self.groups.append(AgeGroup(f"{borders[-1] + 1}+", borders[-1] + 1, float('inf')))

    def add_respondent(self, respondent):
        for group in self.groups:
            if group.min_age <= respondent.age <= group.max_age:
                group.add_respondent(respondent)
                break

    def get_age_groups_info(self):
        sorted_groups = sorted(self.groups, key=lambda x: x.min_age, reverse=True)
        return [str(group) for group in sorted_groups if group.respondents]

    def read_respondents_from_file(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip() == "END":
                    break
                else:
                    name, age = line.strip().split(',')
                    respondent = Respondent(name, int(age))
                    self.add_respondent(respondent)

if __name__ == "__main__":
    input_file_path = "input.txt"
    age_borders = list(map(int, input('Введите возрастные границы:').split()))
    age_groups_manager = AgeGroupsManager(age_borders)
    age_groups_manager.read_respondents_from_file(input_file_path)
    age_groups_info = age_groups_manager.get_age_groups_info()
    for group_info in age_groups_info:
        print(group_info)
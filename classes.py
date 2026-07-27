class Classes:
    @classmethod
    def from_dict(cls, data):
        classes = cls()
        classes.classes_list = data.get("classes_list", [])
        return classes

    def __init__(self):
        self.classes_list = []

    def add_class(self, class_name):
        self.classes_list.append(class_name)

    def remove_class(self, class_name):
        if class_name in self.classes_list:
            self.classes_list.remove(class_name)
        else:
            print(f"Class {class_name} not found.")
        
    def to_dict(self):
        return {
            "classes_list": self.classes_list
        }
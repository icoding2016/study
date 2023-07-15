"""

Nothing stops a caller to call a static
"""

class C():
    cls_var = "I'm a class variable."

    def instance_method(self):
        print(f"access class variable in instance: {C.cls_var}")

    @classmethod
    def class_method(cls):
        print(f"access class variable in classmethod: {cls.cls_var}")

    @staticmethod
    def class_method(a: str=""):
        print(f"access class variable in class staticmethod: {C.cls_var}")
        if a:
            print(f"input arg in class_method: {a}")

def external_method():
    print(f"access class variable from external method: {C.cls_var}")



def test():
    c = C()
    c.instance_method()
    c.class_method('input arg')
    external_method()

    C.cls_var = "Changed from external"
    print(f"C class variable changed by external func, now: {c.class_method()}")


test()

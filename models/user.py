"""
    user modules
"""
from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        """
        print the instance
        :return:
        """
        return ("[{}] ({}) {})".format(
            __class__.__name__,
            self.id,
            self.__dict__))

    def to_dict(self):
        """
            convert  self dict and other public instance
                Return: Dictionary
        """
        dic = dict(self.__dict__)
        dic['__class__'] = self.__class__.__name__
        dic['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dic['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        """
        dic["email"] = User.email
        """
        return dic

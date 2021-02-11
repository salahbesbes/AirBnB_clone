import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        since __object is private class attribute
        we access it like so
        :return:
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        we add the object to the __objects attribute
        the key is generated as <obj class name>.id
        :obj : can have multi type class
        :return: None
        """
        # att of that obj/instance
        dict_attrs = obj.to_dict()
        # generate some thing like "BaseModel.135489484231"
        new_key = "{}.{}".format(dict_attrs["__class__"], dict_attrs["id"])
        # in the class att we append that obj
        FileStorage.__objects[new_key] = obj
        # print("from new", FileStorage.__objects)

    @staticmethod
    def to_json_string(ordinary_dict):
        """ static method that transform dict to str format json
        :param ordinary_dict:
        :return: str
        """
        if ordinary_dict is None:
            return json.dumps({})
        return json.dumps(ordinary_dict, indent=2)

    def save(self):
        """
            each object/instance in the private class att __objects
            we serialise the instance (by creating a newDict of key and dict of attrs)
            then write the newDict to the file.json
        """
        dict_objs = FileStorage.__objects
        with open(FileStorage.__file_path, mode="w") as file:
            if dict_objs is None:
                dict_objs = {}
            # newJson : { BaseModel.123456 : {'id' : 123456, 'name': "holberton"} ..........}
            newJson = {key: instance.to_dict() for key, instance in dict_objs.items()}
            file.write(self.to_json_string(newJson))

    def reload(self):
        """
        read from the file, deserialize the dict obtained from the file
        each val from the dict is a dict of args and kwargs of an instance
        each key found represent an instance we check if it exit else we create new one
        and append if to the __objects
        :return: None
        """
        try:
            with open(FileStorage.__file_path, mode="r") as file:
                content = file.read()
                dict_from_file = json.loads(content)  # type = dict

                for file_key, dict_obj in dict_from_file.items():
                    # if the key_file is not in the storage.keys()
                    # we want to create a new instance and pass it argument and kwargs
                    if file_key not in FileStorage.__objects.keys():
                        newInst = BaseModel(**dict_obj)
                        self.new(newInst)
                    # if the key_file already exist in the __object we dnt want to do any thing
        except FileNotFoundError:
            pass

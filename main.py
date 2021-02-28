#!/usr/bin/python3
"""
    modules
"""
import models
from uuid import uuid4, UUID
import shlex

storage = models.storage
BaseModel = models.BaseModel
User = models.User
Review = models.Review
Place = models.Place

if __name__ == "__main__":
    # test = "User.update(\"38f22813-2753-4d42-b37c-57a17f1e4f88\",
    # {'first_name': \"John\", \"age\": 89})"

    def evallll():
        print(isinstance(5, float))
        # test = "Place.update(\"b32b3561-42cd-41de-8145-31291616edfd\",
        # {\"amenity_ids\": [\"id_1\", \"555\"],\"description\": 55,
        # \'number_bathrooms\': 55.6, \"latitude\": 82,\"max_guest\": 2.22})"

        test = "Place.update(\"b32b3561-42cd-41de-8145-31291616edfd\", name)"
        test = shlex.split(test, comments=True)
        test = " update Place \"12345678\" name [\"salahbesbes\", \"salahbesbes\"]  548912389d  dqds"
        test = test.split(maxsplit=4)
        print(test)


    evallll()

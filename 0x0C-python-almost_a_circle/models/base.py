#!/usr/bin/python3
"""This module defines a class"""
import json
import csv
import turtle


class Base:
    """Representing a class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing a base class
        Args:
            id: initialized to none
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method that returns the json string
            representation of list_dictionary
        """

        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """This method writes the JSON string representation
            of lists_objs to a file
        """

        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                json_string = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(json_string))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""

        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""

        filename = "{}.json".format(str(cls.__name__))
        try:
            with open(filename, "r") as f:
                json_string = f.read()
                list_objs = cls.from_json_string(json_string)
            return [cls.create(**obj_dict) for obj_dict in list_objs]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializing in csv"""

        filename = "{}.csv".format(cls.__name__)
        with open(filename, "w", newline="") as csv_file:
            if list_objs is None or list_objs == []:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)
                for obj in list_objs:
                    csv_writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializing in csv"""

        filename = "{}.csv".format(cls.__name__)
        list_dicts = []
        try:
            with open(filename, "r", newline="") as csv_file:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                csv_reader = csv.DictReader(csv_file, fieldnames=field_names)
                for row in csv_reader:
                    row_dicts = {key: int(val) for key, val in row.items()}
                    list_dicts.append(row_dicts)
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """This method opens a window and draws all the Rectangles and Squares"""

        turtl = turtle.Turtle()
        turtl.screen.bgcolor("#fff")
        turtl.pensize(2)
        turtl.shape("turtle")
        
        turtl.color("orange")
        for r in list_rectangles:
            turtl.showturtle()
            turtl.up()
            turtl.goto(r.x, r.y)
            turtl.down()
            for i  in range(2):
                turtl.fd(r.width)
                turtl.rt(90)
                turtl.fd(r.height)
                turtl.lt(90)
            turtl.ht()

        turtl.exitonclick

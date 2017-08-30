# -*- coding: utf-8 -*-
from peewee import *


db = SqliteDatabase('web.db')

GENDER_VALUES = (
    ('Boy', '男生'),
    ('Girl', '女生')
)

GRADE_CODES = (
    (1, '一年级'),
    (2, '二年级'),
    (3, '三年级'),
    (4, '四年级'),
    (5, '五年级')
)
    

class Student(Model):

    name = CharField(max_length=45)
    gender = CharField(choices=GENDER_VALUES, max_length=4)
    teacher = CharField(max_length=45)
    grade = IntegerField(choices=GRADE_CODES)

    class Meta:
        database = db
        indexes = (
            (('name', 'grade'), True),
        )

    def grade_display(self):
        return unicode(dict(GRADE_CODES)[self.grade])

    def gender_display(self):
        return unicode(dict(GENDER_VALUES)[self.gender])

    def __str__(self):
        return self.name


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        if sys.argv[1] == 'syncdb':
            db.connect()
            db.create_tables([Student,])


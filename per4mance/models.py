from typing import Any

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base: Any = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = sa.Column(sa.INT, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String(30))
    company = sa.Column(sa.String(30), default="")
    account = sa.Column(sa.String(200), unique=True)
    password = sa.Column(sa.String(200))
    email_address = sa.Column(sa.String(200), default="")
    is_evaluator = sa.Column(sa.BOOLEAN, default=False)
    created_at = sa.Column(sa.TIMESTAMP(timezone=True))


class Group(Base):
    __tablename__ = "group"

    id = sa.Column(sa.INT, primary_key=True, autoincrement=True)
    course = sa.Column(sa.Integer, sa.ForeignKey("course.id"))
    member = sa.orm.relationship("GroupXUser")
    name = sa.Column(sa.String(50))
    size = sa.Column(sa.INT)
    created_at = sa.Column(sa.TIMESTAMP(timezone=True))
    updated_at = sa.Column(sa.TIMESTAMP(timezone=True))


class GroupXUser(Base):
    __tablename__ = "groupxuser"
    id = sa.Column(sa.INT, primary_key=True, autoincrement=True)
    group = sa.Column(sa.INT, sa.ForeignKey("group.id"))
    member = sa.Column(sa.INT, sa.ForeignKey("user.id"))

    __table_args__ = (sa.UniqueConstraint("group", "member", name="groupxuser_unique"),)


class Course(Base):
    __tablename__ = "course"

    id = sa.Column(sa.INT, primary_key=True, autoincrement=True)
    evaluator = sa.Column(sa.INT, sa.ForeignKey("user.id"))
    students = sa.orm.relationship("CourseXStudent")
    name = sa.Column(sa.String(50))
    start_term = sa.Column(sa.TIMESTAMP(timezone=True))
    end_term = sa.Column(sa.TIMESTAMP(timezone=True))
    description = sa.Column(sa.TEXT)
    survey_count = sa.Column(sa.Integer)
    scale_factor = sa.Column(sa.FLOAT)
    created_at = sa.Column(sa.TIMESTAMP(timezone=True))
    updated_at = sa.Column(sa.TIMESTAMP(timezone=True))

    __table_args__ = (sa.UniqueConstraint("evaluator", "name", name="course_unique"),)


class CourseXStudent(Base):
    __tablename__ = "coursexstudent"

    id = sa.Column(sa.INT, primary_key=True, autoincrement=True)
    course = sa.Column(sa.INT, sa.ForeignKey("course.id"))
    student = sa.Column(sa.INT, sa.ForeignKey("user.id"))

    __table_args__ = (
        sa.UniqueConstraint("course", "student", name="coursexstudent_unique"),
    )


class Survey(Base):
    __tablename__ = "survey"

    id = sa.Column(sa.INT, primary_key=True, autoincrement=True)
    course = sa.Column(sa.INT, sa.ForeignKey("course.id"))
    completeness = sa.Column(sa.FLOAT)
    name = sa.Column(sa.String(50))
    start_term = sa.Column(sa.TIMESTAMP(timezone=True))
    end_term = sa.Column(sa.TIMESTAMP(timezone=True))
    class_notes = sa.Column(sa.TEXT)
    created_at = sa.Column(sa.TIMESTAMP(timezone=True))
    updated_at = sa.Column(sa.TIMESTAMP(timezone=True))


class GroupSurveyReport(Base):
    __tablename__ = "group_survey_report"

    id = sa.Column(sa.INT, primary_key=True, autoincrement=True)
    survey = sa.Column(sa.INT, sa.ForeignKey("survey.id"))
    group = sa.Column(sa.INT, sa.ForeignKey("group.id"))
    completeness = sa.Column(sa.FLOAT)
    name = sa.Column(sa.String(50))
    team_mark = sa.Column(sa.FLOAT)
    created_at = sa.Column(sa.TIMESTAMP(timezone=True))
    updated_at = sa.Column(sa.TIMESTAMP(timezone=True))


class IndividualScore(Base):
    __tablename__ = "individual_score"

    id = sa.Column(sa.INT, primary_key=True, autoincrement=True)
    group_survey_report = sa.Column(sa.INT, sa.ForeignKey("group_survey_report.id"))
    owner = sa.Column(sa.INT, sa.ForeignKey("user.id"))

    score_qlt_individual = sa.Column(sa.FLOAT)
    score_qnt_individual = sa.Column(sa.FLOAT)
    score_qlt_team = sa.Column(sa.FLOAT)
    score_qnt_team = sa.Column(sa.FLOAT)

    score_ability = sa.Column(sa.FLOAT)
    score_effort = sa.Column(sa.FLOAT)
    score_significant = sa.Column(sa.FLOAT)
    score_attitude = sa.Column(sa.FLOAT)
    iwf = sa.Column(sa.FLOAT)

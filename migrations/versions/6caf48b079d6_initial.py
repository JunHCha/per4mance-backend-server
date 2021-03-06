"""initial

Revision ID: 6caf48b079d6
Revises: 
Create Date: 2021-12-13 14:34:09.349369

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "6caf48b079d6"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=30), nullable=True),
        sa.Column("company", sa.String(length=30), nullable=True),
        sa.Column("account", sa.String(length=200), nullable=True),
        sa.Column("password", sa.String(length=200), nullable=True),
        sa.Column("email_address", sa.String(length=200), nullable=True),
        sa.Column("is_evaluator", sa.BOOLEAN(), nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("account"),
    )
    op.create_table(
        "course",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("evaluator", sa.INTEGER(), nullable=True),
        sa.Column("name", sa.String(length=50), nullable=True),
        sa.Column("start_term", sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column("end_term", sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column("description", sa.TEXT(), nullable=True),
        sa.Column("survey_count", sa.Integer(), nullable=True),
        sa.Column("scale_factor", sa.FLOAT(), nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["evaluator"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("evaluator", "name", name="course_unique"),
    )
    op.create_table(
        "coursexstudent",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("course", sa.INTEGER(), nullable=True),
        sa.Column("student", sa.INTEGER(), nullable=True),
        sa.ForeignKeyConstraint(
            ["course"],
            ["course.id"],
        ),
        sa.ForeignKeyConstraint(
            ["student"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("course", "student", name="coursexstudent_unique"),
    )
    op.create_table(
        "group",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("course", sa.Integer(), nullable=True),
        sa.Column("name", sa.String(length=50), nullable=True),
        sa.Column("size", sa.INTEGER(), nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["course"],
            ["course.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "survey",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("course", sa.INTEGER(), nullable=True),
        sa.Column("completeness", sa.FLOAT(), nullable=True),
        sa.Column("name", sa.String(length=50), nullable=True),
        sa.Column("start_term", sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column("end_term", sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column("class_notes", sa.TEXT(), nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["course"],
            ["course.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "group_survey_report",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("survey", sa.INTEGER(), nullable=True),
        sa.Column("group", sa.INTEGER(), nullable=True),
        sa.Column("completeness", sa.FLOAT(), nullable=True),
        sa.Column("name", sa.String(length=50), nullable=True),
        sa.Column("team_mark", sa.FLOAT(), nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["group"],
            ["group.id"],
        ),
        sa.ForeignKeyConstraint(
            ["survey"],
            ["survey.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "groupxuser",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("group", sa.INTEGER(), nullable=True),
        sa.Column("member", sa.INTEGER(), nullable=True),
        sa.ForeignKeyConstraint(
            ["group"],
            ["group.id"],
        ),
        sa.ForeignKeyConstraint(
            ["member"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("group", "member", name="groupxuser_unique"),
    )
    op.create_table(
        "individual_score",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("group_survey_report", sa.INTEGER(), nullable=True),
        sa.Column("owner", sa.INTEGER(), nullable=True),
        sa.Column("score_qlt_individual", sa.FLOAT(), nullable=True),
        sa.Column("score_qnt_individual", sa.FLOAT(), nullable=True),
        sa.Column("score_qlt_team", sa.FLOAT(), nullable=True),
        sa.Column("score_qnt_team", sa.FLOAT(), nullable=True),
        sa.Column("score_ability", sa.FLOAT(), nullable=True),
        sa.Column("score_effort", sa.FLOAT(), nullable=True),
        sa.Column("score_significant", sa.FLOAT(), nullable=True),
        sa.Column("score_attitude", sa.FLOAT(), nullable=True),
        sa.Column("iwf", sa.FLOAT(), nullable=True),
        sa.ForeignKeyConstraint(
            ["group_survey_report"],
            ["group_survey_report.id"],
        ),
        sa.ForeignKeyConstraint(
            ["owner"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("individual_score")
    op.drop_table("groupxuser")
    op.drop_table("group_survey_report")
    op.drop_table("survey")
    op.drop_table("group")
    op.drop_table("coursexstudent")
    op.drop_table("course")
    op.drop_table("user")
    # ### end Alembic commands ###

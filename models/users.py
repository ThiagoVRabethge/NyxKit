from sqlmodel import Field, SQLModel


class Users(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str = Field(sa_column_kwargs={"unique": True})
    password: str

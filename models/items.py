from sqlmodel import Field, SQLModel


class Items(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str
    example: str
    testes: str

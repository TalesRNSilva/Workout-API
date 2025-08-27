from pydantic import Field, PositiveFloat
from contrib.schemas import BaseSchema
from typing import Annotated

class AtletaIn(BaseSchema):
    nome: Annotated[str, Field(description = 'Nome do atleta', example = 'João', max_length = 50)]
    cpf: Annotated[str, Field(description = 'CPF do atleta', example = '43332921827', max_length = 11)]
    idade: Annotated[int, Field(description = 'Idade do atleta', example = 11)]
    peso: Annotated[PositiveFloat, Field(description = 'Peso do atleta', example = 75.5)]
    altura: Annotated[PositiveFloat, Field(description = 'Altura do atleta', example = 1.75)]
    sexo: Annotated[str, Field(description = 'Sexo do atleta', example = 'M', max_length = 1)]


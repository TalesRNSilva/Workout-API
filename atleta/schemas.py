from pydantic import Field, PositiveFloat
from contrib.schemas import BaseSchema
from typing import Annotated

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description = 'Nome do atleta', example = 'João', max_length = 50)]
    cpf: Annotated[str, Field(description = 'CPF do atleta', example = '43332921827', max_length = 11)]
    idade: Annotated[int, Field(description = 'Idade do atleta', example = 11)]
    peso: Annotated[PositiveFloat, Field(description = 'Peso do atleta', example = 75.5)]
    altura: Annotated[PositiveFloat, Field(description = 'Altura do atleta', example = 1.75)]
    sexo: Annotated[str, Field(description = 'Sexo do atleta', example = 'M', max_length = 1)]


arguments = {'nome' : 'Tales', 'cpf': '12345678910', 'idade': 28, 'peso': 85.2, 'altura':1.80, 'sexo':'M'}
tales = Atleta(**arguments)
print(tales.model_dump_json())
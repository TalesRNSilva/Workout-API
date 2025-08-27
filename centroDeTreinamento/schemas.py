from typing import Annotated

from pydantic import Field
from contrib.schemas import BaseSchema

class CentroDeTreinamento(BaseSchema):
    nome: Annotated[str, Field(description = 'Nome do CT', example = 'Mané Garrincha', max_length = 20)]
    endereco: Annotated[str, Field(description = 'Endereço do CT', example = 'R. Amparo, 155', max_length = 60)]
    proprietario: Annotated[str, Field(description = 'Nome do proprietário do CT', example = 'Eike Batista', max_length = 30)]
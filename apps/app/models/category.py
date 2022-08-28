from typing import Optional, List
from pydantic import BaseModel
import datetime


class CategoryGroup(BaseModel):
    id: int
    title: str
    code: str

class Category(BaseModel):
    id: int
    title: str
    group: Optional[CategoryGroup]


class ContractPoint(BaseModel):
    url: str
    faxNumber: str
    telephone: str
    name: str
    email: str

class Identifier(BaseModel):
    scheme: str
    id: str
    legalName: str

class Address(BaseModel):
    countryName: str
    postalCode: str
    region: str
    streetAddress: str
    locality: str

class ProcuringEntity(BaseModel):
    kind: str
    name: str
    contactPoint: ContractPoint
    identifier: Identifier
    address: Address

class Classification(BaseModel):
    scheme: str
    description: str
    id: str

class Images(BaseModel):
    url: str
    sizes: str

class CategoryNew(BaseModel):
    id: int
    title: str
    status: str
    classification: Classification
    procuringEntity: ProcuringEntity
    images: List[Images]
    dateModified: datetime.datetime
    id: str

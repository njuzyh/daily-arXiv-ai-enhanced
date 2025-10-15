from pydantic import BaseModel, Field, field_validator
import re

class Structure(BaseModel):
    tldr: str = Field(description="generate a too long; didn't read summary")
    motivation: str = Field(description="describe the motivation in this paper")
    challenges: str = Field(description="describe the challenges in this paper")
    contributions: str = Field(description="list the main contributions of this paper")
    results: str = Field(description="describe the results of this paper")
    conclusion: str = Field(description="describe the conclusion of this paper")
    related_work: str = Field(description="list the most related work in this paper")
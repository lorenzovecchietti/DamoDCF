from typing import Literal

from pydantic import BaseModel


class FailureData(BaseModel):
    failure_probability: float
    proceeds_portion: float
    proceeds_value: Literal["book", "fair"]

    def compute_failure(self, pv=None, book_value=None, book_debt=None):
        if self.proceeds_value == "book":
            return (book_value + book_debt) * self.proceeds_portion
        else:
            return pv * self.proceeds_portion

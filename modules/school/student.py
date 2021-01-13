from dataclasses import dataclass, field
from typing import List, Iterable
from school.parent import parent

@dataclass
class student:
    first_name: str
    last_name: str
    parents: List[parent] = field(default_factory=list)

    def add_parent(self, parent):
        self.parents.append(parent)

    def add_parents(self, parents: Iterable[parent]):
        self.parents.extend(parents)


    @property
    def primary_parent(self):
        return self, parents[0]


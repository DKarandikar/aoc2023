import functools
from dataclasses import dataclass


@dataclass
class Part:
    x: int
    m: int
    a: int
    s: int

    @staticmethod
    def from_str(s: str) -> 'Part':
        without_brackets = s[1:-1]
        parts = without_brackets.split(",")
        ints = [int(x.split("=")[1]) for x in parts]
        return Part(ints[0], ints[1], ints[2], ints[3])

    def val_sum(self) -> int:
        return self.a + self.s + self.m + self.x


@dataclass
class Rule:
    ev: str | None
    output: str

    @staticmethod
    def from_str(s: str) -> 'Rule':
        parts = s.split(":")
        if len(parts) == 1:
            return Rule(None, parts[0])
        return Rule(parts[0], parts[1])

    def run_part(self, part: Part) -> str | None:
        if self.ev is None:
            return self.output

        if '<' in self.ev:
            less_than = True
            val = int(self.ev.split('<')[1])
        else:
            less_than = False
            val = int(self.ev.split('>')[1])

        if self.ev[0] == 'a':
            attribute = part.a
        elif self.ev[0] == 'x':
            attribute = part.x
        elif self.ev[0] == 's':
            attribute = part.s
        else:
            attribute = part.m

        if less_than and attribute < val:
            return self.output
        elif not less_than and attribute > val:
            return self.output


@dataclass
class Workflow:
    label: str
    rules: list[Rule]

    @staticmethod
    def from_str(s: str) -> 'Workflow':
        parts = s[:-1].split("{")
        label = parts[0]
        rules = [Rule.from_str(x) for x in parts[1].split(",")]
        return Workflow(label, rules)

    def run_part(self, part: Part) -> str:
        for rule in self.rules:
            output = rule.run_part(part)
            if output is not None:
                return output
        raise RuntimeError("Failed to pass part through workflow")


@dataclass
class PartSorter:
    parts: list[Part]
    workflows: list[Workflow]

    @functools.cached_property
    def workflow_map(self):
        rv = {}
        for workflow in self.workflows:
            rv[workflow.label] = workflow
        return rv

    @staticmethod
    def from_str(s: str) -> 'PartSorter':
        s_parts = s.split("\n\n")
        parts = [Part.from_str(x) for x in s_parts[1].split('\n')]
        workflows = [Workflow.from_str(x) for x in s_parts[0].split('\n')]

        return PartSorter(parts, workflows)

    def run_part(self, part: Part) -> bool:
        initial_workflow = self.workflow_map['in']
        output = initial_workflow.run_part(part)
        while output not in ('A', 'R'):
            output = self.workflow_map[output].run_part(part)
        return output == 'A'

    def accepted_part_sum(self) -> int:
        rv = 0
        for part in self.parts:
            if self.run_part(part):
                rv += part.val_sum()

        return rv


def main():
    with open("../data/day19.txt") as f:
        lines = f.read()

    print(f"Day 19 part 1 is: {PartSorter.from_str(lines).accepted_part_sum()}")


if __name__ == "__main__":
    main()

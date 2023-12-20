import functools
from dataclasses import dataclass


@dataclass
class Range:
    start: int
    length: int


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
class PartRange:
    x: Range
    m: Range
    a: Range
    s: Range

    def product(self) -> int:
        return self.x.length * self.m.length * self.a.length * self.s.length

    def set(self, char: str, r: Range) -> 'PartRange':
        return PartRange(**{'x': self.x, 'm': self.m, 'a': self.a, 's': self.s, char: r})


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

    def run_part_range(self, part_range: PartRange) -> tuple[dict[str, PartRange], PartRange | None]:
        if self.ev is None:
            return {self.output: part_range}, None

        if '<' in self.ev:
            less_than = True
            val = int(self.ev.split('<')[1])
        else:
            less_than = False
            val = int(self.ev.split('>')[1])

        char = self.ev[0]
        if char == 'a':
            attribute = part_range.a
        elif char == 'x':
            attribute = part_range.x
        elif char == 's':
            attribute = part_range.s
        else:
            attribute = part_range.m

        if less_than:
            if val < attribute.start:
                return {}, part_range
            if val >= attribute.start + attribute.length:
                return {self.output: [part_range]}, None
            difference = val - attribute.start
            remainder = attribute.length - difference

            return ({self.output: part_range.set(char, Range(attribute.start, difference))},
                    part_range.set(char, Range(attribute.start + difference, remainder)))

        else:
            if val > attribute.start + attribute.length:
                return {}, part_range
            if val <= attribute.start:
                return {self.output: [part_range]}, None
            difference = 1 + val - attribute.start
            remainder = attribute.length - difference

            return ({self.output: part_range.set(char, Range(attribute.start + difference, remainder))},
                    part_range.set(char, Range(attribute.start, difference)))


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

    def run_ranges(self, part_ranges: list[PartRange]) -> dict[str, list[PartRange]]:
        rv = {}
        for part_range in part_ranges:
            remainder = part_range
            for rule in self.rules:
                res, remainder = rule.run_part_range(remainder)
                for k, v in res.items():
                    entry = rv.setdefault(k, [])
                    entry.append(v)
                if remainder is None:
                    break
        return rv


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

    def distinct_combo(self) -> int:
        initialRange = PartRange(Range(1, 4000), Range(1, 4000), Range(1, 4000), Range(1, 4000))
        output = {"in": [initialRange]}
        while set(output.keys()) != {"A", "R"}:
            keys = filter(lambda x: x not in ('A', 'R'), list(output.keys()))
            next_key = list(keys)[0]
            next_list = output.pop(next_key)
            res = self.workflow_map[next_key].run_ranges(next_list)
            for k, v in res.items():
                entry = output.setdefault(k, [])
                entry.extend(v)

        return sum([x.product() for x in output['A']])


def main():
    with open("../data/day19.txt") as f:
        lines = f.read()

    print(f"Day 19 part 1 is: {PartSorter.from_str(lines).accepted_part_sum()}")
    print(f"Day 19 part 2 is: {PartSorter.from_str(lines).distinct_combo()}")


if __name__ == "__main__":
    main()

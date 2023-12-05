from dataclasses import dataclass


@dataclass
class Range:
    start: int
    length: int


def collapse_ranges(ranges: list[Range]) -> list[Range]:
    result = []
    sorted_ranges = sorted(ranges, key=lambda x: x.start)
    current = sorted_ranges[0]
    for r in sorted_ranges[1:]:
        if current.start + current.length == r.start:
            current = Range(current.start, current.length + r.length)
        else:
            result.append(current)
            current = r
    result.append(current)

    return result


@dataclass
class Mapping:
    source: int
    dest: int
    length: int

    def is_in_range(self, num: int) -> bool:
        return self.source <= num < self.source + self.length

    def map(self, num: int) -> int:
        return self.dest + (num - self.source)


@dataclass
class Map:
    from_: str
    to_: str
    mappings: list[Mapping]

    def map(self, num: int) -> int:
        for mapping in self.mappings:
            if mapping.is_in_range(num):
                return mapping.map(num)
        return num

    def map_range(self, r: Range) -> list[Range]:
        s = sorted(self.mappings, key=lambda x: x.source)
        remaining = r.length
        current = r.start
        res = []

        for mapping in s:
            if mapping.source + mapping.length < current:
                continue

            if mapping.source > current:
                new_range = Range(current, mapping.source - current)
                current = mapping.source
                remaining = remaining - new_range.length
                res.append(new_range)

            if mapping.length > remaining:
                new_start = mapping.map(current)
                res.append(Range(new_start, remaining))
                return collapse_ranges(res)
            else:
                new_start = mapping.map(current)
                current = mapping.source + mapping.length
                remaining = remaining - mapping.length
                res.append(Range(new_start, mapping.length))

        res.append(Range(current, remaining))
        return collapse_ranges(res)


@dataclass
class Input:
    seeds: list[int]
    maps: list[Map]

    def seed_ranges(self) -> list[Range]:
        rv = []
        for i in range(0, len(self.seeds), 2):
            rv.append(Range(self.seeds[i], self.seeds[i+1]))
        return rv

    def process_type(self, num: int, type_: str) -> None | tuple[int, str]:
        """ Try to map (num, type_) using the maps we have, else return None """
        for map in self.maps:
            if type_ == map.from_:
                return map.map(num), map.to_
        return None

    def process_type_range(self, rs: list[Range], type_: str) -> None | tuple[list[Range], str]:
        """ Try to map (num, type_) using the maps we have, else return None """
        for map in self.maps:
            if type_ == map.from_:
                ranges = []
                for r in rs:
                    ranges.extend(map.map_range(r))
                return collapse_ranges(ranges), map.to_
        return None

    def process(self) -> list[dict]:
        """ Return seed maps, e.g. {seed: 1, soil: 10, ...}"""
        rv = []
        for seed in self.seeds:
            seed_dict = {"seed": seed}
            res = self.process_type(seed, "seed")
            while res is not None:
                seed_dict[res[1]] = res[0]
                res = self.process_type(res[0], res[1])
            rv.append(seed_dict)
        return rv

    def process_ranges(self) -> list[dict]:
        """ Return seed range maps, e.g. {seed: [Range(1, 10), soil: [Range(20, 5), Range(47, 5)], ...}"""
        rv = []
        for seed_range in self.seed_ranges():
            seed_dict = {"seed": [seed_range]}
            res = self.process_type_range([seed_range], "seed")
            while res is not None:
                seed_dict[res[1]] = res[0]
                res = self.process_type_range(res[0], res[1])
            rv.append(seed_dict)
        return rv

    def min_location(self) -> int:
        seed_results = self.process()
        locs = [x.get("location") for x in seed_results]
        return min(locs)

    def min_location_ranges(self) -> int:
        seed_results = self.process_ranges()
        locs = [collapse_ranges(x.get("location")) for x in seed_results]
        return min([x[0].start for x in locs])

    @staticmethod
    def from_str(lines: str) -> 'Input':
        maps = []
        current: None | Map = None

        for line in lines.split("\n"):
            if "seeds" in line:
                seeds = [int(x) for x in line.split("seeds: ")[1].split(" ")]
                continue
            if line == "":
                continue
            if "map" in line:
                if current is not None:
                    maps.append(current)
                mapping_name = line.split(" ")[0].split("-to-")
                current = Map(mapping_name[0], mapping_name[1], [])
            else:
                parts = line.split(" ")
                current.mappings.append(Mapping(int(parts[1]), int(parts[0]), int(parts[2])))
        if current is not None:
            maps.append(current)

        return Input(seeds, maps)


def main():
    with open("../data/day5.txt") as f:
        lines = f.read()

    print(f"Day 5 part 1 is: {Input.from_str(lines).min_location()}")
    print(f"Day 5 part 2 is: {Input.from_str(lines).min_location_ranges()}")


if __name__ == "__main__":
    main()

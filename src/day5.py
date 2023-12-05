from dataclasses import dataclass


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


@dataclass
class Input:
    seeds: list[int]
    maps: list[Map]

    def process_type(self, num: int, type_: str) -> None | tuple[int, str]:
        """ Try to map (num, type_) using the maps we have, else return None """
        for map in self.maps:
            if type_ == map.from_:
                return map.map(num), map.to_
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

    def min_location(self) -> int:
        seed_results = self.process()
        locs = [x.get("location") for x in seed_results]
        return min(locs)

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


if __name__ == "__main__":
    main()

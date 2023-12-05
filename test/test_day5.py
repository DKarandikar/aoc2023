from src.day5 import Mapping, Input, Range, collapse_ranges

test_input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


def test_collapse_ranges():
    assert collapse_ranges([Range(45, 5), Range(52, 48), Range(50, 2), Range(100, 45)]) == [Range(45, 100)]
    assert collapse_ranges([Range(45, 5), Range(100, 45)]) == [Range(45, 5), Range(100, 45)]
    assert collapse_ranges([Range(45, 5), Range(52, 48), Range(100, 45)]) == [Range(45, 5), Range(52, 93)]


def test_map_range():
    inp = Input.from_str(test_input)

    assert inp.maps[0].map_range(Range(45, 20)) == [Range(45, 5), Range(52, 15)]

    assert inp.maps[0].map_range(Range(45, 100)) == [Range(45, 100)]


def test_parse_input():
    inp = Input.from_str(test_input)

    assert inp.seeds == [79, 14, 55, 13]
    assert len(inp.maps) == 7


def test_mapping():
    mapping = Mapping(12, 50, 7)

    assert not mapping.is_in_range(8)
    assert mapping.is_in_range(15)

    assert mapping.map(15) == 53


def test_seed_map():
    inp = Input.from_str(test_input)
    map = inp.maps[0]

    assert map.map(51) == 53
    assert map.map(53) == 55
    assert map.map(49) == 49


def test_process_input():
    inp = Input.from_str(test_input)

    assert inp.min_location() == 35


def test_seed_ranges():
    inp = Input.from_str(test_input)

    assert inp.seed_ranges() == [Range(79, 14), Range(55, 13)]


def test_process_input_ranges():
    inp = Input.from_str(test_input)

    assert inp.min_location_ranges() == 46

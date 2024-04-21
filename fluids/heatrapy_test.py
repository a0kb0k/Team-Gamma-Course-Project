import heatrapy as htp

example = htp.SingleObject2D(
    293,
    material='Cu',
    boundaries=(300, 0, 0, 0),
    size=(20, 20)
)
example.change_material(
    material='Al',
    shape='square',
    initial_point=(5, 2),
    length=(4, 4)
)
example.change_material(
    material='water',
    shape='circle',
    initial_point=(5, 13),
    length=4
)
example.compute(100, 10)

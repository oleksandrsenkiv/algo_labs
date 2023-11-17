
import unittest
from main import find_way_to_transport_gas


class TestFindPeakSequences(unittest.TestCase):
    def test_all_vertex_root(self):
        cities = ['Lviv', 'Stryi', 'Dolina', 'Ternopil', 'Dubno', 'Chortkiv']
        gas_storages = ['Warehouse_1', 'Warehouse_2']

        pipelines = [
            ['Lviv', 'Stryi'],
            ['Dolina', 'Lviv'],
            ['Warehouse_1', 'Lviv'],
            ['Warehouse_2', 'Lviv'],
            ['Warehouse_2', 'Ternopil'],
            ['Ternopil', 'Dubno'],
            ['Chortkiv', 'Ternopil']
        ]
        result = find_way_to_transport_gas(cities, gas_storages, pipelines)
        expected = [['Warehouse_1', ['Dolina', 'Ternopil', 'Dubno', 'Chortkiv']], ['Warehouse_2', ['Dolina', 'Chortkiv']]]
        self.assertEqual(result, expected)

    def test_no_root(self):
        cities = ['Lviv', 'Stryi', 'Ternopil', 'Dubno']
        warehouses = ['Warehouse_1', 'Warehouse_2']

        pipelines = [
            ['Lviv', 'Stryi'],
            ['Warehouse_1', 'Lviv'],
            ['Warehouse_2', 'Lviv'],
            ['Warehouse_2', 'Ternopil'],
            ['Ternopil', 'Dubno'],
            ['Warehouse_1', 'Ternopil']
        ]
        result = find_way_to_transport_gas(cities, warehouses, pipelines)
        expected = []
        self.assertEqual(result, expected)

    def test_all_vertex_roo(self):
        cities = ['Lviv', 'Stryi', 'Dolina', 'Ternopil', 'Dubno', 'Chortkiv']
        warehouses = ['Warehouse_1', 'Warehouse_2']

        pipelines = [
            ['Lviv', 'Stryi'],
            ['Dolina', 'Lviv'],
            ['Ternopil', 'Dubno'],
            ['Chortkiv', 'Ternopil']
        ]
        result = find_way_to_transport_gas(cities, warehouses, pipelines)
        expected = [['Warehouse_1', ['Lviv', 'Stryi', 'Dolina', 'Ternopil', 'Dubno', 'Chortkiv']],
                    ['Warehouse_2', ['Lviv', 'Stryi', 'Dolina', 'Ternopil', 'Dubno', 'Chortkiv']]]
        self.assertEqual(result, expected)


import unittest
from main import calculate_energy_financials


class TestEnergyFinancials(unittest.TestCase):

    def test_empty_devices_list(self):
        result = calculate_energy_financials([])
        self.assertEqual(result, (0.0, 0.0, 0.0))

    def test_financials_with_discount(self):
        devices = [
            {
                "id": "M01",
                "old_index": 0,
                "new_index": 60000,
                "status": "Normal"
            }
        ]

        total_kwh, discount, total_money = (
            calculate_energy_financials(devices)
        )

        self.assertEqual(total_kwh, 60000)
        self.assertEqual(discount, 3.0)

        expected = 60000 * 3000 * 0.97
        self.assertEqual(total_money, expected)

    def test_financials_no_discount(self):
        devices = [
            {
                "id": "M01",
                "old_index": 0,
                "new_index": 10000,
                "status": "Normal"
            }
        ]

        total_kwh, discount, total_money = (
            calculate_energy_financials(devices)
        )

        self.assertEqual(total_kwh, 10000)
        self.assertEqual(discount, 0.0)

        expected = 10000 * 3000
        self.assertEqual(total_money, expected)


if __name__ == "__main__":
    unittest.main()
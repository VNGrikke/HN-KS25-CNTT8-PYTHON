import unittest

from pos_logic import (
    calculate_total, 
    process_add_to_order, 
    InvalidQuantityError, 
    ItemNotFoundError
)

class TestHighlandsPOS(unittest.TestCase):

    def test_calculate_total(self):
        """Kiểm tra logic tính tổng tiền với giỏ hàng giả (mock data)."""
        mock_order = [
            {"code": "P1", "name": "Phin Sữa Đá", "price": 35000, "quantity": 2},
            {"code": "F1", "name": "Freeze Trà Xanh", "price": 55000, "quantity": 1}
        ]
        # Tổng mong đợi: (35000 * 2) + (55000 * 1) = 125000
        result = calculate_total(mock_order)
        self.assertEqual(result, 125000)

    def test_invalid_quantity(self):
        """Kiểm tra hàm xử lý có ném ra InvalidQuantityError khi số lượng <= 0 không."""
        # Test số lượng âm
        with self.assertRaises(InvalidQuantityError):
            process_add_to_order("T1", -1)
            
        # Test số lượng bằng 0
        with self.assertRaises(InvalidQuantityError):
            process_add_to_order("T1", 0)

    def test_item_not_found(self):
        """Kiểm tra hàm xử lý có ném ra ItemNotFoundError khi mã món không đúng."""
        with self.assertRaises(ItemNotFoundError):
            process_add_to_order("A1", 2)

if __name__ == "__main__":
    unittest.main()
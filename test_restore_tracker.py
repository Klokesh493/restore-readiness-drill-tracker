import unittest

from restore_tracker import failures


class RestoreTrackerTest(unittest.TestCase):
    def test_flags_rto_miss(self):
        rows = [{"workload": "archive", "restore_minutes": "180", "rto_minutes": "120", "data_loss_minutes": "10", "rpo_minutes": "30"}]
        self.assertEqual(failures(rows), ["archive"])


if __name__ == "__main__":
    unittest.main()

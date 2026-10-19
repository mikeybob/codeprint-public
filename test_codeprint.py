import importlib.util
import pathlib
import unittest
from importlib.machinery import SourceFileLoader

path = pathlib.Path(__file__).with_name("codeprint")
loader = SourceFileLoader("codeprint", str(path))
spec = importlib.util.spec_from_loader("codeprint", loader)
codeprint = importlib.util.module_from_spec(spec)
loader.exec_module(codeprint)


class CenterTest(unittest.TestCase):
    def test_ink_is_in_the_middle_of_the_80mm_image(self) -> None:
        for code in ("123456", "1234567", "12345678"):
            x0, y0, x1, y1 = codeprint.ink_box(code)
            cx = (x0 + x1) / 2
            cy = (y0 + y1) / 2
            self.assertAlmostEqual(cx, (codeprint.WIDTH - 1) / 2, delta=8)
            self.assertAlmostEqual(cy, (codeprint.HEIGHT - 1) / 2, delta=2)
            self.assertGreater(y0, 250)
            self.assertLess(y1, codeprint.HEIGHT - 250)

    def test_ticket_is_80mm_and_uses_raster(self) -> None:
        data = codeprint.build("12345678")
        self.assertIn(b"\x1dv0\x00", data)
        self.assertEqual(data[-3:], b"\x1dV\x01")
        self.assertEqual(len(codeprint.render("12345678")), (codeprint.WIDTH // 8) * codeprint.HEIGHT)
        self.assertEqual(codeprint.HEIGHT, 640)


if __name__ == "__main__":
    unittest.main()

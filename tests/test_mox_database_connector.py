import mox
import os

class TestOs(mox.MoxTestBase):
    def test_getcwd(self):
        self.mox.StubOutWithMock(os, 'getcwd')

        os.getcwd().AndReturn('/mox/path')

        self.mox.replay_all()
        assert os.getcwd() == '/mox/path'
        self.mox.verify_all()


if __name__ == '__main__':
    import unittest
    unittest.main()
import unittest
from abc import ABC, ABCMeta

from app import create_app
from app.algoritmos.algoritmos import fatorial


class TestFatorial(unittest.TestCase):
    def test_fatorial(self):
        self.assertEqual(fatorial(0), 1)
        self.assertEqual(fatorial(1), 1)
        self.assertEqual(fatorial(2), 2)
        self.assertEqual(fatorial(3), 6)
        self.assertEqual(fatorial(4), 24)
        self.assertEqual(fatorial(5), 120)
        self.assertEqual(fatorial(6), 720)


class TestBase(ABC):
    __metaclass__ = ABCMeta

    class Meta:
        abstract = True

    def setUp(self) -> None:
        self.app = create_app().test_client()
        self.response = self.app.get(f'/{self.user}/')
        self.response_str = self.response.data.decode('utf-8')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_content_type(self):
        self.assertIn('text/html', self.response.content_type)

    def test_content(self):
        raise NotImplementedError('Deve ser implementado!')

    def test_bootstrap_css(self):
        self.assertIn('bootstrap.min.css', self.response_str)

    def test_profile_img(self):
        self.assertIn('<img src="', self.response_str)
        self.assertIn('class="img-circle"', self.response_str)

    def test_link(self):
        raise NotImplementedError('Deve ser implementado!')


class TestPedro(TestBase, unittest.TestCase):

    def __init__(self, *args, **kwargs):
        self.user = 'pedro'
        super(TestPedro, self).__init__(*args, **kwargs)

    def test_content(self):
        self.assertIn(f'Pedro Sousa', self.response_str)
        self.assertIn('<title>Pedro Sousa - Home</title>', self.response_str)
        self.assertIn('<h1>Pedro Sousa</h1>', self.response_str)
        self.assertIn('<p>Desenvolvedor', self.response_str)

    def test_link(self):
        self.assertIn('href="https://twitter.com/ppls2106"', self.response_str)
        self.assertIn('>Me siga no Twitter</a>', self.response_str)


class TestCuducos(TestBase, unittest.TestCase):

    def __init__(self, *args, **kwargs):
        self.user = 'cuducos'
        super(TestCuducos, self).__init__(*args, **kwargs)

    def test_content(self):
        self.assertIn(f'Eduardo Cuducos', self.response_str)
        self.assertIn('<title>Eduardo Cuducos - Home</title>', self.response_str)
        self.assertIn('<h1>Eduardo Cuducos</h1>', self.response_str)
        self.assertIn('<p>Sociólogo', self.response_str)

    def test_link(self):
        self.assertIn('href="https://twitter.com/cuducos"', self.response_str)
        self.assertIn('>Me siga no Twitter</a>', self.response_str)


if __name__ == '__main__':
    unittest.main()

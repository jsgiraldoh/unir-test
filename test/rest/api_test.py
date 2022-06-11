import http.client
import os
import unittest
from urllib.error import HTTPError
from urllib.request import urlopen

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_add_err(self):
        self.assert_bad_request(f"{BASE_URL}/calc/add/nan/2")
    
    
    def test_api_substract(self):
        url = f"{BASE_URL}/calc/substract/3/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_substract_err(self):
        self.assert_bad_request(f"{BASE_URL}/calc/substract/3/nan")
    
    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/3/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_multiply_err(self):
        self.assert_bad_request(f"{BASE_URL}/calc/multiply/nan/2")
    
    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/3/1"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_divide_err(self):
        self.assert_bad_request(f"{BASE_URL}/calc/multiply/nan/2")

    def test_api_divide_err_zero(self):
        self.assert_bad_request(f"{BASE_URL}/calc/divide/3/0")

    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/3/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_power_err(self):
        self.assert_bad_request(f"{BASE_URL}/calc/power/3/nan")
    
    def test_api_square_root(self):
        url = f"{BASE_URL}/calc/square-root/9"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_square_root_err(self):
        self.assert_bad_request(f"{BASE_URL}/calc/square-root/nan")
    
    def test_api_square_root_err_negative(self):
        self.assert_bad_request(f"{BASE_URL}/calc/square-root/-23")

    def test_api_common_logarithm(self):
        url = f"{BASE_URL}/calc/common-logarithm/10"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_common_logarithm_err(self):
        self.assert_bad_request(f"{BASE_URL}/calc/common-logarithm/nan")
    
    def test_api_common_logarithm_err_negative(self):
        self.assert_bad_request(f"{BASE_URL}/calc/common-logarithm/-10")

    def assert_bad_request(self, url: str):
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertTrue(False)
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST, f"API {url} respondió correctamente")

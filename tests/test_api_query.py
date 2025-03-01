import pytest

import cats
from cats.CI_api_interface import API_interfaces, InvalidLocationError
from cats.forecast import CarbonIntensityPointEstimate

def test_api_call():
    """
    This just checks the API call runs and returns a list of tuples
    """

    api_interface = API_interfaces["carbonintensity.org.uk"]
    response = cats.CI_api_query.get_CI_forecast('OX1', api_interface)

    assert isinstance(response, list)
    for item in response:
        assert isinstance(item, CarbonIntensityPointEstimate)

def test_bad_postcode():
    api_interface = API_interfaces["carbonintensity.org.uk"]

    with pytest.raises(InvalidLocationError):
        response = cats.CI_api_query.get_CI_forecast('OX48', api_interface)

    with pytest.raises(InvalidLocationError):
        response = cats.CI_api_query.get_CI_forecast('A', api_interface)

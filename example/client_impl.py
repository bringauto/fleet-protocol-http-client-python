from fleet_http_client_python import CarApi, DeviceApi, ApiClient, Configuration, Car, Message


class ClientExample:
    """Example of Client of the Fleet Protocol HTTP API."""

    def __init__(self, host: str, api_key: str) -> None:
        """Create a new ClientExample.

        `host`: The host of the Fleet Protocol HTTP API.
        `api`: The API key to authenticate the client.
        """
        self._configuration = Configuration(host=host, api_key={"AdminAuth": api_key})
        self._api_client = ApiClient(self._configuration)
        self._car_api = CarApi(api_client=self._api_client)
        self._device_api = DeviceApi(api_client=self._api_client)

    def get_statuses_for_all_connected_cars(self) -> dict[str, dict[str, Message]]:
        available_cars = self._get_connected_cars()
        statuses: dict[str, dict[str, Message]] = dict()
        for car in available_cars:
            if not car.company_name in statuses:
                statuses[car.company_name] = dict()
            statuses[car.company_name][car.car_name] = self._device_api.list_statuses(
                car.company_name, car.car_name
            )
        return statuses

    def _get_connected_cars(self) -> list[Car]:
        return self._car_api.available_cars(wait=False)

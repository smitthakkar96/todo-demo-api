from tests.base import FlaskRestfulTestCase


class RootTestCase(FlaskRestfulTestCase):

    def test_api_root(self):
        """
        Ensure that API root returns OK response code
        and that todos endpoint is listed under available
        CRUD endpoints list.
        """
        response = self.app.get('/')
        assert(response.status_code == 200)
        assert('Available CRUD endpoints' in response.data)
        assert('todos' in response.data)

import falcon
from config.logger import logger
from api.resources.users import UsersResource
from api.resources.user import UserResource

logger.info("Started!")

app = falcon.API()

app.add_route('/users', UsersResource())
app.add_route('/user/{_id}', UserResource())
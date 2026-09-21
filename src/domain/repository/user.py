from sqlalchemy.ext.asyncio import AsyncSession


class UserRepository():

    def __int__(self, session: AsyncSession):
        self.session = session


    def create(self, ):


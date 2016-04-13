



class serviceBase(object):

    #__metaclass__ = SingletonByConn

    '''
    def __init__(self, session):
        self._session = session
    '''
    def __init__(self,  session_factory, debug=False):
        '''
         must send in either a session_factory #TODO  or a connection, exclusive or
        '''

        # if connection is  None:
        self._session_factory = session_factory
        # else:
        #     self._session_factory = SessionFactory(connection)

        self._session = self._session_factory.getSession()
        self._debug = debug
        #self._sessiona

    #self._session_factory=""
   # def getSessionFactory( session = None):
    def getSession(self):
        return self._session





from sqlalchemy.ext.declarative import declared_attr
class Base(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    __table_args__ = {u'schema': 'odm2'}

    def __init__(self, *args, **kwargs):
        for name, value in kwargs.items(): setattr(self, name, value)

from sqlalchemy.ext.declarative import declarative_base



class modelBase():

    Base = declarative_base(cls=Base)
    metadata = Base.metadata












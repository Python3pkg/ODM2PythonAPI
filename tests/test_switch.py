__author__ = 'stephanie'
import pytest

from odm2api.ODMconnection import dbconnection
#from odm2api.versionSwitcher import ODM, refreshDB

@pytest.mark.skipif(True,
                    reason="ODM1.1 shim is out of date")
class TestSwitch:

    def setup(self):
        session_factory = dbconnection.createConnection('mysql', 'localhost', 'odm2', 'ODM', 'odm')
        refreshDB(2.0)
        self.session = session_factory.getSession()

    def test_switch(self):
        s=self.session.query(ODM.Site).all()

        print type(ODM.Site)
        #print ODM.Series.get(self.session)
        print s


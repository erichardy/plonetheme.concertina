# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import plonetheme.concertina


class PlonethemeConcertinaLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=plonetheme.concertina)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plonetheme.concertina:default')


PLONETHEME_CONCERTINA_FIXTURE = PlonethemeConcertinaLayer()


PLONETHEME_CONCERTINA_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONETHEME_CONCERTINA_FIXTURE,),
    name='PlonethemeConcertinaLayer:IntegrationTesting'
)


PLONETHEME_CONCERTINA_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONETHEME_CONCERTINA_FIXTURE,),
    name='PlonethemeConcertinaLayer:FunctionalTesting'
)


PLONETHEME_CONCERTINA_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONETHEME_CONCERTINA_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PlonethemeConcertinaLayer:AcceptanceTesting'
)

# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plonetheme.concertina.testing import PLONETHEME_CONCERTINA_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that plonetheme.concertina is properly installed."""

    layer = PLONETHEME_CONCERTINA_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plonetheme.concertina is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'plonetheme.concertina'))

    def test_browserlayer(self):
        """Test that IPlonethemeConcertinaLayer is registered."""
        from plonetheme.concertina.interfaces import (
            IPlonethemeConcertinaLayer)
        from plone.browserlayer import utils
        self.assertIn(IPlonethemeConcertinaLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONETHEME_CONCERTINA_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['plonetheme.concertina'])

    def test_product_uninstalled(self):
        """Test if plonetheme.concertina is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'plonetheme.concertina'))

    def test_browserlayer_removed(self):
        """Test that IPlonethemeConcertinaLayer is removed."""
        from plonetheme.concertina.interfaces import \
            IPlonethemeConcertinaLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IPlonethemeConcertinaLayer,
            utils.registered_layers(),
        )

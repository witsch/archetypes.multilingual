# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4:
from plone.app.multilingual.interfaces import (
    ILanguage,
    LANGUAGE_INDEPENDENT,
)
from zope import interface
from plone.app.layout.navigation.root import getNavigationRootObject
from zope.component.hooks import getSite


class ATLanguage(object):

    interface.implements(ILanguage)

    def __init__(self, context):
        self.context = context

    def get_language(self):
        language = self.context.Language()
        if self.context.portal_factory.isTemporary(self.context):
            navroot = getNavigationRootObject(self.context, getSite())
            if navroot != self.context:
                language = ILanguage(navroot).get_language()
        if not language:
            language = LANGUAGE_INDEPENDENT
        return language

    def set_language(self, language):
        # Override the setLanguage method imposed by LP
        # and access to the direct mutator of the object
        self.context.getField('language').set(self.context, language)

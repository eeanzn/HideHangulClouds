# encoding: utf-8

###########################################################################################################
#
#   Hide Hangul Clouds
#
#   Glyphs 3 plugin to toggle the grey clouds overlay (Hangul Component Cloud)
#   that appears when editing component glyphs referenced by composites.
#
#   View → Hide Hangul Clouds
#
#   Copyright 2026 HyunJun Lee
#   Apache License 2.0
#
###########################################################################################################

from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import Glyphs, VIEW_MENU
from GlyphsApp.plugins import GeneralPlugin
from AppKit import NSMenuItem, NSOnState, NSOffState


class HideHangulClouds(GeneralPlugin):

	@objc.python_method
	def settings(self):
		self.name = "Hide Hangul Clouds"

	@objc.python_method
	def start(self):
		try:
			newMenuItem = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(
				self.name,
				self.toggleHangulClouds_,
				""
			)
			newMenuItem.setTarget_(self)
			Glyphs.menu[VIEW_MENU].append(newMenuItem)
			self.menuItem = newMenuItem
		except Exception as e:
			self.logToConsole("HideHangulClouds Error: %s" % str(e))

	def toggleHangulClouds_(self, sender):
		try:
			current = Glyphs.defaults["drawHangulComponentCloud"]
			Glyphs.defaults["drawHangulComponentCloud"] = not current
			Glyphs.redraw()
		except Exception as e:
			self.logToConsole("HideHangulClouds toggle error: %s" % str(e))

	def validateMenuItem_(self, menuItem):
		try:
			isDrawing = Glyphs.defaults["drawHangulComponentCloud"]
			menuItem.setState_(NSOffState if isDrawing else NSOnState)
		except Exception:
			pass
		return True

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged."""
		return __file__

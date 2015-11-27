#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sublime
import sublime_plugin
import re

class coffeelint(sublime_plugin.EventListener):
	def on_post_save(self, view):
		settings = sublime.load_settings("coffeelint.sublime-settings")
		if re.search( settings.get( "filename_filter" ), view.file_name() ):
			view.window().run_command( "build" )

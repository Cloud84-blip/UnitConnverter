#!/usr/bin/env python3
# Author : Cha
# The purpose of this script is to help with all differents Units that can be find
import sys
import tkinter as tk
from classFunctions import Functions as F

class WinClass:
	def __init__(self, _app, min_width, min_height):
		self.app = _app
		self.app.minsize(min_width, min_height)
		self.app.title('Convertisseur')
		
		self.f = F()
		
		self.function_list, self.current_choice = self.f.unwrap()
		
		self.cur_float= float(0.0)
		self.string_var, self.fst_entry_var, self.snd_entry_var = tk.StringVar(self.app), tk.StringVar(self.app, name="fst_str_var"), tk.StringVar(self.app, name="snd_str_var")
		self.fst_label, self.snd_label= tk.Label(self.app), tk.Label(self.app)
		self.fst_input_entry, self.snd_input_entry = tk.Entry(self.app), tk.Entry(self.app)
		self.mode_menu = tk.OptionMenu(self.app, self.string_var, *self.function_list)
		
		self.init_widgets()
		self.active_entry_calls = []
		self.call_ids = []
		
	def init_widgets(self):
		words = self.current_choice.split("<->")
		
		activate_func = self.app.register(self.activate_entry_call)
		
		self.fst_label.configure(text=words[0], width=10, relief="groove")
		self.snd_label.configure(text=words[1], width=10, relief="groove")
		self.fst_input_entry.configure(width=10, textvariable=self.fst_entry_var,
			validate="focusin", validatecommand=(activate_func, self.fst_entry_var))
		self.snd_input_entry.configure(width=10, textvariable=self.snd_entry_var,
			validate="focusin", validatecommand=(activate_func, self.snd_entry_var))
		self.string_var.set(self.current_choice)
		self.mode_menu.configure(width=15, height=10, fg='blue')
		
		self.fst_label.grid(row=1, column=0)
		self.snd_label.grid(row=1, column=3)
		self.fst_input_entry.grid(row=1, column=1)
		self.snd_input_entry.grid(row=1, column=2)
		self.mode_menu.grid(row=2, column=2)
		
		# by default dest is snd input
		self.current_src_pos = 0
		self.current_dest = self.snd_input_entry
		
		self.string_var.trace_add("write", self.option_callback)
		
	def activate_entry_call(self, entry_name):
		# activate The focused string var trace and prevent same time writing
		entry = self.get_entry_var(entry_name)
		try:
			# remove any active traces and clear lists
			self.del_entry_trace(self.active_entry_calls[0], "write", self.call_ids[0])
			self.active_entry_calls.clear()
			self.call_ids.clear()
		except IndexError:
			pass
		# activate or re-activate trace
		self.active_entry_calls.append(entry)
		call_id = entry.trace("w", self.entry_callback)
		self.call_ids.append(call_id)
		return True
	
	def del_entry_trace(self, entry_name, mode, entryCallId):
		entry=self.get_entry_var(entry_name)
		try:
			entry.trace_remove(mode, entryCallId)
		except:
			print("trace not removed correctly..")
		return
	
	def get_entry_var(self, entry_name):
		if (str(entry_name) == "fst_str_var"):
			return self.fst_entry_var
		return self.snd_entry_var
	
	
	def entry_callback(self, *args):
		print(args)
		try:
			self.cur_float = float(self.active_entry_calls[0].get())
		except ValueError:
			self.cur_float = float(0.0)
		if (args[0] == "fst_str_var"):
			# fst string var trace
			self.current_src_pos = 0
			self.current_dest = self.snd_input_entry
			cur_func = self.f.get_func(self.current_choice, self.current_src_pos)
			self.update_entry(self.current_dest, round(cur_func(self.cur_float), 2))
			return
		# snd string var trace
		self.current_src_pos = 1
		self.current_dest = self.fst_input_entry
		cur_func = self.f.get_func(self.current_choice, self.current_src_pos)
		self.update_entry(self.current_dest , round(cur_func(self.cur_float), 2))
		return
	
	def option_callback(self, *args):
		# menu trace
		self.current_choice = self.string_var.get()
		words = self.current_choice.split("<->")
		self.fst_label.configure(text=words[0])
		self.snd_label.configure(text=words[1])
		
		cur_func = self.f.get_func(self.current_choice, self.current_src_pos)
		self.update_entry(self.current_dest, round(cur_func(self.cur_float), 2))
	
	def update_entry(self, dest, value):
		dest.delete(0, "end")
		dest.insert(0, value)

if __name__ == '__main__':
	app = tk.Tk()
	start = WinClass(app, 500, 700)
	app.mainloop()
	
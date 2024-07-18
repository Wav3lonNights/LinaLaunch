import flet as ft
import minecraft_launcher_lib
import subprocess
import time

dropdown_options = []
for version in minecraft_launcher_lib.utils.get_version_list():
	dropdown_options.append(ft.dropdown.Option(version['id']))

def page(page: ft.Page):
	def start(e):
		if TextField.value=='':
			pass
		else:
			start_button.disabled = True
			start_button.text = 'Установка...'
			page.update()
			minecraft_launcher_lib.install.install_minecraft_version(versionid=dropdown.value, minecraft_directory='game/')
			start_button.text = 'Запуск...'
			page.update()
			if dropdown_gb.value=='1гб':
				Operative_gb = '1G'
			elif dropdown_gb.value=='2гб':
				Operative_gb = '2G'
			elif dropdown_gb.value=='4гб':
				Operative_gb = '4G'
			elif dropdown_gb.value=='6гб':
				Operative_gb = '6G'
			elif dropdown_gb.value=='8гб':
				Operative_gb = '8G'
			elif dropdown_gb.value=='16гб':
				Operative_gb = '16G'
			options = {
				'username': TextField.value,
				'uuid': '',
				'token': '',
				'jvmArguments': [f'-Xmx{Operative_gb}',f'-Xms{Operative_gb}']
			}
			start_button.text = 'Запущено!'
			page.update()
			subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version=dropdown.value, minecraft_directory='game/', options=options))
			start_button.text = 'Запустить'
			start_button.disabled = False
			page.update()
	page.window.width = 350
	page.window.height = 400
	page.window.resizable = False
	page.title = "LinaLaunch"
	page.vertical_alignment = ft.MainAxisAlignment.CENTER
	page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
	page.add(ft.Image(src="assets/logo.png"))
	dropdown = ft.Dropdown(options=dropdown_options,hint_text="Версия",value="1.16.5")
	page.add(dropdown)
	dropdown_gb = ft.Dropdown(
		options=[
			ft.dropdown.Option('1гб'),
			ft.dropdown.Option('2гб'),
			ft.dropdown.Option('4гб'),
			ft.dropdown.Option('6гб'),
			ft.dropdown.Option('8гб'),
			ft.dropdown.Option('16гб')
		],
			
		hint_text="Оперативная память",
		value="2гб")

	page.add(dropdown_gb)
	TextField = ft.TextField(hint_text="Никнейм(Например: Ponchik2024)")
	page.add(TextField)
	start_button = ft.ElevatedButton(text="Запустить", on_click=start)
	page.add(start_button)
	
	page.update()
ft.app(page)
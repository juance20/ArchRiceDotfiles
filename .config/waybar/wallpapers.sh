#!/bin/bash

selection=$1

result=$(echo $(swww query) | grep -o 'image: "[^"]*"')
result=${result#image: \"}
result=${result%\"}
current_wallpaper=${result%\"}

if [ "$selection" = "change" ]; then
	if [ "$current_wallpaper" = "wallpaper1.png" ]; then
		new_wallpaper="wallpaper2.png"
		swww img ~/Pictures/$new_wallpaper --transition-type center
	elif [ "$current_wallpaper" = "wallpaper2.png" ]; then
		new_wallpaper="wallpaper3.png"
		swww img ~/Pictures/$new_wallpaper --transition-type center
	elif [ "$current_wallpaper" = "wallpaper3.png" ]; then
		new_wallpaper="wallpaper4.png"
		swww img ~/Pictures/$new_wallpaper --transition-type center
	elif [ "$current_wallpaper" = "wallpaper4.png" ]; then
		new_wallpaper="wallpaper5.png"
		swww img ~/Pictures/$new_wallpaper --transition-type center
	elif [ "$current_wallpaper" = "wallpaper5.png" ]; then
		new_wallpaper="girl.gif"
		swww img ~/Pictures/$new_wallpaper --transition-type center
	elif [ "$current_wallpaper" = "girl.gif" ]; then
		new_wallpaper="wallpaper1.png"
		swww img ~/Pictures/$new_wallpaper --transition-type center
	else
		new_wallpaper="wallpaper1.png"
		swww img ~/Pictures/$new_wallpaper
	fi
fi

# coding: utf-8
import flet as ft

def navigate_with_transition(page: ft.Page, new_content):
    try:
        # 清理现有内容
        while len(page.controls) > 0:
            page.controls.pop()
        
        # 添加新内容
        page.controls.append(new_content)
        
        # 更新页面
        page.update()
    except Exception as ex:
        print(f"Navigation error: {ex}")
        # 如果发生错误，尝试重新加载页面
        try:
            page.window_destroy()
            page.window_center()
            page.update()
        except:
            pass
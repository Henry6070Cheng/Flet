# coding: utf-8
import flet as ft
from database.user_dal import UserDAL

def main(page: ft.Page):
    # 基本设置
    page.title = "登录"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 1200
    page.window_height = 800
    page.window_maximized = True
    page.padding = 0
    page.fonts = {
        "SimSun": "/fonts/simsun.ttc",
    }
    page.theme = ft.Theme(font_family="SimSun")
    
    # 创建用户名和密码输入框的引用
    username_field = ft.TextField(
        width=300,
        height=45,
        label="用户名",
        hint_text="请输入用户名",
        border_radius=8,
        prefix_icon=ft.icons.PERSON,
        focused_border_color=ft.colors.BLUE,
        border_color=ft.colors.GREY_400,
    )
    
    password_field = ft.TextField(
        width=300,
        height=45,
        label="密码",
        hint_text="请输入密码",
        border_radius=8,
        prefix_icon=ft.icons.LOCK,
        password=True,
        can_reveal_password=True,
        focused_border_color=ft.colors.BLUE,
        border_color=ft.colors.GREY_400,
    )

    # 错误提示文本
    error_text = ft.Text(
        color=ft.colors.RED_400,
        size=14,
        visible=False
    )
    
    def login(e):
        try:
            username = username_field.value
            password = password_field.value
            
            if not username or not password:
                error_text.value = "请输入用户名和密码"
                error_text.visible = True
                page.update()
                return
            
            # 验证用户名和密码
            if UserDAL.verify_password(username, password):
                from mainpage import mainpage
                page.clean()
                mainpage(page)
                page.update()
            else:
                error_text.value = "用户名或密码错误"
                error_text.visible = True
                page.update()
        except Exception as e:
            error_text.value = f"登录失败: {str(e)}"
            error_text.visible = True
            page.update()

    # 创建登录表单
    login_form = ft.Container(
        width=400,
        height=400,
        bgcolor=ft.colors.WHITE,
        border_radius=8,
        padding=30,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            controls=[
                ft.Text(
                    "登录",
                    size=30,
                    color=ft.colors.BLACK,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                ),
                username_field,
                password_field,
                error_text,
                ft.ElevatedButton(
                    content=ft.Text(
                        "登录",
                        size=16,
                        weight=ft.FontWeight.W_500,
                    ),
                    width=300,
                    height=45,
                    style=ft.ButtonStyle(
                        color=ft.colors.WHITE,
                        bgcolor=ft.colors.BLUE,
                        shape=ft.RoundedRectangleBorder(radius=8),
                    ),
                    on_click=login,
                ),
            ],
        ),
    )

    # 创建主容器
    main_container = ft.Container(
        width=page.window_width,
        height=page.window_height,
        bgcolor=ft.colors.GREY_100,
        alignment=ft.alignment.center,
        content=login_form,
    )

    page.add(main_container)
    page.update()

    # 设置页面背景色
    page.bgcolor = ft.colors.GREY_100

ft.app(main)

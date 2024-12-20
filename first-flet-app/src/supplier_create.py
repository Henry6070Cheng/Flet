# coding: utf-8
import flet as ft
from components.sidebar import create_sidebar
from components.breadcrumb import create_breadcrumb
from utils import navigate_with_transition

def supplier_create(page: ft.Page, return_content=False):
    page.title = "新建供应商"
    page.window_maximized = True
    page.padding = 0
    
    def return_to_supplier_list(e):
        from supplier_list import supplier_list
        new_content = supplier_list(page, return_content=True)
        navigate_with_transition(page, new_content)

    def return_to_main(e):
        from mainpage import mainpage
        new_content = mainpage(page, return_content=True)
        navigate_with_transition(page, new_content)

    # 使用通用侧边栏
    sidebar = create_sidebar(page, "suppliers")

    # 创建面包屑区域
    breadcrumb_area = ft.Container(
        content=ft.Row(
            [
                create_breadcrumb(page, [
                    {"text": "首页", "on_click": return_to_main},
                    {"text": "供应商管理", "on_click": return_to_supplier_list},
                    {"text": "新建供应商"},
                ]),
            ],
        ),
        padding=ft.padding.only(left=20, right=20, top=16, bottom=16),
        bgcolor=ft.Colors.WHITE,
        border=ft.border.only(bottom=ft.BorderSide(1, ft.Colors.GREY_200)),
    )

    # 创建主内容区
    content_area = ft.Container(
        content=ft.Column(
            [
                breadcrumb_area,
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Container(
                                content=ft.Column(
                                    [
                                        ft.Container(
                                            content=ft.Text("基本信息", size=16, weight=ft.FontWeight.BOLD),
                                            padding=ft.padding.only(bottom=20),
                                        ),
                                        ft.Container(
                                            content=ft.Column(
                                                [
                                                    ft.Row(
                                                        [
                                                            ft.Text("供应商名称", width=100),
                                                            ft.TextField(
                                                                width=300,
                                                                height=40,
                                                                border_color=ft.Colors.GREY_400,
                                                                focused_border_color=ft.Colors.BLUE_400,
                                                            ),
                                                        ],
                                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                    ),
                                                    ft.Container(height=20),
                                                    ft.Row(
                                                        [
                                                            ft.Text("联系人", width=100),
                                                            ft.TextField(
                                                                width=300,
                                                                height=40,
                                                                border_color=ft.Colors.GREY_400,
                                                                focused_border_color=ft.Colors.BLUE_400,
                                                            ),
                                                        ],
                                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                    ),
                                                    ft.Container(height=20),
                                                    ft.Row(
                                                        [
                                                            ft.Text("联系电话", width=100),
                                                            ft.TextField(
                                                                width=300,
                                                                height=40,
                                                                border_color=ft.Colors.GREY_400,
                                                                focused_border_color=ft.Colors.BLUE_400,
                                                            ),
                                                        ],
                                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                    ),
                                                    ft.Container(height=20),
                                                    ft.Row(
                                                        [
                                                            ft.Text("电子邮箱", width=100),
                                                            ft.TextField(
                                                                width=300,
                                                                height=40,
                                                                border_color=ft.Colors.GREY_400,
                                                                focused_border_color=ft.Colors.BLUE_400,
                                                            ),
                                                        ],
                                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                    ),
                                                    ft.Container(height=20),
                                                    ft.Row(
                                                        [
                                                            ft.Text("地址", width=100),
                                                            ft.TextField(
                                                                width=300,
                                                                height=40,
                                                                multiline=True,
                                                                min_lines=2,
                                                                max_lines=3,
                                                                border_color=ft.Colors.GREY_400,
                                                                focused_border_color=ft.Colors.BLUE_400,
                                                            ),
                                                        ],
                                                        vertical_alignment=ft.CrossAxisAlignment.START,
                                                    ),
                                                ],
                                            ),
                                            padding=20,
                                            border=ft.border.all(1, ft.Colors.GREY_200),
                                            border_radius=8,
                                        ),
                                        ft.Container(height=20),
                                        ft.Container(
                                            content=ft.Column(
                                                [
                                                    ft.Text("上传文件", size=16, weight=ft.FontWeight.BOLD),
                                                    ft.Container(height=20),
                                                    ft.Row(
                                                        [
                                                            ft.ElevatedButton(
                                                                "选择文件",
                                                                icon=ft.icons.UPLOAD_FILE,
                                                                style=ft.ButtonStyle(
                                                                    bgcolor=ft.Colors.BLUE_400,
                                                                    color=ft.Colors.WHITE,
                                                                ),
                                                            ),
                                                            ft.Text("未选择文件", color=ft.Colors.GREY_400),
                                                        ],
                                                        spacing=20,
                                                    ),
                                                ],
                                            ),
                                            padding=20,
                                            border=ft.border.all(1, ft.Colors.GREY_200),
                                            border_radius=8,
                                        ),
                                        ft.Container(height=20),
                                        ft.Row(
                                            [
                                                ft.ElevatedButton(
                                                    "提交",
                                                    style=ft.ButtonStyle(
                                                        bgcolor=ft.Colors.BLUE_400,
                                                        color=ft.Colors.WHITE,
                                                    ),
                                                    on_click=return_to_supplier_list,
                                                ),
                                                ft.OutlinedButton(
                                                    "取消",
                                                    on_click=return_to_supplier_list,
                                                ),
                                            ],
                                            spacing=20,
                                        ),
                                    ],
                                    scroll=ft.ScrollMode.AUTO,
                                ),
                                padding=40,
                                bgcolor=ft.Colors.WHITE,
                            ),
                        ],
                        expand=True,
                    ),
                    expand=True,
                    bgcolor=ft.Colors.WHITE,
                ),
            ],
            spacing=0,
            expand=True,
        ),
        expand=True,
        bgcolor=ft.Colors.WHITE,
    )

    # 创建主要布局
    main_content = ft.Row(
        [
            sidebar,
            content_area,
        ],
        expand=True,
        spacing=0,
    )

    if return_content:
        return main_content
    else:
        page.add(main_content)

    # 设置页面背景色
    page.bgcolor = ft.Colors.WHITE
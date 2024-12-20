# coding: utf-8
import flet as ft
from components.sidebar import create_sidebar
from components.breadcrumb import create_breadcrumb
from utils import navigate_with_transition

def change_create(page: ft.Page, return_content=False):
    page.title = "新建变更"
    page.window_maximized = True
    page.padding = 0
    
    def return_to_change_list(e):
        from change_list import change_list
        new_content = change_list(page, return_content=True)
        navigate_with_transition(page, new_content)

    def return_to_main(e):
        from mainpage import mainpage
        new_content = mainpage(page, return_content=True)
        navigate_with_transition(page, new_content)

    # 使用通用侧边栏
    sidebar = create_sidebar(page, "changes")

    # 创建面包屑区域
    breadcrumb_area = ft.Container(
        content=ft.Row(
            [
                create_breadcrumb(page, [
                    {"text": "首页", "on_click": return_to_main},
                    {"text": "变更管理", "on_click": return_to_change_list},
                    {"text": "新建变更"},
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
                                                            ft.Text("变更名称", width=100),
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
                                                            ft.Text("变更类型", width=100),
                                                            ft.Dropdown(
                                                                width=300,
                                                                height=40,
                                                                border_color=ft.Colors.GREY_400,
                                                                options=[
                                                                    ft.dropdown.Option("ECR"),
                                                                    ft.dropdown.Option("MR"),
                                                                    ft.dropdown.Option("ECO"),
                                                                ],
                                                            ),
                                                        ],
                                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                    ),
                                                    ft.Container(height=20),
                                                    ft.Row(
                                                        [
                                                            ft.Text("变更描述", width=100),
                                                            ft.TextField(
                                                                width=300,
                                                                height=40,
                                                                multiline=True,
                                                                min_lines=3,
                                                                max_lines=5,
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
                                                    ft.Container(height=20),
                                                    ft.DataTable(
                                                        columns=[
                                                            ft.DataColumn(ft.Text("文件名")),
                                                            ft.DataColumn(ft.Text("大小")),
                                                            ft.DataColumn(ft.Text("状态")),
                                                            ft.DataColumn(ft.Text("操作")),
                                                        ],
                                                        rows=[],
                                                        border=ft.border.all(1, ft.Colors.GREY_200),
                                                        border_radius=8,
                                                        vertical_lines=ft.border.BorderSide(1, ft.Colors.GREY_200),
                                                        horizontal_lines=ft.border.BorderSide(1, ft.Colors.GREY_200),
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
                                                    on_click=return_to_change_list,
                                                ),
                                                ft.OutlinedButton(
                                                    "取消",
                                                    on_click=return_to_change_list,
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
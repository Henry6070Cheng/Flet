# coding: utf-8
import flet as ft
from components.sidebar import create_sidebar
from components.breadcrumb import create_breadcrumb
from utils import navigate_with_transition

def document_list(page: ft.Page, return_content=False):
    page.title = "文档列表"
    page.window_maximized = True
    page.padding = 0
    
    def navigate_to_document_create(e):
        from document_create import document_create
        new_content = document_create(page, return_content=True)
        navigate_with_transition(page, new_content)

    # ... 其他代码保持不变 ...

    # 修改搜索和操作区
    search_area = ft.Container(
        content=ft.Row(
            [
                # 左侧搜索区
                ft.Row(
                    [
                        ft.TextField(
                            width=300,
                            height=40,
                            hint_text="搜索文档...",
                            hint_style=ft.TextStyle(
                                color=ft.colors.GREY_400,
                            ),
                            text_style=ft.TextStyle(),
                            prefix_icon=ft.icons.SEARCH,
                            border_color=ft.colors.GREY_400,
                            focused_border_color=ft.colors.BLUE_400,
                        ),
                        ft.IconButton(
                            icon=ft.icons.SEARCH,
                            icon_color=ft.colors.BLUE_400,
                            tooltip="搜索",
                        ),
                    ],
                ),
                # 中间新建文档按钮
                ft.ElevatedButton(
                    "新建文档",
                    icon=ft.icons.ADD,
                    style=ft.ButtonStyle(
                        bgcolor=ft.colors.BLUE_400,
                        color=ft.colors.WHITE,
                    ),
                    on_click=navigate_to_document_create,
                ),
                # 右侧信息提示区
                ft.Row(
                    [
                        ft.Text("您有20项任务", color=ft.colors.BLACK),
                        ft.TextButton(
                            "查看",
                            style=ft.ButtonStyle(color=ft.colors.BLUE_400),
                        ),
                    ],
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=20,
        bgcolor=ft.colors.WHITE,
        border=ft.border.only(bottom=ft.BorderSide(1, ft.colors.GREY_200)),
    )

    # ... 其他代码保持不变 ... 
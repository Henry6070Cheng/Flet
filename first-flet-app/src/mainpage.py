# coding: utf-8
import flet as ft
from components.sidebar import create_sidebar
from components.breadcrumb import create_breadcrumb
from utils import navigate_with_transition

def mainpage(page: ft.Page, return_content=False):
    page.title = "主页"
    page.window_maximized = True
    page.padding = 0
    
    # 添加页面跳转函数
    def navigate_to_document_list(e):
        from document_list import document_list
        new_content = document_list(page, return_content=True)
        navigate_with_transition(page, new_content)
    
    def navigate_to_material_list(e):
        from material_list import material_list
        new_content = material_list(page, return_content=True)
        navigate_with_transition(page, new_content)

    def navigate_to_change_list(e):
        from change_list import change_list
        new_content = change_list(page, return_content=True)
        navigate_with_transition(page, new_content)

    def navigate_to_project_list(e):
        from project_list import project_list
        new_content = project_list(page, return_content=True)
        navigate_with_transition(page, new_content)

    def navigate_to_supplier_list(e):
        from supplier_list import supplier_list
        new_content = supplier_list(page, return_content=True)
        navigate_with_transition(page, new_content)

    def navigate_to_users(e):
        from users import users
        new_content = users(page, return_content=True)
        navigate_with_transition(page, new_content)

    def logout(e):
        page.clean()
        from main import main
        main(page)
        page.update()

    # 使用通用侧边栏，标记首页选中
    sidebar = create_sidebar(page, "home")

    # 创建面包屑区域
    breadcrumb_area = ft.Container(
        content=ft.Row(
            [
                create_breadcrumb(page, [
                    {"text": "首页"},
                ]),
                ft.Row(
                    [
                        ft.Text(
                            "当前版本: 1.0.012",
                            size=14,
                            color=ft.colors.BLACK,
                            selectable=True,
                        ),
                        ft.Container(width=20),
                        ft.IconButton(
                            icon=ft.icons.LOGOUT,
                            icon_color=ft.colors.BLUE_400,
                            tooltip="退出登录",
                            on_click=logout,
                        ),
                    ],
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=ft.padding.only(left=20, right=20, top=16, bottom=16),
        bgcolor=ft.colors.WHITE,
        border=ft.border.only(bottom=ft.BorderSide(1, ft.colors.GREY_200)),
    )

    # 创建搜索和操作区
    search_area = ft.Container(
        content=ft.Row(
            [
                ft.Row(
                    [
                        ft.TextField(
                            width=300,
                            height=40,
                            hint_text="搜索...",
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
                ft.Row(
                    [
                        ft.Text(
                            "您有20项任务",
                            size=14,
                            color=ft.colors.BLACK,
                            selectable=True,
                        ),
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

    # 创建功能卡片
    def create_card(title, icon, on_click=None):
        return ft.Container(
            content=ft.Column(
                [
                    ft.IconButton(
                        icon=icon,
                        icon_color=ft.colors.BLUE_400,
                        icon_size=40,
                        tooltip=title,
                        on_click=on_click,
                    ),
                    ft.Text(
                        title,
                        size=14,
                        color=ft.colors.BLACK,
                        selectable=True,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=5,
            ),
            padding=20,
            bgcolor=ft.colors.WHITE,
            border_radius=8,
            width=150,
            height=150,
            border=ft.border.all(1, ft.colors.GREY_200),
            on_click=on_click,
        )

    # 创建功能按钮区
    function_buttons = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        create_card("文档管理", ft.icons.FOLDER, navigate_to_document_list),
                        create_card("物料管理", ft.icons.INVENTORY, navigate_to_material_list),
                        create_card("变更管理", ft.icons.COMPARE_ARROWS, navigate_to_change_list),
                        create_card("项目管理", ft.icons.BUSINESS_CENTER, navigate_to_project_list),
                        create_card("供应商管理", ft.icons.STORE, navigate_to_supplier_list),
                        create_card("用户管理", ft.icons.PERSON, navigate_to_users),
                    ],
                    spacing=20,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        padding=ft.padding.only(top=40, bottom=40),
        bgcolor=ft.colors.WHITE,
        expand=True,
        width=float("inf"),
    )

    # 创建主内容区
    content_area = ft.Container(
        content=ft.Column(
            [
                breadcrumb_area,
                search_area,
                function_buttons,
            ],
            spacing=0,
            expand=True,
            width=float("inf"),
        ),
        expand=True,
        bgcolor=ft.colors.WHITE,
        width=float("inf"),
    )

    # 创建主要布局
    main_content = ft.Row(
        [
            sidebar,
            content_area,
        ],
        expand=True,
        spacing=0,
        width=float("inf"),
    )

    if return_content:
        return main_content
    else:
        page.add(main_content)

    # 设置页面背景色
    page.bgcolor = ft.colors.WHITE

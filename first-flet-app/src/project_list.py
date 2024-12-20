# coding: utf-8
import flet as ft
from components.sidebar import create_sidebar
from components.breadcrumb import create_breadcrumb
from utils import navigate_with_transition

def navigate_to_project_create(page: ft.Page):
    def handle_click(e):
        from project_create import project_create
        new_content = project_create(page, return_content=True)
        navigate_with_transition(page, new_content)
    return handle_click

def project_list(page: ft.Page, return_content=False):
    page.title = "项目管理"
    page.window_maximized = True
    page.padding = 0
    
    # 设置默认字体样式
    default_style = {
        "size": 14,
        "weight": ft.FontWeight.W_400,
    }
    
    def create_text(text_content, **kwargs):
        style = default_style.copy()
        style.update(kwargs)
        style["selectable"] = True
        return ft.Text(text_content, **style)

    # 返回主页面函数
    def return_to_main(e):
        from mainpage import mainpage
        new_content = mainpage(page, return_content=True)
        navigate_with_transition(page, new_content)

    def logout(e):
        page.clean()
        from main import main
        main(page)
        page.update()

    # 使用通用侧边栏，并标记当前选中项
    sidebar = create_sidebar(page, "projects")

    # 创建面包屑区域
    breadcrumb_area = ft.Container(
        content=ft.Row(
            [
                create_breadcrumb(page, [
                    {"text": "首页", "on_click": return_to_main},
                    {"text": "项目管理"},
                ]),
                ft.Row(
                    [
                        create_text(
                            "当前版本: 1.0.012",
                            color=ft.Colors.BLACK,
                        ),
                        ft.Container(width=20),
                        ft.IconButton(
                            icon=ft.icons.LOGOUT,
                            icon_color=ft.Colors.BLUE_400,
                            tooltip="退出登录",
                            on_click=logout,
                        ),
                    ],
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=ft.padding.only(left=20, right=20, top=16, bottom=16),
        bgcolor=ft.Colors.WHITE,
        border=ft.border.only(bottom=ft.BorderSide(1, ft.Colors.GREY_200)),
    )

    def navigate_to_project_create(e):
        try:
            from project_create import project_create
            new_content = project_create(page, return_content=True)
            navigate_with_transition(page, new_content)
        except Exception as ex:
            print(f"Navigation error: {ex}")

    # 创建搜索和操作区
    search_area = ft.Container(
        content=ft.Row(
            [
                # 左侧搜索区
                ft.Row(
                    [
                        ft.TextField(
                            width=300,
                            height=40,
                            hint_text="搜索项目...",
                            hint_style=ft.TextStyle(
                                color=ft.Colors.GREY_400,
                            ),
                            text_style=ft.TextStyle(),
                            prefix_icon=ft.icons.SEARCH,
                            border_color=ft.Colors.GREY_400,
                            focused_border_color=ft.Colors.BLUE_400,
                        ),
                        ft.IconButton(
                            icon=ft.icons.SEARCH,
                            icon_color=ft.Colors.BLUE_400,
                            tooltip="搜索",
                        ),
                    ],
                ),
                # 中间新建项目按钮
                ft.ElevatedButton(
                    "新建项目",
                    icon=ft.icons.ADD,
                    style=ft.ButtonStyle(
                        bgcolor=ft.Colors.BLUE_400,
                        color=ft.Colors.WHITE,
                    ),
                    on_click=lambda e: navigate_to_project_create(e),
                ),
                # 右侧信息提示区
                ft.Row(
                    [
                        create_text("Show", color=ft.Colors.BLACK),
                        ft.Dropdown(
                            width=70,
                            value="100",
                            border_color=ft.Colors.BLUE_400,
                            text_style=ft.TextStyle(),
                            options=[
                                ft.dropdown.Option("50"),
                                ft.dropdown.Option("100"),
                                ft.dropdown.Option("200"),
                            ],
                        ),
                        create_text("entries", color=ft.Colors.BLACK),
                    ],
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=20,
        bgcolor=ft.Colors.WHITE,
        border=ft.border.only(bottom=ft.BorderSide(1, ft.Colors.GREY_200)),
    )

    # 创建数据表格
    def create_data_row(project_name, project_id, manager, start_date):
        def handle_click(e):
            # TODO: 跳转到项目详情页面
            pass

        return ft.DataRow(
            cells=[
                ft.DataCell(create_text(project_name, color=ft.Colors.BLACK)),
                ft.DataCell(create_text(project_id, color=ft.Colors.BLACK)),
                ft.DataCell(create_text(manager, color=ft.Colors.BLACK)),
                ft.DataCell(create_text(start_date, color=ft.Colors.BLACK)),
                ft.DataCell(create_row_buttons()),
            ],
        )

    def create_row_buttons():
        return ft.Row(
            [
                ft.TextButton(
                    text="成员管理",
                    style=ft.ButtonStyle(
                        color=ft.Colors.BLUE_400,
                        padding=ft.padding.all(0),
                    ),
                ),
                ft.TextButton(
                    text="导出文档列表",
                    style=ft.ButtonStyle(
                        color=ft.Colors.BLUE_400,
                        padding=ft.padding.all(0),
                    ),
                ),
            ],
            spacing=10,
        )

    # 生成示例项目数据
    def generate_sample_projects():
        projects = [
            ("Saturn", "214", "马凌云", "2024-03-12"),
            ("Jupiter", "213", "马凌云", "2024-03-12"),
            ("天马", "212", "杨诗蓓", "2024-01-17"),
            ("古星", "210", "杨诗蓓", "2024-01-03"),
            ("乘黄", "211", "杨诗蓓", "2024-01-03"),
            ("伏羲", "209", "马凌云", "2023-10-23"),
            ("Mars", "208", "杨诗蓓", "2023-09-11"),
            ("共工", "207", "杨诗蓓", "2023-09-06"),
            ("Venus经皮胆道镜", "206", "��凌云", "2023-07-03"),
            ("祝融", "205", "杨诗蓓", "2023-06-09"),
            ("盘古", "204", "马凌云", "2023-01-13"),
            ("胆道镜", "201", "杨诗蓓", "2022-12-01"),
        ]
        
        return [create_data_row(*project) for project in projects]

    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(create_text("项目名称", color=ft.Colors.BLACK)),
            ft.DataColumn(create_text("项目编号", color=ft.Colors.BLACK)),
            ft.DataColumn(create_text("项目经理", color=ft.Colors.BLACK)),
            ft.DataColumn(create_text("启动日期", color=ft.Colors.BLACK)),
            ft.DataColumn(create_text("操作", color=ft.Colors.BLACK)),
        ],
        rows=generate_sample_projects(),
        border=ft.border.all(1, ft.Colors.GREY_200),
        border_radius=8,
        vertical_lines=ft.border.BorderSide(1, ft.Colors.GREY_200),
        horizontal_lines=ft.border.BorderSide(1, ft.Colors.GREY_200),
        heading_row_height=50,
        data_row_min_height=60,
        data_row_max_height=100,
    )

    # 创建分页控件
    pagination = ft.Row(
        [
            create_text("Showing 1 to 12 of 12 entries", color=ft.Colors.BLACK),
            ft.Row(
                [
                    ft.TextButton(
                        text="Previous",
                        style=ft.ButtonStyle(color=ft.Colors.BLUE_400),
                    ),
                    ft.TextButton(
                        text="Next",
                        style=ft.ButtonStyle(color=ft.Colors.BLUE_400),
                    ),
                ],
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    # 创建主内容区
    content_area = ft.Container(
        content=ft.Column(
            [
                breadcrumb_area,
                search_area,
                # 数据表格和分页的容器
                ft.Container(
                    content=ft.Column(
                        [
                            # 可滚动的数据表格区域
                            ft.Container(
                                content=ft.Column(
                                    [
                                        ft.Container(
                                            content=data_table,
                                            padding=20,
                                            bgcolor=ft.Colors.WHITE,
                                            border_radius=8,
                                            width=float("inf"),
                                        ),
                                    ],
                                    scroll=ft.ScrollMode.AUTO,
                                    width=float("inf"),
                                ),
                                expand=True,
                                padding=ft.padding.only(left=20, right=20, top=20),
                                width=float("inf"),
                            ),
                            # 固定在底部的分页控件
                            ft.Container(
                                content=pagination,
                                padding=ft.padding.symmetric(horizontal=20, vertical=20),
                                bgcolor=ft.Colors.WHITE,
                                border=ft.border.only(top=ft.BorderSide(1, ft.Colors.GREY_200)),
                                width=float("inf"),
                            ),
                        ],
                        expand=True,
                        width=float("inf"),
                    ),
                    expand=True,
                    bgcolor=ft.Colors.BLUE_GREY_50,
                    width=float("inf"),
                ),
            ],
            spacing=0,
            expand=True,
            width=float("inf"),
        ),
        expand=True,
        width=float("inf"),
    )

    # 创建主要布
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
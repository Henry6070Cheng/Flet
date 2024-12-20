# coding: utf-8
import flet as ft
from components.sidebar import create_sidebar
from components.breadcrumb import create_breadcrumb
from utils import navigate_with_transition

def navigate_to_user_create(page: ft.Page):
    def handle_click(e):
        from user_create import user_create
        new_content = user_create(page, return_content=True)
        navigate_with_transition(page, new_content)
    return handle_click

def users(page: ft.Page, return_content=False):
    page.title = "用户管理"
    page.window_maximized = True
    page.padding = 0
    
    # 设置默认字体样式
    default_style = {
        "size": 14,
        "weight": ft.FontWeight.W_400,
        "color": ft.colors.BLACK,
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
    sidebar = create_sidebar(page, "users")

    # 创建面包屑区域
    breadcrumb_area = ft.Container(
        content=ft.Row(
            [
                create_breadcrumb(page, [
                    {"text": "首页", "on_click": return_to_main},
                    {"text": "用户管理"},
                ]),
                ft.Row(
                    [
                        create_text(
                            "当前版本: 1.0.012",
                            color=ft.colors.BLACK,
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
                # 左侧搜索区
                ft.Row(
                    [
                        ft.TextField(
                            width=300,
                            height=40,
                            hint_text="搜索用户...",
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
                # 中间新建用户按钮
                ft.ElevatedButton(
                    "新建用户",
                    icon=ft.icons.ADD,
                    style=ft.ButtonStyle(
                        bgcolor=ft.colors.BLUE_400,
                        color=ft.colors.WHITE,
                    ),
                    on_click=navigate_to_user_create(page),
                ),
                # 右侧信息提示区
                ft.Row(
                    [
                        create_text("Show", color=ft.colors.BLACK),
                        ft.Dropdown(
                            width=70,
                            value="100",
                            border_color=ft.colors.BLUE_400,
                            text_style=ft.TextStyle(),
                            options=[
                                ft.dropdown.Option("50"),
                                ft.dropdown.Option("100"),
                                ft.dropdown.Option("200"),
                            ],
                        ),
                        create_text("entries", color=ft.colors.BLACK),
                    ],
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=20,
        bgcolor=ft.colors.WHITE,
        border=ft.border.only(bottom=ft.BorderSide(1, ft.colors.GREY_200)),
    )

    # 创建数据表格
    def create_data_row(username, title, position, last_login, last_operation):
        return ft.DataRow(
            cells=[
                ft.DataCell(create_text(username, color=ft.colors.BLACK)),
                ft.DataCell(create_text(title, color=ft.colors.BLACK)),
                ft.DataCell(create_text(position, color=ft.colors.BLACK)),
                ft.DataCell(create_text(last_login, color=ft.colors.BLACK)),
                ft.DataCell(create_text(last_operation, color=ft.colors.BLACK)),
                ft.DataCell(create_row_buttons()),
            ],
        )

    def create_row_buttons():
        return ft.Row(
            [
                ft.IconButton(
                    icon=ft.icons.EDIT,
                    icon_color=ft.colors.BLUE_400,
                    tooltip="编辑用户",
                ),
                ft.IconButton(
                    icon=ft.icons.LOCK_RESET,
                    icon_color=ft.colors.BLUE_400,
                    tooltip="修改密码",
                ),
                ft.IconButton(
                    icon=ft.icons.DELETE,
                    icon_color=ft.colors.RED_400,
                    tooltip="删除用户",
                ),
            ],
            spacing=0,
        )

    # 生成示例用户数据
    def generate_sample_users():
        users = [
            ("张三", "项目经理", "研发部", "2024-03-12 09:30:00", "修改项目信息"),
            ("李四", "工程师", "研发部", "2024-03-12 10:15:00", "上传文档"),
            ("王五", "主管", "质量部", "2024-03-11 16:45:00", "审核变更"),
            ("赵六", "工程师", "研发部", "2024-03-11 15:20:00", "创建变更"),
            ("孙七", "经理", "质量部", "2024-03-11 14:30:00", "审批文档"),
            ("周八", "工程师", "研发部", "2024-03-11 11:20:00", "更新物料信息"),
            ("吴九", "主管", "生产部", "2024-03-10 17:40:00", "查看报告"),
            ("郑十", "工程师", "研发部", "2024-03-10 16:15:00", "创建文档"),
            ("陈一", "经理", "生产部", "2024-03-10 15:00:00", "审核变更"),
            ("杨二", "工程师", "研发部", "2024-03-10 14:20:00", "上传文档"),
            ("刘三", "主管", "质量部", "2024-03-10 11:30:00", "创建项目"),
            ("马四", "工程师", "研发部", "2024-03-10 10:45:00", "更新文档"),
        ]
        
        return [create_data_row(*user) for user in users]

    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(create_text("用户名", color=ft.colors.BLACK)),
            ft.DataColumn(create_text("职务", color=ft.colors.BLACK)),
            ft.DataColumn(create_text("岗位", color=ft.colors.BLACK)),
            ft.DataColumn(create_text("最后登录", color=ft.colors.BLACK)),
            ft.DataColumn(create_text("最后操作", color=ft.colors.BLACK)),
            ft.DataColumn(create_text("操作", color=ft.colors.BLACK)),
        ],
        rows=generate_sample_users(),
        border=ft.border.all(1, ft.colors.GREY_200),
        border_radius=8,
        vertical_lines=ft.border.BorderSide(1, ft.colors.GREY_200),
        horizontal_lines=ft.border.BorderSide(1, ft.colors.GREY_200),
        heading_row_height=50,
        data_row_min_height=60,
        data_row_max_height=100,
    )

    # 创建分页控件
    pagination = ft.Row(
        [
            create_text("Showing 1 to 12 of 12 entries", color=ft.colors.BLACK),
            ft.Row(
                [
                    ft.TextButton(
                        text="Previous",
                        style=ft.ButtonStyle(color=ft.colors.BLUE_400),
                    ),
                    ft.TextButton(
                        text="Next",
                        style=ft.ButtonStyle(color=ft.colors.BLUE_400),
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
                                            bgcolor=ft.colors.WHITE,
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
                                bgcolor=ft.colors.WHITE,
                                border=ft.border.only(top=ft.BorderSide(1, ft.colors.GREY_200)),
                                width=float("inf"),
                            ),
                        ],
                        expand=True,
                        width=float("inf"),
                    ),
                    expand=True,
                    bgcolor=ft.colors.WHITE,
                    width=float("inf"),
                ),
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
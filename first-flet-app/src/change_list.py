# coding: utf-8
import flet as ft
from components.sidebar import create_sidebar
from components.breadcrumb import create_breadcrumb
from utils import navigate_with_transition

def change_list(page: ft.Page, return_content=False):
    page.title = "变更管理"
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

    def navigate_to_change_create(e):
        try:
            from change_create import change_create
            new_content = change_create(page, return_content=True)
            navigate_with_transition(page, new_content)
        except Exception as ex:
            print(f"Navigation error: {ex}")

    # 使用通用侧边栏，并标记当前选中项
    sidebar = create_sidebar(page, "changes")

    # 创建面包屑区域
    breadcrumb_area = ft.Container(
        content=ft.Row(
            [
                create_breadcrumb(page, [
                    {"text": "首页", "on_click": return_to_main},
                    {"text": "变更管理"},
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
                            hint_text="搜索变更...",
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
                # 中间新建变更按钮
                ft.ElevatedButton(
                    "新建变更",
                    icon=ft.icons.ADD,
                    style=ft.ButtonStyle(
                        bgcolor=ft.Colors.BLUE_400,
                        color=ft.Colors.WHITE,
                    ),
                    on_click=navigate_to_change_create,
                ),
                # 右侧信息提示区
                ft.Row(
                    [
                        create_text("您有0项任务", color=ft.Colors.BLACK),
                        ft.TextButton(
                            "查看",
                            style=ft.ButtonStyle(color=ft.Colors.BLUE_400),
                        ),
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
    def create_data_row(change_id, name, status, owner, create_date, modify_date):
        def handle_click(e):
            from change_detail import change_detail
            new_content = change_detail(page, change_id, return_content=True)
            navigate_with_transition(page, new_content)

        return ft.DataRow(
            cells=[
                ft.DataCell(
                    ft.Container(
                        content=ft.TextButton(
                            text=change_id,
                            on_click=handle_click,
                            style=ft.ButtonStyle(
                                color=ft.Colors.BLUE_400,
                                padding=ft.padding.all(0),
                            ),
                        ),
                        padding=ft.padding.all(0),
                    ),
                ),
                ft.DataCell(create_text(name, color=ft.Colors.BLACK)),
                ft.DataCell(
                    ft.Container(
                        content=create_text(status, color=ft.Colors.BLACK),
                        bgcolor=ft.Colors.BLUE_50 if status == "新建" else (
                            ft.Colors.GREEN_50 if status == "批准" else (
                                ft.Colors.ORANGE_50 if status == "评审中" else ft.Colors.RED_50
                            )
                        ),
                        border_radius=15,
                        padding=ft.padding.symmetric(horizontal=10, vertical=5),
                    )
                ),
                ft.DataCell(create_text(owner, color=ft.Colors.BLACK)),
                ft.DataCell(create_text(create_date, color=ft.Colors.BLACK)),
                ft.DataCell(create_text(modify_date, color=ft.Colors.BLACK)),
                ft.DataCell(create_row_buttons()),
            ],
        )

    def create_row_buttons():
        return ft.Row(
            [
                ft.IconButton(
                    icon=ft.icons.VISIBILITY,
                    icon_color=ft.Colors.BLUE_400,
                    tooltip="查看",
                ),
                ft.IconButton(
                    icon=ft.icons.EDIT,
                    icon_color=ft.Colors.BLUE_400,
                    tooltip="修改",
                ),
                ft.IconButton(
                    icon=ft.icons.RATE_REVIEW,
                    icon_color=ft.Colors.BLUE_400,
                    tooltip="评审",
                ),
                ft.IconButton(
                    icon=ft.icons.CANCEL,
                    icon_color=ft.Colors.BLUE_400,
                    tooltip="取消变更",
                ),
                ft.IconButton(
                    icon=ft.icons.DRIVE_FILE_MOVE,
                    icon_color=ft.Colors.BLUE_400,
                    tooltip="转移",
                ),
            ],
            spacing=0,
        )

    # 生成示例变更数据
    def generate_sample_changes(count=15):
        import random
        from datetime import datetime, timedelta
        
        change_types = ["ECR", "MR", "ECO"]
        statuses = ["新建", "评审中", "批准", "关闭"]
        owners = ["王慧轩", "刘沛霖", "陈慧敏", "闫文韬", "程慧群"]
        base_date = datetime(2024, 1, 1)
        
        changes = []
        
        for i in range(count):
            # 生成变更编号
            change_type = random.choice(change_types)
            change_id = f"{change_type}100{(i+1):03d}"
            
            # 随机生成数据
            status = random.choice(statuses)
            owner = random.choice(owners)
            
            # 生成日期
            create_date = base_date + timedelta(days=random.randint(0, 60))
            modify_date = create_date + timedelta(days=random.randint(0, 10))
            
            # 生成变更名称
            if change_type == "ECR":
                name = f"盘古-H5.0按钮版、盘古-H3.8按钮版变更"
            elif change_type == "MR":
                name = f"Mercury 注册变更防范发布"
            else:
                name = f"主机红外触控滤光片移除变更申请"
            
            changes.append(create_data_row(
                change_id,
                name,
                status,
                owner,
                create_date.strftime("%Y-%m-%d %H:%M:%S"),
                modify_date.strftime("%Y-%m-%d %H:%M:%S")
            ))
        
        return changes

    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(create_text("变更号", color=ft.Colors.BLACK)),
            ft.DataColumn(create_text("变更名称", color=ft.Colors.BLACK)),
            ft.DataColumn(create_text("状态", color=ft.Colors.BLACK)),
            ft.DataColumn(create_text("负责人", color=ft.Colors.BLACK)),
            ft.DataColumn(create_text("创建日期", color=ft.Colors.BLACK)),
            ft.DataColumn(create_text("修改日期", color=ft.Colors.BLACK)),
            ft.DataColumn(create_text("操作", color=ft.Colors.BLACK)),
        ],
        rows=generate_sample_changes(15),
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
            create_text("页面大小:", color=ft.Colors.BLACK),
            ft.Dropdown(
                width=70,
                value="20",
                border_color=ft.Colors.BLUE_400,
                text_style=ft.TextStyle(),
                options=[
                    ft.dropdown.Option("10"),
                    ft.dropdown.Option("20"),
                    ft.dropdown.Option("50"),
                ],
            ),
            ft.IconButton(
                icon=ft.icons.ARROW_BACK_IOS,
                icon_color=ft.Colors.BLUE_400,
            ),
            create_text("1/12", color=ft.Colors.BLACK),
            ft.IconButton(
                icon=ft.icons.ARROW_FORWARD_IOS,
                icon_color=ft.Colors.BLUE_400,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
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
                                padding=ft.padding.symmetric(vertical=20),
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
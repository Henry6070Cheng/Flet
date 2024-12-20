# coding: utf-8
import flet as ft
from components.sidebar import create_sidebar
from components.breadcrumb import create_breadcrumb
from utils import navigate_with_transition

def document_list(page: ft.Page, return_content=False):
    page.title = "文档列表"
    page.window_maximized = True
    page.padding = 0
    # 设置页面编码和语言
    page.web_renderer = ft.WebRenderer.HTML
    page.locale = "zh_CN"
    page.rtl = False
    page.theme = ft.Theme(
        use_material3=True,
        visual_density=ft.ThemeVisualDensity.STANDARD,
    )
    
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

    # 跳转到文档详情页面
    def doc_number_clicked(e, doc_id):
        from document_detail import document_detail
        new_content = document_detail(page, doc_id, return_content=True)
        navigate_with_transition(page, new_content)

    # 使用通用侧边栏，并标记当前选中项
    sidebar = create_sidebar(page, "documents")

    # 创建面包屑区域
    breadcrumb_area = ft.Container(
        content=ft.Row(
            [
                create_breadcrumb(page, [
                    {"text": "首页", "on_click": return_to_main},
                    {"text": "文档管理"},
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

    def navigate_to_document_create(e):
        try:
            from document_create import document_create
            new_content = document_create(page, return_content=True)
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
                            hint_text="搜索文档...",
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
                # 中间新建文档按钮
                ft.ElevatedButton(
                    "新建文档",
                    icon=ft.icons.ADD,
                    style=ft.ButtonStyle(
                        bgcolor=ft.Colors.BLUE_400,
                        color=ft.Colors.WHITE,
                    ),
                    on_click=lambda e: navigate_to_document_create(e),
                ),
                # 右侧信息提示区
                ft.Row(
                    [
                        create_text("您有20项任务", color=ft.Colors.BLACK),
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
    def create_data_row(doc_id, name, type, project, status, create_date, modify_date, version):
        def handle_click(e):
            from document_detail import document_detail
            new_content = document_detail(page, doc_id, return_content=True)
            navigate_with_transition(page, new_content)

        return ft.DataRow(
            cells=[
                ft.DataCell(
                    ft.Container(
                        content=ft.TextButton(
                            text=doc_id,
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
                ft.DataCell(create_text(type, color=ft.Colors.BLACK)),
                ft.DataCell(create_text(project, color=ft.Colors.BLACK)),
                ft.DataCell(
                    ft.Container(
                        content=create_text(status, color=ft.Colors.BLACK),
                        bgcolor=ft.Colors.BLUE_50 if status == "评审中" else ft.Colors.GREEN_50,
                        border_radius=15,
                        padding=ft.padding.symmetric(horizontal=10, vertical=5),
                    )
                ),
                ft.DataCell(create_text(create_date, color=ft.Colors.BLACK)),
                ft.DataCell(create_text(modify_date, color=ft.Colors.BLACK)),
                ft.DataCell(create_text(version, color=ft.Colors.BLACK)),
                ft.DataCell(create_row_buttons()),
            ],
        )

    def create_row_buttons():
        return ft.Row(
            [
                ft.IconButton(
                    icon=ft.icons.VISIBILITY,
                    icon_color=ft.Colors.BLUE_400,
                    tooltip="浏览",
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
                    icon=ft.icons.PUBLISH,
                    icon_color=ft.Colors.BLUE_400,
                    tooltip="发布",
                ),
                ft.IconButton(
                    icon=ft.icons.CANCEL,
                    icon_color=ft.Colors.BLUE_400,
                    tooltip="取消变更",
                ),
                ft.IconButton(
                    icon=ft.icons.UPGRADE,
                    icon_color=ft.Colors.BLUE_400,
                    tooltip="升版",
                ),
                ft.IconButton(
                    icon=ft.icons.DRIVE_FILE_MOVE,
                    icon_color=ft.Colors.BLUE_400,
                    tooltip="转移",
                ),
                ft.IconButton(
                    icon=ft.icons.DELETE_FOREVER,
                    icon_color=ft.Colors.RED_400,
                    tooltip="作",
                ),
            ],
            spacing=0,
        )

    # 添加生成示例文档数据数
    def generate_sample_documents(count=15):
        import random
        from datetime import datetime, timedelta

        doc_types = ["项目文件", "技术文档", "设计文档", "测试文档", "规范文档"]
        projects = ["星源测试", "Mercury项目", "Venus计划", "Earth工程", "Mars研发"]
        statuses = ["评审中", "发布"]
        
        documents = []
        base_date = datetime(2024, 1, 1)
        
        for i in range(count):
            # 生成文档号 D201-xxxxx，保证5位数字
            doc_id = f"D201-{(i+1):05d}"
            
            # 随机生成日期
            create_date = base_date + timedelta(days=random.randint(0, 60))
            modify_date = create_date + timedelta(days=random.randint(0, 10))
            
            # 随机选择文档类型和项目
            doc_type = random.choice(doc_types)
            project = random.choice(projects)
            status = random.choice(statuses)
            
            # 生成版本号 Rev xx
            version = f"Rev {(i % 5 + 1):02d}"
            
            documents.append(create_data_row(
                doc_id,
                f"{project}_{doc_type}_{doc_id}计划档",
                doc_type,
                project,
                status,
                create_date.strftime("%Y-%m-%d"),
                modify_date.strftime("%Y-%m-%d"),
                version
            ))
        
        return documents

    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(create_text("文档号", color=ft.Colors.BLACK)),
            ft.DataColumn(create_text("文档名称", color=ft.Colors.BLACK)),
            ft.DataColumn(create_text("文档类型", color=ft.Colors.BLACK)),
            ft.DataColumn(create_text("项目名称", color=ft.Colors.BLACK)),
            ft.DataColumn(create_text("状态", color=ft.Colors.BLACK)),
            ft.DataColumn(create_text("创建日期", color=ft.Colors.BLACK)),
            ft.DataColumn(create_text("修改日期", color=ft.Colors.BLACK)),
            ft.DataColumn(create_text("版本", color=ft.Colors.BLACK)),
            ft.DataColumn(create_text("操作", color=ft.Colors.BLACK)),
        ],
        rows=generate_sample_documents(15),
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
            create_text("1/178", color=ft.Colors.BLACK),
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
                # 数据表格和页的容器
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
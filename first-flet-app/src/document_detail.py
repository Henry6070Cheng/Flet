# coding: utf-8
import flet as ft
from components.sidebar import create_sidebar
from components.breadcrumb import create_breadcrumb
from utils import navigate_with_transition

def document_detail(page: ft.Page, doc_id: str = None, return_content=False):
    page.title = "文档详情"
    page.window_maximized = True
    page.padding = 0
    
    # 返回文档列表函数
    def return_to_list(e):
        from document_list import document_list
        new_content = document_list(page, return_content=True)
        navigate_with_transition(page, new_content)

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

    # 创建面包屑区域
    breadcrumb_area = ft.Container(
        content=ft.Row(
            [
                create_breadcrumb(page, [
                    {"text": "首页", "on_click": return_to_main},
                    {"text": "文档管理", "on_click": return_to_list},
                    {"text": "文档详情"},
                ]),
                ft.Row(
                    [
                        ft.Text(
                            "当前版本: 1.0.012",
                            size=14,
                            color=ft.colors.GREY_700,
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

    # 使用通用侧边栏，保持文档管理选中
    sidebar = create_sidebar(page, "documents")

    # 创建顶部信息栏
    top_info = ft.Container(
        content=ft.Row(
            [
                # 左侧搜索区
                ft.Container(
                    content=ft.Row(
                        [
                            ft.TextField(
                                width=300,
                                height=40,
                                hint_text="搜索文档...",
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
                ),
                # 右侧信息提示区
                ft.Container(
                    content=ft.Row(
                        [
                            ft.Text("您有20项任务", size=14, color=ft.colors.GREY_700),
                            ft.TextButton(
                                "查看",
                                style=ft.ButtonStyle(color=ft.colors.BLUE_400),
                            ),
                        ],
                    ),
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=20,
        bgcolor=ft.colors.WHITE,
        border=ft.border.only(bottom=ft.BorderSide(1, ft.colors.GREY_200)),
    )

    # 创建信息卡片
    def create_info_field(label, value):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(label, size=12, color=ft.colors.BLACK54),
                    ft.Text(value, size=14, color=ft.colors.BLACK),
                ],
                spacing=5,
            ),
            padding=10,
        )

    info_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Icon(ft.icons.DESCRIPTION, color=ft.colors.BLACK),
                            ft.Text("基本信息", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                        ],
                        spacing=10,
                    ),
                    ft.Divider(height=1, color=ft.colors.BLACK12),
                    ft.ResponsiveRow(
                        [
                            ft.Column([create_info_field("文档编号", doc_id)], col={"sm": 6, "md": 4}),
                            ft.Column([create_info_field("文档名称", "Mercury一次性使用流感导管_ECR100062设计变更申请评审申请单")], col={"sm": 12, "md": 8}),
                            ft.Column([create_info_field("文档类型", "项目文件")], col={"sm": 6, "md": 4}),
                            ft.Column([create_info_field("项目", "星源测试")], col={"sm": 6, "md": 4}),
                            ft.Column([create_info_field("负责人", "蔡金慧")], col={"sm": 6, "md": 4}),
                            ft.Column([create_info_field("创建者", "黄旺红")], col={"sm": 6, "md": 4}),
                            ft.Column([create_info_field("创建时间", "2024-12-18 10:47:20")], col={"sm": 6, "md": 4}),
                            ft.Column([create_info_field("修改时间", "2024-12-19 11:42:59")], col={"sm": 6, "md": 4}),
                            ft.Column([create_info_field("当前版本", "1")], col={"sm": 6, "md": 4}),
                            ft.Column([
                                create_info_field(
                                    "当前状态",
                                    ft.Container(
                                        content=ft.Text("评审中"),
                                        bgcolor=ft.colors.BLUE_50,
                                        border_radius=15,
                                        padding=ft.padding.symmetric(horizontal=10, vertical=5),
                                    ),
                                )
                            ], col={"sm": 6, "md": 4}),
                        ],
                    ),
                ],
                spacing=20,
            ),
            padding=20,
            bgcolor=ft.colors.WHITE,
        ),
    )

    # 创建文件列表
    files_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Icon(ft.icons.FOLDER_OPEN, color=ft.colors.BLACK),
                            ft.Text("文件列表", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                        ],
                        spacing=10,
                    ),
                    ft.Divider(height=1, color=ft.colors.BLACK12),
                    ft.DataTable(
                        columns=[
                            ft.DataColumn(ft.Text("文件名称", color=ft.colors.BLACK)),
                            ft.DataColumn(ft.Text("操作", color=ft.colors.BLACK)),
                        ],
                        rows=[
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text(f"{doc_id}_Mercury一次性使用流感导管_ECR100062设计变更申请评审申请单_签字版.pdf", color=ft.colors.BLACK)),
                                    ft.DataCell(
                                        ft.Row(
                                            [
                                                ft.IconButton(
                                                    icon=ft.icons.VISIBILITY,
                                                    icon_color=ft.colors.BLACK54,
                                                    tooltip="预览",
                                                ),
                                                ft.IconButton(
                                                    icon=ft.icons.DOWNLOAD,
                                                    icon_color=ft.colors.BLACK54,
                                                    tooltip="下载",
                                                ),
                                            ],
                                            spacing=0,
                                        )
                                    ),
                                ],
                            ),
                        ],
                        border=ft.border.all(1, ft.colors.BLACK12),
                        border_radius=8,
                        vertical_lines=ft.border.BorderSide(1, ft.colors.BLACK12),
                        horizontal_lines=ft.border.BorderSide(1, ft.colors.BLACK12),
                    ),
                ],
                spacing=20,
            ),
            padding=20,
            bgcolor=ft.colors.WHITE,
        ),
    )

    # 创建操作记录
    history_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Icon(ft.icons.HISTORY, color=ft.colors.BLACK),
                            ft.Text("操作记录", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                        ],
                        spacing=10,
                    ),
                    ft.Divider(height=1, color=ft.colors.BLACK12),
                    ft.DataTable(
                        columns=[
                            ft.DataColumn(ft.Text("操作时间", color=ft.colors.BLACK)),
                            ft.DataColumn(ft.Text("操作人", color=ft.colors.BLACK)),
                            ft.DataColumn(ft.Text("操作类型", color=ft.colors.BLACK)),
                            ft.DataColumn(ft.Text("备注", color=ft.colors.BLACK)),
                        ],
                        rows=[
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text("2024-12-19 11:42", color=ft.colors.BLACK)),
                                    ft.DataCell(ft.Text("蔡金慧", color=ft.colors.BLACK)),
                                    ft.DataCell(ft.Text("上传文件", color=ft.colors.BLACK)),
                                    ft.DataCell(ft.Text("上传签字版PDF", color=ft.colors.BLACK)),
                                ],
                            ),
                        ],
                        border=ft.border.all(1, ft.colors.BLACK12),
                        border_radius=8,
                        vertical_lines=ft.border.BorderSide(1, ft.colors.BLACK12),
                        horizontal_lines=ft.border.BorderSide(1, ft.colors.BLACK12),
                    ),
                ],
                spacing=20,
            ),
            padding=20,
            bgcolor=ft.colors.WHITE,
        ),
    )

    # 创建可滚动的内容区域
    content_scroll = ft.Container(
        content=ft.Column(
            [
                info_card,
                files_card,
                history_card,
            ],
            spacing=20,
            scroll=ft.ScrollMode.AUTO,
        ),
        padding=20,
        expand=True,
        bgcolor=ft.colors.BLUE_GREY_50,
    )

    # 创建右侧内容区
    content_area = ft.Container(
        content=ft.Column(
            [
                breadcrumb_area,
                top_info,
                content_scroll,
            ],
            spacing=0,
            expand=True,
        ),
        expand=True,
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
    page.bgcolor = ft.colors.WHITE
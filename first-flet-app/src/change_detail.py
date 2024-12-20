# coding: utf-8
import flet as ft
from components.sidebar import create_sidebar
from components.breadcrumb import create_breadcrumb
from utils import navigate_with_transition

def change_detail(page: ft.Page, change_id, return_content=False):
    page.title = "变更详情"
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

    # 返回变更列表页面
    def return_to_change_list(e):
        from change_list import change_list
        new_content = change_list(page, return_content=True)
        navigate_with_transition(page, new_content)

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
    sidebar = create_sidebar(page, "changes")

    # 创建面包屑区域
    breadcrumb_area = ft.Container(
        content=ft.Row(
            [
                create_breadcrumb(page, [
                    {"text": "首页", "on_click": return_to_main},
                    {"text": "变更管理", "on_click": return_to_change_list},
                    {"text": change_id},
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

    # 创建基本信息区域
    def create_info_row(label, value, bgcolor=None):
        return ft.Row(
            [
                ft.Container(
                    content=create_text(label, color=ft.colors.BLACK),
                    width=100,
                    bgcolor=ft.colors.BLUE_50,
                    padding=10,
                ),
                ft.Container(
                    content=create_text(value, color=ft.colors.BLACK),
                    expand=True,
                    bgcolor=bgcolor if bgcolor else ft.colors.WHITE,
                    padding=10,
                ),
            ],
            spacing=0,
        )

    basic_info = ft.Container(
        content=ft.Column(
            [
                create_text("变更信息", size=16, weight=ft.FontWeight.W_500),
                ft.Container(height=10),
                create_info_row("变更号", change_id),
                create_info_row("变更名称", "Mercury流感导管新物料专业设计适用范围"),
                create_info_row("状态", "批准"),
                create_info_row("创建人", "闫文韬"),
                create_info_row("创建日期", "2024-10-16 15:51:02"),
                create_info_row("修改日期", "2024-12-18 15:00:50"),
            ],
            spacing=1,
        ),
        padding=20,
        bgcolor=ft.colors.WHITE,
        border_radius=8,
        border=ft.border.all(1, ft.colors.GREY_200),
    )

    # 创建技术文件区域
    tech_files = ft.Container(
        content=ft.Column(
            [
                create_text("技术文件", size=16, weight=ft.FontWeight.W_500),
                ft.Container(height=10),
                ft.DataTable(
                    columns=[
                        ft.DataColumn(create_text("文件名称", color=ft.colors.BLACK)),
                        ft.DataColumn(create_text("操作", color=ft.colors.BLACK)),
                    ],
                    rows=[
                        ft.DataRow(
                            cells=[
                                ft.DataCell(create_text("ECR100062-Mercury流感导管新物料专业设计适用范围-专项验证综合评估报告-1216.docx", color=ft.colors.BLACK)),
                                ft.DataCell(
                                    ft.Row(
                                        [
                                            ft.IconButton(
                                                icon=ft.icons.DOWNLOAD,
                                                icon_color=ft.colors.BLUE_400,
                                                tooltip="下载",
                                            ),
                                        ],
                                        spacing=0,
                                    )
                                ),
                            ]
                        ),
                        ft.DataRow(
                            cells=[
                                ft.DataCell(create_text("ECR100062-RevA-Mercury流感导管新物料专业设计适用范围-signature.pdf", color=ft.colors.BLACK)),
                                ft.DataCell(
                                    ft.Row(
                                        [
                                            ft.IconButton(
                                                icon=ft.icons.DOWNLOAD,
                                                icon_color=ft.colors.BLUE_400,
                                                tooltip="下载",
                                            ),
                                        ],
                                        spacing=0,
                                    )
                                ),
                            ]
                        ),
                    ],
                    border=ft.border.all(1, ft.colors.GREY_200),
                    horizontal_lines=ft.border.BorderSide(1, ft.colors.GREY_200),
                    vertical_lines=ft.border.BorderSide(1, ft.colors.GREY_200),
                    heading_row_height=40,
                ),
            ],
        ),
        padding=20,
        bgcolor=ft.colors.WHITE,
        border_radius=8,
        border=ft.border.all(1, ft.colors.GREY_200),
    )

    # 创建变更物料区域
    change_materials = ft.Container(
        content=ft.Column(
            [
                create_text("变更物料", size=16, weight=ft.FontWeight.W_500),
                ft.Container(height=10),
                ft.DataTable(
                    columns=[
                        ft.DataColumn(create_text("序号", color=ft.colors.BLACK)),
                        ft.DataColumn(create_text("料号", color=ft.colors.BLACK)),
                        ft.DataColumn(create_text("物料描述", color=ft.colors.BLACK)),
                        ft.DataColumn(create_text("版本", color=ft.colors.BLACK)),
                        ft.DataColumn(create_text("新建", color=ft.colors.BLACK)),
                        ft.DataColumn(create_text("状态", color=ft.colors.BLACK)),
                        ft.DataColumn(create_text("物料规格", color=ft.colors.BLACK)),
                        ft.DataColumn(create_text("月份", color=ft.colors.BLACK)),
                    ],
                    rows=[
                        ft.DataRow(
                            cells=[
                                ft.DataCell(create_text("1", color=ft.colors.BLACK)),
                                ft.DataCell(create_text("P1000098", color=ft.colors.BLACK)),
                                ft.DataCell(create_text("一次性使用流感导管组件(中文)", color=ft.colors.BLACK)),
                                ft.DataCell(create_text("Rev A", color=ft.colors.BLACK)),
                                ft.DataCell(create_text("新建", color=ft.colors.BLACK)),
                                ft.DataCell(create_text("已发布", color=ft.colors.BLACK)),
                                ft.DataCell(create_text("一次性使用流感导管组件(中文)", color=ft.colors.BLACK)),
                                ft.DataCell(create_text("是", color=ft.colors.BLACK)),
                            ]
                        ),
                        # ... 更多物料行
                    ],
                    border=ft.border.all(1, ft.colors.GREY_200),
                    horizontal_lines=ft.border.BorderSide(1, ft.colors.GREY_200),
                    vertical_lines=ft.border.BorderSide(1, ft.colors.GREY_200),
                    heading_row_height=40,
                ),
            ],
        ),
        padding=20,
        bgcolor=ft.colors.WHITE,
        border_radius=8,
        border=ft.border.all(1, ft.colors.GREY_200),
    )

    # 创建变更记录区域
    change_records = ft.Container(
        content=ft.Column(
            [
                create_text("变更记录", size=16, weight=ft.FontWeight.W_500),
                ft.Container(height=10),
                ft.DataTable(
                    columns=[
                        ft.DataColumn(create_text("变更号", color=ft.colors.BLACK)),
                        ft.DataColumn(create_text("变更名称", color=ft.colors.BLACK)),
                        ft.DataColumn(create_text("变更描述", color=ft.colors.BLACK)),
                        ft.DataColumn(create_text("创建日期", color=ft.colors.BLACK)),
                        ft.DataColumn(create_text("修改日期", color=ft.colors.BLACK)),
                    ],
                    rows=[
                        ft.DataRow(
                            cells=[
                                ft.DataCell(create_text("ECR100062", color=ft.colors.BLACK)),
                                ft.DataCell(create_text("Mercury流感导管新物料专业设计适用范围", color=ft.colors.BLACK)),
                                ft.DataCell(create_text("1.新增物料，2.新增适配方方案适用范围", color=ft.colors.BLACK)),
                                ft.DataCell(create_text("2024-12-18 15:15:14", color=ft.colors.BLACK)),
                                ft.DataCell(create_text("2024-12-18 15:00:30", color=ft.colors.BLACK)),
                            ]
                        ),
                    ],
                    border=ft.border.all(1, ft.colors.GREY_200),
                    horizontal_lines=ft.border.BorderSide(1, ft.colors.GREY_200),
                    vertical_lines=ft.border.BorderSide(1, ft.colors.GREY_200),
                    heading_row_height=40,
                ),
            ],
        ),
        padding=20,
        bgcolor=ft.colors.WHITE,
        border_radius=8,
        border=ft.border.all(1, ft.colors.GREY_200),
    )

    # 创建文件操作记录区域
    file_operations = ft.Container(
        content=ft.Column(
            [
                create_text("文件操作记录", size=16, weight=ft.FontWeight.W_500),
                ft.Container(height=10),
                ft.DataTable(
                    columns=[
                        ft.DataColumn(create_text("文件名称", color=ft.colors.BLACK)),
                        ft.DataColumn(create_text("用户", color=ft.colors.BLACK)),
                        ft.DataColumn(create_text("操作时间", color=ft.colors.BLACK)),
                        ft.DataColumn(create_text("操作", color=ft.colors.BLACK)),
                    ],
                    rows=[
                        ft.DataRow(
                            cells=[
                                ft.DataCell(create_text("ECR100062-Mercury流感导管新物料专业设计适用范围-专项验证综合评估报告-1216.docx", color=ft.colors.BLACK)),
                                ft.DataCell(create_text("闫文韬", color=ft.colors.BLACK)),
                                ft.DataCell(create_text("2024-12-19 14:14:03", color=ft.colors.BLACK)),
                                ft.DataCell(create_text("上传", color=ft.colors.BLACK)),
                            ]
                        ),
                        # ... 更多操作记录
                    ],
                    border=ft.border.all(1, ft.colors.GREY_200),
                    horizontal_lines=ft.border.BorderSide(1, ft.colors.GREY_200),
                    vertical_lines=ft.border.BorderSide(1, ft.colors.GREY_200),
                    heading_row_height=40,
                ),
            ],
        ),
        padding=20,
        bgcolor=ft.colors.WHITE,
        border_radius=8,
        border=ft.border.all(1, ft.colors.GREY_200),
    )

    # 创建主内容区
    content_area = ft.Container(
        content=ft.Column(
            [
                breadcrumb_area,
                ft.Container(
                    content=ft.Column(
                        [
                            basic_info,
                            ft.Container(height=20),
                            tech_files,
                            ft.Container(height=20),
                            change_materials,
                            ft.Container(height=20),
                            change_records,
                            ft.Container(height=20),
                            file_operations,
                        ],
                        scroll=ft.ScrollMode.AUTO,
                    ),
                    padding=20,
                    expand=True,
                    bgcolor=ft.colors.BLUE_GREY_50,
                ),
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
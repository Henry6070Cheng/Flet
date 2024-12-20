# coding: utf-8
import flet as ft
from components.sidebar import create_sidebar
from components.breadcrumb import create_breadcrumb
from utils import navigate_with_transition

def material_detail(page: ft.Page, material_id, return_content=False):
    page.title = "物料详情"
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

    # 返回物料列表页面
    def return_to_material_list(e):
        from material_list import material_list
        new_content = material_list(page, return_content=True)
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
    sidebar = create_sidebar(page, "materials")

    # 创建面包屑区域
    breadcrumb_area = ft.Container(
        content=ft.Row(
            [
                create_breadcrumb(page, [
                    {"text": "首页", "on_click": return_to_main},
                    {"text": "物料管理", "on_click": return_to_material_list},
                    {"text": material_id},
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
                create_text("物料信息", size=16, weight=ft.FontWeight.W_500),
                ft.Container(height=10),
                create_info_row("料号", material_id),
                create_info_row("版本", "RevA"),
                create_info_row("物料编号", "NA"),
                create_info_row("状态", "新建"),
                create_info_row("流程编号", "流程编号"),
                create_info_row("物料类型", "半成品"),
                create_info_row("物料子类型", "N/A"),
                create_info_row("制造商名称", ""),
                create_info_row("创建人", "陈慧敏"),
                create_info_row("创建日期", "2024-12-01 11:00:46"),
                create_info_row("状态", "未启用"),
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
                    rows=[],
                    border=ft.border.all(1, ft.colors.GREY_200),
                    horizontal_lines=ft.border.BorderSide(1, ft.colors.GREY_200),
                    heading_row_height=40,
                ),
            ],
        ),
        padding=20,
        bgcolor=ft.colors.WHITE,
        border_radius=8,
        border=ft.border.all(1, ft.colors.GREY_200),
    )

    # 创建验证报告区域
    validation_reports = ft.Container(
        content=ft.Column(
            [
                create_text("验证报告", size=16, weight=ft.FontWeight.W_500),
                ft.Container(height=10),
                ft.DataTable(
                    columns=[
                        ft.DataColumn(create_text("文件名称", color=ft.colors.BLACK)),
                        ft.DataColumn(create_text("操作", color=ft.colors.BLACK)),
                    ],
                    rows=[],
                    border=ft.border.all(1, ft.colors.GREY_200),
                    horizontal_lines=ft.border.BorderSide(1, ft.colors.GREY_200),
                    heading_row_height=40,
                ),
            ],
        ),
        padding=20,
        bgcolor=ft.colors.WHITE,
        border_radius=8,
        border=ft.border.all(1, ft.colors.GREY_200),
    )

    # 创建BOM信息区域
    bom_info = ft.Container(
        content=ft.Column(
            [
                create_text("BOM信息", size=16, weight=ft.FontWeight.W_500),
                ft.Container(height=10),
                ft.DataTable(
                    columns=[
                        ft.DataColumn(create_text("序号", color=ft.colors.BLACK)),
                        ft.DataColumn(create_text("料号", color=ft.colors.BLACK)),
                        ft.DataColumn(create_text("名称", color=ft.colors.BLACK)),
                        ft.DataColumn(create_text("版本", color=ft.colors.BLACK)),
                        ft.DataColumn(create_text("状态", color=ft.colors.BLACK)),
                        ft.DataColumn(create_text("物料状态", color=ft.colors.BLACK)),
                        ft.DataColumn(create_text("前缀", color=ft.colors.BLACK)),
                        ft.DataColumn(create_text("物料描述", color=ft.colors.BLACK)),
                        ft.DataColumn(create_text("物料规格", color=ft.colors.BLACK)),
                        ft.DataColumn(create_text("采购规格", color=ft.colors.BLACK)),
                        ft.DataColumn(create_text("制造商料号", color=ft.colors.BLACK)),
                        ft.DataColumn(create_text("单位", color=ft.colors.BLACK)),
                        ft.DataColumn(create_text("单位用量", color=ft.colors.BLACK)),
                        ft.DataColumn(create_text("位号", color=ft.colors.BLACK)),
                    ],
                    rows=[],
                    border=ft.border.all(1, ft.colors.GREY_200),
                    horizontal_lines=ft.border.BorderSide(1, ft.colors.GREY_200),
                    heading_row_height=40,
                ),
            ],
        ),
        padding=20,
        bgcolor=ft.colors.WHITE,
        border_radius=8,
        border=ft.border.all(1, ft.colors.GREY_200),
    )

    # 创建使用记录区域
    usage_records = ft.Container(
        content=ft.Column(
            [
                create_text("使用记录", size=16, weight=ft.FontWeight.W_500),
                ft.Container(height=10),
                ft.DataTable(
                    columns=[
                        ft.DataColumn(create_text("物料版本")),
                        ft.DataColumn(create_text("用户")),
                        ft.DataColumn(create_text("操作时间")),
                        ft.DataColumn(create_text("修改内容描述")),
                    ],
                    rows=[
                        ft.DataRow(
                            cells=[
                                ft.DataCell(create_text("RevA")),
                                ft.DataCell(create_text("陈慧敏")),
                                ft.DataCell(create_text("2024/12/19 16:21:16")),
                                ft.DataCell(create_text("文件操作")),
                            ]
                        )
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
                        ft.DataColumn(create_text("文件名")),
                        ft.DataColumn(create_text("用户")),
                        ft.DataColumn(create_text("操作时间")),
                        ft.DataColumn(create_text("操作")),
                    ],
                    rows=[],
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
                            validation_reports,
                            ft.Container(height=20),
                            bom_info,
                            ft.Container(height=20),
                            usage_records,
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
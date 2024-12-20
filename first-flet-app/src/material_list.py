# coding: utf-8
import flet as ft
from database.material_dal import MaterialDAL
from components.sidebar import create_sidebar
from components.breadcrumb import create_breadcrumb
from utils.navigation import navigate_with_transition

def material_list(page: ft.Page, return_content=False):
    page.title = "物料管理"
    page.window_maximized = True
    page.padding = 0
    
    # 状态变量
    current_page = 1
    page_size = 10
    search_term = ""
    category_filter = None
    status_filter = None
    
    # 搜索框
    search_field = ft.TextField(
        width=300,
        height=40,
        hint_text="搜索物料...",
        prefix_icon=ft.icons.SEARCH,
        border_color=ft.colors.GREY_400,
        focused_border_color=ft.colors.BLUE_400,
    )
    
    # 数据表格
    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("物料编号")),
            ft.DataColumn(ft.Text("名称")),
            ft.DataColumn(ft.Text("类别")),
            ft.DataColumn(ft.Text("规格")),
            ft.DataColumn(ft.Text("单位")),
            ft.DataColumn(ft.Text("库存数量")),
            ft.DataColumn(ft.Text("状态")),
            ft.DataColumn(ft.Text("操作")),
        ],
        rows=[],
    )
    
    # 分页控件
    pagination = ft.Row(
        controls=[
            ft.IconButton(
                icon=ft.icons.ARROW_BACK,
                on_click=lambda e: load_data(current_page - 1),
                disabled=True,
            ),
            ft.Text("1/1"),
            ft.IconButton(
                icon=ft.icons.ARROW_FORWARD,
                on_click=lambda e: load_data(current_page + 1),
                disabled=True,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    
    def load_data(page_number=1):
        nonlocal current_page
        current_page = page_number
        
        # 构建过滤条件
        filters = {}
        if search_term:
            filters['search'] = search_term
        if category_filter:
            filters['category'] = category_filter
        if status_filter:
            filters['status'] = status_filter
            
        # 获取数据
        result = MaterialDAL.get_all_materials(filters, page_number, page_size)
        
        # 更新表格数据
        data_table.rows = []
        for item in result['items']:
            data_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(item['material_no'])),
                        ft.DataCell(ft.Text(item['name'])),
                        ft.DataCell(ft.Text(item['category'])),
                        ft.DataCell(ft.Text(item['specification'] or '-')),
                        ft.DataCell(ft.Text(item['unit'] or '-')),
                        ft.DataCell(ft.Text(str(item['stock_quantity']))),
                        ft.DataCell(ft.Text(item['status'])),
                        ft.DataCell(
                            ft.Row(
                                [
                                    ft.IconButton(
                                        icon=ft.icons.EDIT,
                                        icon_color=ft.colors.BLUE_400,
                                        tooltip="编辑",
                                        data=item['id'],
                                        on_click=lambda e: edit_material(e.control.data),
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.DELETE,
                                        icon_color=ft.colors.RED_400,
                                        tooltip="删除",
                                        data=item['id'],
                                        on_click=lambda e: delete_material(e.control.data),
                                    ),
                                ]
                            )
                        ),
                    ]
                )
            )
        
        # 更新分页控件
        pagination.controls[0].disabled = page_number <= 1
        pagination.controls[1].value = f"{page_number}/{result['total_pages']}"
        pagination.controls[2].disabled = page_number >= result['total_pages']
        
        page.update()
    
    def search_materials(e):
        nonlocal search_term
        search_term = search_field.value
        load_data(1)
    
    def edit_material(material_id):
        # 跳转到编辑页面
        from material_edit import material_edit
        new_content = material_edit(page, material_id, return_content=True)
        navigate_with_transition(page, new_content)
    
    def delete_material(material_id):
        def confirm_delete(e):
            try:
                MaterialDAL.delete_material(material_id)
                dialog.open = False
                page.update()
                load_data(current_page)
            except Exception as ex:
                error_text.value = f"删除失败: {str(ex)}"
                error_text.visible = True
                page.update()
        
        error_text = ft.Text(
            color=ft.colors.RED_400,
            size=14,
            visible=False
        )
        
        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("确认删除"),
            content=ft.Column(
                [
                    ft.Text("确定要删除这个物料吗？此操作不可恢复。"),
                    error_text,
                ],
                tight=True,
            ),
            actions=[
                ft.TextButton("取消", on_click=lambda e: setattr(dialog, 'open', False)),
                ft.TextButton("确定", on_click=confirm_delete),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        
        page.dialog = dialog
        dialog.open = True
        page.update()
    
    def return_to_main(e):
        from mainpage import mainpage
        new_content = mainpage(page, return_content=True)
        navigate_with_transition(page, new_content)
    
    def create_new_material(e):
        from material_create import material_create
        new_content = material_create(page, return_content=True)
        navigate_with_transition(page, new_content)
    
    # 创建页面布局
    sidebar = create_sidebar(page, "materials")
    
    # 创建面包屑
    breadcrumb_area = ft.Container(
        content=ft.Row(
            [
                create_breadcrumb(page, [
                    {"text": "首页", "on_click": return_to_main},
                    {"text": "物料管理"},
                ]),
            ],
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
                        search_field,
                        ft.IconButton(
                            icon=ft.icons.SEARCH,
                            icon_color=ft.colors.BLUE_400,
                            tooltip="搜索",
                            on_click=search_materials,
                        ),
                    ],
                ),
                ft.ElevatedButton(
                    "新建物料",
                    icon=ft.icons.ADD,
                    style=ft.ButtonStyle(
                        bgcolor=ft.colors.BLUE_400,
                        color=ft.colors.WHITE,
                    ),
                    on_click=create_new_material,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=20,
        bgcolor=ft.colors.WHITE,
        border=ft.border.only(bottom=ft.BorderSide(1, ft.colors.GREY_200)),
    )
    
    # 创建主内容区
    content_area = ft.Container(
        content=ft.Column(
            [
                breadcrumb_area,
                search_area,
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Container(
                                content=data_table,
                                padding=20,
                                bgcolor=ft.colors.WHITE,
                                border_radius=8,
                            ),
                        ],
                        scroll=ft.ScrollMode.AUTO,
                    ),
                    expand=True,
                    padding=ft.padding.only(left=20, right=20, top=20),
                ),
                ft.Container(
                    content=pagination,
                    padding=ft.padding.symmetric(horizontal=20, vertical=20),
                    bgcolor=ft.colors.WHITE,
                    border=ft.border.only(top=ft.BorderSide(1, ft.colors.GREY_200)),
                ),
            ],
            spacing=0,
            expand=True,
        ),
        expand=True,
        bgcolor=ft.colors.WHITE,
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
    
    # 加载初始数据
    load_data()
    
    if return_content:
        return main_content
    else:
        page.add(main_content)
        
    # 设置页面背景色
    page.bgcolor = ft.colors.WHITE
